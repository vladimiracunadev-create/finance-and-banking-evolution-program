# Regulatory Perimeter Engine

Motor de perímetro regulatorio de la **Parte 22**. Cuatro módulos que implementan
la determinación de actividades por hechos observables, la calificación de
instrumentos, la verificación de cumplimiento y el ensamblaje del expediente,
**con la biblioteca estándar y sin red**.

> ## Aviso
>
> **Todo lo que hay aquí es didáctico y trabaja con casos sintéticos.** No
> constituye asesoría legal, no sustituye el criterio de un abogado y **no
> proporciona técnicas para eludir ninguna norma**. Su propósito es preparar una
> discusión con especialistas, no reemplazarla.

## Qué demuestra ejecutando

Cuatro afirmaciones habituales que el motor contrasta con hechos:

| Afirmación habitual | Lo que el motor demuestra | Clase |
|---|---|---|
| «Somos tecnología, no finanzas» | Siete regímenes activados y ninguno declarado | 1 |
| «Es un token de utilidad» | Cuatro criterios de valor cumplidos por la promoción | 3 |
| «Los fondos están en cuenta segregada» | Falta la renuncia del banco a compensar | 6 |
| «Trabajamos con 41 proveedores» | Que se apoyan en tres infraestructuras | 14 |

## Estructura

```text
apps/regulatory_perimeter_engine/
├── README.md
├── __init__.py
├── perimeter.py      seis preguntas sobre hechos, con fuente obligatoria
├── qualification.py  cuatro criterios y análisis del material de promoción
├── compliance.py     salvaguarda, vigilancia y concentración de terceros
├── dossier.py        doce piezas y su lectura cruzada por parejas
└── cli.py
```

## Uso

Determinar qué regímenes activa una entidad por sus hechos:

```bash
python apps/regulatory_perimeter_engine/cli.py perimeter
```

Calificar un instrumento y ver qué frase de la promoción lo cambia:

```bash
python apps/regulatory_perimeter_engine/cli.py qualification
```

Verificar salvaguarda, calibrar vigilancia y medir concentración:

```bash
python apps/regulatory_perimeter_engine/cli.py compliance
```

Ensamblar el expediente y cruzarlo por parejas:

```bash
python apps/regulatory_perimeter_engine/cli.py dossier
```

## Pruebas

```bash
python -m pytest tests/test_regulatory_perimeter_engine.py -q
```

Seis de ellas **documentan defectos o errores de razonamiento y deben pasar**:

- `test_una_entidad_puede_ejercer_siete_regimenes_sin_declarar_ninguno`
- `test_un_hecho_sin_fuente_no_es_observable_documenta_el_problema`
- `test_la_promocion_forma_parte_de_la_calificacion_documenta_el_problema`
- `test_la_salvaguarda_falla_en_la_renuncia_a_compensar_documenta_el_problema`
- `test_contar_proveedores_oculta_la_concentracion_documenta_el_problema`
- `test_la_remediacion_exige_medida_provisional_documenta_el_problema`

Sin ellas, el material afirmaría cosas que el código no sostiene.

## Decisiones de diseño que conviene mirar

**Un hecho sin fuente se rechaza.** `Hecho.__post_init__` lanza `ValueError` si
la fuente está vacía. Es la diferencia entre un hecho observable y una
declaración disfrazada: aceptar la segunda convierte el análisis en una
transcripción de lo que dice la entidad.

**La promoción se analiza, no se declara.** `frases_que_crean_expectativa()`
recorre el material con patrones en vez de preguntar al emisor si crea
expectativa. Es lo que hace de la calificación un análisis y no una preferencia.

**La asesoría exige dos hechos juntos.** Destacar instrumentos por sí solo es
discutible; destacar cobrando por ello, no. Los activadores son combinaciones de
hechos y no hechos sueltos precisamente por casos como este.

**La salvaguarda cuantifica cada fallo por separado.** `exposicion()` devuelve lo
que se pierde por compensación y lo que se pierde por conciliación, porque son
dos correcciones distintas con dos costes distintos.

**La concentración se mide dos veces.** `concentracion_por_proveedor()` da la
diversificación aparente y `concentracion_por_infraestructura()` la real. Están
las dos para poder contrastarlas: es el hallazgo de la clase 14.

**La remediación exige medida provisional.** `Remediacion.__post_init__` se niega
a construirse sin ella. Entre que se detecta un hallazgo y se corrige hay un
intervalo, y el cliente está expuesto durante ese intervalo.

**`revision_miro_donde_debia` es un control de calidad de la revisión.** Si todos
los hallazgos son de nivel ordinario, lo más probable no es que la entidad esté
perfecta: es que nadie cruzó las piezas.

## Límites declarados

- El motor cubre **ocho regímenes habituales**; una jurisdicción concreta puede
  tener más, y su lista es la que manda.
- Los activadores no modelan umbrales de importe ni de habitualidad, que en
  varias jurisdicciones deciden si una actividad queda dentro del perímetro.
- Los patrones de expectativa son una **heurística**: detectan las formulaciones
  habituales y no sustituyen la lectura del material completo.
- Los costes de cumplimiento por calificación son **supuestos declarados** y
  varían mucho entre mercados.
- La conclusión de `puede_operar()` es didáctica y **no sustituye ninguna
  resolución administrativa**.
- Todos los casos, entidades e instrumentos son sintéticos y no representan a
  ninguna organización real.

## Referencias

- [Parte 22 — Regulación de mercados financieros digitales](../../modules/21-regulacion-de-mercados-financieros-digitales/README.md)
- [Metodología de verificación regulatoria](../../docs/metodologia-verificacion-regulatoria.md)
- [Fichas normativas](../../regulatory/README.md)
- [Etapa 5](../../docs/etapa-5-finanzas-digitales.md)
