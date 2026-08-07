---
part: 9
class: 16
title: "Proyecto: motor de evaluación crediticia"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 16 · Proyecto: motor de evaluación crediticia

> [← 15 · Cobranza y reestructuración](15-cobranza-y-reestructuracion.md) · [Índice de la parte](../README.md) · [Proyecto de la parte →](../project/README.md)

**Parte 09 — Análisis y gestión de crédito** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir una herramienta que evalúe solicitudes de crédito de principio a fin, con la política
codificada, la decisión trazable y el precio calculado según el riesgo. Es el proyecto que integra las
quince clases de la parte y el insumo directo del banco virtual de la Parte 16.

## 📚 Objetivos

Al finalizar podrás:

1. **Codificar** una política de crédito en reglas verificables.
2. **Implementar** el cálculo de capacidad, endeudamiento, scoring y pricing.
3. **Producir** una decisión trazable con su fundamento.
4. **Validar** el motor contra casos con resultado conocido.
5. **Defender** las decisiones de diseño y sus límites.

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
| `motor de decisión` | Sistema que aplica la política a una solicitud y produce una decisión fundada. |
| `política codificada` | Reglas expresadas de forma ejecutable y auditable. |
| `trazabilidad` | Capacidad de reconstruir por qué se decidió lo que se decidió. |
| `excepción` | Desviación de la política, que el motor identifica y escala. |
| `explicabilidad` | Capacidad de indicar los factores principales de la decisión. |
| `caso de validación` | Solicitud con resultado conocido, evaluado independientemente. |

## 🧠 Modelo mental

Un motor de decisión debe producir **tres salidas, no una**:

```text
1. la DECISIÓN         aprobar, rechazar o condicionar
2. el FUNDAMENTO       qué reglas se aplicaron y con qué resultado
3. las CONDICIONES     qué mitigantes, qué monto, qué plazo, qué precio
```

Un motor que solo entrega la decisión es una caja negra: **no se puede auditar, no se puede explicar
al cliente y no se puede mejorar**.

## 📖 Desarrollo

### 1. Requisitos funcionales

| # | Requisito | Entrada | Salida |
|---:|---|---|---|
| 1 | Validar completitud del expediente | Documentos declarados | Faltantes identificados |
| 2 | Calcular renta admisible | Componentes de renta | Renta ponderada por tipo |
| 3 | Consolidar endeudamiento | Deudas, cupos, avales | Endeudamiento total |
| 4 | Calcular capacidad de pago | Renta, gastos, cuotas | Carga financiera y excedente |
| 5 | Aplicar pruebas de estrés | Escenarios definidos | Capacidad en cada escenario |
| 6 | Calcular score y PD | Variables del solicitante | Puntaje y probabilidad |
| 7 | Aplicar reglas de política | Todo lo anterior | Cumple / no cumple por regla |
| 8 | Determinar monto máximo | Capacidad y límites | Monto y plazo máximos |
| 9 | Calcular pricing | PD, LGD, costos | Tasa mínima y tasa propuesta |
| 10 | Identificar mitigantes aplicables | Perfil del solicitante | Lista de mitigantes y su efecto |
| 11 | Producir la decisión | Todo lo anterior | Aprobar / rechazar / condicionar |
| 12 | Generar el fundamento | Reglas evaluadas | Documento trazable |
| 13 | Identificar excepciones | Reglas incumplidas | Nivel de aprobación requerido |
| 14 | Registrar la evaluación | Todo | Registro auditable con marca de tiempo |

### 2. Arquitectura

```text
apps/credit_engine/
  models.py       Solicitante, Operacion, Decision (dataclasses)
  income.py       cálculo de renta admisible
  debt.py         consolidación de endeudamiento
  capacity.py     capacidad de pago y pruebas de estrés
  scoring.py      cálculo de score y PD
  policy.py       reglas de política, codificadas y versionadas
  pricing.py      cálculo de tasa mínima y propuesta
  mitigants.py    catálogo de mitigantes y su efecto
  engine.py       orquestación y decisión
  audit.py        registro trazable
  cli.py          interfaz
tests/
  test_income.py, test_debt.py, test_capacity.py,
  test_policy.py, test_pricing.py, test_engine.py
portfolio/parte-09/clase-16/
  politica.md     política de crédito documentada
  validacion.md   casos con resultado conocido
  informe.md      ejemplo de evaluación completa
  defensa.md      decisiones de diseño y límites
```

