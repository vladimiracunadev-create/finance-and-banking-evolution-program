# Estado del contenido

Este archivo lo genera `tools/progress.py` a partir de los archivos reales
del repositorio. No se edita a mano: refleja lo que hay, no lo que se planea.

## Avance global: 164 de 240 clases (68.3 %)

`███████████████████████████░░░░░░░░░░░░░`

| Parte | Tema | Clases | Plan | Avance | Tamaño medio |
|---:|---|---:|---:|---|---:|
| 1 | Parte 1: Matemática financiera básica | 14 | 14 | `████████████████████` | 12.3 KB |
| 2 | Parte 2: Finanzas personales | 14 | 14 | `████████████████████` | 13.6 KB |
| 3 | Parte 3: Productos y servicios financieros | 14 | 14 | `████████████████████` | 13.3 KB |
| 4 | Parte 4: Seguridad y consumo financiero | 14 | 14 | `████████████████████` | 14.2 KB |
| 5 | Parte 5: Contabilidad financiera | 15 | 15 | `████████████████████` | 14.5 KB |
| 6 | Parte 6: Economía y sistema financiero | 15 | 15 | `████████████████████` | 14.6 KB |
| 7 | Parte 7: Matemática financiera avanzada | 15 | 15 | `████████████████████` | 14.3 KB |
| 8 | Parte 8: Inversiones y mercados | 15 | 15 | `████████████████████` | 15.6 KB |
| 9 | Parte 9: Análisis y gestión de crédito | 16 | 16 | `████████████████████` | 16.9 KB |
| 10 | Parte 10: Operaciones bancarias | 16 | 16 | `████████████████████` | 16.3 KB |
| 11 | Parte 11: Gestión integral de riesgos | 16 | 16 | `████████████████████` | 16.6 KB |
| 12 | Parte 12: Regulación, cumplimiento y auditoría | 0 | 16 | `░░░░░░░░░░░░░░░░░░░░` | 0.0 KB |
| 13 | Parte 13: Finanzas corporativas y banca empresarial | 0 | 14 | `░░░░░░░░░░░░░░░░░░░░` | 0.0 KB |
| 14 | Parte 14: Fintech, datos e inteligencia artificial | 0 | 14 | `░░░░░░░░░░░░░░░░░░░░` | 0.0 KB |
| 15 | Parte 15: Estrategia y dirección bancaria | 0 | 14 | `░░░░░░░░░░░░░░░░░░░░` | 0.0 KB |
| 16 | Parte 16: Proyecto Banco Virtual | 0 | 18 | `░░░░░░░░░░░░░░░░░░░░` | 0.0 KB |
| | **Total** | **164** | **240** | `██████████████░░░░░░` | **14.8 KB** |

## Qué significa que una clase esté completa

Una clase solo se cuenta aquí si supera `tools/validate_program.py`, que exige:

- encabezado con parte, número, título, nivel, duración y estado;
- las once secciones obligatorias, incluidas ejemplo numérico guiado,
  puente «del cliente al banco», errores frecuentes y entregable;
- navegación, agenda docente y bloque de ética generados por
  `tools/render_program.py`;
- al menos cuatro fuentes verificables en «Fuentes y verificación».

## Otros componentes

| Componente | Estado |
|---|---|
| Arquitectura curricular (16 partes) | Completa |
| Laboratorios (96) | Estructurados |
| Evaluaciones (32) | Diagnóstico y final por parte |
| Proyectos integradores (16) | Especificados |
| Calculadoras financieras | MVP funcional con pruebas |
| Banco virtual (SQLite) | MVP funcional con pruebas |
| Datasets sintéticos | Iniciales |
| Adaptación normativa por país | Plantilla; cada clase indica qué verificar |

## Cómo verificarlo

```bash
python tools/validate_program.py     # estructura, secciones y fuentes
python tools/render_program.py --check  # navegación y bloques generados
python tools/progress.py --check     # este archivo contra la realidad
pytest -q                            # calculadoras y banco virtual
```
