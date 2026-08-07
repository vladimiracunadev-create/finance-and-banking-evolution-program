---
part: 7
class: 15
title: "Proyecto: motor de valoración"
level: avanzado
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 15 · Proyecto: motor de valoración

> [← 14 · Modelamiento con Excel y Python](14-modelamiento-con-excel-y-python.md) · [Índice de la parte](../README.md) · [Proyecto de la parte →](../project/README.md)

**Parte 07 — Matemática financiera avanzada** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir una herramienta que evalúe proyectos de inversión con todos los criterios de la parte,
incorpore análisis de riesgo y produzca un informe defendible ante un comité. Es el entregable
técnico más exigente del programa hasta este punto y el insumo directo de la evaluación crediticia de
la Parte 9 y de las finanzas corporativas de la Parte 13.

## 📚 Objetivos

Al finalizar podrás:

1. **Especificar** los requisitos de un motor de valoración completo.
2. **Implementar** los criterios de evaluación con verificación automática.
3. **Incorporar** sensibilidad, escenarios y simulación.
4. **Generar** un informe de comité con la estructura profesional.
5. **Defender** las decisiones de diseño y las limitaciones declaradas.

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
| `motor de valoración` | Herramienta que transforma supuestos en criterios de decisión con su análisis de riesgo. |
| `informe de comité` | Documento de una a tres páginas con recomendación, evidencia y condiciones. |
| `caso de validación` | Proyecto con resultado conocido, calculado de forma independiente. |
| `limitación declarada` | Lo que el motor no calcula. Su omisión hace que la herramienta afirme de más. |
| `defensa técnica` | Justificación de cada decisión de diseño con argumentos verificables. |

## 🧠 Modelo mental

El motor debe responder **cinco preguntas en orden**:

```text
1. ¿el proyecto crea valor?          → VAN
2. ¿cuánto rinde?                    → TIR, TIRM
3. ¿cuándo se recupera?              → payback
4. ¿qué tendría que fallar?          → sensibilidad
5. ¿cuál es la probabilidad de perder? → simulación
```

Un motor que responde las tres primeras es una calculadora. Uno que responde las cinco es una
herramienta de decisión.

## 📖 Desarrollo

### 1. Requisitos funcionales

| # | Requisito | Entrada | Salida |
|---:|---|---|---|
| 1 | Construir flujo de caja libre | Supuestos operativos, inversión, impuestos, capital de trabajo | Serie de FCF |
| 2 | Calcular VAN | FCF, tasa | VAN |
| 3 | Calcular TIR y TIRM | FCF, tasa de reinversión | TIR, TIRM |
| 4 | Calcular payback | FCF | Simple y descontado |
| 5 | Calcular índice de rentabilidad | FCF, inversión | IR |
| 6 | Sensibilidad univariante | Variables y rangos | Tabla y tornado |
| 7 | Sensibilidad bivariante | Dos variables | Tabla cruzada con frontera |
| 8 | Escenarios | Tres conjuntos de supuestos con probabilidad | Valor esperado y dispersión |
| 9 | Simulación | Distribuciones y correlaciones | Distribución, percentiles, probabilidad de pérdida |
| 10 | Valores de equilibrio | Variable objetivo | Valor que anula el VAN y margen de seguridad |
| 11 | Detectar TIR múltiple | FCF | Advertencia si hay más de un cambio de signo |
| 12 | Generar informe | Todo lo anterior | Documento de comité |

Requisitos transversales:

```text
· toda entrada valida su rango y exige fuente
· todo resultado incluye la tasa y los supuestos usados
· la herramienta declara sus limitaciones en cada salida
· ningún resultado se presenta como punto único sin su rango
```

### 2. Arquitectura

