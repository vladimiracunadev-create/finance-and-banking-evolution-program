<!-- portada:inicio -->
<div align="center">

# 🏛️ Metodología de verificación regulatoria

**Cómo se cita una norma, cómo se comprueba que sigue vigente y qué se hace cuando no se puede.**

[![aplica a](https://img.shields.io/badge/aplica%20a-8%20fichas%20normativas-7c5cff?style=flat-square)](../regulatory/README.md)
[![validador](https://img.shields.io/badge/validador-validate__metadata.py-2e8b57?style=flat-square)](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/blob/main/tools/validate_metadata.py)

[⬅️ Documentación](README.md) ·
[🏠 Inicio](../README.md) ·
[🗂️ Fichas normativas](../regulatory/README.md) ·
[📗 Fuentes](fuentes.md)

</div>
<!-- portada:fin -->

---

Cómo el programa cita una norma, cómo comprueba que sigue vigente y qué hace
cuando no puede comprobarlo.

> **Nada de este repositorio es asesoría legal.** El material enseña a leer y a
> verificar normas; no sustituye el criterio de un profesional habilitado en tu
> jurisdicción.

## ❓ El problema

Una norma citada sin fecha es una afirmación que no caduca. Dentro de un año
nadie sabrá si seguía siendo cierta, y quien la lea la tratará como vigente. En
un programa que se apoya en marcos regulatorios de trece jurisdicciones, ese
descuido convierte material formativo en desinformación con buena presentación.

La respuesta del repositorio es sencilla y automática: **toda cita de un
instrumento concreto lleva su fecha de verificación, y un validador falla si no
la lleva**.

## 📄 Qué se considera un instrumento concreto

Activan la regla:

```text
Ley N.º 21.521
NCG N.º 502
Reglamento (UE) 2023/1114
Directiva (UE) 2015/2366
Decreto N.º 137
```

No la activan —porque no caducan del mismo modo— los marcos y principios sin
número: Basilea III, las recomendaciones del GAFI, los principios del CPMI-IOSCO
o las guías de la OCDE. Aun así, el programa indica su año de publicación.

## ❓ Las siete preguntas de una lectura normativa

Se aplican siempre, en este orden. La destreza se enseña en la Parte 17, clase 3.

| # | Pregunta | Dónde se responde |
|---:|---|---|
| 1 | **Ámbito**: ¿a quién aplica, desde qué umbral, con qué exclusiones? | Primeros artículos |
| 2 | **Definiciones**: ¿qué significa cada término *en este texto*? | Artículo de definiciones |
| 3 | **Obligaciones**: ¿qué hay que hacer, con qué frecuencia, ante quién? | Cuerpo |
| 4 | **Vigencia**: publicación ≠ entrada en vigor ≠ exigibilidad | Disposiciones finales |
| 5 | **Transitorios**: ¿cuál es el calendario real? | Disposiciones transitorias |
| 6 | **Remisiones**: ¿qué otro cuerpo normativo abre? | «En lo no previsto…» |
| 7 | **Anexos técnicos**: ¿dónde está la especificación? | Anexos |

Los pasos 5 y 7 son los que más se saltan y los que más caro salen: el
calendario real casi nunca está en el cuerpo del instrumento, y en finanzas
abiertas la especificación de las APIs vive en el anexo técnico.

## 🗃️ Cómo se registra una cita

### En la clase

```yaml
jurisdictions: [chile]
regulatory_topics: [open-finance, licenciamiento]
regulation_last_verified: 2026-08-06
regulatory_status: en-despliegue-por-fases
primary_authorities: [CMF, Banco Central de Chile, UAF]
requires_legal_review: true
```

Y en «Fuentes y verificación», una línea final que dice **qué hay que comprobar
en la fuente oficial** y **cuándo se comprobó**. Si `requires_legal_review` es
`true`, la clase declara además de forma explícita que no constituye asesoría
legal; el validador lo exige.

### En la ficha normativa

Una ficha por instrumento en [`regulatory/`](../regulatory/README.md), con
autoridad, número, fechas, estado, alcance, actividades cubiertas, fuente
oficial y `last_verified`.

## 🤖 Qué hace el validador

```bash
python tools/validate_metadata.py
```

| Regla | Alcance | Falla si… |
|---|---|---|
| Cita con verificación | Todas las clases | Cita un instrumento y no hay línea de verificación |
| Encabezado regulatorio | Etapa 5 | Falta alguna de las seis claves |
| Secciones de la etapa | Etapa 5 | Falta *Modelo mental*, *Perspectivas*, *Riesgos y controles*, *Práctica* o *Referencias cruzadas* |
| Fecha válida | Etapa 5 y fichas | La fecha no es ISO o está en el futuro |
| Aviso legal | Etapa 5 | `requires_legal_review: true` sin la declaración explícita |
| Ficha completa | `regulatory/` | Falta un campo obligatorio o `official_source` no es una URL |

Lo que el validador **no** puede hacer es comprobar que la norma siga vigente:
eso exige consultar la fuente. Lo que sí garantiza es que exista la fecha
contra la que medir, y que nadie pueda añadir una cita sin ella.

## 🚧 Cuando no se puede verificar

Ocurre: el sitio del supervisor está caído, la norma está en consulta pública, o
el material se escribe sin acceso a la fuente. El procedimiento es:

1. **No inventar.** Ni el número, ni la fecha, ni el estado, ni la autoridad.
2. **Declarar el estado real** en `regulatory_status`: `en-despliegue`,
   `en-consulta`, `en-implantacion`, `derogado`.
3. **Escribir en la clase qué hay que verificar**, con nombre y sitio de la
   autoridad, para que el lector pueda cerrarlo él.
4. **Preferir el principio al detalle.** «El régimen exige capital mínimo según
   la actividad y su escala» es verificable y duradero; una cifra sin fuente no
   es ninguna de las dos cosas.

## 📗 Jerarquía de fuentes

| Nivel | Fuente | Uso |
|---:|---|---|
| 1 | Sitio oficial de la autoridad emisora | Cita normativa |
| 2 | Diario o boletín oficial | Fecha de publicación |
| 3 | Organismos internacionales (BIS, FSB, IOSCO, GAFI, FMI) | Marcos y estándares |
| 4 | Organismos de estandarización (ISO, IETF, OpenID Foundation, NIST) | Especificaciones técnicas |
| 5 | Literatura académica revisada | Evidencia empírica |
| — | Blogs, prensa, notas de proveedores | **Nunca como fuente normativa** |

## ⚠️ Errores que esta metodología evita

| Error | Consecuencia | Qué lo corta |
|---|---|---|
| Citar de segunda mano | Se propaga un error ajeno | Jerarquía de fuentes |
| Confundir publicación con vigencia | Se planifica contra una fecha falsa | Pregunta 4 |
| Ignorar los transitorios | Se compromete un lanzamiento imposible | Pregunta 5 |
| Ignorar el anexo técnico | Implementación no conforme | Pregunta 7 |
| Citar sin fecha | La afirmación no caduca nunca | El validador |
| Inventar una cifra plausible | Desinformación con apariencia de rigor | Preferir el principio |

## 🔁 Revisión periódica

| Tarea | Frecuencia |
|---|---|
| Revisión de fichas con `last_verified` de más de 12 meses | Anual |
| Revisión de las jurisdicciones en despliegue por fases | Semestral |
| Comprobación de enlaces a fuentes oficiales | Trimestral, en CI |
| Actualización tras una modificación normativa conocida | Al publicarse |

---

**Ver también:** [Fichas normativas](../regulatory/README.md) ·
[Etapa 5](etapa-5-finanzas-digitales.md) · [Fuentes](fuentes.md) ·
[Ética y limitaciones](etica-y-limitaciones.md)

<!-- pie:inicio -->
---

<div align="center">

[⬅️ Documentación](README.md) · [🏠 Inicio](../README.md) · [🗂️ Fichas normativas](../regulatory/README.md) · [📗 Fuentes](fuentes.md)

</div>
<!-- pie:fin -->