### 3. Implementación de referencia

```python
from dataclasses import dataclass, field
from enum import Enum

class Resultado(Enum):
    APROBAR = "aprobar"
    CONDICIONAR = "condicionar"
    RECHAZAR = "rechazar"

@dataclass(frozen=True)
class EvaluacionRegla:
    """Resultado de una regla de política, con su fundamento."""

    codigo: str
    descripcion: str
    valor_observado: float
    limite: float
    cumple: bool
    es_excepcionable: bool
    nivel_aprobacion: str = "automatico"

@dataclass
class Decision:
    """Salida completa del motor: decisión, fundamento y condiciones."""

    resultado: Resultado
    monto_aprobado: float
    plazo_meses: int
    tasa_anual: float
    reglas: list[EvaluacionRegla] = field(default_factory=list)
    mitigantes: list[str] = field(default_factory=list)
    excepciones: list[EvaluacionRegla] = field(default_factory=list)
    factores_principales: list[str] = field(default_factory=list)

    @property
    def nivel_aprobacion(self) -> str:
        """El nivel más alto exigido por cualquier excepción."""
        niveles = ["automatico", "supervisor", "comite", "directorio"]
        maximo = "automatico"
        for regla in self.excepciones:
            if niveles.index(regla.nivel_aprobacion) > niveles.index(maximo):
                maximo = regla.nivel_aprobacion
        return maximo

def evaluar_carga_financiera(
    cuotas_totales: float, renta_admisible: float, limite: float
) -> EvaluacionRegla:
    """Regla P-001: la carga financiera no debe superar el límite del segmento."""
    carga = cuotas_totales / renta_admisible if renta_admisible else 1.0
    return EvaluacionRegla(
        codigo="P-001",
        descripcion="Carga financiera máxima del segmento",
        valor_observado=carga,
        limite=limite,
        cumple=carga <= limite,
        es_excepcionable=carga <= limite * 1.10,
        nivel_aprobacion="comite" if carga > limite else "automatico",
    )
```

### 4. Codificar la política

```text
cada regla debe tener:
  · código único y versión
  · descripción en lenguaje natural
  · valor observado y límite
  · si admite excepción y hasta qué margen
  · nivel de aprobación requerido si se excepciona
  · fecha de vigencia
```

```text
CATÁLOGO MÍNIMO DE REGLAS

P-001  carga financiera ≤ límite del segmento
P-002  excedente disponible ≥ mínimo absoluto
P-003  score ≥ punto de corte del producto
P-004  sin mora ≥ 90 días vigente
P-005  sin castigos en los últimos 24 meses
P-006  endeudamiento relativo ≤ límite
P-007  monto ≤ múltiplo máximo de la renta
P-008  plazo ≤ máximo del segmento
P-009  edad al vencimiento ≤ límite
P-010  antigüedad laboral ≥ mínimo
P-011  renta admisible ≥ mínimo del producto
P-012  capacidad cumple en escenario de estrés
P-013  LTV ≤ límite (productos con garantía)
P-014  expediente completo según tipo de deudor
P-015  identificación y beneficiario final verificados
```

### 5. Validación

