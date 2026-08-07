# Qué sigue

Estado y prioridades del programa. Las contribuciones en cualquiera de estas líneas son
bienvenidas: ver **[CONTRIBUTING.md](CONTRIBUTING.md)**.

> El avance real, contado sobre los archivos, está en **[STATUS.md](STATUS.md)**.
> Este documento describe el plan; aquel describe lo que existe.

---

## ✅ Completado

| Línea | Versión | Estado |
|---|---|---|
| 240 clases de las 16 partes originales, con fuentes | 1.0.0 | ✅ Completo |
| 96 laboratorios, 32 evaluaciones, 16 proyectos | 1.0.0 | ✅ Estructurados |
| Calculadoras, scoring y banco virtual con pruebas | 1.0.0 | ✅ Funcionales |
| Portal de estudio en GitHub Pages | 1.1.0 | ✅ Publicado |
| Integración continua endurecida y auditada | 1.1.0 | ✅ Completo |
| **Parte 17 — Finanzas abiertas, APIs y economía de datos** | 1.2.0 | ✅ Publicada |
| **Parte 18 — Pagos transfronterizos, remesas y liquidación** | 1.3.0 | ✅ Publicada |
| **Parte 19 — Blockchain y DLT para instituciones financieras** | 1.4.0 | ✅ Publicada |
| **Parte 20 — Activos digitales, stablecoins y dinero programable** | 1.5.0 | ✅ Publicada |
| **Parte 21 — Tokenización, FX on-chain y mercados programables** | 1.6.0 | ✅ Publicada |
| **Parte 22 — Regulación de mercados financieros digitales** | 1.7.0 | ✅ Publicada |
| Entorno `open_finance_sandbox` con 28 pruebas | 1.2.0 | ✅ Funcional |
| Entorno `cross_border_payments_lab` con 56 pruebas | 1.3.0 | ✅ Funcional |
| Entorno `dlt_financial_lab` con 38 pruebas | 1.4.0 | ✅ Funcional |
| Entorno `digital_assets_risk_lab` con 49 pruebas | 1.5.0 | ✅ Funcional |
| Entornos `tokenization_platform` y `onchain_fx_lab` con 62 pruebas | 1.6.0 | ✅ Funcionales |
| Entorno `regulatory_perimeter_engine` con 29 pruebas | 1.7.0 | ✅ Funcional |
| Validadores de metadatos, OpenAPI, datasets, secretos y PII | 1.2.0 | ✅ En CI |
| Fichas normativas estructuradas | 1.2.0 | ✅ Iniciadas |

---

## 🚧 En curso — Etapa 5, hacia la v2.0.0

**Etapa 5 — Finanzas digitales, infraestructura y mercados tokenizados.**
La ampliación se publicará como `2.0.0` cuando existan sus siete partes. Cada
parte se entrega completa —clases, laboratorios con solución, evaluaciones,
proyecto y aplicación— y en verde antes de empezar la siguiente.

| Parte | Tema | Clases | Aplicación asociada | Estado |
|---:|---|---:|---|---|
| 17 | Finanzas abiertas, APIs y economía de datos | 14 | `open_finance_sandbox` | ✅ Publicada |
| 18 | Pagos transfronterizos, remesas y liquidación | 16 | `cross_border_payments_lab` | ✅ Publicada |
| 19 | Blockchain y DLT para instituciones financieras | 14 | `dlt_financial_lab` | ✅ Publicada |
| 20 | Activos digitales, stablecoins y dinero programable | 16 | `digital_assets_risk_lab` | ✅ Publicada |
| 21 | Tokenización, FX on-chain y mercados programables | 16 | `tokenization_platform`, `onchain_fx_lab` | ✅ Publicada |
| 22 | Regulación de mercados financieros digitales | 18 | `regulatory_perimeter_engine` | ✅ Publicada |
| 23 | Proyecto: banco digital y mercado tokenizado | 18 | Capstone integrado | 🔜 Siguiente |

### Qué incluye cada parte antes de darse por publicada

1. Todas sus clases, con encabezado regulatorio y las cinco secciones adicionales.
2. Sus laboratorios, cada uno con **solución de referencia comentada**.
3. Evaluación diagnóstica y final, con rúbrica y guía de corrección.
4. Proyecto integrador con criterios de aceptación verificables.
5. Aplicación ejecutable con pruebas, en su mayoría negativas.
6. Modelo de amenazas priorizado, con una prueba por control.
7. Documento de mapa en `docs/` y ampliación del glosario digital.
8. Fichas normativas de los instrumentos que cita.
9. Todo el repositorio en verde: nueve validadores y las pruebas.

