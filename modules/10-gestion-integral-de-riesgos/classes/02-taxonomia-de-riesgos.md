---
part: 11
class: 2
title: "Taxonomía de riesgos bancarios"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 02 · Taxonomía de riesgos bancarios

> [← 01 · Qué es el riesgo y cómo se gobierna](01-que-es-el-riesgo.md) · [Índice de la parte](../README.md) · [03 · Riesgo de crédito de cartera y concentración →](03-riesgo-de-credito-de-cartera.md)

**Parte 11 — Gestión integral de riesgos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir el mapa completo de los riesgos de un banco y aprender a leerlo. Una taxonomía no es una lista:
es la estructura que determina quién responde por cada riesgo, cómo se mide y con qué se cubre. Un riesgo
sin lugar en la taxonomía es un riesgo sin dueño.

## 📚 Objetivos

Al finalizar podrás:

1. **Clasificar** cualquier evento de pérdida en la categoría de riesgo que le corresponde.
2. **Distinguir** riesgos financieros, no financieros y transversales.
3. **Explicar** cómo un riesgo se transforma en otro y por qué eso complica la medición.
4. **Construir** una matriz de riesgos con probabilidad, impacto y control.
5. **Detectar** los riesgos que ninguna categoría clásica captura.

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
| `riesgo financiero` | Aquel cuyo origen está en variables de mercado o en el incumplimiento de una contraparte. |
| `riesgo no financiero` | Aquel cuyo origen está en procesos, personas, sistemas o conducta. |
| `riesgo transversal` | Se manifiesta a través de otros riesgos: estratégico, reputacional, climático. |
| `riesgo de segundo orden` | El que aparece cuando un riesgo se materializa y desencadena otro. |
| `matriz de riesgos` | Instrumento que ordena riesgos por probabilidad e impacto, antes y después de controles. |
| `riesgo inherente` | El que existe antes de aplicar controles. |
| `riesgo residual` | El que queda después de aplicarlos. Es el que debe compararse con el apetito. |
| `riesgo emergente` | Aún no materializado en el sector, con potencial de serlo. |

## 🧠 Modelo mental

**Los riesgos no ocurren en compartimentos: ocurren en cadena.**

```text
un ciberincidente (RIESGO TECNOLÓGICO)
  → interrumpe pagos (RIESGO OPERACIONAL)
  → los clientes retiran depósitos (RIESGO DE LIQUIDEZ)
  → el banco vende activos con descuento (RIESGO DE MERCADO)
  → publican el caso (RIESGO REPUTACIONAL)
  → el supervisor sanciona (RIESGO DE CUMPLIMIENTO)
  → el negocio pierde viabilidad (RIESGO ESTRATÉGICO)
```

**Medir cada riesgo por separado y sumar subestima siempre el total.** Por eso existen las pruebas de
estrés integradas (clase 13) y por eso el capital económico no es la suma de los capitales por riesgo
(clase 14).

## 📖 Desarrollo

### 1. Riesgos financieros

| Riesgo | Definición operativa | Se mide con | Clase |
|---|---|---|---|
| Crédito | La contraparte no paga | PD, LGD, EAD, pérdida esperada | 3 |
| Liquidez | No hay fondos para cumplir a tiempo | Brechas, cobertura, financiamiento estable | 4 |
| Tasa de interés en el libro de banca | Cambios de tasa afectan margen y valor | Brechas de repreciación, duración | 5 |
| Mercado | Cambios de precio afectan posiciones | Valor en riesgo, sensibilidades, estrés | 6 |
| Moneda | Cambios de tipo de cambio | Posición neta por moneda | 7 |
| País y contraparte | Restricción soberana o falla de contraparte | Exposición cruzada, exposición al incumplimiento | 8 |

### 2. Riesgos no financieros

