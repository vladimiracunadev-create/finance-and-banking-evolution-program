---
part: 7
class: 14
title: "Modelamiento con Excel y Python"
level: avanzado
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 14 · Modelamiento con Excel y Python

> [← 13 · Escenarios y simulación](13-escenarios-y-simulacion.md) · [Índice de la parte](../README.md) · [15 · Proyecto: motor de valoración →](15-proyecto-motor-de-valoracion.md)

**Parte 07 — Matemática financiera avanzada** · **Nivel:** Avanzado — perfil analista · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir modelos financieros que otras personas puedan revisar, auditar y mantener. Un modelo que
solo su autor entiende es un riesgo operacional, no un activo. Esta clase entrega los estándares de
construcción, las pruebas que todo modelo debe superar y el criterio para elegir la herramienta.

Las trece clases anteriores producen modelos. Esta trata de cómo construirlos para que otra persona los pueda auditar, porque un modelo que solo entiende quien lo hizo no se puede usar para decidir. El riesgo de modelo es una categoría de riesgo con nombre propio en la regulación bancaria.

## 📚 Objetivos

Al finalizar podrás:

1. **Aplicar** los estándares de construcción de modelos auditables.
2. **Estructurar** un modelo con separación de entradas, cálculo y salidas.
3. **Implementar** controles automáticos de integridad.
4. **Escribir** pruebas que validen el modelo contra casos conocidos.
5. **Elegir** entre planilla y código según el problema.

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

Los tres primeros términos son estándares de construcción; los tres siguientes, la documentación y el control. La **validación independiente** es la exigencia que separa un modelo profesional de una planilla: alguien que no lo construyó tiene que poder reproducir sus resultados.

| Concepto | Comprensión verificable |
|---|---|
| `separación de capas` | Entradas, cálculo y salidas en zonas o módulos distintos. Ninguna fórmula contiene números. |
| `celda de control` | Verificación automática que se pone en rojo si algo deja de cuadrar. |
| `caso de prueba` | Entrada con salida conocida, calculada de forma independiente. |
| `documentación del modelo` | Supuestos, fuentes, versión, limitaciones y responsable. |
| `riesgo de modelo` | Pérdida por decisiones basadas en un modelo incorrecto o mal usado. |
| `validación independiente` | Revisión por alguien distinto del constructor. |

## 🧠 Modelo mental

Un modelo financiero tiene **tres capas y una regla**:

```text
ENTRADAS    datos y supuestos, con fuente y fecha       ← zona azul
CÁLCULO     fórmulas, sin ningún número escrito         ← zona negra
SALIDAS     resultados, gráficos, tablas                ← zona verde

REGLA: si aparece un número dentro de una fórmula de cálculo, está mal
```

Esa única regla resuelve la mayoría de los problemas de mantenibilidad: cualquier supuesto se cambia
en un solo lugar y el modelo entero se recalcula.

## 📖 Desarrollo

### 1. Estándares de construcción en planilla

Una planilla auditable cumple reglas concretas de estructura. La tabla las recoge, y todas se pueden comprobar en un minuto.

```text
ESTRUCTURA DE HOJAS
  01_Portada       propósito, autor, versión, fecha, limitaciones
  02_Supuestos     todas las entradas, con fuente y fecha de cada dato
  03_Calculo       motor del modelo
  04_EEFF          estados proyectados
  05_Salidas       tablas y gráficos de resultado
  06_Sensibilidad  tablas de datos
  07_Controles     todas las verificaciones automáticas
  08_Registro      historial de cambios
```

```text
CONVENCIONES
  · azul   = entrada manual
  · negro  = fórmula de esta hoja
  · verde  = referencia a otra hoja
  · rojo   = alerta o control fallido
  · una fila = un concepto, consistente en todas las columnas
  · un solo cálculo por celda; si es largo, se divide en filas intermedias
  · sin celdas combinadas en zonas de cálculo
  · nombres de rango para constantes importantes
```

