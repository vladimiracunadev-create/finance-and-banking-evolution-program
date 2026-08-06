# Open Finance Sandbox

Entorno simulado de finanzas abiertas para la **Parte 17**. Reúne las cinco
piezas del ecosistema —consentimiento, autorización, API de información,
iniciación de pagos y batería de conformidad— en un paquete de Python que
funciona **sin red, sin dependencias y sin credenciales reales**.

> **No es un banco ni un proveedor autorizado.** Es material formativo. No se
> conecta con entidades reales, no procesa dinero y no sustituye la inscripción
> o autorización ante ningún supervisor.

## Qué demuestra

| Pieza | Decisión de diseño que demuestra | Clase |
|---|---|---|
| `consent_dashboard` | Alcance por finalidad, plazo absoluto, revocación con efecto | 5 |
| `authorization_server` | PKCE obligatorio, `redirect_uri` exacta, código de un solo uso | 6 |
| `bank_api` | Importe como cadena decimal, cursor sobre orden total, errores indistinguibles | 4, 8, 9 |
| `payment_initiation` | Idempotencia con huella canónica y bloqueo, estados reales | 8, 10 |
| `third_party_provider` | Minimización: descarte en la ingesta | 12 |
| `conformance_tests` | 16 casos negativos y limitaciones declaradas | 13, 14 |

## Estructura

```text
apps/open_finance_sandbox/
├── README.md
├── __init__.py                 # ensambla el entorno: build()
├── authorization_server/       # /authorize y /token con PKCE
├── bank_api/                   # cuentas, saldos, movimientos
│   └── openapi.json            # contrato validado en CI
├── consent_dashboard/          # modelo de consentimiento y panel
│   └── cli.py                  # demostración de la revocación
├── payment_initiation/         # órdenes, idempotencia y estados
├── third_party_provider/       # el tercero: minimización e ingesta
├── conformance_tests/          # batería de cuatro familias
│   └── run.py
├── threat_models/              # amenazas priorizadas
└── data/                       # 6 cuentas y 216 movimientos sintéticos
```

## Uso

```bash
python apps/open_finance_sandbox/consent_dashboard/cli.py demo
```

```bash
python apps/open_finance_sandbox/conformance_tests/run.py
```

```bash
python tools/validate_openapi.py
```

```bash
python -m pytest tests/test_open_finance_sandbox.py -q
```

## En tres líneas

```python
from apps.open_finance_sandbox import build

sandbox = build()
concesion = sandbox.grant(["accounts:balances"])
print(sandbox.bank.balances(concesion.access_token, "acc_0100"))
```

Y la demostración que importa —el segundo posterior a una revocación—:

```python
sandbox.consents.revoke(concesion.consent_id, actor="cliente", reason="demo")
sandbox.bank.balances(concesion.access_token, "acc_0100")  # AuthError
```

## Datos

Seis cuentas y 216 movimientos generados con semilla fija. **Dos movimientos
comparten fecha a propósito**: sin desempate por identificador, el cursor tendría
el mismo defecto que la paginación por desplazamiento, y la prueba
`test_paginacion_por_cursor_no_repite_ni_omite` no detectaría nada.

Ningún dato corresponde a una persona real. `tools/detect_pii.py` lo comprueba
en cada ejecución de CI.

## Claves de juguete

El servidor de autorización usa identificadores y secretos de juguete que viven
en el repositorio **a propósito**, porque el material necesita mostrar la forma
de un flujo completo. Fuera de un laboratorio, versionar eso sería un incidente
de seguridad. `tools/detect_secrets.py` distingue los dos casos.

## Límites declarados

- El canal se **simula**: no hay TLS, ni autenticación mutua, ni certificados de
  una autoridad del esquema. En una implementación real esos controles son
  obligatorios y su ausencia invalidaría todo lo demás.
- No hay liquidación real: el estado `liquidado` se simula.
- Una sola moneda. La multidivisa se trata en la Parte 18.
- La batería de conformidad prueba la implementación contra su contrato, **no
  contra la norma**. Que pase no significa que la actividad esté autorizada.
- No se ejecuta carga sostenida, solo una ráfaga corta.

## Referencias

- [Parte 17 — Finanzas abiertas, APIs y economía de datos](../../modules/16-finanzas-abiertas-apis-y-economia-de-datos/README.md)
- [Modelo de amenazas](threat_models/README.md)