```text
apps/valuation_engine/
  models.py         Supuestos, Resultado, Escenario (dataclasses)
  cashflow.py       construcción del flujo de caja libre
  criteria.py       VAN, TIR, TIRM, payback, IR
  sensitivity.py    univariante, bivariante, tornado, equilibrio
  simulation.py     Monte Carlo con correlaciones
  report.py         generación del informe de comité
  cli.py            interfaz de línea de comandos
  README.md         uso, supuestos y limitaciones
tests/
  test_cashflow.py
  test_criteria.py
  test_sensitivity.py
  test_simulation.py
portfolio/parte-07/clase-15/
  supuestos.md      hoja de supuestos del caso
  validacion.md     casos verificados independientemente
  informe.md        informe de comité del caso
  defensa.md        justificación de decisiones de diseño
```

### 3. Implementación de referencia

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Resultado:
    """Resultado completo de una evaluación, con sus advertencias."""

    van: float
    tir: float | None
    tirm: float
    payback_simple: float | None
    payback_descontado: float | None
    indice_rentabilidad: float
    advertencias: tuple[str, ...] = ()

    def decision(self, umbral_van: float = 0.0) -> str:
        if self.van > umbral_van:
            return "APROBAR"
        return "RECHAZAR"

def detectar_tir_multiple(flujos: list[float]) -> bool:
    """Advierte si el flujo cambia de signo más de una vez.

    Con más de un cambio de signo puede existir más de una TIR, y la regla
    de decisión basada en TIR deja de ser aplicable. En ese caso el motor
    reporta la TIRM y omite la TIR.
    """
    signos = [1 if f > 0 else -1 for f in flujos if f != 0]
    cambios = sum(1 for a, b in zip(signos, signos[1:]) if a != b)
    return cambios > 1

def payback_descontado(flujos: list[float], tasa: float) -> float | None:
    """Periodos hasta recuperar la inversión con flujos descontados.

    Devuelve None si la inversión no se recupera en el horizonte, lo que es
    una respuesta legítima y no un error.
    """
    acumulado = 0.0
    for t, flujo in enumerate(flujos):
        vp = flujo / (1 + tasa) ** t
        anterior = acumulado
        acumulado += vp
        if anterior < 0 <= acumulado:
            return t - 1 + abs(anterior) / vp
    return None
```

### 4. El informe de comité

```text
EVALUACIÓN DE PROYECTO — Ampliación de capacidad planta norte
Fecha: 2026-08-05 · Analista: [nombre] · Versión del modelo: 2.1

RECOMENDACIÓN: APROBAR con condiciones

1. RESUMEN
   Inversión 2 400 millones · Horizonte 8 años · WACC 13,5 %
   VAN 2 581 millones · TIR 26,4 % · TIRM 18,1 % · Payback descontado 4,2 años
   Probabilidad de VAN negativo: 12,4 %

2. VARIABLES CRÍTICAS
   El precio de venta explica el 71 % de la variación del resultado.
   Margen de seguridad del precio: 13,1 % (equilibrio en 851 183).
   Probabilidad histórica de cruzar el equilibrio: 30 % sin cobertura.

3. ESCENARIOS
   Adverso (20 %)   VAN −1 087   cobertura del servicio 0,82
   Base    (55 %)   VAN  2 581   cobertura 1,74
   Favorable (25 %) VAN  5 702   cobertura 2,41
   Valor esperado: 2 496 millones

4. CONDICIONES DE APROBACIÓN
   C1  contratos de precio mínimo por ≥ 60 % de la producción
   C2  covenant de cobertura de servicio de deuda ≥ 1,15, medición anual
   C3  cuenta de reserva equivalente a 6 meses de servicio
   C4  seguimiento trimestral del precio, umbral de alerta en 880 000

5. LIMITACIONES DEL ANÁLISIS
   · no incorpora opciones reales (expansión, abandono)
   · supone estructura de capital constante
   · el precio se modela con la distribución histórica de 10 años
   · no considera efectos tributarios de pérdidas acumuladas
   · las correlaciones se estimaron con datos sectoriales, no del proyecto