### 2. Controles automáticos

Un modelo debe avisar cuando algo no cuadra en vez de esperar a que alguien lo note. La tabla recoge los controles mínimos.

```text
HOJA DE CONTROLES

  C1  Balance cuadra                =SI(ABS(activo−pasivo−patrimonio)<1;"OK";"ERROR")
  C2  Flujo cuadra con caja         =SI(ABS(var_caja_flujo−var_caja_balance)<1;"OK";"ERROR")
  C3  Suma de amortizaciones        =SI(ABS(suma_amort−capital)<1;"OK";"ERROR")
  C4  Saldo final del crédito = 0   =SI(ABS(saldo_final)<1;"OK";"ERROR")
  C5  Márgenes en rango razonable   =SI(Y(margen>0;margen<0,6);"OK";"REVISAR")
  C6  Sin referencias circulares    =SI(ESERROR(...);"ERROR";"OK")
  C7  Todas las entradas tienen fuente =CONTAR.SI(fuentes;"")=0
  
  ESTADO GENERAL  =SI(CONTAR.SI(C1:C7;"ERROR")=0;"MODELO VÁLIDO";"REVISAR")
```

La hoja de controles debe ser **la primera que se mira** al abrir el modelo, no la última.

### 3. Estructura en Python

En Python la separación de capas es más fácil de imponer y de probar. El esquema siguiente muestra la estructura.

```python
"""Motor de valoración de proyectos.

Separa datos (dataclass), cálculo (funciones puras) y presentación (CLI).
Cada función es verificable de forma aislada.
"""

from dataclasses import dataclass, field

@dataclass(frozen=True)
class Supuestos:
    """Entradas del modelo. Inmutable: garantiza que el cálculo no las altere."""

    inversion: float
    horizonte: int
    wacc: float
    ingresos_iniciales: float
    crecimiento: float
    margen_operativo: float
    tasa_impuesto: float
    capital_trabajo_pct: float
    fuente: str = ""
    fecha_datos: str = ""

    def __post_init__(self) -> None:
        if not 0 < self.wacc < 1:
            raise ValueError("El WACC debe expresarse en decimal entre 0 y 1")
        if self.horizonte < 1:
            raise ValueError("El horizonte debe ser al menos 1 periodo")
        if not self.fuente:
            raise ValueError("Todo supuesto debe declarar su fuente")

def flujos_libres(s: Supuestos) -> list[float]:
    """Flujo de caja libre de cada periodo, sin incluir la inversión inicial."""
    flujos = []
    ingresos_previos = s.ingresos_iniciales / (1 + s.crecimiento)
    for t in range(1, s.horizonte + 1):
        ingresos = s.ingresos_iniciales * (1 + s.crecimiento) ** (t - 1)
        operativo = ingresos * s.margen_operativo
        impuesto = operativo * s.tasa_impuesto
        delta_kt = (ingresos - ingresos_previos) * s.capital_trabajo_pct
        flujos.append(operativo - impuesto - delta_kt)
        ingresos_previos = ingresos
    return flujos

def van(s: Supuestos) -> float:
    """Valor actual neto del proyecto."""
    return sum(
        f / (1 + s.wacc) ** t for t, f in enumerate(flujos_libres(s), start=1)
    ) - s.inversion

def tir(s: Supuestos, tol: float = 1e-7, max_iter: int = 200) -> float:
    """Tasa interna de retorno por bisección.

    Bisección en lugar de Newton-Raphson: converge siempre si hay cambio de
    signo y es explicable a un auditor no técnico.
    """
    bajo, alto = -0.99, 10.0
    for _ in range(max_iter):
        medio = (bajo + alto) / 2
        candidato = Supuestos(**{**s.__dict__, "wacc": medio})
        valor = van(candidato)
        if abs(valor) < tol:
            return medio
        if valor > 0:
            bajo = medio
        else:
            alto = medio
    return (bajo + alto) / 2
```

