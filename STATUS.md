# Estado del contenido

Este archivo lo genera `tools/progress.py` a partir de los archivos reales
del repositorio. No se edita a mano: refleja lo que hay, no lo que se planea.

## Avance global: 334 de 352 clases (94.9 %)

`██████████████████████████████████████░░`

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
| 12 | Parte 12: Regulación, cumplimiento y auditoría | 16 | 16 | `████████████████████` | 17.4 KB |
| 13 | Parte 13: Finanzas corporativas y banca empresarial | 14 | 14 | `████████████████████` | 17.4 KB |
| 14 | Parte 14: Fintech, datos e inteligencia artificial | 14 | 14 | `████████████████████` | 17.8 KB |
| 15 | Parte 15: Estrategia y dirección bancaria | 14 | 14 | `████████████████████` | 17.8 KB |
| 16 | Parte 16: Proyecto Banco Virtual | 18 | 18 | `████████████████████` | 17.5 KB |
| 17 | Parte 17: Finanzas abiertas, APIs y economía de datos | 14 | 14 | `████████████████████` | 17.6 KB |
| 18 | Parte 18: Pagos transfronterizos, remesas y liquidación internacional | 16 | 16 | `████████████████████` | 17.7 KB |
| 19 | Parte 19: Blockchain y DLT para instituciones financieras | 14 | 14 | `████████████████████` | 16.7 KB |
| 20 | Parte 20: Activos digitales, stablecoins y dinero programable | 16 | 16 | `████████████████████` | 15.7 KB |
| 21 | Parte 21: Tokenización, FX on-chain y mercados programables | 16 | 16 | `████████████████████` | 15.9 KB |
| 22 | Parte 22: Regulación de mercados financieros digitales | 18 | 18 | `████████████████████` | 15.8 KB |
| 23 | Parte 23: Proyecto — banco digital y mercado tokenizado | 0 | 18 | `░░░░░░░░░░░░░░░░░░░░` | 0.0 KB |
| | **Total** | **334** | **352** | `███████████████████░` | **15.9 KB** |

## Qué significa que una clase esté completa

Una clase solo se cuenta aquí si supera `tools/validate_program.py`, que exige:

- encabezado con parte, número, título, nivel, duración y estado;
- las once secciones obligatorias, incluidas ejemplo numérico guiado,
  puente «del cliente al banco», errores frecuentes y entregable;
- navegación, agenda docente y bloque de ética generados por
  `tools/render_program.py`;
- al menos cuatro fuentes verificables en «Fuentes y verificación».

## Otros componentes

Las cifras de esta tabla se cuentan sobre los archivos reales; no se
escriben a mano.

| Componente | Cantidad | Estado |
|---|---:|---|
| Arquitectura curricular (partes) | 22 | Completa |
| Laboratorios | 141 | Estructurados |
| Evaluaciones | 44 | Diagnóstico y final por parte |
| Proyectos integradores | 22 | Especificados |
| Aplicaciones didácticas | 10 | Ejecutables con pruebas |
| Estudios de caso | 0 | Con hechos, fuentes y preguntas |
| Fichas normativas estructuradas | 8 | Con fecha de verificación |
| Datasets documentados | 6 | Sintéticos, con diccionario |
| Adaptación normativa por país | — | Plantilla; cada clase indica qué verificar |

## Cómo verificarlo

```bash
python tools/validate_program.py     # estructura, secciones y fuentes
python tools/render_program.py --check  # navegación y bloques generados
python tools/progress.py --check     # este archivo contra la realidad
pytest -q                            # calculadoras y banco virtual
```
