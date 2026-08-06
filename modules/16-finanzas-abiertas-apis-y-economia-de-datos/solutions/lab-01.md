# Solución de referencia — Laboratorio 1: consentimiento granular

> Material docente. Las tablas dependen del producto que el estudiante haya
> definido en el paso 1; lo que se corrige es el **criterio**, no la coincidencia
> literal con este documento.

## Paso 1 — dato mínimo

Para un panel de saldos y movimientos, el dato mínimo es:

| Dato | ¿Por qué es necesario? |
|---|---|
| Identificador y tipo de cuenta | Distinguir cuentas en la vista |
| Saldo disponible y contable | Es el producto |
| Movimientos de N meses | Es el producto |
| Moneda | Sin ella el importe no significa nada |

Y **no** es necesario: nombre completo del titular, documento de identidad,
dirección, ni productos distintos de los que el cliente eligió mostrar.

## Paso 2–3 — tabla de alcances

| Alcance | Finalidad única | Dato | Plazo | Si no se otorga |
|---|---|---|---|---|
| `accounts:list` | Mostrar qué cuentas existen | Id, tipo, moneda, alias | 12 meses | No hay panel |
| `accounts:balances` | Mostrar el saldo | Saldo disponible y contable | 12 meses | Panel sin saldos |
| `accounts:transactions` | Mostrar movimientos | Movimientos de 12 meses | 12 meses | Panel sin detalle |

Errores típicos que se penalizan:

- Un único alcance `accounts:read` que agrupa las tres finalidades: impide que el
  cliente acepte una y rechace otra.
- Solicitar 24 meses «por si acaso» cuando el producto muestra 12.
- Incluir datos de identidad del titular, que el proveedor ya conoce.

## Paso 4 — objeto de consentimiento

```json
{
  "consent_id": "cns_01HZ...",
  "customer_ref": "cus_synthetic_0042",
  "provider_id": "tpp_cuentas_claras",
  "institution_id": "bank_004",
  "scopes": ["accounts:list", "accounts:balances", "accounts:transactions"],
  "purpose": "panel de posicion consolidada",
  "created_at": "2026-08-06T14:02:11Z",
  "expires_at": "2027-08-06T14:02:11Z",
  "status": "vigente",
  "notice_version": "consent-notice-v3",
  "evidence": {
    "auth_method": "sca-otp",
    "channel": "web",
    "ip_hash": "…",
    "presented_scopes": ["accounts:list", "accounts:balances", "accounts:transactions"]
  }
}
```

Claves que la corrección busca:

- `notice_version`: sin ella no se puede demostrar **qué texto** vio el cliente.
- `presented_scopes` separado de `scopes`: permite detectar si se concedió algo
  que no se presentó.
- `expires_at` absoluto, no «12 meses»: el plazo relativo se recalcula mal.

## Paso 5 — máquina de estados

```text
borrador ──► autorizado ──► vigente ──┬──► revocado    (acto del cliente)
    │                                 ├──► expirado    (llegó expires_at)
    └──► rechazado                    └──► terminado   (fin de la relación)

ninguna transición vuelve atrás; una renovación crea un consentimiento NUEVO
```

La renovación como **nuevo objeto** es la decisión importante: si se «extiende»
el existente se pierde la prueba de qué autorizó el cliente en cada periodo.

## Paso 6 — evidencia

Lo mínimo para reconstruir la decisión seis meses después:

1. Versión del texto presentado.
2. Alcances presentados y alcances concedidos.
3. Método de autenticación empleado.
4. Marca temporal con zona horaria.
5. Canal e identificador de sesión.
6. Identificador del proveedor solicitante.

## Paso 8 — la prueba que importa

```python
def test_acceso_con_consentimiento_revocado_falla(sandbox):
    consent = sandbox.autorizar(scopes=["accounts:balances"])
    assert sandbox.saldo(consent) is not None

    sandbox.revocar(consent)

    with pytest.raises(PermissionError):
        sandbox.saldo(consent)
```

Una prueba que solo comprueba `consent.status == "revocado"` **no vale**:
comprueba el campo, no el efecto.

## Límites

- El plazo de 12 meses es un supuesto del ejercicio, no una regla universal:
  depende de la norma aplicable y debe verificarse en la fuente oficial vigente.
- El modelo no cubre consentimientos de iniciación de pagos, que son de un solo
  uso y se tratan en el laboratorio 4.