```text
CASO 1 — aprobación limpia
  entrada: solicitante con todas las reglas cumplidas
  esperado: APROBAR, nivel automático, sin excepciones
  
CASO 2 — rechazo por capacidad
  entrada: carga financiera 52 % con límite de 40 %
  esperado: RECHAZAR, regla P-001 incumplida, no excepcionable
  
CASO 3 — condicionamiento por monto
  entrada: monto solicitado excede el múltiplo máximo
  esperado: CONDICIONAR con monto reducido al máximo permitido
  
CASO 4 — excepción escalable
  entrada: carga financiera 43 % con límite de 40 % (dentro del 10 % de margen)
  esperado: CONDICIONAR, excepción P-001, nivel comité
  
CASO 5 — rechazo por identificación
  entrada: beneficiario final no identificado
  esperado: RECHAZAR, regla P-015, sin posibilidad de excepción
  
CASO 6 — efecto de mitigantes
  entrada: solicitante con score 540, con y sin débito automático
  esperado: tasa 0,84 puntos menor con el mitigante
  
CASO 7 — trazabilidad
  entrada: cualquier solicitud
  esperado: el registro permite reconstruir cada valor y cada regla evaluada
  
CASO 8 — explicabilidad
  entrada: solicitud rechazada
  esperado: los tres factores principales del rechazo, en lenguaje comprensible
```

## 🧮 Ejemplo guiado

**Situación de defensa.** Presentas el motor y el comité formula cuatro preguntas.

**Pregunta 1: "El motor rechaza automáticamente. ¿Qué pasa si se equivoca?"**

```text
"El motor NO rechaza automáticamente en todos los casos. Distingue tres situaciones:

  · reglas NO excepcionables (identificación, mora vigente, castigos):
    rechazo automático, porque son condiciones normativas o de política
    que no admiten discrecionalidad

  · reglas excepcionables dentro de un margen (carga financiera hasta 10 %
    sobre el límite): no rechaza, CONDICIONA y escala al nivel correspondiente

  · reglas de monto o plazo: no rechaza, ajusta la operación al máximo permitido
    y la aprueba en esa forma

 Además, toda decisión adversa incluye los tres factores principales en lenguaje
 comprensible, y el solicitante puede pedir revisión con intervención humana.
 Esa revisión queda registrada y alimenta el análisis de calibración."
```

**Pregunta 2: "¿Cómo sabemos que la política codificada corresponde a la política aprobada?"**

```text
"Por tres mecanismos:

 1. cada regla tiene un código y una versión que corresponde a un artículo
    específico del manual de política aprobado por el comité

 2. existe una prueba automática por cada regla, con al menos un caso que
    la cumple y uno que la incumple, derivados del texto de la política

 3. el cambio de cualquier parámetro exige modificar el archivo de política,
    que está bajo control de versiones. El registro muestra quién cambió qué,
    cuándo y con qué aprobación

 Lo que el motor NO puede garantizar es que la política sea correcta:
 solo que se aplique consistentemente."
```

**Pregunta 3: "El pricing usa una PD del modelo. ¿Qué pasa si el modelo está mal calibrado?"**

```text
"Es el riesgo principal del motor y lo mitigo de tres formas:

 1. el motor registra la PD estimada de cada operación. El área de riesgo
    contrasta trimestralmente la PD estimada con la observada por cosecha,
    y el desvío se reporta al comité

 2. el pricing incluye un margen de seguridad sobre la tasa mínima calculada:
    si la PD estuviera subestimada en un 30 %, el margen sigue siendo positivo
    en todos los segmentos salvo el E

 3. existe un umbral de alerta: si el PSI supera 0,15 o si la PD observada
    excede en 25 % a la estimada en dos trimestres consecutivos, el motor
    marca las operaciones de ese segmento para revisión manual

 Y una limitación que declaro: el modelo se calibró con datos de un periodo
 sin recesión severa. Su comportamiento en un escenario de estrés no está
 validado empíricamente."
```

**Pregunta 4: "¿Qué NO hace este motor?"**

```text
"Cinco cosas, y las declaro en la documentación:

 1. NO verifica la autenticidad de los documentos: asume que la verificación
    documental ya ocurrió en el proceso previo

 2. NO evalúa el riesgo cualitativo de empresas: para crédito comercial
    produce el análisis cuantitativo y marca la operación para evaluación
    cualitativa por un analista

 3. NO decide sobre reestructuraciones: es un motor de originación

 4. NO reemplaza la evaluación de idoneidad para productos de inversión

 5. NO detecta fraude: identifica inconsistencias entre datos declarados,
    pero la detección de fraude requiere herramientas específicas

 Declararlo importa porque un motor que se usa fuera de su alcance
 produce decisiones sin fundamento, y el usuario no lo sabe."
```

