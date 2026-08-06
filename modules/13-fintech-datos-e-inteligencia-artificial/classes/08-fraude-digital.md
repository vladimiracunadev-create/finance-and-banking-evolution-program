---
part: 14
class: 8
title: "Fraude digital"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 08 · Fraude digital

> [← 07 · Crédito digital y datos alternativos](07-credito-digital-y-datos-alternativos.md) · [Índice de la parte](../README.md) · [09 · Criptoactivos y registro distribuido →](09-criptoactivos-y-registro-distribuido.md)

**Parte 14 — Fintech, datos e inteligencia artificial** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir la defensa contra el fraude en canales digitales. Es el único riesgo de esta parte con un
adversario que se adapta en días, y donde cada control añade fricción a clientes legítimos: **la
optimización no es minimizar el fraude, es minimizar el costo total**.

## 📚 Objetivos

Al finalizar podrás:

1. **Clasificar** los tipos de fraude digital y su mecánica.
2. **Diseñar** un sistema de detección por capas.
3. **Calibrar** el equilibrio entre fraude, fricción y falsos positivos.
4. **Calcular** el costo total del fraude, incluido el de la prevención.
5. **Gestionar** un evento de fraude masivo.

<!-- gen:agenda:start -->
## Agenda de 90 minutos

| Minutos | Bloque | Qué ocurre |
|---:|---|---|
| 0–10 | Activación | Pregunta diagnóstica y recuperación de la clase anterior. |
| 10–35 | Conceptos | Desarrollo guiado con la fuente oficial a la vista. |
| 35–55 | Ejemplo guiado | El docente resuelve el caso numérico paso a paso. |
| 55–80 | Práctica | El estudiante replica con datos propios o sintéticos. |
| 80–90 | Cierre | Preguntas de comprobación y registro en el portafolio. |
<!-- gen:agenda:end -->

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| `apropiación de cuenta` | El atacante toma control de la cuenta del cliente. |
| `fraude de identidad` | Se abre una cuenta o un crédito con identidad ajena o falsa. |
| `fraude por inducción` | El cliente ejecuta el pago engañado. |
| `falso positivo` | Operación legítima bloqueada como fraude. |
| `falso negativo` | Fraude no detectado. |
| `autenticación reforzada` | Verificación con dos o más factores independientes. |
| `huella de dispositivo` | Conjunto de señales que identifican el equipo usado. |
| `regla de decisión` | Criterio que aprueba, rechaza o escala una operación. |

## 🧠 Modelo mental

```text
EL COSTO TOTAL DEL FRAUDE TIENE TRES COMPONENTES

  PÉRDIDA POR FRAUDE      lo que se pierde por lo no detectado
  COSTO DE FRICCIÓN       operaciones legítimas bloqueadas
                          + clientes que abandonan
  COSTO DE PREVENCIÓN     sistemas, análisis, personas

  MINIMIZAR EL PRIMERO SOLO
  suele multiplicar el segundo

EL ÓPTIMO ESTÁ DONDE LA SUMA ES MÍNIMA
  y ese punto casi nunca es fraude cero
```

**La organización que persigue fraude cero pierde más dinero que la que acepta un nivel de fraude
calculado.** Un bloqueo excesivo genera abandono de compras, llamadas al centro de contacto y clientes
que se cambian de banco, y todo eso tiene un costo que rara vez se atribuye al área de fraude.

## 📖 Desarrollo

### 1. Tipos y mecánica

| Tipo | Mecánica | Detección |
|---|---|---|
| Apropiación de cuenta | Credenciales robadas o suplantación de canal | Dispositivo, comportamiento, geolocalización |
| Suplantación de identidad al abrir | Documentos ajenos o alterados | Verificación documental y biométrica |
| Identidad sintética | Datos reales combinados con inventados | Contraste múltiple, historial anómalo |
| Fraude por inducción | El cliente paga engañado | Comportamiento, destinatario nuevo, urgencia |
| Fraude de tarjeta no presente | Datos de tarjeta robados | Comportamiento, dispositivo, autenticación |
| Fraude en originación | Ingresos o documentos falsificados | Verificación de fuente |
| Fraude interno | Personal con acceso | Segregación, revisión de accesos |
| Fraude de primera parte | El titular niega su propia operación | Evidencia de autenticación |

