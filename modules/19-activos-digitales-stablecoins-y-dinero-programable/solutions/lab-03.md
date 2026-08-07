# Solución de referencia — Laboratorio 3: cola de redención

> Material docente.

## La corrida la causa el diseño de la cola

Es el hallazgo del laboratorio y de la clase 5.

```python
def test_el_orden_de_llegada_premia_al_primero_documenta_el_problema():
    resultado = _cola().resolver(Regla.ORDEN_DE_LLEGADA)
    assert resultado.ventaja_del_primero == pytest.approx(1.0)

    fracciones = [p.fraccion for p in resultado.pagos]
    assert fracciones[0]  == pytest.approx(1.0)   # cobra todo
    assert fracciones[-1] == pytest.approx(0.0)   # no cobra nada
```

**Esta prueba debe pasar.** Documenta que con orden de llegada ser el primero
vale el 100 % del importe, y todo tenedor racional lo sabe. No hace falta pánico:
basta con saber que los demás también lo saben.

## Los dos resultados

```text
                          ORDEN DE LLEGADA      PRORRATEO

  primeros 6 000          100 %                 50 %
  últimos 6 000             0 %                 50 %

  ventaja del primero     1,0000                0,0000
```

## La antidilución y a quién protege

```python
sin = _cola(antidilucion=False).resolver(Regla.PRORRATEO)
con = _cola(antidilucion=True ).resolver(Regla.PRORRATEO)

assert sin.coste_total == 0        # lo pagan los que se quedan
assert con.coste_total >  0        # lo paga quien sale
```

El coste de realizar activos es real (laboratorio 2: 1,112 % en este caso). Sin
comisión antidilución lo soportan **los que permanecen**, que es exactamente el
premio por salir primero. Con ella, redimir sin necesidad deja de ser gratis.

## El tramo mínimo íntegro

```python
def test_el_tramo_minimo_integro_protege_al_pequeno_sin_reabrir_la_carrera():
    pequeno = ...  # solicita 6 000
    grande  = ...  # solicita 150 000

    assert pequeno.pagado >= 5_000
    assert pequeno.fraccion > grande.fraccion

    grandes = [p.fraccion for p in resultado.pagos if p.tenedor.startswith("grande")]
    assert max(grandes) - min(grandes) < 0.01     # sin carrera entre ellos
```

La segunda comprobación es la importante. El tramo mínimo protege al minorista y
**el grande sigue prorrateado**, de modo que la ventaja de ser primero sigue
siendo cero para quien podría provocar la corrida.

## El día siguiente

```text
ORDEN DE LLEGADA
  vuelven todos los que no cobraron   900 000 000
  más nuevos por miedo                625 000 000
  total                             1 525 000 000

PRORRATEO CON ANTIDILUCIÓN
  vuelven los que necesitan          360 000 000
  nuevos, sin ventaja por correr     150 000 000
  total                               510 000 000

DIFERENCIA: casi tres veces
```

La diferencia entre 1,11 % y 0 % de ventaja decide si hay corrida o no.

## Ventana propuesta

| Parámetro | Valor | Justificación |
|---|---|---|
| Regla | Prorrateo | La ventaja del primero es cero |
| Ventana | 4 horas | Suficiente para agregar, corta para el cliente |
| Comisión antidilución | Coste real de realización | El coste lo soporta quien lo causa |
| Tramo mínimo íntegro | 5 000 | Protege al minorista sin reabrir la carrera |
| Plazo máximo de inmovilización | 2 días hábiles | Acota el intervalo sin instrumento ni dinero |
| Reanudación | A prorrata de lo pendiente | Reanudar por turno reabre la carrera entera |

## Cláusula de suspensión

```text
1 CAUSA
    tasada: imposibilidad material de valorar la reserva,
    requerimiento de autoridad competente o fallo técnico
    verificado. NO «a criterio del emisor».

2 PLAZO
    máximo de 5 días hábiles, prorrogable una sola vez
    con comunicación motivada.

3 AVISO
    en un plazo máximo de 2 horas desde la decisión,
    por los mismos canales por los que se opera.

4 REANUDACIÓN
    a prorrata de todo lo pendiente acumulado durante
    la suspensión, no por orden de llegada.
```

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Culpar al pánico | El diseño crea el incentivo |
| Orden de llegada por defecto | Parece justo y produce la corrida |
| Prorrateo sin tramo mínimo | El minorista se queda sin efectivo |
| Sin antidilución | El coste lo pagan los que se quedan |
| Suspensión «a criterio» | No es una causa: es una carta blanca |
| Reanudar por turno | Reabre la carrera al reabrir |

## Límites

- El modelo supone que todas las solicitudes llegan en la misma ventana; en la
  práctica llegan de forma continua y el prorrateo exige definir cortes.
- La proporción de tenedores que «necesita el dinero» es un supuesto y no se
  observa: se estima con el histórico del propio emisor.
- El modelo no incluye la venta en mercado secundario, que compite con la
  redención y suaviza la cola para quien puede vender.
