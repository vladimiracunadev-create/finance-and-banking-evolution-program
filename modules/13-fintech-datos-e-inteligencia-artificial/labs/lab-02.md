# Laboratorio 2: APIs financieras

## Propósito

Diseñar un consentimiento con alcance por finalidad y **probar el orden correcto de la revocación**.

El laboratorio 1 dio el marco. Este entra en el eslabón que se desagregó por norma, donde el consentimiento es el régimen y la interfaz solo el medio.

## Escenario

Un agregador que quiere leer saldos, movimientos e información de créditos de los clientes de un banco, para tres finalidades distintas.

## Datos

Las tres finalidades con los datos que cada una necesita realmente.

## Supuestos del ejercicio

- Cada finalidad tiene un dato mínimo distinto.
- El consentimiento se otorga por finalidad y no en bloque.
- La revocación tiene que invalidar los tokens antes de responder al cliente.

## Pasos

1. Determina el dato mínimo de cada finalidad antes de mirar la interfaz.
2. Diseña los alcances de consentimiento, uno por finalidad.
3. Define la vigencia de cada uno y su renovación.
4. Construye la evidencia que reconstruye qué autorizó el cliente y cuándo.
5. Implementa la revocación y prueba que invalida antes de responder.
6. Mide la ventana entre invalidación y respuesta.
7. Diseña la idempotencia de una operación de pago con huella canónica.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El dato mínimo está determinado por finalidad | Antes de la interfaz |
| 2 | Los alcances son por finalidad | No en bloque |
| 3 | La evidencia reconstruye la decisión | Qué, para qué, cuándo |
| 4 | La revocación invalida antes de responder | Con la ventana medida |
| 5 | La idempotencia está implementada | Con huella canónica |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Pedir todo el alcance disponible | Es lo contrario de la minimización |
| Consentimiento en bloque | No resiste una revisión |
| Responder antes de invalidar | Deja una ventana de acceso indebido |
| Reintento no idempotente | Produce el pago duplicado más caro |

## Entregables

- `solution.md` con el dato mínimo de las tres finalidades.
- Los alcances diseñados con su vigencia.
- La prueba de revocación con su ventana medida.
- La implementación idempotente con su huella.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Dato mínimo | 25 |
| Alcances por finalidad | 25 |
| Evidencia | 15 |
| Revocación probada | 20 |
| Idempotencia | 15 |
