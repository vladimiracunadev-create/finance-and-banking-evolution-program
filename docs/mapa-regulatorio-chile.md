# Matriz normativa de Chile

**Qué norma alcanza a qué actividad, quién la supervisa y dónde se estudia.** Esta
matriz es una herramienta de orientación, no una fuente de derecho: su función es
que sepas **a qué puerta llamar y qué verificar**, no darte la respuesta.

Conviene decirlo antes de la primera tabla: el calendario real de exigibilidad de
casi todo lo que aparece aquí está en las **disposiciones transitorias de las
normas de carácter general**, no en el cuerpo de las leyes. Quien planifique
leyendo solo la ley planificará mal. Ese es el error más frecuente y el más caro.

---

## Cómo se lee esta matriz

```text
CADA FILA RESPONDE CUATRO PREGUNTAS

  ¿QUÉ ACTIVIDAD?     por hechos observables,
                      no por el nombre del
                      producto

  ¿QUÉ NORMA?         el instrumento, con su
                      número

  ¿QUIÉN SUPERVISA?   la autoridad competente

  ¿DÓNDE SE ESTUDIA?  la parte y la clase

Y NINGUNA FILA SUSTITUYE A LA CONSULTA
DE LA FUENTE OFICIAL VIGENTE.
```

---

## Autoridades y su ámbito

| Autoridad | Ámbito | Sitio oficial |
|---|---|---|
| **CMF** — Comisión para el Mercado Financiero | Bancos, valores, seguros, prestadores de servicios financieros | <https://www.cmfchile.cl/> |
| **Banco Central de Chile** | Política monetaria, sistemas de pago, normas de cambios internacionales | <https://www.bcentral.cl/> |
| **UAF** — Unidad de Análisis Financiero | Prevención de lavado de activos y financiamiento del terrorismo | <https://www.uaf.cl/> |
| **SERNAC** | Protección del consumidor financiero | <https://www.sernac.cl/> |
| **Ministerio de Hacienda** | Política financiera y proyectos normativos | <https://www.hacienda.cl/> |
| **BCN** — Biblioteca del Congreso Nacional | Texto oficial de las leyes | <https://www.bcn.cl/leychile> |

---

## Actividades y régimen

| Actividad | Instrumento principal | Autoridad | Dónde se estudia |
|---|---|---|---|
| Plataforma de financiamiento colectivo | Ley N.º 21.521 y normativa CMF | CMF | Parte 22, clases 1 y 4 |
| Sistema alternativo de transacción | Ley N.º 21.521 y normativa CMF | CMF | Parte 22, clases 1 y 10 |
| Intermediación de instrumentos financieros | Ley N.º 21.521; régimen de valores | CMF | Parte 22, clases 1 y 10 |
| Enrutamiento de órdenes | Ley N.º 21.521 y normativa CMF | CMF | Parte 22, clase 1 |
| Custodia de instrumentos financieros | Ley N.º 21.521 y normativa CMF | CMF | Parte 22, clase 9 |
| Asesoría crediticia y de inversión | Ley N.º 21.521 y normativa CMF | CMF | Parte 22, clases 1 y 6 |
| Sistema de Finanzas Abiertas | Ley N.º 21.521, normativa y anexo técnico | CMF | Parte 17, clase 3 |
| Iniciación de pagos | Ley N.º 21.521 y normativa del SFA | CMF | Parte 17, clase 10 |
| Operación de cambios internacionales | Compendio de Normas de Cambios Internacionales | Banco Central | Parte 18, clase 9 |
| Sistemas de pago de alto valor | Normativa del Banco Central | Banco Central | Parte 18, clases 7 y 13 |
| Emisión y operación de medios de pago | Normativa CMF y del Banco Central | CMF y Banco Central | Parte 18, clase 13 |
| Prevención de lavado y financiamiento | Ley N.º 19.913 y normativa UAF | UAF | Parte 22, clase 12 |
| Protección del consumidor financiero | Régimen de protección al consumidor | SERNAC y CMF | Parte 22, clase 6 |
| Protección de datos personales | Régimen de datos personales | Autoridad competente vigente | Parte 22, clase 13 |
| Continuidad operacional y tercerización | Normativa CMF | CMF | Parte 22, clase 14 |

---

## Las piezas que hay que verificar siempre

```text
ANTES DE USAR CUALQUIER FILA

  1 · ¿qué normas de carácter general
      desarrollan hoy la Ley N.º 21.521,
      y cuáles se han modificado?

  2 · ¿en qué fase de exigibilidad está tu
      actividad concreta?

  3 · ¿qué versión del anexo técnico del
      Sistema de Finanzas Abiertas rige?

  4 · ¿hay disposiciones transitorias
      abiertas que te alcancen?

  5 · ¿qué requisitos patrimoniales y de
      garantía aplican a tu escala?

  6 · ¿la actividad activa además el
      régimen de otra jurisdicción por
      comercialización activa?

LAS SEIS SE RESPONDEN EN EL SITIO DE LA
AUTORIDAD, NO EN ESTE DOCUMENTO.
```

---

## Fichas normativas del repositorio

| Ficha | Instrumento |
|---|---|
| [`ley-21521.yml`](../regulatory/chile/ley-21521.yml) | Ley que promueve la competencia e inclusión financiera |
| [`ncg-502-prestadores-fintec.yml`](../regulatory/chile/ncg-502-prestadores-fintec.yml) | Registro y autorización de prestadores |

Cada ficha lleva su campo `last_verified`. Una ficha sin verificar en los últimos
meses **es una afirmación caducada**, y el validador
`tools/validate_metadata.py` comprueba que la fecha exista y no sea futura, no que
siga siendo cierta. Eso lo compruebas tú.

---

## Qué NO cubre esta matriz

- **Tributación.** El tratamiento fiscal de los activos digitales y de las
  operaciones de cambio no se aborda aquí y cambia con frecuencia.
- **Derecho laboral, societario y concursal**, que condicionan buena parte de las
  estructuras que el programa estudia.
- **Normativa sectorial** de seguros y pensiones.
- **Criterios interpretativos** de la autoridad, que orientan y no obligan del
  mismo modo que una norma; la distinción está en la Parte 22, clase 16.

---

## Método

Cómo se cita una norma, cómo se comprueba su vigencia y qué hacer cuando no se
puede verificar está en
**[metodologia-verificacion-regulatoria.md](metodologia-verificacion-regulatoria.md)**.
La comparación con otras jurisdicciones está en
**[mapa-regulatorio-internacional.md](mapa-regulatorio-internacional.md)**.

---

## Limitaciones

- **Esta matriz no es asesoría legal.** Ninguna fila sustituye la consulta de la
  fuente oficial vigente ni el criterio de un abogado.
- El régimen **cambia**: lo que el programa enseña es el método de determinación,
  no un catálogo estable.
- La asignación de actividades a normas es orientativa; una misma operación puede
  activar varios regímenes a la vez.

**Fecha de verificación de este documento: 2026-08-12.**

---

[🏠 Inicio](../README.md) · [📚 Documentación](README.md) · [📖 Programa](../SYLLABUS.md)