| Riesgo | Definición operativa | Se mide con | Clase |
|---|---|---|---|
| Operacional | Falla de procesos, personas, sistemas o eventos externos | Pérdidas históricas, escenarios, indicadores | 10 |
| Tecnológico y ciber | Disrupción o compromiso de sistemas y datos | Incidentes, tiempo de recuperación, superficie | 11 |
| Modelo | Decisiones basadas en modelos incorrectos o mal usados | Validación, desempeño, uso | 12 |
| Cumplimiento | Incumplimiento normativo | Hallazgos, sanciones, brechas | Parte 12 |
| Conducta | Daño al cliente o al mercado por la actuación del banco | Reclamos fundados, ventas indebidas | Parte 12 |
| Legal | Contratos, litigios, ejecución de garantías | Contingencias, provisiones | Parte 12 |

### 3. Riesgos transversales

```text
ESTRATÉGICO     decisiones de negocio erróneas o entorno que cambia
                se manifiesta como caída sostenida de rentabilidad
                NO tiene capital regulatorio asignado, y es el que más bancos ha matado

REPUTACIONAL    pérdida de confianza
                se manifiesta como fuga de depósitos y de clientes
                es el amplificador de todos los demás

CLIMÁTICO       físico (eventos) y de transición (cambio de política y tecnología)
                se manifiesta a través de crédito, mercado, operacional y legal
                → clase 15
```

**El riesgo estratégico y el reputacional no se «gestionan» como los demás:** no tienen una métrica
única ni un capital asignado. Se gestionan reduciendo la probabilidad de los riesgos que los desencadenan
y preparando la respuesta.

### 4. Riesgo inherente y residual

```text
RIESGO INHERENTE  ──── CONTROLES ────► RIESGO RESIDUAL ──── comparar con APETITO
  probabilidad × impacto              probabilidad × impacto
  sin controles                       con controles operando

ERROR FRECUENTE: evaluar el residual asumiendo que los controles funcionan
CORRECCIÓN:      el residual se estima con la EFECTIVIDAD PROBADA del control,
                 no con su diseño
```

| Efectividad del control | Evidencia requerida |
|---|---|
| Efectivo | Probado en el período, sin excepciones relevantes |
| Parcialmente efectivo | Probado, con excepciones acotadas y plan de corrección |
| Inefectivo | Falla en la prueba, o no se probó |
| No evaluado | Se trata como inefectivo hasta que se pruebe |

### 5. Matriz de riesgos

```text
IMPACTO
  crítico │  M  │  A  │  A  │  C  │  C  │
  alto    │  B  │  M  │  A  │  A  │  C  │
  medio   │  B  │  B  │  M  │  A  │  A  │
  bajo    │  B  │  B  │  B  │  M  │  A  │
  mínimo  │  B  │  B  │  B  │  B  │  M  │
          └─────┴─────┴─────┴─────┴─────┘
           raro  poco  posi- prob- casi
                 prob. ble   able  cierto
                    PROBABILIDAD

  B bajo   M moderado   A alto   C crítico
```

```text
LO QUE LA MATRIZ HACE BIEN
  ordena la conversación, obliga a comparar, prioriza recursos

LO QUE LA MATRIZ HACE MAL
  un evento de probabilidad "rara" e impacto "crítico" aparece como moderado
  y es exactamente el perfil de los eventos que quiebran bancos

CORRECCIÓN: los riesgos de impacto crítico se tratan aparte,
            por escenario y no por matriz
```

### 6. Riesgos que la taxonomía clásica no captura

```text
· CONCENTRACIÓN         no es un riesgo: es un multiplicador de todos
· CONTAGIO              la falla de otro banco te alcanza
· MODELO DE NEGOCIO     tu negocio deja de ser viable aunque nada falle
· TERCEROS Y CADENA     el riesgo está fuera de tu perímetro
· DATOS                 calidad, linaje y gobierno de la información
· ALGORÍTMICO           decisiones automáticas sesgadas o no explicables
```

Los tres últimos crecen con la digitalización y son el objeto de la Parte 14.

## 🧮 Ejemplo guiado

**Situación.** El comité de riesgos evalúa un evento y debe clasificarlo, medirlo y decidir.

