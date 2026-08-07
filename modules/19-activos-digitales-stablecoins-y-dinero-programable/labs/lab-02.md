# Laboratorio 2: Análisis de una cartera de reservas

## Propósito

Comprobar ejecutando que **la cobertura publicada puede subir mientras el riesgo
empeora**, y que el descuento por venta forzada cambia la conclusión.

## Escenario

Un emisor publica una cobertura del 102,3 %. Hay que calcular qué queda de esa
cartera tras una redención del 35 % en 24 horas y decidir si el remanente
soporta un segundo golpe.

## Contexto

La clase 4 sostiene que una reserva tiene tres cifras y solo se publica la
primera. La clase 15 añade el efecto de la clasificación contable sobre el
balance de quien la mantiene.

## Datos

Cartera sintética de 8 593 200 000 sobre un circulante de 8 400 000 000, con seis
tramos.

## Supuestos del ejercicio

- Los descuentos por tramo están declarados en `DESCUENTO_BASE` y son supuestos,
  no observaciones.
- La escalera multiplica el descuento por 1,5 cada mil millones vendidos.
- El orden de venta es de coste creciente.

## Requisitos

- Laboratorio 1 completado.
- Haber leído las clases 4 y 15.

## Pasos

1. Construye la cartera y calcula cobertura contable, cobertura líquida y peso
   ilíquido.
2. Construye una segunda cartera con **la misma cobertura contable** y
   composición distinta, y compara sus coberturas líquidas.
3. Atiende una redención del 35 % y anota el coste de venta.
4. Recalcula las tres métricas y demuestra que **la cobertura sube y el peso
   ilíquido también**.
5. Repite con `escalera=True` y compara el coste.
6. Calcula el punto de no retorno con `punto_de_no_retorno` y exprésalo como
   porcentaje del circulante.
7. Aplica un segundo golpe del 35 % sobre el remanente y decide si lo soporta.
8. Escribe las cinco preguntas al informe de atestación y respóndelas sobre un
   informe real.

## Arquitectura

```text
Cartera(circulante, tramos)
   ├── cobertura_contable    la cifra publicada
   ├── cobertura_liquida     la que paga redenciones
   └── peso_iliquido         la que anticipa el problema

atender(cartera, importe, escalera)
   vende por orden de coste creciente y DEJA
   la cartera deteriorada: ese es el punto
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Dos carteras iguales en cobertura difieren en liquidez | Comparación directa |
| 2 | La redención del 35 % está cubierta | `cubierta` verdadero |
| 3 | El coste de venta es 1 862 794 | Comparación exacta |
| 4 | La cobertura sube tras la redención | Antes y después |
| 5 | El peso ilíquido empeora | Antes y después |
| 6 | La escalera encarece la venta | Comparación con descuento plano |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Valorar a precio de pantalla | Se sobreestima lo realizable | Descuento por tramo |
| Descuento constante | El punto de no retorno se aleja | Escalera creciente |
| Mirar solo la cobertura | El deterioro pasa inadvertido | Publicar composición y plazo |
| Un solo escenario | El segundo golpe no se prueba | Dos redenciones seguidas |
| Confundir atestación con auditoría | Se sobrevalora el informe | Cinco preguntas al alcance |

## Pruebas

```bash
python -m pytest tests/test_digital_assets_risk_lab.py -q -k "cobertura or redencion or escalera or punto"
```

```bash
python apps/digital_assets_risk_lab/cli.py reserves --redemption 0.35
```

## Entregables

- La descomposición de la cartera con las tres métricas.
- El resultado de la redención con su coste.
- La demostración de que la cobertura sube mientras el riesgo empeora.
- El punto de no retorno como porcentaje del circulante.
- `solution.md` con las cinco preguntas al informe, respondidas.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Cálculo de las tres coberturas | 20 |
| Redención con coste correcto | 20 |
| Demostración del deterioro | 25 |
| Punto de no retorno con escalera | 20 |
| Preguntas al informe | 15 |

## Solución de referencia

En [`solutions/lab-02.md`](../solutions/lab-02.md).