6. TRAZABILIDAD
   Supuestos: portfolio/parte-07/clase-15/supuestos.md
   Validación: portfolio/parte-07/clase-15/validacion.md
   Modelo: apps/valuation_engine, commit a1b2c3d
```

La sección 5 es la que distingue un informe profesional. **Un análisis que no declara lo que no
cubre está afirmando implícitamente que lo cubre todo.**

### 5. Casos de validación

```text
Caso 1 — VAN con flujos constantes (verificado a mano)
  I₀ = 100 000 · FCF = 25 000 × 6 años · k = 10 %
  esperado: 25 000 × 4,35526 − 100 000 = 8 882
  obtenido: 8 882  ✔

Caso 2 — TIR igual a la tasa que anula el VAN
  cualquier proyecto: van(tir(p)) ≈ 0
  obtenido: |VAN| < 1,0  ✔

Caso 3 — TIR múltiple detectada
  FCF: −60 000, +155 000, −100 000
  esperado: advertencia activada, TIR omitida, TIRM reportada
  obtenido: advertencia "flujo no convencional: 2 cambios de signo"  ✔

Caso 4 — payback no alcanzado
  FCF: −100 000, 10 000 × 5 años
  esperado: None (no se recupera)
  obtenido: None  ✔

Caso 5 — monotonía del VAN respecto del WACC
  esperado: VAN decreciente al aumentar el WACC
  obtenido: decreciente en 20 valores probados  ✔

Caso 6 — simulación converge
  esperado: media de 10 000 iteraciones ≈ media de 50 000 iteraciones (±2 %)
  obtenido: diferencia de 0,8 %  ✔
```

## 🧮 Ejemplo guiado

**Situación de defensa.** El comité formula tres preguntas sobre tu motor.

**Pregunta 1: "Tu motor reporta TIR y TIRM. ¿Cuál debemos mirar?"**

```text
"Ninguna de las dos para decidir: la decisión es por VAN.

 La TIR se reporta porque es el lenguaje del comité y de los promotores del
 proyecto, y porque permite comparar con el WACC de un vistazo.

 La TIRM se reporta al lado porque la brecha entre ambas mide cuánto de la
 TIR depende de un supuesto de reinversión que la empresa no puede cumplir.
 En este proyecto la brecha es de 8,3 puntos (26,4 % contra 18,1 %), lo que
 significa que la TIR de 26,4 % supone reinvertir los flujos al 26,4 %, y
 nuestro WACC es 13,5 %.

 Si el comité solo mira un número, que mire el VAN. Si mira dos, VAN y TIRM."
```

**Pregunta 2: "La simulación dice 12,4 % de probabilidad de VAN negativo. ¿Qué tan confiable es ese
número?"**

```text
"Es tan confiable como sus supuestos, y esos supuestos son de tres calidades distintas:

 · la distribución del precio se estimó con 10 años de datos oficiales:
   confianza alta, aunque el periodo no incluye un shock de oferta extremo
 · la distribución de producción proviene del estudio agronómico del proyecto:
   confianza media, es una estimación sin historial
 · las correlaciones se estimaron con datos sectoriales, no del proyecto:
   confianza media-baja

 El número que sí es robusto es el ORDEN de magnitud: la probabilidad de
 pérdida está entre 8 % y 18 % según la correlación que se suponga.
 Ese rango es la información relevante, y en cualquier punto de ese rango
 la condición C1 (contratos de precio mínimo) se justifica."
```

**Pregunta 3: "¿Por qué tu motor no calcula opciones reales? El proyecto tiene opción de expansión."**

```text
"Porque no sé valorarla con la información disponible y prefiero declararlo
 antes que producir un número que parezca riguroso.

 Valorar la opción de expansión exigiría estimar la volatilidad del valor
 subyacente del proyecto, y no tenemos base empírica para ese parámetro.
 Un modelo binomial con una volatilidad inventada produciría un número
 preciso y sin fundamento.

 Lo que sí puedo afirmar: la opción de expansión tiene valor positivo, de modo
 que el VAN de 2 581 millones es un PISO, no una estimación centrada.
 Si el comité quiere cuantificarla, propongo encargar un estudio de
 volatilidad sectorial antes de modelarla."
