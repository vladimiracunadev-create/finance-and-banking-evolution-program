# Laboratorio 6: Interconexión de pagos inmediatos

## Propósito

Enlazar dos sistemas de pagos inmediatos y resolver los seis problemas del
enlace, de los que cinco no son técnicos.

## Escenario

Los bancos centrales de `País P` y `País Q` te encargan el diseño del enlace. Los
dos sistemas funcionan, son 24/7 y hablan ISO 20022. El equipo técnico dice que
«es conectar dos APIs». Tu tarea es demostrar qué falta.

## Contexto

Un enlace baja el coste del tramo técnico y deja intacto el coste de todo lo
demás. El análisis que importa no es el del 71 % que se beneficia: es el del
29 % que queda fuera.

## Datos

`apps/cross_border_payments_lab/data/instant_link.json` — parámetros de los dos
sistemas, cobertura de cuentas en destino y cotizaciones de cuatro proveedores
de liquidez.

## Supuestos del ejercicio

- Ambos sistemas liquidan en segundos y operan 24/7.
- El límite del sistema de destino es el menor de los dos.
- Los proveedores de liquidez cotizan cada 30 segundos.
- No hay red real: la liquidación se simula.

## Requisitos

- Laboratorios 1 y 2 completados.
- Haber leído las clases 8, 9 y 13.

## Pasos

1. Implementa la **resolución de alias**: teléfono o identificador → cuenta y
   banco, con confirmación de nombre antes de pagar.
2. Añade límite de consultas por origen: sin él, el servicio permite enumerar.
3. Implementa el **cambio de divisa en el enlace** (diseño B): subasta entre los
   proveedores de liquidez, con el mejor tipo ganador.
4. Modela el caso de **un solo proveedor** y mide el efecto en el diferencial.
5. Implementa la liquidación: dos pagos domésticos y la posición del proveedor.
6. Aplica el **límite de importe** del sistema menor y mide qué proporción del
   corredor queda fuera.
7. Calcula la **cobertura real**: importe y canal del beneficiario.
8. Escribe las **cinco reglas mínimas**: ley aplicable, responsabilidad por pago
   no autorizado, plazo de devolución, arbitraje de disputas y contingencia si
   un sistema cae.

## Arquitectura

```text
ordenante ──► sistema P ──► ENLACE ──► sistema Q ──► beneficiario
                              │
                              ├── resolución de alias
                              ├── confirmación de nombre
                              ├── subasta de liquidez
                              └── liquidación de las dos patas

proveedor de liquidez: recibe P, entrega Q, gestiona su posición
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Confirmación de nombre antes de pagar | Prueba con nombre distinto |
| 2 | Límite de consultas de alias | Prueba de enumeración |
| 3 | Subasta con el mejor tipo | Prueba con cuatro cotizaciones |
| 4 | Con un proveedor, el diferencial sube | Prueba comparativa |
| 5 | El límite del sistema menor se aplica | Prueba de importe alto |
| 6 | La cobertura real se calcula y se publica | Informe del corredor |
| 7 | Las cinco reglas están escritas | Revisión del documento |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Enumeración por alias | Se descubre quién tiene cuenta | Límite y confirmación de nombre |
| Proveedor único | Diferencial sin presión | Mínimo de dos y revisión del modelo |
| Pago al beneficiario equivocado | Pérdida irreversible | Confirmación de nombre |
| Un sistema cae a mitad | Pago a medias | Procedimiento de contingencia |
| Exclusión del segmento sin cuenta | La brecha crece | Entrega alternativa en fase 1 |
| Ley aplicable indefinida | Disputa sin foro | Regla escrita antes de operar |

## Pruebas

```bash
python -m pytest tests/test_cross_border_payments_lab.py -q -k link
```

```bash
python apps/cross_border_payments_lab/cli.py link --amount 300 --alias +5551234567
```

## Entregables

- El enlace funcional con resolución de alias y subasta.
- El cálculo de cobertura real y del segmento excluido.
- La comparación con uno y con cuatro proveedores de liquidez.
- Las cinco reglas mínimas escritas.
- `solution.md` con la propuesta de mitigación del segmento excluido.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Resolución de alias con sus controles | 20 |
| Subasta de liquidez y su sensibilidad | 20 |
| Cobertura real calculada y publicada | 20 |
| Mitigación del segmento excluido | 25 |
| Las cinco reglas escritas | 15 |

## Solución de referencia

En [`solutions/lab-06.md`](../solutions/lab-06.md).
