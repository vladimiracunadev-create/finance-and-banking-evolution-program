<!-- portada:inicio -->
<div align="center">

# 🧾 Ficha técnica

**Ficha técnica del repositorio: qué se genera, con qué herramienta y qué garantiza cada comprobación.**

[![generado](https://img.shields.io/badge/generado-4%20documentos-007c83?style=flat-square)](STATUS.md)
[![validadores](https://img.shields.io/badge/validadores-15-2e8b57?style=flat-square)](README.md#-calidad-y-ci)

[🏠 Inicio](README.md) ·
[📊 Estado](STATUS.md) ·
[📚 Documentación](docs/README.md)

</div>
<!-- portada:fin -->

---

## 🏷️ Identificación

| Campo | Valor |
|---|---|
| **Nombre** | `finance-and-banking-evolution-program` |
| **Versión** | `2.0.0` |
| **Fecha** | 2026-08-07 |
| **Estado** | Programa completo · 5 etapas · 23 partes publicadas |
| **Licencia** | MIT |
| **Idioma** | Español |
| **Repositorio** | <https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program> |

> Las cantidades de esta ficha describen la **entrega actual**. El avance vivo lo
> calcula [`STATUS.md`](STATUS.md) contando los archivos: si esta ficha y aquel
> documento discrepan, el correcto es aquel.

## 📚 Contenido

| Componente | Cantidad |
|---|---:|
| Partes publicadas | 23 |
| Partes planificadas | 23 |
| Clases publicadas | 356 |
| Clases planificadas | 356 |
| Horas de sesión publicadas | 534 |
| Duración por clase | 90 min |
| Laboratorios | 150 |
| Soluciones de referencia | 54 |
| Evaluaciones | 46 |
| Proyectos integradores | 23 |
| Aplicaciones funcionales | 11 |
| Conjuntos de datos sintéticos | 6 |
| Fichas normativas estructuradas | 8 |

## 🧱 Estructura de una clase

| Elemento | Obligatorio | Verificado por |
|---|:---:|---|
| Encabezado YAML completo | ✅ | `validate_program.py` |
| 11 secciones estructurales | ✅ | `validate_program.py` |
| Ejemplo numérico guiado | ✅ | `validate_program.py` |
| Puente «del cliente al banco» | ✅ | `validate_program.py` |
| Mínimo 4 fuentes verificables | ✅ | `validate_program.py` |
| Bloques generados al día | ✅ | `render_program.py --check` |
| Enlaces relativos que resuelvan | ✅ | `check_links.py` |
| Línea de verificación si cita una norma | ✅ | `validate_metadata.py` |

### Adicional en la Etapa 5 (parte ≥ 17)

| Elemento | Obligatorio | Verificado por |
|---|:---:|---|
| Encabezado regulatorio de 6 claves | ✅ | `validate_metadata.py` |
| Secciones *Modelo mental*, *Perspectivas*, *Riesgos y controles*, *Práctica*, *Referencias cruzadas* | ✅ | `validate_metadata.py` |
| `regulation_last_verified` válida y no futura | ✅ | `validate_metadata.py` |
| Aviso legal explícito si `requires_legal_review` | ✅ | `validate_metadata.py` |

## 📊 Cobertura por etapa

| Etapa | Partes | Clases publicadas | Horas |
|---|:---:|---:|---:|
| Fundamentos | 1 – 4 | 56 | 84 |
| Analista | 5 – 8 | 60 | 90 |
| Bancario | 9 – 12 | 64 | 96 |
| Dirección | 13 – 16 | 60 | 90 |
| Finanzas digitales | 17 – 23 | 116 | 174 |
| **Total** | **23** | **356** | **534** |

## 🐍 Aplicaciones incluidas

| Aplicación | Descripción | Pruebas |
|---|---|:---:|
| `financial_calculators` | Interés compuesto, anualidades, amortización, VPN, TIR | ✅ |
| `credit_scoring` | Modelo de scoring con métricas de discriminación | ✅ |
| `openbank_simulator` | Banco con cuentas y movimientos sobre SQLite | ✅ |
| `open_finance_sandbox` | Consentimiento, autorización con PKCE, API de cuentas, iniciación de pagos y batería de conformidad | ✅ |
| `cross_border_payments_lab` | Cuatro flujos, motor de rutas, ISO 20022, screening, PvP, enlace de pagos inmediatos y ruta con stablecoin | ✅ |
| `dlt_financial_lab` | Cadena, firmas, árbol de Merkle con sumas, consenso bizantino, contrato con reentrada y oráculo | ✅ |
| `digital_assets_risk_lab` | Clasificación por promesa, reservas, cola de redención, espiral algorítmica, custodia, profundidad y contagio | ✅ |
| `tokenization_platform` | Registro de referencia, emisión, ciclo de vida, entrega contra pago atómica y cascada de colateral | ✅ |
| `onchain_fx_lab` | Coste total por ruta, creador de mercado automatizado y riesgo de liquidación en divisas | ✅ |
| `regulatory_perimeter_engine` | Perímetro por hechos, calificación por criterios, salvaguarda, vigilancia y expediente cruzado | ✅ |

## ⚙️ Documentos generados automáticamente

Estos archivos se producen desde el contenido y **no se editan a mano**:

| Archivo | Generador |
|---|---|
| `SYLLABUS.md` | `tools/build_syllabus.py` |
| `STATUS.md` | `tools/progress.py` |
| `FILE_INDEX.md` | `tools/build_file_index.py` |
| Bloques `gen:*` de cada clase | `tools/render_program.py` |
| Portal de estudio (`site/`) | `tools/build_site.py` |

## 📋 Requisitos técnicos

| Requisito | Versión |
|---|---|
| Python | 3.11, 3.12 o 3.13 |
| Dependencias de pruebas | `requirements.txt` (`pytest`) |
| Dependencias del portal | `requirements-site.txt` (`markdown`) |
| Dependencias de las herramientas | Ninguna: biblioteca estándar |
| Codificación | UTF-8 sin BOM |
| Finales de línea | LF |

## ✅ Verificación de la entrega

```bash
python tools/validate_program.py
```

```bash
python tools/render_program.py --check && python tools/build_syllabus.py --check
```

```bash
python tools/progress.py --check && python tools/build_file_index.py --check
```

```bash
python tools/check_links.py && python tools/build_site.py --check
```

```bash
python tools/validate_metadata.py && python tools/validate_openapi.py
```

```bash
python tools/validate_iso20022.py && python tools/validate_datasets.py
```

```bash
python tools/detect_secrets.py && python tools/detect_pii.py
```

```bash
pytest -q
```

Todas se ejecutan en cada cambio mediante integración continua.

---

**Ver también:** [Estado del contenido](STATUS.md) · [Historial](CHANGELOG.md) ·
[Qué sigue](ROADMAP.md) · [Índice del programa](SYLLABUS.md) ·
[Etapa 5](docs/etapa-5-finanzas-digitales.md)

<!-- pie:inicio -->
---

<div align="center">

[🏠 Inicio](README.md) · [📊 Estado](STATUS.md) · [📚 Documentación](docs/README.md)

</div>
<!-- pie:fin -->
