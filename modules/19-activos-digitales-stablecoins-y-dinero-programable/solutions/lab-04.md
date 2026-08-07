# Solución de referencia — Laboratorio 4: anatomía de una pérdida de paridad

> Material docente.

## Un arbitraje rentable que nadie ejecuta es la señal

Es el hallazgo del laboratorio y de las clases 3 y 6.

```text
PRECIO 0,9940 · TAMAÑO 2 400 000

  bruto                                14 400
  comisión de redención (0,10 %)        2 400
  operación en registro                    12
  financiación 2 días al 5,20 %            689
  NETO                                 11 299

  rentabilidad         0,474 % en 2 días
  ANUALIZADA          85,3 %

SI RINDE UN 85 % Y NADIE LO HACE,
EL CANAL DE REDENCIÓN ESTÁ CERRADO.
```

## La banda de no arbitraje

```python
def test_la_paridad_no_es_un_punto_sino_una_banda():
    bajo, alto = banda_de_no_arbitraje(_costes(), 2_400_000)
    assert bajo == pytest.approx(0.99871, abs=0.00002)
    assert alto == pytest.approx(1.00129, abs=0.00002)
```

```text
coste por unidad
  comisión        0,001000
  financiación    0,000289
  operación       0,000005
  TOTAL           0,001294  ≈ 12,9 puntos básicos

BANDA: 0,99871 – 1,00129
Dentro de ella, el desvío es normal y nadie arbitra.
```

## El mínimo de redención elimina la banda para el pequeño

```python
def test_quien_no_alcanza_el_minimo_no_puede_arbitrar():
    resultado = arbitraje_rentable(0.9940, _costes(), 40_000)
    assert not resultado["puede_arbitrar"]
```

Para el tenedor de 40 000 no hay banda: el precio de mercado es el único precio,
y su pérdida es de 240 sin que nada se lo compense.

## El indicador de desvío persistente

```python
vigilancia = VigilanciaDeDesvio(banda=(0.99871, 1.00129), horas_para_alerta=6)
for _ in range(5):
    vigilancia.observar(0.9940)
assert not vigilancia.en_alerta

vigilancia.observar(0.9940)
assert vigilancia.en_alerta          # sexta hora consecutiva
```

**Volver a la banda reinicia el contador**, y es correcto: un desvío que se
corrige demuestra que el arbitraje opera, que es justo lo que se quiere medir.

## Los dos episodios

```text
CANAL QUE FUNCIONA
  1 detonante        efectivo atrapado en un depositario
  3 prueba del canal el emisor pagó vendiendo letras
  → episodio cerrado en horas
  → canal_funciono = True
  → llego_a_realizacion_forzada = False

CANAL QUE NO FUNCIONA
  1 detonante        informe filtrado sobre las reservas
  3 prueba del canal la redención se suspendió
  4 carrera          todos solicitan
  5 realización      venta con descuento creciente
  → la noticia deja de ser el detonante:
    pasa a ser «no se puede salir»
```

La fase 3 es la que decide. Todo lo anterior es anécdota operativa; todo lo
posterior es irreversible.

## Punto de no retorno

```text
MARGEN = 1,45 % del circulante = 174 000 000

ESCALERA DE DESCUENTOS SOBRE DEUDA 1–3 AÑOS
  1.º millar de millones   1,40 %  →  14 000 000
  2.º                      2,10 %  →  21 000 000
  3.º                      3,20 %  →  32 000 000
  4.º                      4,80 %  →  48 000 000
  5.º                      7,00 %  →  70 000 000

  acumulado tras 4 000 M: 115 000 000
  acumulado tras 5 000 M: 185 000 000

  PUNTO ≈ 4 840 000 000 de venta de deuda
  → redención acumulada ≈ 9 280 000 000
  → 77 % del circulante

INDICADOR OPERATIVO
  vigilar la redención acumulada frente al 77 %,
  no la cobertura publicada.
```

## Ante una recuperación del precio

```python
assert recuperacion_corrige_la_causa("se reanudó la redención")

for motivo in ("liquidez externa del emisor",
               "un tercero compró para sostener",
               "dejó de haber vendedores"):
    assert not recuperacion_corrige_la_causa(motivo)
```

Preguntas obligatorias:

1. ¿Se reanudó la redención, y con qué condiciones?
2. ¿Qué queda en la reserva y en qué proporción es líquida?
3. ¿Cuántos participantes autorizados siguen activos?
4. ¿Cambió la cláusula de suspensión?

Si las cuatro respuestas son «igual que antes», el mecanismo sigue intacto y el
siguiente detonante encontrará una reserva peor.

## Separación de capas

| Capa | Contenido |
|---|---|
| **Hecho** | El 55 % del efectivo quedó indisponible; el emisor pagó el lunes vendiendo letras |
| **Supuesto** | Recuperación del 90 %, escalera de descuentos, orden de venta |
| **Interpretación** | Es un episodio de disponibilidad, no de solvencia, y solo se vuelve de solvencia si la venta forzada supera el margen |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Explicar el episodio por el detonante | El detonante no se repite |
| Banda de cero | Se confunde ruido con crisis |
| Comprar el desvío | Es una señal, no una oportunidad |
| Vigilar la cobertura | Sube mientras el riesgo empeora |
| Dar por cerrado el caso | Pregunta qué cambió en el canal |
| Descuento constante | Aleja el punto de no retorno |

## Límites

- La escalera de descuentos es un supuesto del analista: ningún informe de
  reservas la publica, y cada institución debe estimarla por su cuenta.
- El modelo no incluye la intervención de una autoridad, que en la práctica
  cambia el desenlace de varios episodios históricos.
- Las series de precio son sintéticas y están construidas para reproducir el
  mecanismo, no para representar ningún episodio concreto.
