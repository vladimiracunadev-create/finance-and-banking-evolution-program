---
part: 1
class: 14
title: "Proyecto: calculadora financiera personal"
level: fundamento
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 14 · Proyecto: calculadora financiera personal

> [← 13 · Herramientas: calculadora, Excel y Python](13-herramientas-calculadora-excel-y-python.md) · [Índice de la parte](../README.md) · [Proyecto de la parte →](../project/README.md)

**Parte 01 — Matemática financiera básica** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Integrar las trece clases anteriores en un producto único, funcional y defendible: una calculadora
financiera personal que resuelva los cálculos que una persona necesita de verdad y que **muestre su
razonamiento**, no solo el resultado. Este proyecto es el primer entregable serio del portafolio y el
modelo de todos los proyectos posteriores.

## 📚 Objetivos

Al finalizar podrás:

1. **Especificar** los requisitos funcionales de una herramienta financiera.
2. **Implementar** las siete funciones básicas con verificación automática.
3. **Documentar** supuestos, límites y fuentes de cada cálculo.
4. **Validar** los resultados contra un caso verificado a mano.
5. **Defender** tus decisiones de diseño ante una revisión.

<!-- gen:agenda:start -->
## Agenda de 90 minutos

La clase dura noventa minutos y se recorre en cinco tramos. No es un horario
rígido: es el orden en que los bloques de esta página se sostienen unos a otros, y
por eso conviene respetarlo aunque cambien los tiempos.

Los **diez primeros minutos** se dedican a recuperar la clase anterior, porque casi
todo lo que aquí se explica supone algo que ya se vio. Los **veinticinco
siguientes** desarrollan los conceptos con la fuente oficial a la vista: las
referencias del final de la página no son un adorno bibliográfico, se consultan
mientras se estudia. Del **minuto 35 al 55** se resuelve el ejemplo guiado paso a
paso, sin saltarse ninguno, porque el error típico vive precisamente en el paso que
parece obvio. Los **veinticinco minutos siguientes** son de práctica con datos
propios o sintéticos —nunca reales de terceros—, que es cuando se comprueba si se
entendió. Los **diez últimos** cierran con las preguntas de comprobación y el
registro del entregable.

Si el tiempo aprieta, lo que se recorta es la práctica y se traslada al
laboratorio de la parte; lo que no se recorta nunca es el ejemplo guiado.
<!-- gen:agenda:end -->

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| `requisito funcional` | Qué debe hacer la herramienta, escrito de forma verificable: "dado capital, tasa y plazo, devuelve la cuota". |
| `caso de prueba` | Entrada con salida conocida. Es el contrato entre lo que crees que hace y lo que hace. |
| `alcance declarado` | Qué **no** hace la herramienta. Tan importante como lo que hace. |
| `interfaz` | Cómo se usan las funciones: línea de comandos, planilla o notebook. Debe ser usable por alguien que no la escribió. |
| `defensa` | Explicar por qué elegiste cada supuesto, ante preguntas. Es el ejercicio profesional real. |

## 🧠 Modelo mental

Un entregable financiero se juzga por **tres capas**, en este orden:

```text
1. ¿el número es correcto?        ← pruebas
2. ¿se sabe de dónde salió?       ← supuestos y fuentes
3. ¿se entiende qué NO cubre?     ← límites declarados
```

Una herramienta que acierta el número y falla las capas 2 y 3 no es utilizable en un entorno
profesional. Este proyecto se evalúa en las tres.

## 📖 Desarrollo

### 1. Requisitos mínimos

La calculadora debe resolver, como mínimo:

| # | Función | Entrada | Salida | Clase de origen |
|---:|---|---|---|---|
| 1 | Interés simple | `C, i, n` | `I, M` | 5 |
| 2 | Interés compuesto | `C, i, n, m` | `M`, TEA | 6 |
| 3 | Valor presente | `F, i, n` | `VP` | 9 |
| 4 | Valor futuro de aportes | `A, i, n` | `VF`, aporte vs. rendimiento | 10 |
| 5 | Cuota de crédito | `P, i, n` | cuota, interés total | 11 |
| 6 | Tabla de desarrollo | `P, i, n` | tabla completa + controles | 11 |
| 7 | Tasa implícita | `P, cuota, n` | `i` mensual y efectiva anual | 11 |

Requisitos transversales obligatorios:

- Toda salida monetaria redondeada al peso, con la política declarada.
- Toda tasa mostrada en su forma periódica **y** efectiva anual.
- Rechazo explícito de entradas inválidas (tasa negativa, plazo cero, capital cero).
- Al menos una prueba por función.

