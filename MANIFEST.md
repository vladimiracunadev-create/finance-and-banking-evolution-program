# Ficha técnica

## Identificación

| Campo | Valor |
|---|---|
| **Nombre** | `finance-and-banking-evolution-program` |
| **Versión** | `1.0.0` |
| **Fecha** | 2026-08-06 |
| **Estado** | Contenido completo y verificado |
| **Licencia** | MIT |
| **Idioma** | Español |
| **Repositorio** | <https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program> |

## Contenido

| Componente | Cantidad |
|---|---:|
| Partes | 16 |
| Clases | 240 |
| Horas de sesión | 360 |
| Duración por clase | 90 min |
| Laboratorios | 96 |
| Evaluaciones | 32 |
| Proyectos integradores | 16 |
| Aplicaciones funcionales | 3 |
| Conjuntos de datos sintéticos | 3 |

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

## Cobertura por etapa

| Etapa | Partes | Clases | Horas |
|---|:---:|---:|---:|
| Fundamentos | 1 – 4 | 56 | 84 |
| Analista | 5 – 8 | 60 | 90 |
| Bancario | 9 – 12 | 64 | 96 |
| Dirección | 13 – 16 | 60 | 90 |
| **Total** | **16** | **240** | **360** |

## Aplicaciones incluidas

| Aplicación | Descripción | Pruebas |
|---|---|:---:|
| `financial_calculators` | Interés compuesto, anualidades, amortización, VPN, TIR | ✅ |
| `credit_scoring` | Modelo de scoring con métricas de discriminación | ✅ |
| `openbank_simulator` | Banco con cuentas y movimientos sobre SQLite | ✅ |

## Documentos generados automáticamente

Estos archivos se producen desde el contenido y **no se editan a mano**:

| Archivo | Generador |
|---|---|
| `SYLLABUS.md` | `tools/build_syllabus.py` |
| `STATUS.md` | `tools/progress.py` |
| Bloques `gen:*` de cada clase | `tools/render_program.py` |

## Requisitos técnicos

| Requisito | Versión |
|---|---|
| Python | 3.12 |
| Dependencias | `requirements.txt` |
| Pruebas | `pytest` |
| Codificación | UTF-8 sin BOM |
| Finales de línea | LF |

## Verificación de la entrega

```bash
python tools/validate_program.py
python tools/render_program.py --check
python tools/build_syllabus.py --check
python tools/progress.py --check
python tools/check_links.py
pytest -q
```

Las seis comprobaciones se ejecutan en cada cambio mediante integración continua.

---

**Ver también:** [Estado del contenido](STATUS.md) · [Historial](CHANGELOG.md) ·
[Qué sigue](ROADMAP.md) · [Índice del programa](SYLLABUS.md)
