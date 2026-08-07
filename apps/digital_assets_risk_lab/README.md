# Digital Assets Risk Lab

Laboratorio de riesgo de activos digitales de la **Parte 20**. Ocho módulos que
implementan la clasificación por promesa, el análisis de reservas, la cola de
redención, la espiral algorítmica, la custodia por umbral, la profundidad de
mercado y el grafo de contagio, **con la biblioteca estándar y sin red**.

> ## Aviso
>
> **Todo lo que hay aquí es didáctico y trabaja con datos sintéticos.** No se
> conecta a ninguna red, no mueve fondos, **no crea ningún activo** y **no
> recomienda ninguna inversión**. No contiene, ni contendrá, herramientas para
> ocultar fondos, evadir controles ni eludir obligaciones de cumplimiento.

## Qué demuestra ejecutando

Seis afirmaciones que se repiten mucho y se comprueban poco:

| Afirmación habitual | Lo que el laboratorio demuestra | Clase |
|---|---|---|
| «La cobertura subió, vamos mejor» | Sube mientras la composición empeora | 4 |
| «La corrida la causó el pánico» | La causa el orden de la cola | 5 |
| «El ratio de absorción está sano» | Sube durante todo el colapso | 7 |
| «Es un 3 de 5, es robusto» | Puede tener independencia efectiva 1 | 12 |
| «Mueve 184 millones al día» | Absorbe 2 con un 1 % de impacto | 13 |
| «No tenemos exposición» | Cero directo, 117 millones de liquidez | 14 |

## Estructura

```text
apps/digital_assets_risk_lab/
├── README.md
├── __init__.py
├── classification.py  ficha de cinco preguntas y rastreo de respaldo
├── reserves.py        coberturas, descuentos y punto de no retorno
├── redemption.py      orden de llegada, prorrateo y antidilución
├── depeg.py           banda de no arbitraje, fases y vigilancia
├── algorithmic.py     espiral de dos tokens y descomposición del rendimiento
├── custody.py         independencia efectiva, recuperación y retiradas
├── market.py          libro, profundidad, impacto y límite de posición
├── contagion.py       grafo, segundo grado y dependencias comunes
└── cli.py
```

## Uso

Ver cómo la cobertura sube mientras el riesgo empeora:

```bash
python apps/digital_assets_risk_lab/cli.py reserves --redemption 0.35
```

Comparar orden de llegada con prorrateo:

```bash
python apps/digital_assets_risk_lab/cli.py queue
```

Ejecutar la espiral de un diseño de dos tokens:

```bash
python apps/digital_assets_risk_lab/cli.py spiral --rounds 5
```

Medir la independencia efectiva de un esquema de custodia:

```bash
python apps/digital_assets_risk_lab/cli.py custody
```

Contrastar volumen con profundidad:

```bash
python apps/digital_assets_risk_lab/cli.py market --position 12000000
```

Calcular la exposición económica de quien declara cero:

```bash
python apps/digital_assets_risk_lab/cli.py contagion
```

## Pruebas

```bash
python -m pytest tests/test_digital_assets_risk_lab.py -q
```

Cinco de ellas **documentan defectos y deben pasar**:

- `test_la_cobertura_sube_mientras_la_composicion_empeora_documenta_el_problema`
- `test_el_orden_de_llegada_premia_al_primero_documenta_el_problema`
- `test_el_ratio_de_absorcion_sube_durante_el_colapso_documenta_el_problema`
- `test_un_3_de_5_puede_tener_independencia_efectiva_1_documenta_el_problema`
- `test_los_dos_cocientes_dan_conclusiones_opuestas_documenta_el_problema`
- `test_exposicion_cero_con_38_millones_en_riesgo_documenta_el_problema`

Sin ellas, el material afirmaría cosas que el código no sostiene.

## Decisiones de diseño que conviene mirar

**La clasificación no mira la tecnología.** `clasificar()` recibe una ficha de
cinco preguntas y ninguna es técnica. Es deliberado: si para clasificar hace
falta mirar el código, se está mirando el sitio equivocado.

**El descuento crece con el tamaño.** `coste_de_vender(..., escalera=True)`
multiplica el descuento por 1,5 cada mil millones. Con descuento constante el
punto de no retorno se aleja tanto que deja de existir, y esa es exactamente la
conclusión falsa que se quiere evitar.

**La venta que agota el libro exige declarar el precio de cola.** `Libro.vender`
lanza `ValueError` si no se le da. Un modelo que rellena el hueco con un supuesto
invisible produce una cifra que nadie revisa.

**El ratio de absorción se calcula aunque sea el indicador equivocado.** Está en
`algorithmic.py` precisamente para poder demostrar que sube mientras el sistema
cae, junto a `emision_por_unidad`, que es el que funciona.

**La probabilidad de bloqueo supone independencia.** Y la función que la calcula
convive con `tolera_evento_correlacionado()`, porque la primera solo es
defendible después de que la segunda sea verdadera.

## Límites declarados

- Los descuentos por tramo son **supuestos declarados**, no observaciones de
  mercado. Cambiarlos cambia la conclusión, y por eso están en una constante
  visible y no escondidos en una fórmula.
- El traslado lineal de pérdidas al capital sirve para **ordenar** contrapartes,
  no para predecir importes: en un concurso la recuperación depende de la
  prelación y del tiempo.
- El impacto de mercado lineal por importe vendido es una simplificación; en
  tensión el libro desaparece y el impacto no es lineal.
- El modelo de independencia usa cuatro factores; en la práctica hay más.
- Todos los instrumentos, carteras, libros y entidades son **sintéticos** y no
  representan a ningún emisor, plataforma ni organización real.

## Referencias

- [Parte 20 — Activos digitales, stablecoins y dinero programable](../../modules/19-activos-digitales-stablecoins-y-dinero-programable/README.md)
- [Etapa 5](../../docs/etapa-5-finanzas-digitales.md)
