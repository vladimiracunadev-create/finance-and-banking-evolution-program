# Finance & Banking Evolution Program

Programa abierto de formación en finanzas y banca que recorre, clase a clase, el camino desde el
manejo de un porcentaje hasta la dirección de un banco.

[![Validate program](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/actions/workflows/validate.yml/badge.svg)](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/actions/workflows/validate.yml)
[![Licencia](https://img.shields.io/badge/licencia-MIT-black)](LICENSE)
[![Estado](https://img.shields.io/badge/avance-ver%20STATUS.md-blue)](STATUS.md)

> Cada clase incluye desarrollo conceptual, un ejemplo numérico resuelto paso a paso, el puente entre
> la decisión personal y la práctica bancaria, errores frecuentes, preguntas de comprobación y
> **bibliografía oficial verificable**.

---

## Qué es esto

Un currículo completo de 16 partes y 240 clases de 90 minutos, diseñado para que una misma persona
avance sin saltos desde no saber calcular un interés hasta poder sentarse en un comité de crédito.

No es una colección de apuntes. Cada clase sigue una estructura fija verificada por integración
continua, y cada afirmación técnica está respaldada por fuentes consultables: manuales universitarios
de referencia, normas contables NIIF, documentos del Comité de Basilea, y marcos de la OCDE, el FMI,
el Banco Mundial, el GAFI y los organismos de estándares del sector.

**Estado actual del contenido: [STATUS.md](STATUS.md)**, generado automáticamente desde los archivos
del repositorio. Nunca declara más de lo que existe.

## Para quién

| Perfil | Punto de entrada | Qué obtiene |
|---|---|---|
| Sin conocimientos previos | Parte 1, clase 1 | Base matemática y control de sus finanzas |
| Persona que quiere ordenar su dinero | Partes 1 a 4 | Presupuesto, deuda, seguridad y derechos |
| Estudiante de finanzas o contabilidad | Partes 5 a 8 | Contabilidad, economía, valoración e inversión |
| Analista financiero | Partes 7 a 9 y 13 | Modelamiento, crédito y finanzas corporativas |
| Profesional bancario | Partes 9 a 12 | Crédito, operaciones, riesgos y cumplimiento |
| Dirección y gestión | Partes 14 a 16 | Fintech, estrategia y el banco virtual completo |

## Cómo está construida cada clase

```text
🎯 Propósito              por qué existe la clase y qué problema resuelve
📚 Objetivos              cinco resultados verificables
   Agenda de 90 minutos   guía docente, generada automáticamente
🧩 Conceptos centrales    tabla de término y comprensión verificable
🧠 Modelo mental          la idea que ordena todo lo demás
📖 Desarrollo             el contenido, con fórmulas, tablas y casos
🧮 Ejemplo guiado         un caso numérico resuelto paso a paso, con su interpretación
🏦 Del cliente al banco   el mismo concepto visto desde ambos lados del mostrador
🧪 Práctica               qué hacer en el laboratorio de la parte
⚠️ Errores frecuentes     síntoma, causa probable y corrección
❓ Preguntas              cinco preguntas de comprobación
📥 Entregable             qué guardar en el portafolio
🔐 Seguridad y ética      límites del material, generado automáticamente
📗 Fuentes                bibliografía oficial, mínimo cuatro por clase
```

El **puente «del cliente al banco»** es lo que hace que el programa sirva a los dos extremos del
recorrido: la misma clase que enseña a una persona a leer su estado de cuenta explica al futuro
bancario cómo se decide ese cobro y qué norma lo regula.

## Estructura del programa

| # | Parte | Clases | Etapa |
|---:|---|---:|---|
| 1 | [Matemática financiera básica](modules/00-matematica-financiera-basica/README.md) | 14 | Fundamentos |
| 2 | [Finanzas personales](modules/01-finanzas-personales/README.md) | 14 | Fundamentos |
| 3 | [Productos y servicios financieros](modules/02-productos-y-servicios-financieros/README.md) | 14 | Fundamentos |
| 4 | [Seguridad y consumo financiero](modules/03-seguridad-y-consumo-financiero/README.md) | 14 | Fundamentos |
| 5 | [Contabilidad financiera](modules/04-contabilidad-financiera/README.md) | 15 | Analista |
| 6 | [Economía y sistema financiero](modules/05-economia-y-sistema-financiero/README.md) | 15 | Analista |
| 7 | [Matemática financiera avanzada](modules/06-matematica-financiera-avanzada/README.md) | 15 | Analista |
| 8 | [Inversiones y mercados](modules/07-inversiones-y-mercados/README.md) | 15 | Analista |
| 9 | [Análisis y gestión de crédito](modules/08-analisis-y-gestion-de-credito/README.md) | 16 | Bancario |
| 10 | [Operaciones bancarias](modules/09-operaciones-bancarias/README.md) | 16 | Bancario |
| 11 | [Gestión integral de riesgos](modules/10-gestion-integral-de-riesgos/README.md) | 16 | Bancario |
| 12 | [Regulación, cumplimiento y auditoría](modules/11-regulacion-cumplimiento-y-auditoria/README.md) | 16 | Bancario |
| 13 | [Finanzas corporativas y banca empresarial](modules/12-finanzas-corporativas-y-banca-empresarial/README.md) | 14 | Dirección |
| 14 | [Fintech, datos e inteligencia artificial](modules/13-fintech-datos-e-inteligencia-artificial/README.md) | 14 | Dirección |
| 15 | [Estrategia y dirección bancaria](modules/14-estrategia-y-direccion-bancaria/README.md) | 14 | Dirección |
| 16 | [Proyecto: Banco Virtual](modules/15-proyecto-banco-virtual/README.md) | 18 | Integración |

Detalle completo en [SYLLABUS.md](SYLLABUS.md).

## Inicio rápido

```bash
git clone https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program.git
```

```bash
cd finance-and-banking-evolution-program && python -m venv .venv && pip install -r requirements.txt
```

```bash
python tools/validate_program.py
```

Calculadoras financieras:

```bash
python apps/financial_calculators/cli.py compound --principal 100000 --rate 0.08 --years 5
```

Simulador de banco:

```bash
python apps/openbank_simulator/cli.py demo
```

## Cómo estudiarlo

1. Lee el `README.md` de la parte para ubicarte.
2. Recorre las clases en orden: cada una supone la anterior.
3. Resuelve el **ejemplo guiado** antes de leer su interpretación.
4. Haz el laboratorio de la parte y guarda la evidencia en `portfolio/`.
5. Responde las preguntas de comprobación sin volver al texto.
6. Entrega el proyecto integrador de la parte.

Ritmos sugeridos: 6 h/semana durante 60 semanas · 8 h/semana durante 45 · 12 h/semana durante 30.

## Verificación

Todo el repositorio se valida en cada cambio:

```bash
python tools/validate_program.py
```

```bash
python tools/render_program.py --check
```

```bash
python tools/progress.py --check
```

```bash
python tools/check_links.py
```

```bash
pytest -q
```

## Fuentes

El contenido se apoya en bibliografía verificable. Entre las obras y marcos citados de forma
recurrente:

- **Finanzas corporativas y valoración:** Brealey, Myers & Allen; Ross, Westerfield & Jaffe; Damodaran; Koller, Goedhart & Wessels
- **Matemática financiera:** Kellison; Broverman; Blank & Tarquin
- **Contabilidad:** Marco Conceptual y normas NIIF/NIC; Kieso, Weygandt & Warfield; Penman; Palepu, Healy & Peek
- **Economía y banca central:** Mankiw; Blanchard; Mishkin; Krugman, Obstfeld & Melitz
- **Inversiones:** Bodie, Kane & Marcus; Fabozzi; Markowitz; Sharpe; Malkiel; Bogle
- **Banca y riesgo:** Saunders & Cornett; Rose & Hudgins; Caouette & Altman; Anderson; Siddiqi; Hull
- **Marcos institucionales:** Comité de Basilea (BIS), FSB, IOSCO, CPMI, GAFI/FATF, OCDE, FMI, Banco Mundial, NIST, COSO, IFRS Foundation

Cada clase cierra con sus propias referencias y con una línea de **verificación local**: los datos
normativos, tasas y límites cambian por país y por fecha, y el programa indica siempre qué debe
comprobarse en la fuente oficial vigente.

## Alcance y límites

Este material es **formativo**. No constituye asesoría financiera, tributaria ni legal, no reemplaza
títulos, certificaciones ni autorizaciones regulatorias, y todos los nombres, cifras y casos son
educativos salvo indicación expresa. Los contenidos normativos se presentan de forma general: **cada
país y cada fecha exigen su propia verificación**.

## Contribuir

Las contribuciones son bienvenidas. Revisa [CONTRIBUTING.md](CONTRIBUTING.md) y verifica que
`tools/validate_program.py` y `pytest -q` pasen antes de abrir una propuesta.

## Licencia

[MIT](LICENSE). El código y los materiales originales son de uso libre citando la fuente.