```text
EVENTO
  Un proveedor de verificación de identidad falla durante 11 horas.
  Durante ese lapso, el banco mantiene abierta la contratación digital
  con un procedimiento de contingencia manual simplificado.
  Resultado: 3 400 cuentas abiertas con verificación reducida.
  Dos semanas después se detecta que 62 de ellas usan identidades falsas
  y han recibido 480 millones en transferencias de origen sospechoso.
```

**Paso 1 — clasifica el evento en la taxonomía.**

```text
ORIGEN                        riesgo de TERCEROS (proveedor crítico)
MANIFESTACIÓN INMEDIATA       riesgo OPERACIONAL (falla de proceso de control)
CONSECUENCIA REGULATORIA      riesgo de CUMPLIMIENTO (prevención de lavado)
CONSECUENCIA LEGAL            riesgo LEGAL (responsabilidad por las cuentas)
CONSECUENCIA PÚBLICA          riesgo REPUTACIONAL
AMPLIFICADOR                  decisión de mantener el canal abierto → riesgo ESTRATÉGICO

el evento pertenece a SEIS categorías
si se registra solo como "operacional", se pierde la mitad de la historia
```

**Paso 2 — cuantifica cada componente.**

```text
OPERACIONAL   costo de revisión de las 3 400 cuentas
              3 400 × 28 000 (costo unitario de revisión)  =  95,2 millones
              cierre y bloqueo de 62 cuentas                =   4,1
CUMPLIMIENTO  sanción estimada por deficiencias de control  = 320,0
LEGAL         contingencia por reclamos de terceros         = 140,0
              (provisión estimada, rango 60–260)
REPUTACIONAL  fuga estimada 0,3 % de la base
              1 900 clientes × 96 000 × 3,89 (VP 5 años)    = 709,5
TOTAL ESTIMADO                                                1 268,8 millones
```

**Paso 3 — compara con la decisión que originó todo.**

```text
¿por qué se mantuvo la contratación abierta durante la falla?
  ingreso comercial estimado de 11 horas de contratación: 12,4 millones

DECISIÓN: se arriesgaron 1 268,8 por 12,4
RAZÓN 102 a 1 en contra
```

**Paso 4 — reconstruye por qué se tomó esa decisión.**

```text
· la meta comercial del trimestre estaba en riesgo
· el procedimiento de contingencia existía y estaba "aprobado"
· nadie tenía autoridad explícita para cerrar el canal
· la decisión la tomó el área comercial: PRIMERA LÍNEA
· la segunda línea se enteró al día siguiente

FALLA DE GOBIERNO, no de proceso:
el procedimiento de contingencia no definía QUIÉN decide
mantenerlo o suspenderlo, ni con qué criterio
```

**Paso 5 — sitúa el evento en la matriz, antes y después.**

```text
INHERENTE   probabilidad: posible     impacto: crítico   → CRÍTICO
CONTROL     verificación de identidad automatizada
            efectividad evaluada: "efectiva"
            efectividad PROBADA en escenario de indisponibilidad: NUNCA SE PROBÓ
RESIDUAL declarado antes del evento: MODERADO
RESIDUAL real:                       CRÍTICO
```

**Paso 6 — extrae la lección de medición.**

```text
el residual estaba mal estimado porque:
  · se evaluó el control en operación normal
  · no se evaluó el procedimiento de contingencia como control
  · el control de contingencia nunca se probó

REGLA: un control de contingencia no probado
       se clasifica como INEFECTIVO
```

**Paso 7 — decisiones del comité.**

```text
1. TAXONOMÍA
   registrar el evento en las seis categorías, con la pérdida asignada
   a cada una; la base de pérdidas operacionales recibe 99,3 millones,
   no 1 268,8: el resto se registra donde corresponde

2. GOBIERNO
   todo procedimiento de contingencia debe declarar quién decide
   suspender el servicio, con qué criterio y en qué plazo

3. CONTROLES
   los controles de contingencia se prueban con la misma exigencia
   que los ordinarios; sin prueba, se clasifican como inefectivos

4. PROVEEDORES
   verificación de identidad: activar proveedor alterno (Parte 10, clase 16)

5. INCENTIVOS
   revisar si la meta comercial trimestral indujo la decisión
```

