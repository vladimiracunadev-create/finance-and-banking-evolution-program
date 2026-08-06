"""Servidor de autorizacion didactico con PKCE.

Implementa el flujo de codigo de la Parte 17, clase 6 con los siete controles
que la clase enumera. El objetivo del modulo no es que el camino feliz funcione
—eso lo consigue cualquiera— sino que los caminos infelices fallen del modo
documentado.

AVISO: las claves y secretos de este modulo son de juguete y viven en el
repositorio a proposito. Fuera de un laboratorio, eso seria un incidente.
"""

from __future__ import annotations

import base64
import hashlib
import secrets
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone

CODE_TTL_SECONDS = 60
ACCESS_TOKEN_TTL_SECONDS = 600


class AuthError(Exception):
    """Error del flujo de autorizacion. El `code` es el del catalogo OAuth."""

    def __init__(self, code: str, description: str = "") -> None:
        super().__init__(f"{code}: {description}" if description else code)
        self.code = code
        self.description = description


@dataclass(frozen=True)
class Client:
    client_id: str
    redirect_uris: frozenset[str]
    allowed_scopes: frozenset[str]
    # Un cliente publico no puede guardar un secreto: por eso PKCE es
    # obligatorio para el y recomendado para todos.
    is_public: bool = True
    secret: str | None = None


@dataclass
class AuthorizationCode:
    code: str
    client_id: str
    consent_id: str
    granted_scopes: tuple[str, ...]
    code_challenge: str
    issued_at: datetime
    used: bool = False


@dataclass
class AccessToken:
    value: str
    client_id: str
    consent_id: str
    scopes: tuple[str, ...]
    issued_at: datetime
    revoked: bool = False


def s256(verifier: str) -> str:
    """Transformacion S256 de PKCE (RFC 7636)."""
    digest = hashlib.sha256(verifier.encode("ascii")).digest()
    return base64.urlsafe_b64encode(digest).decode("ascii").rstrip("=")


