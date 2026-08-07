# Solución de referencia — Laboratorio 1: transferencia con corresponsales

> Material docente. Corrige el **criterio**, no la coincidencia literal.

## Descomposición del tiempo, escenario base

Pago ordenado el martes a las 16:40 hora de Santiago.

| Tramo | Causa del tiempo | Duración |
|---|---|---:|
| Validación y controles internos | Proceso propio | 2 min |
| Screening en origen | Proceso propio | 5 min |
| Mensaje CL → NY | Mensajería | 2 s |
| Liquidación en Nueva York | Ventana abierta | 31 min |
| Mensaje NY → SG | Mensajería | 2 s |
| Espera a la apertura de Singapur | **Huso horario** | 15 h 40 min |
| Liquidación en Singapur | Ventana | 20 min |
| Acreditación del banco vietnamita | Proceso del receptor | 2 h |
| **Total** | | **18 h 38 min** |

```text
MENSAJERÍA:      6 segundos           0,01 %
PROCESO PROPIO:  7 minutos            0,63 %
VENTANAS:        51 minutos           4,56 %
HUSO HORARIO:    15 h 40 min         84,08 %
PROCESO AJENO:   2 horas             10,73 %
```

La conclusión que el laboratorio busca: **el 84 % del tiempo es huso horario**.
Optimizar el software del banco actúa sobre el 0,63 %.

## Escenario con festivo

Mismo pago, ordenado el jueves, con festivo el viernes en Singapur.

```text
mensaje llega a SG el viernes 03:41 hora local
viernes: festivo → no liquida
sábado y domingo: no liquida
lunes 09:00: liquida

TOTAL: 3 días 18 horas
```

El mensaje siguió tardando 6 segundos.

## El error que se penaliza

Modelar un solo flujo. Si el simulador solo tiene mensajes, el pago con festivo
tarda lo mismo que el normal, y el laboratorio no demuestra nada.

## Estructura mínima esperada

```text
cross_border_payments_lab/
├── flows/
│   ├── message.py      latencia por salto
│   ├── funds.py        ventanas, husos, calendarios
│   ├── accounting.py   asientos nostro y vostro
│   └── compliance.py   screening por eslabón
└── trace.py            informe de descomposición
```

## La prueba que importa

```python
def test_el_mensaje_no_espera_a_los_fondos(sandbox):
    traza = sandbox.pagar(corredor="CL-VN", importe=10_000, hora="16:40")

    assert traza.mensaje.duracion_segundos < 10
    assert traza.fondos.duracion_horas > 15
    # y, sobre todo: son independientes
    assert traza.mensaje.completado_en < traza.fondos.completado_en
```

## Contabilidad: la comprobación de suma cero

```python
def test_cada_asiento_tiene_contrapartida(traza):
    for eslabon in traza.contable:
        assert sum(a.importe for a in eslabon.asientos) == 0
```

Un asiento sin contrapartida es un descuadre que la conciliación del mes
siguiente tendrá que encontrar (clase 4).

## Cumplimiento: el detalle que se olvida

Una alerta detiene el **flujo de fondos**, no el de mensaje. El mensaje ya salió
y el eslabón siguiente lo tiene. Si el modelo detiene los dos, no reproduce el
caso real de «el banco dice que ya salió y el dinero no llega».

## Límites

- Las latencias y ventanas son parámetros del ejercicio, no medidas reales.
- No se modela el reintento ni la investigación: eso es el laboratorio 3.
- El screening usa una probabilidad fija; el laboratorio 4 lo trata en serio.