### 4. Pruebas del modelo

Las pruebas comparan el modelo con casos resueltos independientemente. La tabla recoge los tipos de prueba y qué detecta cada uno.

```python
def test_van_cero_cuando_wacc_igual_tir():
    """Si se descuenta a la TIR, el VAN debe ser cero."""
    s = supuestos_base()
    r = tir(s)
    s_tir = Supuestos(**{**s.__dict__, "wacc": r})
    assert abs(van(s_tir)) < 1.0

def test_caso_verificado_a_mano():
    """Caso calculado independientemente en planilla (ver validacion.md)."""
    s = Supuestos(
        inversion=180_000, horizonte=5, wacc=0.12,
        ingresos_iniciales=120_000, crecimiento=0.04,
        margen_operativo=0.22, tasa_impuesto=0.25,
        capital_trabajo_pct=0.10, fuente="caso de prueba",
    )
    assert round(van(s)) == -70_313

def test_rechaza_wacc_invalido():
    with pytest.raises(ValueError):
        Supuestos(inversion=1, horizonte=1, wacc=12, ingresos_iniciales=1,
                  crecimiento=0, margen_operativo=0.1, tasa_impuesto=0.25,
                  capital_trabajo_pct=0, fuente="x")

def test_exige_fuente():
    with pytest.raises(ValueError):
        Supuestos(inversion=1, horizonte=1, wacc=0.1, ingresos_iniciales=1,
                  crecimiento=0, margen_operativo=0.1, tasa_impuesto=0.25,
                  capital_trabajo_pct=0)

def test_monotonia_del_van():
    """A mayor WACC, menor VAN. Propiedad estructural del modelo."""
    s = supuestos_base()
    vanes = [van(Supuestos(**{**s.__dict__, "wacc": w}))
             for w in (0.08, 0.10, 0.12, 0.14)]
    assert vanes == sorted(vanes, reverse=True)
```

La última prueba —**verificar una propiedad estructural**— es más valiosa que verificar un número:
detecta errores que un caso puntual no revelaría.

### 5. Elegir la herramienta

La herramienta se elige por la frecuencia de uso y por quién tiene que auditarlo. La tabla los relaciona.

| Criterio | Planilla | Código |
|---|---|---|
| Prototipado rápido | **Mejor** | Peor |
| Revisión por no técnicos | **Mejor** | Peor |
| Volumen de datos | Peor | **Mejor** |
| Repetición y automatización | Peor | **Mejor** |
| Control de versiones | Peor | **Mejor** |
| Pruebas automáticas | Muy limitado | **Mejor** |
| Trazabilidad de errores | Peor | **Mejor** |
| Simulación de miles de iteraciones | Peor | **Mejor** |

Regla práctica:

```text
· decisión única, pocos datos, revisada por no técnicos → PLANILLA
· proceso recurrente, muchos datos, con reglas complejas → CÓDIGO
· modelo crítico que alimenta decisiones regulatorias → CÓDIGO con validación independiente
```

Y una advertencia documentada: **los errores en planillas son frecuentes y difíciles de detectar**.
Estudios sobre modelos en uso real han encontrado errores materiales en una proporción alta de las
planillas auditadas. Los controles automáticos de la sección 2 son la mitigación más efectiva.

## 🧮 Ejemplo guiado

**Situación.** Auditas un modelo de valoración que otro analista construyó y que sustenta una decisión
de 8 000 millones.

**Paso 1 — revisión estructural, antes de mirar un solo número.**

```text
□ ¿hay hoja de supuestos separada?            SÍ
□ ¿cada entrada tiene fuente y fecha?         NO — 14 de 31 entradas sin fuente ✗
□ ¿hay números dentro de fórmulas?            SÍ — 23 celdas detectadas ✗
□ ¿hay hoja de controles?                     NO ✗
□ ¿hay documentación de limitaciones?         NO ✗
□ ¿hay registro de versiones?                 NO ✗
□ ¿hay celdas combinadas en el cálculo?       SÍ ✗
```