### 2. Arquitectura sugerida

```text
apps/financial_calculators/
  calculators.py     funciones puras, sin entrada/salida
  cli.py             interfaz de línea de comandos
  README.md          uso, supuestos y límites
tests/
  test_calculators.py
portfolio/parte-01/clase-14/
  supuestos.md       hoja de supuestos del proyecto
  validacion.md      caso verificado a mano vs. salida del programa
```

La separación entre `calculators.py` (cálculo puro) y `cli.py` (interacción) no es un capricho: es lo
que permite probar el cálculo sin simular teclas, y es el mismo principio que el banco virtual de la
Parte 16 aplica a escala.

### 3. Implementación de referencia

Las funciones ya existen parcialmente en este repositorio. Amplíalas:

```python
def implied_rate(principal: float, payment: float, periods: int,
                 tol: float = 1e-10, max_iter: int = 200) -> float:
    """Tasa periódica que iguala `principal` con `periods` cuotas de `payment`.

    Usa bisección: robusta y suficiente para el rango de tasas de crédito
    de consumo. Devuelve la tasa en decimal (0,0145 = 1,45 % periódico).
    """
    if payment * periods <= principal:
        raise ValueError("Sin interés positivo: revisa los datos de entrada")
    low, high = 0.0, 1.0
    for _ in range(max_iter):
        mid = (low + high) / 2
        cuota = fixed_payment(principal, mid, periods)
        if abs(cuota - payment) < tol:
            return mid
        if cuota < payment:
            low = mid
        else:
            high = mid
    return (low + high) / 2
```

### 4. Validación contra caso conocido

`portfolio/parte-01/clase-14/validacion.md` debe contener al menos:

```text
Caso 1 — cuota (verificado a mano en la clase 11)
  entrada   P=5 000 000  i=0,0145  n=36
  esperado  179 787
  obtenido  179 787       ✔

Caso 2 — tasa implícita (verificado a mano en la clase 11)
  entrada   P=3 200 000  cuota=158 900  n=24
  esperado  1,515 % mensual (±0,005)
  obtenido  1,5148 %       ✔

Caso 3 — tabla cierra en cero
  entrada   P=1 000 000  i anual=0,12  n=12
  esperado  saldo final < 0,01
  obtenido  0,00           ✔

Caso 4 — entrada inválida
  entrada   P=1 000 000  i=−0,05  n=12
  esperado  error controlado con mensaje claro
  obtenido  ValueError("La tasa no puede ser negativa")  ✔
```

### 5. Límites que debes declarar

Ninguna calculadora de este nivel cubre lo siguiente, y omitirlo sería afirmar de más:

- No incluye seguros, comisiones ni gastos notariales salvo que se ingresen manualmente.
- No calcula carga anual equivalente según la fórmula regulatoria de ningún país concreto.
- No considera prepagos parciales ni mora.
- No sustituye la simulación oficial de una institución financiera.
- Los resultados son estimaciones educativas, no ofertas.

## 🧮 Ejemplo guiado

**Situación de defensa.** Presentas la calculadora y el revisor pregunta: *"¿Por qué tu tasa implícita
usa bisección y no Newton-Raphson, que converge más rápido?"*

**Respuesta defendible.** Tres argumentos, en orden de fuerza:

1. **Robustez sobre velocidad.** Newton-Raphson necesita derivada y puede divergir con un valor
   inicial malo. Bisección converge siempre si hay cambio de signo en el intervalo, y el intervalo
   `[0, 1]` cubre cualquier tasa periódica de crédito de consumo real.
2. **El costo no importa aquí.** 200 iteraciones de bisección sobre una función trivial son
   microsegundos. La velocidad sería relevante procesando millones de créditos, no uno.
3. **Auditabilidad.** Bisección se explica en una frase a un auditor no técnico. Ese criterio importa
   más de lo que parece en un entorno regulado (Parte 12, clase 13).

**Contra-pregunta esperable:** *"¿Y si la tasa real supera el 100 % periódico?"* Respuesta: el
intervalo se amplía y se documenta; pero una tasa periódica superior a 100 % excede los límites de
usura de la mayoría de las jurisdicciones, así que el caso pertenece al validador de entrada, no al
algoritmo.

**Lo que este intercambio enseña:** en finanzas, *"funciona"* no es una defensa. Se defiende con
robustez, proporcionalidad al problema y auditabilidad.

## 🏦 Del cliente al banco