### Trabajo transversal pendiente de la etapa

| Línea | Descripción | Cuándo |
|---|---|---|
| **Integración con partes antiguas** | Bloques «para profundizar» en las Partes 8, 10, 11, 12, 13, 14 y 16 | Con cada parte nueva |
| **Biblioteca de casos** | `case-studies/` por tema, con hechos, fuentes y preguntas | Con cada parte nueva |
| **Mapas de documentación** | Uno por parte, como el de finanzas abiertas | Con cada parte |
| **Glosario digital** | Se amplía con los términos de cada parte | Con cada parte |
| **Fichas normativas** | Chile, Unión Europea e internacional comparada | Partes 22 y 23 |

---

## 🔧 Herramientas

| Línea | Descripción | Estado |
|---|---|---|
| Validación de metadatos regulatorios | Ninguna norma sin fecha | ✅ 1.2.0 |
| Validación de contratos OpenAPI | Alcances, errores, importes, enumerados | ✅ 1.2.0 |
| Validación de datasets | Ficha y diccionario obligatorios | ✅ 1.2.0 |
| Detección de secretos y de PII | Distingue el ejemplo del secreto | ✅ 1.2.0 |
| Índice de archivos generado | `FILE_INDEX.md` deja de escribirse a mano | ✅ 1.2.0 |
| Validación de mensajes ISO 20022 sintéticos | Campos, formatos y referencia estable | ✅ 1.3.0 |
| Matriz de competencias generada | Desde los encabezados de clase | Prevista |
| Inventario de aplicaciones generado | Desde `apps/` | Prevista |
| Generador de datos sintéticos configurable | Por segmento, cosecha y escenario | Prevista |

---

## 🌎 Ediciones locales

El programa describe marcos internacionales. Las ediciones locales **añaden** la norma
nacional sin sustituir el contenido base.

| Edición | Alcance | Estado |
|---|---|---|
| **Chile** | CMF, Banco Central, UAF, Ley Fintec, Sistema de Finanzas Abiertas | En curso, dentro de la Etapa 5 |
| **Unión Europea** | MiCA, DORA, DLT Pilot Regime, PSD2, RGPD | Con la Parte 22 |
| **Latinoamérica comparada** | Brasil, México, Colombia | Con la Parte 22 |

### Requisitos de una edición local

1. Se añade **al final** de la clase, en su propia sección; no modifica el contenido base.
2. Cita la norma con su identificador y su **fecha de vigencia**.
3. Registra la **fecha de verificación** de la adaptación.
4. Mantiene la línea de verificación local: las normas cambian.
5. Pasa todas las verificaciones del repositorio.

---

## 📚 Material complementario

| Línea | Descripción | Prioridad |
|---|---|:---:|
| **Soluciones de laboratorios anteriores** | Respuestas comentadas de los 96 laboratorios de las Partes 1 a 16 | Alta |
| **Rúbricas por proyecto** | Rúbrica detallada de cada proyecto integrador | Alta |
| **Cuadernos ejecutables** | Notebooks para valoración, carteras, scoring y estrés | Media |
| **Hojas de trabajo** | Plantillas descargables para los ejercicios largos | Media |
| **Índice de conceptos** | Dónde se define y dónde se usa cada término | Baja |

---

## 🌐 Traducciones

| Idioma | Estado | Nota |
|---|---|---|
| Español | ✅ Completo | Idioma base |
| Inglés | Buscando colaboración | Traducción por partes completas |
| Portugués | Buscando colaboración | Traducción por partes completas |

> Las traducciones se aceptan **por parte completa**, no por clases sueltas: el
> encadenamiento de conceptos entre clases se rompería.

---

## 🔄 Mantenimiento continuo

| Tarea | Frecuencia |
|---|---|
| Revisión de fichas normativas con más de 12 meses | Anual |
| Revisión de jurisdicciones en despliegue por fases | Semestral |
| Revisión de enlaces a fuentes oficiales | Trimestral, en CI |
| Actualización de marcos normativos revisados | Al publicarse |
| Verificación de dependencias | Continua, en CI |

---

## Cómo proponer una línea nueva

Abre un [issue](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/issues)
describiendo:

1. Qué problema resuelve para quien estudia o enseña.
2. Qué parte o partes afecta.
3. Si requiere cambios en la estructura verificada por CI.

---

**Ver también:** [Historial](CHANGELOG.md) · [Ficha técnica](MANIFEST.md) ·
[Contribuir](CONTRIBUTING.md) · [Etapa 5](docs/etapa-5-finanzas-digitales.md)