class AuthorizationServer:
    def __init__(self, consents) -> None:
        self.clients: dict[str, Client] = {}
        self._codes: dict[str, AuthorizationCode] = {}
        self._tokens: dict[str, AccessToken] = {}
        self.consents = consents
        self.audit: list[dict] = []
        # La revocacion de un consentimiento invalida sus tokens vivos. Sin
        # esto, «revocar» significa «revocar cuando el token expire».
        consents.on_revoke(self.invalidate_tokens_for_consent)

    # ---------------------------------------------------------------- clientes

    def register(self, client: Client) -> None:
        self.clients[client.client_id] = client

    def _client(self, client_id: str) -> Client:
        if client_id not in self.clients:
            raise AuthError("invalid_client", "client_id no registrado")
        return self.clients[client_id]

    # ----------------------------------------------------------------- /authorize

    def authorize(
        self,
        client_id: str,
        redirect_uri: str,
        scope: str,
        state: str,
        code_challenge: str | None,
        code_challenge_method: str | None,
        consent_id: str,
        granted_scopes: list[str] | None = None,
        now: datetime | None = None,
    ) -> dict[str, str]:
        now = now or datetime.now(timezone.utc)
        client = self._client(client_id)

        # Coincidencia EXACTA. Un filtro por prefijo autoriza
        # https://app.ejemplo.cl.atacante.io, que es otro dominio.
        if redirect_uri not in client.redirect_uris:
            self._log("authorize", client_id, "rechazado", "redirect_uri no registrada")
            raise AuthError("invalid_request", "redirect_uri no registrada")

        if not code_challenge:
            self._log("authorize", client_id, "rechazado", "falta code_challenge")
            raise AuthError("invalid_request", "PKCE obligatorio")
        if code_challenge_method != "S256":
            self._log("authorize", client_id, "rechazado", "metodo PKCE no admitido")
            raise AuthError("invalid_request", "solo se admite S256")
        if not state:
            raise AuthError("invalid_request", "state obligatorio")

        solicitados = tuple(s for s in scope.split() if s)
        fuera = set(solicitados) - client.allowed_scopes
        if fuera:
            raise AuthError("invalid_scope", f"alcances no permitidos: {sorted(fuera)}")

        consent = self.consents.get(consent_id)
        if not consent.is_active(now):
            raise AuthError("access_denied", "consentimiento no vigente")

        # El token se emitira sobre los alcances CONCEDIDOS, no sobre los
        # solicitados: es la diferencia entre pedir y obtener.
        concedidos = tuple(
            s for s in (granted_scopes or solicitados) if s in consent.scopes
        )
        if not concedidos:
            raise AuthError("access_denied", "ningun alcance concedido")

        code = secrets.token_urlsafe(24)
        self._codes[code] = AuthorizationCode(
            code=code,
            client_id=client_id,
            consent_id=consent_id,
            granted_scopes=concedidos,
            code_challenge=code_challenge,
            issued_at=now,
        )
        self._log("authorize", client_id, "emitido", f"scopes={','.join(concedidos)}")
        return {"code": code, "state": state}

    # --------------------------------------------------------------------- /token

    def token(
        self,
        client_id: str,
        code: str,
        code_verifier: str,
        client_secret: str | None = None,
        now: datetime | None = None,
    ) -> dict[str, object]:
        now = now or datetime.now(timezone.utc)
        client = self._client(client_id)
        if not client.is_public and client.secret != client_secret:
            raise AuthError("invalid_client", "credencial de cliente invalida")

        record = self._codes.get(code)
        if record is None:
            raise AuthError("invalid_grant", "codigo desconocido")
        if record.client_id != client_id:
            raise AuthError("invalid_grant", "el codigo pertenece a otro cliente")
        if record.used:
            raise AuthError("invalid_grant", "codigo ya utilizado")
        if (now - record.issued_at).total_seconds() > CODE_TTL_SECONDS:
            raise AuthError("invalid_grant", "codigo expirado")
        if s256(code_verifier) != record.code_challenge:
            raise AuthError("invalid_grant", "code_verifier no coincide")

        record.used = True
        value = secrets.token_urlsafe(32)
        self._tokens[value] = AccessToken(
            value=value,
            client_id=client_id,
            consent_id=record.consent_id,
            scopes=record.granted_scopes,
            issued_at=now,
        )
        self._log("token", client_id, "emitido", f"consent={record.consent_id}")
        return {
            "access_token": value,
            "token_type": "Bearer",
            "expires_in": ACCESS_TOKEN_TTL_SECONDS,
            "scope": " ".join(record.granted_scopes),
        }

    # ------------------------------------------------------------------ recursos

    def check(self, token_value: str, scope: str, now: datetime | None = None) -> AccessToken:
        """Valida un token para un alcance. Se llama en CADA peticion."""
        now = now or datetime.now(timezone.utc)
        token = self._tokens.get(token_value)
        if token is None or token.revoked:
            raise AuthError("invalid_token", "token desconocido o revocado")
        if (now - token.issued_at).total_seconds() > ACCESS_TOKEN_TTL_SECONDS:
            raise AuthError("invalid_token", "token expirado")
        # Sin esta comprobacion, revocar el consentimiento no cerraria el acceso
        # hasta que el token expirase por si solo.
        if not self.consents.get(token.consent_id).is_active(now):
            raise AuthError("consent_revoked", "consentimiento no vigente")
        if scope not in token.scopes:
            raise AuthError("resource_forbidden", "fuera del alcance concedido")
        return token

    def invalidate_tokens_for_consent(self, consent_id: str) -> int:
        afectados = 0
        for token in self._tokens.values():
            if token.consent_id == consent_id and not token.revoked:
                token.revoked = True
                afectados += 1
        return afectados

    # ------------------------------------------------------------------ registro

    def _log(self, event: str, client_id: str, outcome: str, detail: str) -> None:
        """Registro de auditoria.

        Nunca escribe el token ni el code_verifier: un token en el registro
        convierte al sistema de observabilidad en un almacen de credenciales.
        """
        self.audit.append(
            {
                "event": event,
                "client_id": client_id,
                "outcome": outcome,
                "detail": detail,
                "at": datetime.now(timezone.utc).isoformat(),
            }
        )