**Interpreta:** el evento se registró inicialmente como «incidente operacional de proveedor». Clasificarlo
bien mostró que **la pérdida operacional era el 8 % del total** y que el origen no era técnico sino de
gobierno. Una taxonomía existe para eso: **si el evento se registra en la categoría equivocada, la
corrección también será la equivocada**.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Abrieron cuentas con mi identidad» | Riesgo de identidad y control de admisión | 4, clase 8 |
| «El banco tuvo un problema, ¿me afecta?» | Cadena de transformación de riesgos | 11, clase 2 |
| «Salió en las noticias y me cambié de banco» | Riesgo reputacional como amplificador | 11, clase 2 |
| «El banco no me devolvió el dinero» | Asignación de responsabilidad y riesgo legal | 12, clase 9 |
| «Todo funcionaba bien hasta que dejó de funcionar» | Control no probado en contingencia | 11, clase 10 |

## 🧪 Práctica

En `labs/lab-01.md`, sección de taxonomía:

1. Clasifica quince eventos de pérdida en la taxonomía completa.
2. Traza la cadena de transformación de tres de ellos.
3. Construye la matriz de riesgos de un banco sintético con inherente y residual.
4. Identifica tres riesgos que la taxonomía clásica no captura en tu contexto.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Un evento se registra en una sola categoría | Taxonomía aplicada superficialmente | Registra todas las categorías afectadas. |
| El residual se estima con el control de diseño | Efectividad no probada | Usa la efectividad probada. |
| Los eventos raros y críticos quedan en «moderado» | Limitación de la matriz | Trátalos por escenario. |
| La concentración se trata como un riesgo más | Es un multiplicador | Mídela dentro de cada riesgo. |
| Se suman los capitales por riesgo | Ignora las correlaciones | Usa medición integrada. |
| El riesgo estratégico no aparece | No tiene capital regulatorio | Inclúyelo con escenarios. |

## ❓ Preguntas de comprobación

1. ¿Por qué medir cada riesgo por separado y sumar subestima el total?
2. ¿Qué diferencia el riesgo inherente del residual y cómo debe estimarse este último?
3. ¿Por qué la matriz de riesgos falla precisamente con los eventos que quiebran bancos?
4. ¿Por qué la concentración no es un riesgo sino un multiplicador?
5. ¿Qué riesgos crecen con la digitalización y no aparecen en la taxonomía clásica?

## 📥 Entregable

Guarda en `portfolio/parte-11/clase-02/`:

- los quince eventos clasificados en la taxonomía completa;
- las tres cadenas de transformación trazadas;
- la matriz de riesgos con inherente, control y residual;
- los riesgos no capturados identificados, con su justificación.

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

- Basel Committee on Banking Supervision (2021). *Revisions to the Principles for the Sound Management of Operational Risk*. BIS. <https://www.bis.org/bcbs/publ/d515.htm>
- Basel Committee on Banking Supervision (2019). *Overview of Pillar 2 supervisory review practices*. BIS.
- COSO (2017). *Enterprise Risk Management — Integrating with Strategy and Performance*. COSO.
- ISO (2018). *ISO 31000: Risk management — Guidelines*. ISO.
- Hull, J. (2018). *Risk Management and Financial Institutions* (5.ª ed.). Wiley. Capítulos 1 y 2: panorama de riesgos.
- Verificación local: revisa la taxonomía de riesgos exigida por tu supervisor y las categorías de la base de eventos de pérdida operacional.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 01 · Qué es el riesgo y cómo se gobierna](01-que-es-el-riesgo.md) | [Parte 11](../README.md) · [Programa](../../../SYLLABUS.md) | [03 · Riesgo de crédito de cartera y concentración →](03-riesgo-de-credito-de-cartera.md) |
<!-- gen:footer:end -->