**Siete hallazgos antes de verificar un cálculo.** Un modelo con estas características no es auditable,
independientemente de si sus números son correctos.

**Paso 2 — busca los números dentro de fórmulas.**

```text
celda H47: =G47*0,25          ← tasa de impuesto escrita en la fórmula
celda K12: =J12*1,04          ← crecimiento escrito en la fórmula
celda M89: =L89/12*30/360     ← convención de días escrita en la fórmula
```

Consecuencia: si cambia la tasa de impuesto, hay que encontrar y modificar **cada aparición**. El
modelo tiene 23. La probabilidad de olvidar alguna es alta.

**Paso 3 — verifica los controles que el modelo no tenía.**

```text
control 1: activo − pasivo − patrimonio en el año 5 → diferencia de 1 247  ✗ ERROR
control 2: suma de amortizaciones vs. capital       → OK
control 3: variación de caja del flujo vs. balance  → diferencia de 1 247  ✗ ERROR
```

**El descuadre de 1 247 aparece en dos controles**, lo que indica una sola causa. Rastreando:

```text
el año 5 incluye una venta de activo fijo registrada en el flujo de inversión
pero no dada de baja del balance
```

**Paso 4 — verifica un caso conocido.**

```text
recalcula el VAN con los mismos supuestos en un modelo independiente:
  modelo auditado:  VAN = 2 847 millones
  recálculo:        VAN = 2 692 millones
  diferencia:            155 millones (5,4 %)
```

Rastreando la diferencia:

```text
el modelo auditado descuenta el flujo del año 1 con exponente 0 en lugar de 1
→ sobrestima el valor de todos los flujos en un periodo completo de descuento
```

**Paso 5 — verifica propiedades estructurales.**

```text
¿el VAN disminuye monótonamente con el WACC?
  WACC 10 % → 3 942
  WACC 12 % → 2 847
  WACC 14 % → 1 918
  WACC 16 % → 2 104   ✗ ANOMALÍA
```

La no monotonía indica un error. Investigando: la celda del WACC no está referenciada en el cálculo
del valor terminal, que usa un valor fijo del 13 %.

**Paso 6 — informe de auditoría.**

```text
HALLAZGOS

Materiales (afectan el resultado):
  H1  error de descuento en el primer periodo → sobrestima el VAN en 155 millones (5,4 %)
  H2  el WACC no se propaga al valor terminal → sensibilidad del modelo inválida
  H3  descuadre de 1 247 por activo no dado de baja

De construcción (afectan la auditabilidad):
  H4  23 números escritos dentro de fórmulas
  H5  14 entradas sin fuente ni fecha
  H6  sin hoja de controles
  H7  sin documentación de limitaciones ni registro de versiones

CONCLUSIÓN
  El modelo NO es apto para sustentar la decisión en su estado actual.
  El VAN corregido es 2 692 millones, un 5,4 % menor al reportado.
  El análisis de sensibilidad presentado al comité es INVÁLIDO por H2.
  
RECOMENDACIÓN
  Reconstruir con separación de capas y controles antes de someter al comité.
  Estimación de esfuerzo: 3 días.
```

**Interpreta:** los hallazgos de construcción (H4 a H7) no cambiaban ningún número y **fueron los que
permitieron encontrar los materiales**: sin ellos, H2 habría pasado inadvertido y el comité habría
decidido con un análisis de sensibilidad que no variaba nada. Los estándares de construcción no son
formalismo: son el mecanismo que hace detectables los errores.

## 🏦 Del cliente al banco

El analista construye un modelo y el banco lo somete a validación independiente. La tabla enfrenta las dos lecturas.

