# Solución de referencia — Laboratorio 2: motor de rutas

> Material docente.

## Por qué el orden de los criterios importa

Los tres primeros son **filtros**; los tres últimos son **factores**.

```text
FILTRO        elimina rutas. No se compensa con nada.
FACTOR        ordena las rutas que quedan.

SI SE PONDERAN LOS FILTROS
  una ruta muy barata que no soporta un control exigido
  puede ganar la comparación
  → el motor elige una operación no autorizada
```

Es el mismo principio de la clase 12: en sanciones no hay apetito de riesgo. Un
filtro de cumplimiento que se pondera deja de ser un control.

## Implementación de referencia

```python
def elegir(pago: Pago, rutas: list[Ruta], pesos: Pesos) -> Decision:
    elegibles = [r for r in rutas if r.admite(pago)]
    if not elegibles:
        return Decision(None, None, motivo="ninguna ruta admite este pago")

    conformes = [r for r in elegibles if r.soporta(pago.controles)]
    if not conformes:
        return Decision(None, None,
                        motivo=f"ninguna ruta soporta {pago.controles}")

    disponibles = [r for r in conformes if r.disponible_ahora()]
    if not disponibles:
        return Decision(None, None, motivo="todas las rutas no disponibles")

    # Regla de la clase 14: el enlace directo gana antes de ponderar.
    enlaces = [r for r in disponibles if r.tipo == "enlace_pagos_inmediatos"]
    if enlaces:
        elegida = min(enlaces, key=lambda r: r.coste_total(pago))
        return Decision(elegida, _siguiente(disponibles, elegida),
                        motivo="enlace de pagos inmediatos disponible")

    ordenadas = sorted(disponibles, key=lambda r: r.puntuacion(pago, pesos))
    return Decision(ordenadas[0], ordenadas[1] if len(ordenadas) > 1 else None,
                    motivo=_explicar(ordenadas[0], ordenadas, pesos))
```

## El campo `motivo`

```text
BIEN   «enlace de pagos inmediatos disponible»
BIEN   «menor coste total (2,4 % frente a 3,1 %) con plazo dentro
        del compromiso; la alternativa es 6 h más rápida y 0,7 pp más cara»
MAL    «mejor puntuación»
MAL    «ruta preferente»
```

Un motivo que no permite reconstruir la decisión no es un motivo: es una
etiqueta.

## Las pruebas que separan un buen motor de uno malo

```python
def test_un_filtro_no_se_compensa_con_precio(motor):
    barata_no_conforme = Ruta(coste=0.001, soporta_travel_rule=False)
    cara_conforme = Ruta(coste=0.05, soporta_travel_rule=True)
    pago = Pago(controles={"travel_rule"})

    decision = motor.elegir(pago, [barata_no_conforme, cara_conforme])

    assert decision.ruta is cara_conforme


def test_cambiar_un_peso_cambia_la_eleccion(motor):
    rapida_cara = Ruta(plazo_h=1, coste=0.04)
    lenta_barata = Ruta(plazo_h=30, coste=0.012)

    con_prisa = motor.elegir(pago, [rapida_cara, lenta_barata],
                             Pesos(tiempo=0.8, coste=0.2))
    con_precio = motor.elegir(pago, [rapida_cara, lenta_barata],
                              Pesos(tiempo=0.2, coste=0.8))

    assert con_prisa.ruta is rapida_cara
    assert con_precio.ruta is lenta_barata
```

## Configuración de pesos

Se versiona y se documenta, como el contrato de una API:

```json
{
  "version": "2026-08-06",
  "pesos": { "tiempo": 0.35, "coste": 0.50, "riesgo": 0.15 },
  "motivo_del_cambio": "el coste pesa mas tras la queja de la asociacion",
  "aprobado_por": "comite de pagos",
  "vigente_desde": "2026-08-06"
}
```

Sin `motivo_del_cambio` y `aprobado_por`, nadie puede explicar dentro de un año
por qué el motor elige lo que elige.

## Errores frecuentes en la corrección

| Error | Por qué se penaliza |
|---|---|
| Ponderar el cumplimiento | Convierte un control en una preferencia |
| Motor sin alternativa | Un corredor cae y no hay plan |
| Pesos codificados en el código | No se pueden auditar ni cambiar sin desplegar |
| Motivo genérico | No permite corregir una elección equivocada |
| Ignorar la frescura del dato de disponibilidad | Se enruta hacia una ruta caída |

## Límites

- La disponibilidad se simula con una serie histórica; en producción sería una
  señal en tiempo real con su propia latencia.
- El motor no negocia precio: en algunos corredores el diferencial se cotiza al
  momento (laboratorio 6).
