# Solución de referencia — Laboratorio 2: servidor de autorización simulado

> Material docente.

## Por qué «usuario y clave a cambio de token» no es un servidor de autorización

Porque el proveedor de información vería la credencial del cliente. Con eso puede
hacer todo lo que el cliente puede hacer, para siempre, sin registro y sin que el
cliente pueda revocarlo salvo cambiando la clave. El flujo con código existe para
que **la credencial nunca salga del dominio de la institución**.

## Los siete controles y el ataque que cada uno corta

| Control | Ataque que corta | Prueba negativa |
|---|---|---|
| PKCE obligatorio | Robo del código por una aplicación pública | `authorize` sin `code_challenge` → `invalid_request` |
| `redirect_uri` exacta | Redirección abierta | `https://app.ejemplo.cl.atacante.io/cb` → `invalid_request` |
| `state` verificado | Falsificación de petición entre sitios | Respuesta sin `state` original → descarta |
| Código de un solo uso | Repetición | Segundo canje → `invalid_grant` |
| Vida del código < 60 s | Uso diferido de un código filtrado | Canje a los 61 s → `invalid_grant` |
| Alcance concedido ≠ solicitado | Escalada de alcance | Token pedido con `payments:write` no concedido → `403` |
| Autenticación del cliente | Suplantación del proveedor | `client_id` sin credencial válida → `invalid_client` |

## El ataque sin PKCE, paso a paso

1. La aplicación del cliente es pública: no puede guardar un secreto.
2. Una aplicación maliciosa instalada en el mismo dispositivo registra el mismo
   esquema de redirección.
3. El sistema operativo entrega el código a la aplicación maliciosa.
4. Sin PKCE, esa aplicación canjea el código por un token: solo necesita el
   `client_id`, que es público por definición.
5. Con PKCE, el canje exige el `code_verifier`, que nunca salió del proceso
   legítimo. El código robado no sirve.

## Por qué el prefijo no basta en la validación de redirección

`https://app.ejemplo.cl` como prefijo autoriza también:

- `https://app.ejemplo.cl.atacante.io/callback`
- `https://app.ejemplo.cl@atacante.io/callback`
- `https://app.ejemplo.cl/../../redirect?to=atacante.io`

La comparación debe ser **de cadena completa** contra el conjunto registrado.

## Registro: qué se escribe y qué no

```text
SÍ   client_id, consent_id, scopes solicitados y concedidos,
     resultado, causa del rechazo, marca temporal, hash del código
NO   access_token, refresh_token, code_verifier, contraseña,
     cabecera Authorization completa
```

Un token en el registro convierte al sistema de observabilidad en un almacén de
credenciales, con un perímetro de acceso mucho más ancho.

## Estructura mínima esperada

```text
authorization_server/
├── __init__.py
├── endpoints.py      # /authorize y /token
├── pkce.py           # verificación S256
├── clients.py        # registro de clientes y redirect_uri
├── codes.py          # emisión, vida y un solo uso
└── tokens.py         # emisión acotada al alcance concedido
```

## Límites

- El entorno simula el canal: no hay TLS ni autenticación mutua real. En una
  implementación real, esos dos controles son obligatorios y su ausencia
  invalidaría todo lo anterior.
- Las claves del repositorio son de juguete y están versionadas a propósito. En
  cualquier otro contexto, eso sería un incidente de seguridad.
