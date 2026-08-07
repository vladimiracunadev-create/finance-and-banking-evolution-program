# Solución de referencia — Laboratorio 7: Payment versus Payment

> Material docente.

## Exposición máxima simultánea

El error habitual es tomar la operación mayor. La exposición se acumula:

```python
def exposicion_maxima(operaciones: list[Operacion]) -> Decimal:
    eventos = []
    for op in operaciones:
        eventos.append((op.hora_entrega, +op.importe))
        eventos.append((op.hora_recepcion, -op.importe))
    eventos.sort()

    viva = maxima = Decimal(0)
    for _, delta in eventos:
        viva += delta
        maxima = max(maxima, viva)
    return maxima
```

Con las tres operaciones del ejemplo (40 M, 25 M, 30 M), la exposición máxima es
**95 M** entre las 14:00 y las 15:00, no 40 M.

## El mecanismo, y el detalle que lo hace correcto

```python
def liquidar_pvp(op: Operacion, sistema_a, sistema_b, plazo_s: int) -> Resultado:
    reserva_a = sistema_a.reservar(op.pata_a, plazo_s)
    if not reserva_a.ok:
        return Resultado.fallido("reserva A")

    reserva_b = sistema_b.reservar(op.pata_b, plazo_s)
    if not reserva_b.ok:
        sistema_a.deshacer(reserva_a)          # ← atomicidad
        return Resultado.fallido("reserva B")

    # Punto crítico: si el coordinador cae AQUÍ, las dos reservas
    # quedan vivas. Por eso la reserva lleva plazo propio y los
    # sistemas la deshacen solos: la seguridad no puede depender
    # de que el coordinador siga en pie.
    sistema_a.liberar(reserva_a)
    sistema_b.liberar(reserva_b)
    return Resultado.liquidado()
```

La corrección busca que el plazo de reserva viva **en cada sistema**, no en el
coordinador. Un plazo gestionado por el coordinador no protege del fallo del
coordinador.

## Los dos escenarios de fallo

```text
ESCENARIO 1 · el coordinador cae tras ambas reservas
  ambas reservas expiran a los N segundos
  ambos sistemas deshacen
  exposición final: 0
  coste: liquidez inmovilizada durante N segundos
  → el mecanismo se comporta bien

ESCENARIO 2 · el sistema A libera y el B falla al liberar
  la pata A se liquidó; la B no
  exposición: el importe completo, sin protección

  ESTE ES EL CASO PELIGROSO, y hay que documentarlo:
  la atomicidad del protocolo no cubre un fallo
  posterior a la primera liberación

  MITIGACIONES POSIBLES
    · liberación en un solo asiento (liquidador central)
    · confirmación previa de capacidad de liberar
    · procedimiento de compensación acordado
```

Un laboratorio que no ejecuta el escenario 2 no ha entendido para qué sirve el
mecanismo. La atomicidad es una propiedad del protocolo, no una garantía
absoluta.

## Coste frente a capital liberado

```text
COSTE ANUAL
  cuota                              240 000
  operaciones 27 900 × 1,20           33 480
  prefinanciación 85 M × 4,1 %     3 485 000
  TOTAL                            3 758 480

BENEFICIO
  pérdida esperada evitada         4 120 000   ← supuesto frágil
  coste de capital liberado
    28,4 M × 11 % × 74 %           2 311 760   ← dato del banco
  TOTAL                            6 431 760

MARGEN                             2 673 280
```

La lección de método: el primer componente depende de una probabilidad que nadie
puede estimar; el segundo es un dato del propio banco. **Cuando una decisión
depende de un número inventado, hay que buscar el argumento que no dependa de
él.** Con la probabilidad más baja del rango, el margen sigue siendo positivo
gracias al capital.

## Los riesgos que persisten

| Riesgo | ¿Lo cubre el PvP? | Control necesario |
|---|:---:|---|
| Entregar sin recibir | Sí | — |
| Reposición al precio nuevo | No | Límite por contraparte |
| Liquidez inmovilizada | No | Gestión del saldo (clase 8) |
| Fallo del coordinador | Parcial | Plazo en cada sistema |
| Fallo tras la primera liberación | **No** | Documentado, con mitigación |
| Concentración en el liquidador | No, la agrava | Contingencia declarada |
| Bloqueo no oponible en quiebra | No | Verificación jurídica |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Exposición = mayor operación | Ignora la acumulación |
| Plazo gestionado por el coordinador | No protege de su fallo |
| No ejecutar el escenario 2 | Es el que enseña el límite del mecanismo |
| Omitir la prefinanciación del coste | Es el componente mayor |
| Decidir solo con la pérdida esperada | Depende de un número inventado |

## Límites

- Los sistemas de liquidación son simulados y no reproducen sus reglas reales de
  finalidad.
- La oponibilidad del bloqueo en un procedimiento de insolvencia es una cuestión
  jurídica por jurisdicción que el laboratorio no resuelve.
- No se modela el fondo de garantía de un mecanismo con compensación
  multilateral.