```text
EL FRAUDE POR INDUCCIÓN ES EL DE MAYOR CRECIMIENTO
  no hay compromiso técnico que detectar:
  el cliente se autentica correctamente
  y ordena el pago voluntariamente

  → la detección debe basarse en el COMPORTAMIENTO
    de la operación, no en la autenticación
```

### 2. Defensa por capas

```text
CAPA 1 — PREVENCIÓN
  autenticación reforzada, educación del cliente,
  límites por defecto, canales seguros

CAPA 2 — DETECCIÓN EN TIEMPO REAL
  huella de dispositivo, geolocalización,
  comportamiento de sesión, reglas y modelos

CAPA 3 — DECISIÓN
  aprobar, escalar a verificación, retardar, bloquear

CAPA 4 — RESPUESTA
  contacto con el cliente, bloqueo de destino,
  recuperación de fondos

CAPA 5 — APRENDIZAJE
  análisis del caso, actualización de reglas y modelos
```

| Señal | Qué detecta | Falsos positivos |
|---|---|---|
| Dispositivo nuevo | Apropiación de cuenta | Altos (cambio de teléfono) |
| Geolocalización imposible | Sesión comprometida | Bajos |
| Velocidad de escritura anómala | Automatización o coacción | Medios |
| Destinatario nuevo + monto alto | Inducción | Altos |
| Sesión con navegación atípica | Suplantación | Medios |
| Horario inusual para el cliente | Varios | Altos |
| Combinación de tres o más señales | Fraude probable | Bajos |

```text
NINGUNA SEÑAL AISLADA JUSTIFICA UN BLOQUEO
  la potencia está en la COMBINACIÓN
  y en calibrar el umbral de combinación
```

### 3. Calibración

```text
LA MATRIZ DE DECISIÓN

                    operación legítima   fraude
  aprobada          ✓ correcto           ✗ falso negativo → pérdida
  bloqueada         ✗ falso positivo     ✓ correcto
                      → fricción

CADA UMBRAL PRODUCE UNA COMBINACIÓN DISTINTA
  umbral bajo:  más bloqueos, menos fraude, más fricción
  umbral alto:  menos bloqueos, más fraude, menos fricción
```

```text
COSTO DE UN FALSO POSITIVO
  · operación no realizada: margen perdido
  · llamada al centro de contacto
  · tiempo del cliente
  · probabilidad de abandono del producto o del banco
  · en comercio: venta perdida, y el comercio culpa al banco

típicamente, entre 5 y 30 veces menor que un fraude
POR CASO, y muy superior EN AGREGADO
porque los falsos positivos son mucho más numerosos
```

### 4. Costo total y su optimización

```text
COSTO TOTAL = pérdida por fraude
            + falsos positivos × costo unitario
            + costo del sistema y del análisis

SE MINIMIZA BUSCANDO EL UMBRAL ÓPTIMO
  y el óptimo depende del canal, del producto,
  del monto y del segmento
  → un umbral único para todo es siempre subóptimo
```

### 5. Evento masivo

```text
CUANDO UN FRAUDE AFECTA A MUCHOS CLIENTES A LA VEZ

  1. CONTENER      bloquear el vector, no la operación entera
  2. DIMENSIONAR   cuántos clientes, qué exposición
  3. COMUNICAR     al cliente afectado, con instrucciones claras
  4. REPARAR       reembolso rápido; discutir después
  5. NOTIFICAR     al supervisor, según plazo normativo
  6. INVESTIGAR    causa raíz y responsabilidad
  7. CORREGIR      el control que falló

ERROR HABITUAL: retrasar el reembolso mientras se investiga
  el costo reputacional de la demora
  suele superar al monto reembolsado indebidamente
```

## 🧮 Ejemplo guiado

**Situación.** Un banco optimiza su sistema antifraude de pagos digitales.

```text
DATOS ANUALES
  operaciones digitales                    68 M
  operaciones bloqueadas por el sistema   184 000
  de ellas, fraude real                    12 400   (6,7 %)
  de ellas, falsos positivos              171 600   (93,3 %)
  fraude no detectado (falsos negativos)    8 900
  monto medio de una operación fraudulenta    0,42
  monto medio de una operación legítima       0,18

COSTOS
  pérdida por fraude no detectado: 8 900 × 0,42 = 3 738
  costo del sistema: 640 anuales
```

**Paso 1 — cuantifica el costo de los falsos positivos.**