| Concepto | Aplicación bancaria | Parte |
|---|---|---|
| Riesgo de modelo | Marco de gestión exigido por el supervisor | 12, clase 12 |
| Validación independiente | Requisito regulatorio para modelos internos | 12, clase 13 |
| Documentación del modelo | Condición para su uso en decisiones | 12, clase 14 |
| Controles automáticos | Control interno de primera línea | 12, clase 12 |
| Trazabilidad del dato | Principio de agregación de datos de riesgo | 14, clase 8 |

## 🧪 Práctica

El laboratorio pide construir el mismo modelo con los estándares y luego auditar uno ajeno. La auditoría del modelo ajeno es la parte que enseña qué estándares importan.

En `labs/lab-06.md`, sección de modelamiento:

1. Construye un modelo de valoración con separación de capas y hoja de controles.
2. Implementa al menos siete controles automáticos.
3. Escribe cinco pruebas, incluyendo una de propiedad estructural.
4. Audita un modelo ajeno con la lista de verificación y emite un informe de hallazgos.

## ⚠️ Errores frecuentes

Los síntomas de la tabla aparecen cuando alguien intenta reproducir el modelo. Las causas están en supuestos incrustados y en ausencia de controles.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Cambiar un supuesto no cambia el resultado | Número escrito dentro de una fórmula | Toda entrada en su celda, referenciada. |
| El modelo cuadra pero el resultado es incorrecto | Sin casos de prueba independientes | Verifica contra un cálculo externo. |
| Nadie puede mantener el modelo | Sin separación de capas ni documentación | Aplica los estándares de construcción. |
| Un error pasa inadvertido durante meses | Sin controles automáticos | Hoja de controles visible al abrir. |
| La sensibilidad no varía nada | Una variable no se propaga | Verifica propiedades estructurales. |
| Se usa planilla para procesar miles de casos | Herramienta inadecuada | Migra a código con pruebas. |

## ❓ Preguntas de comprobación

1. ¿Cuál es la regla única que resuelve la mayoría de los problemas de mantenibilidad?
2. Nombra cinco controles automáticos que todo modelo financiero debe tener.
3. ¿Por qué una prueba de propiedad estructural es más valiosa que un caso puntual?
4. ¿Cuándo conviene planilla y cuándo código?
5. ¿Por qué los hallazgos de construcción permiten encontrar los materiales?

## 📥 Entregable

Guarda en `portfolio/parte-07/clase-14/`:

- el modelo construido con separación de capas y su hoja de controles;
- los siete controles automáticos implementados y su evidencia de funcionamiento;
- las cinco pruebas con la salida de su ejecución;
- el informe de auditoría de un modelo ajeno con hallazgos clasificados.

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

- Benninga, S. (2014). *Financial Modeling* (4.ª ed.). MIT Press. Estándares de construcción y validación.
- Swan, J. (2015). *Practical Financial Modelling* (3.ª ed.). Elsevier. Convenciones de diseño y controles.
- Federal Reserve / OCC (2011). *Supervisory Guidance on Model Risk Management* (SR 11-7). Marco de gestión del riesgo de modelo, documentación y validación independiente.
- European Spreadsheet Risks Interest Group. *Spreadsheet Risk Management*. Evidencia sobre frecuencia y tipo de errores en planillas. <https://eusprig.org/>
- Basel Committee on Banking Supervision (2013). *BCBS 239: Principles for effective risk data aggregation and risk reporting*. BIS. Trazabilidad y calidad del dato.
- Verificación local: revisa qué exige tu supervisor sobre validación y documentación de modelos internos usados en decisiones de crédito o de capital.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 13 · Escenarios y simulación](13-escenarios-y-simulacion.md) | [Parte 07](../README.md) · [Programa](../../../SYLLABUS.md) | [15 · Proyecto: motor de valoración →](15-proyecto-motor-de-valoracion.md) |
<!-- gen:footer:end -->
