# Laboratorio 2: Servidor de autorización simulado

## Propósito

Implementar y romper un flujo de autorización. El objetivo no es que funcione:
es que **falle donde debe fallar**.

## Escenario

La institución proveedora del laboratorio 1 debe exponer un servidor de
autorización. El equipo propone «un endpoint que devuelve un token si el usuario
y la clave son correctos». Tienes que explicar por qué eso no es un servidor de
autorización y construir el que sí lo es.

## Contexto

En un flujo de autorización correcto, el proveedor de información **nunca ve las
credenciales del cliente**. Ese es el punto entero del diseño: sustituir el
reparto de contraseñas por la delegación acotada.

## Datos

`datasets/synthetic/open_finance_consents.csv` y las cuentas sintéticas de
`apps/open_finance_sandbox/bank_api/data/`.

## Supuestos del ejercicio

- Todo ocurre en `localhost`. No hay red externa.
- Las claves son de juguete y están en el repositorio a propósito: **jamás se
  hace esto fuera de un laboratorio**.
- El canal se simula; en producción sería TLS con autenticación mutua.

## Requisitos

- Python 3.11 o superior, biblioteca estándar.
- Comprensión de los conceptos de la clase 6.

## Pasos

1. Implementa el endpoint de autorización: recibe `client_id`, `redirect_uri`,
   `scope`, `state`, `code_challenge` y `code_challenge_method`.
2. Rechaza cualquier `redirect_uri` que no coincida **exactamente** con la
   registrada. Sin comodines, sin prefijos.
3. Autentica al usuario y presenta los alcances solicitados en lenguaje claro.
4. Emite un código de autorización de un solo uso, con vida menor a 60 segundos.
5. Implementa el endpoint de token: valida el código, el `code_verifier` y la
   identidad del cliente.
6. Emite un token de acceso con los alcances efectivamente concedidos, no con los
   solicitados.
7. Escribe pruebas negativas para cada uno de los siete ataques de la tabla.
8. Registra cada emisión y cada rechazo con causa.

## Arquitectura

```text
proveedor          navegador          servidor de           API de
de información     del cliente        autorización          recursos
      │                 │                   │                   │
      │─ 1. redirige ──►│                   │                   │
      │                 │─ 2. authorize ───►│                   │
      │                 │◄─ 3. login+scopes─│                   │
      │                 │─ 4. aprueba ─────►│                   │
      │◄─ 5. código ────│◄──────────────────│                   │
      │─ 6. token (code + code_verifier) ──►│                   │
      │◄─ 7. access_token ──────────────────│                   │
      │─ 8. GET /accounts (Bearer) ─────────────────────────────►│
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El código se usa una sola vez | Segundo canje devuelve error |
| 2 | PKCE es obligatorio | Petición sin `code_challenge` es rechazada |
| 3 | `redirect_uri` exacta | Variante con sufijo es rechazada |
| 4 | `state` se verifica | Respuesta sin `state` original es rechazada |
| 5 | Token acotado al alcance | Llamada fuera de alcance devuelve 403 |
| 6 | Código expirado no sirve | Prueba con reloj adelantado |
| 7 | Todo rechazo queda registrado | Revisión del registro |

## Amenazas a considerar

| Amenaza | Vector | Control |
|---|---|---|
| Intercepción del código | Aplicación pública sin secreto | PKCE (RFC 7636) |
| Redirección abierta | `redirect_uri` laxa | Coincidencia exacta registrada |
| Falsificación de petición | Falta de `state` | `state` aleatorio verificado |
| Repetición del código | Código reutilizable | Un solo uso y vida corta |
| Escalada de alcance | Token con más alcances | Alcance concedido, no solicitado |
| Confusión de cliente | `client_id` no verificado | Autenticación del cliente |
| Fuga por registro | Token escrito en el log | Nunca registrar el token completo |

## Pruebas

```bash
python -m pytest tests/test_open_finance_sandbox.py -q -k authorization
```

## Entregables

- `authorization_server/` funcional.
- Batería de pruebas negativas: una por amenaza.
- `solution.md` explicando por qué cada control existe.
- Registro de ejemplo con un rechazo de cada tipo.
- Tabla de supuestos y límites.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Flujo correcto extremo a extremo | 25 |
| PKCE y validación de redirección | 20 |
| Pruebas negativas completas | 25 |
| Registro y trazabilidad | 15 |
| Explicación del porqué de cada control | 15 |

## Solución de referencia

En [`solutions/lab-02.md`](../solutions/lab-02.md).