```text
POR CADA FALSO POSITIVO
  margen de la operación perdida: 0,18 × 0,4 % = 0,00072
  llamada al centro de contacto (38 % llama): 0,38 × 0,0021 = 0,0008
  reintento fallido y abandono (12 %): 0,12 × 0,18 × 0,4 % = 0,00009
  probabilidad de fuga del cliente (0,4 %):
    0,004 × 0,096 (margen anual) × 3,89 (VP) = 0,00149
  COSTO UNITARIO: 0,0031

COSTO TOTAL DE FALSOS POSITIVOS
  171 600 × 0,0031 = 532
```

**Paso 2 — calcula el costo total actual.**

```text
pérdida por fraude:        3 738
falsos positivos:            532
costo del sistema:           640
COSTO TOTAL ACTUAL:        4 910
```

**Paso 3 — simula umbrales alternativos.**

```text
                bloqueos   fraude det.  falsos pos.  fraude no det.
umbral actual    184 000     12 400      171 600        8 900
umbral −20 %     312 000     16 800      295 200        4 500
umbral −10 %     238 000     14 900      223 100        6 400
umbral +10 %     142 000     10 200      131 800       11 100
umbral +20 %      98 000      7 900       90 100       13 400
```

**Paso 4 — calcula el costo total de cada umbral.**

```text
              pérdida    falsos pos.   sistema    TOTAL
umbral −20 %   1 890        915          640      3 445
umbral −10 %   2 688        692          640      4 020
actual         3 738        532          640      4 910
umbral +10 %   4 662        409          640      5 711
umbral +20 %   5 628        279          640      6 547

EL ÓPTIMO ESTÁ EN EL UMBRAL MÁS ESTRICTO DE LOS SIMULADOS
```

**Paso 5 — cuestiona el resultado.**

```text
EL UMBRAL −20 % BLOQUEA 312 000 OPERACIONES
  · 295 200 son legítimas
  · el costo unitario de 0,0031 asume una fuga del 0,4 %

¿ES ESTABLE ESE SUPUESTO CON 295 200 BLOQUEOS?
  · un cliente bloqueado una vez tolera
  · bloqueado tres veces, se cambia de banco

  clientes con 3 o más bloqueos al año:
    umbral actual:   8 400
    umbral −20 %:   34 600

  probabilidad de fuga con 3+ bloqueos: 4,2 % (no 0,4 %)
  fuga adicional: 26 200 × 4,2 % = 1 100 clientes
  costo: 1 100 × 0,096 × 3,89 = 411

  COSTO CORREGIDO DEL UMBRAL −20 %: 3 445 + 411 = 3 856
  sigue siendo mejor que el actual (4 910)
```

**Paso 6 — busca la mejora que no exige elegir.**

```text
EL DILEMA SOLO EXISTE CON UN SISTEMA DE UNA SOLA DECISIÓN

  AÑADIR UNA TERCERA OPCIÓN: VERIFICACIÓN EN LÍNEA
    en lugar de aprobar o bloquear,
    solicitar un segundo factor para operaciones dudosas

  efecto:
    · el cliente legítimo verifica en 15 segundos y continúa
    · el fraude no puede verificar
    · el falso positivo deja de ser un bloqueo
      y pasa a ser una fricción de 15 segundos
```

```text
SIMULACIÓN CON VERIFICACIÓN EN LÍNEA
  umbral estricto (−20 %), con tres zonas:
    aprobar directo:        67,4 M
    verificar en línea:     298 000
    bloquear:                14 000

  de las 298 000 verificaciones:
    legítimas que verifican con éxito:  289 100
    fraude que no puede verificar:        8 900

  costo de una verificación (no de un bloqueo):
    fricción de 15 segundos: 0,00012
    abandono en la verificación (6 %): 0,06 × 0,18 × 0,4 % = 0,0000432
    sin llamada al centro de contacto
    COSTO UNITARIO: 0,00016
```

**Paso 7 — calcula el costo del diseño con verificación.**

```text
fraude no detectado: 4 500 × 0,42 =        1 890
falsos positivos (verificación):
  289 100 × 0,00016 =                         46
bloqueos definitivos (14 000, de ellos
  5 600 legítimos): 5 600 × 0,0031 =          17
costo del sistema (verificación incluida):   860
COSTO TOTAL:                               2 813

comparación
  actual:              4 910
  umbral −20 % simple: 3 856
  con verificación:    2 813

AHORRO SOBRE EL ACTUAL: 2 097 anuales
```

