# Ficha técnica

## Identificación

| Campo | Valor |
|---|---|
| **Nombre** | `finance-and-banking-evolution-program` |
| **Versión** | `1.4.0` |
| **Fecha** | 2026-08-06 |
| **Estado** | 16 partes completas · Etapa 5 en ampliación activa (3 de 7 partes publicadas) |
| **Licencia** | MIT |
| **Idioma** | Español |
| **Repositorio** | <https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program> |

> Las cantidades de esta ficha describen la **entrega actual**. El avance vivo lo
> calcula [`STATUS.md`](STATUS.md) contando los archivos: si esta ficha y aquel
> documento discrepan, el correcto es aquel.

## Contenido

| Componente | Cantidad |
|---|---:|
| Partes publicadas | 19 |
| Partes planificadas | 23 |
| Clases publicadas | 284 |
| Clases planificadas | 352 |
| Horas de sesión publicadas | 426 |
| Duración por clase | 90 min |
| Laboratorios | 116 |
| Soluciones de referencia | 20 |
| Evaluaciones | 38 |
| Proyectos integradores | 19 |
| Aplicaciones funcionales | 6 |
| Conjuntos de datos sintéticos | 6 |
| Fichas normativas estructuradas | 3 |

## Estructura de una clase

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

## Cobertura por etapa

| Etapa | Partes | Clases publicadas | Horas |
|---|:---:|---:|---:|
| Fundamentos | 1 – 4 | 56 | 84 |
| Analista | 5 – 8 | 60 | 90 |
| Bancario | 9 – 12 | 64 | 96 |
| Dirección | 13 – 16 | 60 | 90 |
| Finanzas digitales | 17 – 23 | 44 de 112 | 66 |
| **Total** | **23** | **284 de 352** | **426** |

## Aplicaciones incluidas

| Aplicación | Descripción | Pruebas |
|---|---|:---:|
| `financial_calculators` | Interés compuesto, anualidades, amortización, VPN, TIR | ✅ |
| `credit_scoring` | Modelo de scoring con métricas de discriminación | ✅ |
| `openbank_simulator` | Banco con cuentas y movimientos sobre SQLite | ✅ |
| `open_finance_sandbox` | Consentimiento, autorización con PKCE, API de cuentas, iniciación de pagos y batería de conformidad | ✅ |
| `cross_border_payments_lab` | Cuatro flujos, motor de rutas, ISO 20022, screening, PvP, enlace de pagos inmediatos y ruta con stablecoin | ✅ |
| `dlt_financial_lab` | Cadena, firmas, árbol de Merkle con sumas, consenso bizantino, contrato con reentrada y oráculo | ✅ |

## Documentos generados automáticamente

Estos archivos se producen desde el contenido y **no se editan a mano**:

| Archivo | Generador |
|---|---|
| `SYLLABUS.md` | `tools/build_syllabus.py` |
| `STATUS.md` | `tools/progress.py` |
| `FILE_INDEX.md` | `tools/build_file_index.py` |
| Bloques `gen:*` de cada clase | `tools/render_program.py` |
| Portal de estudio (`site/`) | `tools/build_site.py` |

## Requisitos técnicos

| Requisito | Versión |
|---|---|
| Python | 3.11, 3.12 o 3.13 |
| Dependencias de pruebas | `requirements.txt` (`pytest`) |
| Dependencias del portal | `requirements-site.txt` (`markdown`) |
| Dependencias de las herramientas | Ninguna: biblioteca estándar |
| Codificación | UTF-8 sin BOM |
| Finales de línea | LF |

## Verificación de la entrega

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