```

**Lo que estas tres respuestas enseñan:** un motor de valoración se defiende **explicando qué mide
cada indicador, graduando la confianza de cada supuesto y declarando lo que no se sabe**. La respuesta
"no lo calculo porque no tengo base para hacerlo" es más profesional que cualquier número inventado.

## 🏦 Del cliente al banco

| Componente del motor | Equivalente profesional | Parte |
|---|---|---|
| Flujo de caja libre | Base del análisis de crédito comercial | 13, clase 3 |
| Criterios de decisión | Evaluación de proyectos en comité | 13, clase 13 |
| Simulación | Cálculo de pérdida esperada | 11, clase 2 |
| Informe de comité | Formato del acta de aprobación | 9, clase 2 |
| Limitaciones declaradas | Documentación de modelo exigida | 12, clase 13 |

## 🧪 Práctica

Este proyecto es la práctica. Trabaja en `project/README.md` de esta parte.

1. Implementa los doce requisitos con sus pruebas en verde.
2. Documenta los seis casos de validación con verificación independiente.
3. Evalúa un proyecto real o sintético y genera el informe de comité completo.
4. Prepara la defensa de tres decisiones de diseño con sus limitaciones.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El motor recomienda sin advertir | Limitaciones no declaradas | Toda salida incluye sus límites. |
| Se reporta TIR de un flujo no convencional | Sin detección de TIR múltiple | Implementa la advertencia. |
| La simulación se presenta como precisa | Confianza no graduada | Declara la calidad de cada supuesto. |
| Las pruebas validan el propio código | Sin verificación independiente | Usa casos calculados por otro medio. |
| El informe tiene ocho páginas | Sin jerarquía | Máximo tres páginas, con resumen en la primera. |
| Se inventa un parámetro faltante | Falsa completitud | Declara que no se calcula y por qué. |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las cinco preguntas que un motor de valoración debe responder?
2. ¿Por qué se reportan TIR y TIRM juntas y cuál se usa para decidir?
3. ¿Qué debe contener la sección de limitaciones de un informe?
4. ¿Por qué una prueba de propiedad estructural es indispensable?
5. ¿Cómo se responde cuando falta información para calcular algo relevante?

## 📥 Entregable

Guarda en `portfolio/parte-07/clase-15/` y en `apps/valuation_engine/`:

- el código con los doce requisitos y sus pruebas en verde;
- `validacion.md` con los seis casos verificados de forma independiente;
- `informe.md` con el informe de comité completo de un proyecto evaluado;
- `defensa.md` con la justificación de tres decisiones de diseño y sus limitaciones.

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

- Benninga, S. (2014). *Financial Modeling* (4.ª ed.). MIT Press. Construcción de modelos de valoración completos.
- Damodaran, A. (2012). *Investment Valuation* (3.ª ed.). Wiley. Capítulos 5, 6 y 28: criterios, riesgo y opciones reales.
- Brealey, R., Myers, S. y Allen, F. (2023). *Principios de finanzas corporativas* (14.ª ed.). McGraw-Hill. Capítulos 5, 6, 10 y 22.
- Federal Reserve / OCC (2011). *Supervisory Guidance on Model Risk Management* (SR 11-7). Documentación, validación y limitaciones de un modelo.
- Koller, T., Goedhart, M. y Wessels, D. (2020). *Valuation* (7.ª ed.). McKinsey/Wiley. Estructura de un informe de valoración.
- Verificación local: contrasta el formato de tu informe con el que exige el comité de crédito de una institución de tu mercado, si tienes acceso a uno.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 14 · Modelamiento con Excel y Python](14-modelamiento-con-excel-y-python.md) | [Parte 07](../README.md) · [Programa](../../../SYLLABUS.md) | [Proyecto de la parte →](../project/README.md) |
<!-- gen:footer:end -->