| Tu calculadora | Equivalente en producción |
|---|---|
| `fixed_payment()` | Motor de cotización del simulador del banco |
| `implied_rate()` | Cálculo de CAE del área de cumplimiento |
| Tabla de desarrollo | Documento contractual generado por el core bancario |
| Casos de prueba | Suite de regresión del área de tecnología |
| Hoja de supuestos | Documentación de modelo exigida por el supervisor |

## 🧪 Práctica

Este proyecto **es** la práctica. Trabaja en `project/README.md` de esta parte.

1. Escribe los siete requisitos como casos de prueba antes de programar.
2. Implementa las funciones que falten y ejecuta `pytest -q` hasta ver todo en verde.
3. Redacta `supuestos.md` y `validacion.md`.
4. Prepara una defensa de tres minutos con dos decisiones de diseño justificadas.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| La calculadora acierta pero nadie la puede usar | No hay interfaz ni documentación de uso | Escribe el `README.md` con ejemplos ejecutables. |
| Las pruebas pasan pero el resultado es incorrecto | Se probó contra el propio código, no contra un caso verificado a mano | Usa como esperado un valor calculado independientemente. |
| Falla con entradas extremas | No hay validación de entrada | Rechaza tasa negativa, plazo cero y capital no positivo con mensaje claro. |
| El proyecto afirma calcular la CAE | Se confundió tasa implícita con carga anual equivalente regulatoria | Declara el límite: la CAE tiene fórmula normativa por país. |
| No se puede reproducir el resultado meses después | Faltó hoja de supuestos | Documenta datos, fuente, fecha y versión. |
| La defensa se limita a "así lo hice" | No se justificaron las decisiones | Prepara una razón técnica por cada elección de diseño. |

## ❓ Preguntas de comprobación

1. ¿Por qué las funciones de cálculo deben estar separadas de la interfaz?
2. ¿Qué diferencia hay entre una prueba que valida el código y una que valida el resultado?
3. ¿Por qué la calculadora no debe afirmar que calcula la carga anual equivalente?
4. Defiende en tres frases la elección de bisección para la tasa implícita.
5. ¿Qué cinco límites declararías al entregar esta herramienta a otra persona?

## 📥 Entregable

Guarda en `portfolio/parte-01/clase-14/` y en `apps/financial_calculators/`:

- el código de las siete funciones con sus pruebas;
- la salida de `pytest -q` completamente en verde;
- `supuestos.md` con datos, fuentes, convenciones y versión;
- `validacion.md` con al menos cuatro casos verificados a mano;
- las notas de tu defensa de tres minutos.

<!-- gen:etica:start -->
## 🔐 Seguridad, ética y límites

Trabaja siempre con datos sintéticos o propios: nunca uses datos reales de terceros,
números de cuenta, documentos de identidad ni antecedentes crediticios ajenos. Este
material es formativo y **no constituye asesoría financiera, tributaria ni legal**; las
tasas, comisiones, límites y normas citados cambian y deben verificarse en la fuente
oficial vigente del país donde se aplique. Cuando un cálculo alimente una decisión que
afecte a otra persona, registra los supuestos y quién los aprobó.
<!-- gen:etica:end -->

## 📗 Fuentes y verificación

- Benninga, S. (2014). *Financial Modeling* (4.ª ed.). MIT Press. Diseño y validación de modelos financieros.
- Ross, S., Westerfield, R. y Jordan, B. (2022). *Fundamentos de finanzas corporativas* (12.ª ed.). McGraw-Hill. Capítulos 4 a 6: el conjunto de cálculos que la herramienta debe cubrir.
- Broverman, S. (2017). *Mathematics of Investment and Credit* (7.ª ed.). ACTEX. Casos de referencia para validar resultados.
- Federal Reserve / OCC (2011). *Supervisory Guidance on Model Risk Management* (SR 11-7). Estructura de documentación y validación exigida a un modelo.
- Basel Committee on Banking Supervision (2013). *BCBS 239: Principles for effective risk data aggregation and risk reporting*. BIS. Trazabilidad y reproducibilidad.
- Verificación local: si tu herramienta se usará con datos reales, revisa la normativa de protección de datos personales y de información precontractual de crédito de tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 13 · Herramientas: calculadora, Excel y Python](13-herramientas-calculadora-excel-y-python.md) | [Parte 01](../README.md) · [Programa](../../../SYLLABUS.md) | [Proyecto de la parte →](../project/README.md) |
<!-- gen:footer:end -->
