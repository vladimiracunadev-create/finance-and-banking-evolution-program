<!-- portada:inicio -->
<div align="center">

# 🌐 Etapa 5 — Finanzas digitales, infraestructura y mercados tokenizados

**Qué es y qué no es la etapa de infraestructura financiera digital, y los seis criterios que la ordenan.**

[![partes](https://img.shields.io/badge/partes-17%20a%2023-8957e5?style=flat-square)](../SYLLABUS.md)
[![clases](https://img.shields.io/badge/clases-112-7c5cff?style=flat-square)](../STATUS.md)

[⬅️ Documentación](README.md) ·
[🏠 Inicio](../README.md) ·
[📘 Glosario de la etapa](glosario-finanzas-digitales.md) ·
[🧪 Laboratorios](guia-laboratorios-digitales.md)

</div>
<!-- portada:fin -->

---

La Etapa 5 continúa el programa donde la Parte 14 lo dejó. Las Partes 1 a 16
llevan de los porcentajes a la dirección bancaria; esta etapa lleva de la
**introducción fintech** a la **infraestructura financiera**: cómo se comparte
un dato con consentimiento, cómo se mueve un pago entre países, qué es
exactamente un activo digital y qué cambia cuando un instrumento financiero se
representa en un registro programable.

## 🚫 Qué NO es esta etapa

Conviene decirlo antes que nada, porque determina el criterio de todo lo demás:

- **No es un curso de programación blockchain.** La tecnología aparece cuando
  resuelve un problema, y se compara siempre con la alternativa que no la usa.
- **No es un curso de criptomonedas ni de inversión.** No hay recomendaciones de
  inversión, ni precios, ni estrategias.
- **No es una colección de documentos legales.** La norma se estudia por lo que
  obliga a hacer, no por su articulado.
- **No es un catálogo de conceptos fintech.** Cada concepto se conecta con el
  cliente, el producto, la entidad, la infraestructura, el mercado, el riesgo,
  la regulación, la supervisión y la decisión ejecutiva.

## 🧩 Las siete partes

Las siete están publicadas. Se recorren en orden, porque cada una supone la
anterior: no se puede tokenizar un instrumento sin haber entendido qué registro
manda en él, ni determinar el perímetro regulatorio de algo que aún no se sabe
cómo funciona.

| Parte | Tema | Clases | Estado |
|---:|---|---:|---|
| 17 | [Finanzas abiertas, APIs y economía de datos](../modules/16-finanzas-abiertas-apis-y-economia-de-datos/README.md) | 14 | Publicada |
| 18 | [Pagos transfronterizos, remesas y liquidación](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/README.md) | 16 | Publicada |
| 19 | [Blockchain y DLT para instituciones financieras](../modules/18-blockchain-y-dlt-para-instituciones-financieras/README.md) | 14 | Publicada |
| 20 | [Activos digitales, stablecoins y dinero programable](../modules/19-activos-digitales-stablecoins-y-dinero-programable/README.md) | 16 | Publicada |
| 21 | [Tokenización, FX on-chain y mercados programables](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/README.md) | 16 | Publicada |
| 22 | [Regulación de mercados financieros digitales](../modules/21-regulacion-de-mercados-financieros-digitales/README.md) | 18 | Publicada |
| 23 | [Proyecto: banco digital y mercado tokenizado](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/README.md) | 18 | Publicada |

El recuento —no el plan— está en **[STATUS.md](../STATUS.md)**, que se genera
contando los archivos. Esta tabla describe la arquitectura; aquel documento
describe lo que existe.

La última cambia de naturaleza respecto de las seis anteriores. No enseña nada
nuevo: reúne los métodos de las veintidós partes del programa y los hace
funcionar juntos, que es cuando aparecen las contradicciones entre decisiones que
por separado eran correctas. Su mapa está en
**[mapa-capstone.md](mapa-capstone.md)**.

## 🧩 De dónde viene cada parte

```text
Parte 14 · Fintech, datos e IA          (introducción, se mantiene)
   │  clase 3  banca abierta y APIs        ──► Parte 17
   │  clase 2  pagos digitales             ──► Parte 18
   │  clase 9  criptoactivos y registro    ──► Partes 19 y 20
   │  clase 10 monedas digitales de BC     ──► Parte 20
   │  clase 12 regulación de la tecnología ──► Parte 22
   │
Parte 8  · Inversiones y mercados          ──► Parte 21
Parte 10 · Operaciones bancarias           ──► Parte 18
Parte 11 · Riesgos                         ──► Partes 19, 20 y 21
Parte 12 · Regulación                      ──► Parte 22
Parte 16 · Banco Virtual                   ──► Parte 23
```

Las clases de las partes anteriores **se mantienen** y actúan como
prerrequisito. La Etapa 5 no las repite: las profundiza, las implementa y les
añade la capa regulatoria y de riesgo que una introducción no puede sostener.

## 📐 Los seis criterios que ordenan toda la etapa

### 1. Separación terminológica estricta

Estos términos **no son sinónimos** y el material nunca los usa como tales:

```text
activo digital ≠ criptoactivo ≠ token
tokenización ≠ DLT ≠ blockchain ≠ contrato inteligente
stablecoin ≠ dinero electrónico ≠ depósito tokenizado ≠ CBDC
pago transfronterizo ≠ remesa ≠ operación FX
compensación ≠ liquidación
finanzas abiertas ≠ banca abierta ≠ DeFi
```

### 2. Neutralidad tecnológica

Ningún caso presenta una tecnología como solución automática. Cada uno compara,
como mínimo: base de datos centralizada, sistema tradicional, red autorizada,
blockchain privada, blockchain pública, arquitectura híbrida y solución sin
blockchain. Y se pregunta siempre si el problema es de **confianza**,
**coordinación**, **datos**, **proceso**, **regulación** o **liquidez**.

### 3. Trece perspectivas

Cliente, comercio, fintech, banco, banco central, infraestructura,
inversionista, emisor, custodio, mercado, supervisor, auditor y sociedad. No
todas aparecen en cada clase; la sección **Perspectivas** de cada una declara
cuáles y qué decide cada actor.

### 4. Hecho, supuesto e interpretación

Cada afirmación cuantitativa dice de dónde sale. Los ejemplos guiados declaran
sus supuestos con la etiqueta *supuestos del ejercicio*, y ninguna cifra
ilustrativa se presenta como dato de mercado.

### 5. Seis planos de viabilidad

Ninguna decisión se resuelve en uno solo:

```text
técnicamente posible
económicamente viable
jurídicamente válido
prudencialmente aceptable
operacionalmente resiliente
éticamente defendible
```

### 6. Verificación regulatoria con fecha

Toda norma citada lleva autoridad, identificador, fuente oficial y **fecha de
verificación**. `tools/validate_metadata.py` falla si una clase cita un
instrumento y no declara su línea de verificación. El método está en
**[Metodología de verificación regulatoria](metodologia-verificacion-regulatoria.md)**.

## 🐍 Aplicaciones de la etapa

| Aplicación | Parte | Estado |
|---|---:|---|
| [`open_finance_sandbox`](../apps/open_finance_sandbox/README.md) | 17 | Funcional, con pruebas |
| `cross_border_payments_lab` | 18 | En preparación |
| `dlt_financial_lab` | 19 | En preparación |
| `digital_assets_risk_lab` | 20 | En preparación |
| `tokenization_platform` | 21 | En preparación |
| `onchain_fx_lab` | 21 | En preparación |
| `regulatory_perimeter_engine` | 22 | En preparación |
| Capstone integrado | 23 | En preparación |

Todas comparten las mismas restricciones: **sin red externa, sin credenciales
reales, sin fondos reales, sin datos personales y con dependencias mínimas**.

## 🚫 Qué se prohíbe construir

El material no incluye —y no aceptará contribuciones que incluyan— herramientas
para ocultar el origen de fondos, evadir controles de prevención de lavado,
mezclar activos con fin de romper la trazabilidad, manipular mercados o cometer
fraude. Los ataques se describen para poder **detectarlos y cortarlos**, siempre
acompañados de su control y de la prueba que lo verifica.

## 🎓 Cómo estudiarla

1. Comprueba los prerrequisitos en el README de la parte antes de empezar.
2. Haz la evaluación diagnóstica: no puntúa, pero te dice dónde vas a sufrir.
3. Recorre las clases en orden; cada una supone la anterior.
4. Ejecuta los laboratorios. En esta etapa, **un laboratorio no leído no cuenta
   como estudiado**: la mitad del aprendizaje está en ver fallar el control.
5. Entrega el proyecto y defiéndelo con las preguntas del panel.

## ✅ Verificación

```bash
python tools/validate_program.py && python tools/validate_metadata.py
```

---

**Ver también:** [Ruta de aprendizaje](ruta-aprendizaje.md) ·
[Mapa de finanzas abiertas](mapa-finanzas-abiertas.md) ·
[Guía de laboratorios digitales](guia-laboratorios-digitales.md) ·
[Glosario de finanzas digitales](glosario-finanzas-digitales.md)

<!-- pie:inicio -->
---

<div align="center">

[⬅️ Documentación](README.md) · [🏠 Inicio](../README.md) · [📘 Glosario de la etapa](glosario-finanzas-digitales.md) · [🧪 Laboratorios](guia-laboratorios-digitales.md)

</div>
<!-- pie:fin -->
