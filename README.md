# Finance & Banking Evolution Program

Programa abierto y progresivo de educación financiera, banca, inversiones, riesgo, regulación, tecnología financiera y dirección bancaria.

> Desde cero absoluto hasta la construcción y administración de un banco virtual educativo.

[![Estado](https://img.shields.io/badge/estado-contenido%20parcial-orange)](#estado-del-contenido)
[![Clases](https://img.shields.io/badge/clases-240-blue)](#estructura-general)
[![Horas](https://img.shields.io/badge/horas-360-green)](#estructura-general)
[![Licencia](https://img.shields.io/badge/licencia-MIT-black)](LICENSE)

## Propósito

Este repositorio busca que una persona sin conocimientos previos pueda avanzar, paso a paso, desde el manejo de porcentajes y presupuestos hasta el análisis crediticio, la gestión de riesgos, las operaciones bancarias, fintech, inteligencia artificial y dirección bancaria.

El programa **no reemplaza títulos, certificaciones, licencias profesionales ni autorizaciones regulatorias**. Es una ruta de aprendizaje técnico y práctico.

## Estructura general

- **5 etapas** de progresión.
- **16 partes**.
- **240 clases** de 90 minutos.
- **360 horas** guiadas.
- **96 laboratorios**.
- **32 evaluaciones**.
- **16 proyectos integradores**.
- **1 banco virtual** como proyecto final.

## Etapas

| Etapa | Enfoque | Clases | Horas |
|---|---|---:|---:|
| 1 | Fundamentos y vida financiera | 56 | 84 |
| 2 | Formación de analista financiero | 60 | 90 |
| 3 | Formación bancaria profesional | 64 | 96 |
| 4 | Banca avanzada y dirección | 42 | 63 |
| 5 | Banco virtual integral | 18 | 27 |
| **Total** |  | **240** | **360** |

## Estado del contenido

Esta versión es una **base parcial utilizable**:

- Las 240 clases tienen objetivos, contenidos, agenda, práctica y entregable.
- Las 16 partes poseen introducción, resultados y proyecto.
- Existen 96 laboratorios guiados.
- Se incluyen evaluaciones diagnósticas y finales por parte.
- Hay simuladores funcionales iniciales en Python.
- El Banco Virtual incluye un MVP ejecutable con SQLite.
- Los contenidos regulatorios se presentan de forma general y deben adaptarse al país y fecha de uso.

Consulta [STATUS.md](STATUS.md) para conocer qué está desarrollado y qué falta.

## Inicio rápido

```bash
git clone <URL-DEL-REPOSITORIO>
cd finance-and-banking-evolution-program
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate
pip install -r requirements.txt
python tools/validate_program.py
pytest
```

Ejecutar el banco virtual:

```bash
python apps/openbank_simulator/cli.py demo
```

Ejecutar calculadoras:

```bash
python apps/financial_calculators/cli.py compound --principal 100000 --rate 0.08 --years 5
python apps/financial_calculators/cli.py loan --principal 5000000 --annual-rate 0.18 --months 36
```

## Cómo estudiar

1. Lee el `README.md` de cada parte.
2. Recorre las clases en orden.
3. Completa al menos un laboratorio por semana.
4. Responde el diagnóstico y la evaluación final.
5. Entrega el proyecto de la parte.
6. Registra evidencias en `portfolio/`.

## Rutas sugeridas

- **Equilibrada:** 6 horas por semana durante 60 semanas.
- **Profesional:** 8 horas por semana durante 45 semanas.
- **Intensiva:** 12 horas por semana durante 30 semanas.
- **Autodidacta:** 3 horas por semana durante 120 semanas.

## Tecnologías

- Markdown y Mermaid para documentación.
- Python para cálculos, datos, riesgo y simuladores.
- SQLite para el banco virtual educativo.
- CSV y JSON para ejercicios y datasets sintéticos.
- JavaScript/TypeScript opcional con `pnpm` en futuras interfaces.

## Navegación

- [Programa completo](SYLLABUS.md)
- [Ruta de aprendizaje](docs/ruta-aprendizaje.md)
- [Mapa de competencias](docs/mapa-competencias.md)
- [Guía docente](docs/guia-docente.md)
- [Glosario](docs/glosario.md)
- [Fórmulas](docs/formulas.md)
- [Banco virtual](apps/openbank_simulator/README.md)
- [Proyectos](projects/README.md)

## Principios

1. Aprender haciendo.
2. No invertir ni endeudarse sin comprender.
3. Separar hechos, supuestos y estimaciones.
4. Documentar decisiones.
5. Proteger datos y actuar éticamente.
6. Validar siempre normativa, tasas y productos vigentes.

## Licencia

Código y materiales originales bajo licencia MIT. Los nombres, datos y escenarios del programa son educativos y ficticios, salvo que se indique expresamente lo contrario.