**Paso 8 — define la implantación.**

```text
DISEÑO APROBADO
  · tres zonas de decisión, con umbrales calibrados
    por canal, producto y monto
  · verificación en línea con segundo factor
  · bloqueo definitivo solo con evidencia fuerte
  · límite de verificaciones por cliente y período:
    si un cliente legítimo verifica más de 4 veces al mes,
    se revisa su perfil de comportamiento

MEDICIÓN CONTINUA
  · costo total mensual, con sus tres componentes
  · clientes con 3+ fricciones al año
  · tasa de abandono en la verificación
  · tiempo medio de verificación
  · fraude por vector, para recalibrar

RECALIBRACIÓN
  el adversario se adapta: los umbrales pierden
  efectividad en semanas
  → revisión mensual y simulación antes de cada cambio
```

**Interpreta:** el análisis de umbrales llevaba a un dilema real —más fraude o más fricción— y **la
solución no estuvo en elegir mejor sino en cambiar el espacio de decisiones**. Introducir una tercera
opción redujo el costo total en 43 % respecto del sistema actual y en 27 % respecto del mejor umbral
simple. Cuando un problema se presenta como un intercambio entre dos males, la pregunta útil suele ser
si las dos opciones son las únicas.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me bloquearon la tarjeta sin razón» | Falso positivo | 14, clase 8 |
| «Me piden verificar cada compra» | Umbral mal calibrado por segmento | 14, clase 8 |
| «Me estafaron y me autentiqué bien» | Fraude por inducción | 14, clase 2 |
| «El banco me reembolsó rápido» | La demora cuesta más que el reembolso | 12, clase 9 |
| «Abrieron un crédito a mi nombre» | Fraude de identidad | 12, clase 4 |

## 🧪 Práctica

En `labs/lab-04.md`, sección de fraude:

1. Clasifica veinte casos por tipo de fraude y señala su mecánica.
2. Calcula el costo unitario de un falso positivo con todos sus componentes.
3. Simula cinco umbrales y determina el que minimiza el costo total.
4. Diseña un sistema de tres zonas y compara su costo con el de dos.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Se persigue fraude cero | Multiplica la fricción | Minimiza el costo total. |
| No se cuantifica el falso positivo | Costo invisible | Inclúyelo con todos sus componentes. |
| Umbral único para todo | Siempre subóptimo | Calibra por canal y segmento. |
| Solo aprobar o bloquear | Dilema innecesario | Añade verificación en línea. |
| Se retrasa el reembolso | Costo reputacional mayor | Reembolsa rápido, investiga después. |
| Umbrales fijos | El adversario se adapta | Recalibración mensual. |

## ❓ Preguntas de comprobación

1. ¿Cuáles son los tres componentes del costo total del fraude?
2. ¿Por qué perseguir fraude cero cuesta más dinero?
3. ¿Por qué el fraude por inducción no se detecta con autenticación?
4. ¿Qué aporta una tercera zona de decisión que no aportan dos?
5. ¿Por qué la fuga de un cliente con tres bloqueos no es diez veces la de uno con uno?

## 📥 Entregable

Guarda en `portfolio/parte-14/clase-08/`:

- los veinte casos clasificados con su mecánica;
- el costo unitario del falso positivo con sus componentes;
- la simulación de umbrales con el óptimo identificado;
- el diseño de tres zonas con su comparación de costo total.

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

- Financial Stability Board (2020). *Effective Practices for Cyber Incident Response and Recovery*. FSB.
- Committee on Payments and Market Infrastructures (2016). *Fast payments*, sección de gestión de fraude. BIS.
- European Banking Authority (2018). *Guidelines on fraud reporting under PSD2*. EBA.
- NIST (2024). *Cybersecurity Framework 2.0*. NIST.
- Bolton, R. y Hand, D. (2002). "Statistical Fraud Detection: A Review". *Statistical Science*, 17(3).
- Verificación local: revisa las obligaciones de autenticación reforzada, los plazos de reembolso y las reglas de responsabilidad por operaciones no autorizadas en tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 07 · Crédito digital y datos alternativos](07-credito-digital-y-datos-alternativos.md) | [Parte 14](../README.md) · [Programa](../../../SYLLABUS.md) | [09 · Criptoactivos y registro distribuido →](09-criptoactivos-y-registro-distribuido.md) |
<!-- gen:footer:end -->
