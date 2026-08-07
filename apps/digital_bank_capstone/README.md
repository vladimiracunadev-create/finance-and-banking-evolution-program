# Digital Bank Capstone

Motor del proyecto capstone de la **Parte 23**. Cuatro módulos que implementan las
decisiones que un equipo toma al construir un banco digital completo: qué entra en
el alcance, qué se construye y qué se integra, qué contradicciones aparecen al
integrar y dónde se rompe el sistema, **con la biblioteca estándar y sin red**.

> ## Aviso
>
> **Todo lo que hay aquí es didáctico y trabaja con datos sintéticos.** No es un
> banco, no se conecta con ninguna infraestructura real, no usa credenciales ni
> fondos, y ninguna de sus salidas constituye asesoría legal, financiera ni de
> inversión. Su propósito es sostener las decisiones de un capstone, no operar.

## Qué demuestra ejecutando

Cuatro conclusiones contraintuitivas que el motor obliga a comprobar:

| Intuición habitual | Lo que el motor demuestra | Clase |
|---|---|---|
| «Reducir el alcance baja el ingreso» | El ingreso no cambia: las excluidas no lo generaban | 1 |
| «Se integra lo que es más barato integrar» | Sin salida real, integrar es una dependencia estructural | 2 |
| «Cada componente está bien, luego el sistema está bien» | Una tensión sin resolver bloquea la operación | 12 |
| «Tres fallos a la vez son improbables» | Un proveedor con tres papeles los produce con uno solo | 15 |

## Estructura

```text
apps/digital_bank_capstone/
├── README.md
├── __init__.py
├── scope.py      las cuatro preguntas, exclusiones con razón y carga regulatoria
├── build.py      construir, integrar o comprar, con la salida por encima del coste
├── tensions.py   decisiones, tolerancias del consejo y tensiones que hay que resolver
├── stress.py     fuente de correlación, escenario y punto de rotura en desviaciones
└── cli.py
```

## Uso

Aplicar las cuatro preguntas al alcance y calcular la cifra que decide si el
proyecto existe:

```bash
python apps/digital_bank_capstone/cli.py scope
```

Decidir componente a componente entre construir, integrar o comprar:

```bash
python apps/digital_bank_capstone/cli.py build
```

Ver cómo dos decisiones correctas por separado bloquean el sistema al integrarse:

```bash
python apps/digital_bank_capstone/cli.py tensions
```

Construir el escenario desde la fuente de correlación y medir el punto de rotura:

```bash
python apps/digital_bank_capstone/cli.py stress
```

## Decisiones de diseño

Cuatro reglas están implementadas como restricciones del código y no como
consejos, porque en un capstone lo que se recomienda se omite:

- **Una exclusión sin razón escrita se rechaza.** `Alcance.excluir` lanza
  `ValueError` si la razón está vacía, porque una exclusión sin razón reaparece en
  la reunión siguiente.
- **La salida manda sobre el coste.** `Componente.decidir` devuelve `CONSTRUIR`
  cuando no hay salida real, aunque integrar sea más barato.
- **La tolerancia al impacto la fija el consejo.** `Sistema.fijar_tolerancia`
  rechaza cualquier origen que no sea el consejo, porque una tolerancia fijada por
  el área técnica es una cifra de disponibilidad, no de daño al cliente.
- **Una tensión sin resolver bloquea la operación.** `Sistema.puede_operar`
  devuelve falso mientras quede una tensión declarada y sin sacrificio escrito.

## Pruebas

```bash
python -m pytest tests/test_digital_bank_capstone.py -q
```

Veinticuatro pruebas. Cuatro llevan el sufijo `_documenta_el_problema` y **deben
pasar**: reproducen los razonamientos que el capstone persigue, y si dejaran de
pasar sería el modelo el que habría cambiado, no el problema.

## Límites

- Los ingresos, costes y volúmenes son **sintéticos**: la comparación entre
  alternativas es robusta, las cifras absolutas no.
- El liquidador de tensiones no ordena las contradicciones por importancia: esa
  decisión es del consejo, no del modelo.
- El escenario conserva la peor interrupción por componente y no acumula fallos
  sucesivos sobre el mismo componente.
- El modelo no cubre la cadena de suministro del software, que exige su propio
  análisis.