**Lo que estas cuatro respuestas enseñan:** un motor de decisión se defiende **explicando qué decide
automáticamente y qué escala, cómo se verifica la correspondencia con la política aprobada, cómo se
monitorea el modelo que lo alimenta y qué queda fuera de su alcance**.

## 🏦 Del cliente al banco

| Componente del motor | Equivalente en producción | Parte |
|---|---|---|
| Política codificada | Motor de decisión del core bancario | 14, clase 12 |
| Trazabilidad | Requisito de auditoría y de supervisión | 12, clase 14 |
| Explicabilidad | Derecho del cliente ante decisión automatizada | 14, clase 13 |
| Escalamiento de excepciones | Facultades de aprobación delegadas | 9, clase 1 |
| Monitoreo del modelo | Gobierno de modelos | 12, clase 13 |

## 🧪 Práctica

Este proyecto es la práctica. Trabaja en `project/README.md` de esta parte.

1. Documenta la política de crédito con al menos quince reglas codificables.
2. Implementa los catorce requisitos con sus pruebas en verde.
3. Valida contra los ocho casos, con resultados calculados de forma independiente.
4. Prepara la defensa de las cuatro preguntas con tus propios datos y límites.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El motor solo entrega la decisión | Sin fundamento ni condiciones | Produce las tres salidas. |
| No se distingue rechazo de condicionamiento | Lógica binaria | Ajusta monto y plazo antes de rechazar. |
| Las reglas están dispersas en el código | Política no centralizada | Concentra las reglas en un módulo versionado. |
| No hay pruebas por regla | Correspondencia con la política no verificable | Una prueba por regla, con caso positivo y negativo. |
| No se declara lo que el motor no hace | Uso fuera de alcance | Documenta las limitaciones. |
| La PD no se monitorea | Deriva no detectada | Registra la PD y contrasta con lo observado. |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las tres salidas que debe producir un motor de decisión?
2. ¿Qué distingue una regla excepcionable de una que no lo es?
3. ¿Cómo se verifica que la política codificada corresponde a la aprobada?
4. ¿Cómo se mitiga el riesgo de que el modelo de PD esté mal calibrado?
5. ¿Por qué declarar lo que el motor no hace es parte del diseño?

## 📥 Entregable

Guarda en `portfolio/parte-09/clase-16/` y en `apps/credit_engine/`:

- `politica.md` con al menos quince reglas codificables y versionadas;
- el código con los catorce requisitos y sus pruebas en verde;
- `validacion.md` con los ocho casos verificados independientemente;
- `informe.md` con una evaluación completa de ejemplo y `defensa.md` con las cuatro respuestas.

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

- Anderson, R. (2007). *The Credit Scoring Toolkit*. Oxford University Press. Diseño de motores de decisión crediticia.
- Federal Reserve / OCC (2011). *Supervisory Guidance on Model Risk Management* (SR 11-7). Gobierno, validación y documentación.
- European Banking Authority (2020). *Guidelines on loan origination and monitoring*. EBA. Requisitos del proceso de originación.
- Basel Committee on Banking Supervision (2000). *Principles for the Management of Credit Risk*. BIS. Estándares del proceso de crédito.
- European Union (2016). *GDPR*, artículo 22: decisiones automatizadas y derecho a intervención humana. <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
- Verificación local: revisa qué exige tu supervisor sobre motores de decisión automatizada, trazabilidad de la originación y facultades de aprobación.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 15 · Cobranza y reestructuración](15-cobranza-y-reestructuracion.md) | [Parte 09](../README.md) · [Programa](../../../SYLLABUS.md) | [Proyecto de la parte →](../project/README.md) |
<!-- gen:footer:end -->
