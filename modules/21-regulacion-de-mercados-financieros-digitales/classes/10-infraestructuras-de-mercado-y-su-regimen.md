---
part: 22
class: 10
title: "Infraestructuras de mercado y su régimen"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [union-europea, internacional]
regulatory_topics: [infraestructura, liquidacion, resiliencia]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [CPMI, IOSCO, CMF]
requires_legal_review: true
---

## 🎯 Propósito

Aplicar a una infraestructura tokenizada el régimen que se escribió para los
depositarios y los sistemas de liquidación. **Los principios son anteriores a la
tokenización y siguen decidiendo el diseño.**

## 📚 Objetivos

Al finalizar podrás:

1. **Identificar** qué principios de infraestructura alcanzan a una plataforma
   tokenizada.
2. **Evaluar** la finalidad jurídica de la liquidación frente a la técnica.
3. **Analizar** un régimen piloto por lo que exige y por lo que exime.
4. **Diseñar** la estrategia de transición obligatoria.
5. **Determinar** el régimen de un enlace entre infraestructuras.

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| `infraestructura de mercado` | Sistema que negocia, compensa, liquida o registra |
| `finalidad jurídica` | Momento en que la liquidación es irrevocable en derecho |
| `firmeza` | Protección de las órdenes frente a un concurso |
| `régimen piloto` | Autorización temporal con exenciones tasadas |
| `estrategia de transición` | Plan de cese ordenado con traspaso de posiciones |
| `enlace` | Conexión entre dos infraestructuras |
| `acceso justo` | Criterios de participación objetivos y públicos |
| `vigilancia` | Supervisión específica de infraestructuras |

## 🧠 Modelo mental

```text
LOS PRINCIPIOS DE 2012 SIGUEN APLICANDO

  base jurídica sólida
  gobierno
  gestión integral de riesgos
  riesgo de crédito y de liquidez
  finalidad de la liquidación
  liquidación en dinero de banco central
  custodia y riesgo de inversión
  riesgo operativo
  acceso y participación
  eficiencia y transparencia

Y LA TOKENIZACIÓN NO CREA NINGUNO NUEVO:
cambia CÓMO se cumplen tres de ellos
—finalidad, dinero de liquidación y
riesgo operativo— y deja los demás igual.
```

## 📖 Desarrollo

### 1. Finalidad técnica y finalidad jurídica

```text
FINALIDAD TÉCNICA
  el registro considera la operación cerrada

FINALIDAD JURÍDICA
  el ordenamiento la considera irrevocable
  frente a terceros y frente a un concurso

NO COINCIDEN POR DEFECTO
  · la firmeza suele reconocerse a sistemas
    designados por una autoridad
  · un registro no designado puede tener
    finalidad técnica y ninguna firmeza legal

CONSECUENCIA
  una liquidación atómica en un sistema
  no designado puede deshacerse en el
  concurso de un participante
  → la atomicidad no protege de eso
```

### 2. El régimen piloto

```text
QUÉ HACE

  permite operar con exenciones tasadas
  a cambio de límites y de vigilancia
  reforzada

QUÉ EXIME HABITUALMENTE
  · requisitos que suponen intermediarios
    que el diseño elimina
  · formatos de registro incompatibles

QUÉ EXIGE A CAMBIO
  · límites de volumen por instrumento
    y por infraestructura
  · plan de negocio y de riesgos
  · ESTRATEGIA DE TRANSICIÓN obligatoria
  · reporte reforzado

LA ESTRATEGIA DE TRANSICIÓN ES LA PIEZA
MÁS IMPORTANTE Y LA MENOS COMENTADA:
es el equivalente regulatorio del plan de
sustitución del custodio.
```

### 3. La estrategia de transición

```text
QUÉ PASA SI LA INFRAESTRUCTURA CESA

  · quién asume las posiciones
  · en qué plazo
  · cómo se acredita cada titular
  · quién custodia mientras tanto
  · quién paga el traslado
  · cómo se comunica a los participantes

SIN ELLA, EL CESE SE IMPROVISA
  y en ese momento el operador puede estar
  en concurso, sin personal y sin acceso

QUÉ LA HACE ÚTIL
  · aprobada por el supervisor
  · con una entidad receptora identificada
  · con copia diaria del registro en un tercero
  · probada al menos una vez
```

### 4. Acceso justo

```text
UNA INFRAESTRUCTURA CONCENTRA ACTIVIDAD

  → sus criterios de participación deciden
    quién puede competir

QUÉ EXIGE EL PRINCIPIO
  · criterios objetivos, públicos y
    proporcionados al riesgo
  · procedimiento de admisión con plazo
  · motivación de la denegación
  · vía de revisión

EN UNA PLATAFORMA TOKENIZADA
  el criterio suele ser técnico —soportar
  el protocolo— y eso puede excluir de facto
  → un requisito técnico desproporcionado
    es una barrera de entrada, aunque
    no lo parezca
```

### 5. Enlaces

```text
CONECTAR DOS INFRAESTRUCTURAS
CREA RIESGO EN AMBAS

  QUÉ EXIGE EL RÉGIMEN
  · evaluación del riesgo del enlace
  · base jurídica del enlace en ambas
    jurisdicciones
  · regla común de finalidad
  · gestión del riesgo de crédito y liquidez
    que introduce

Y UN PUENTE ES UN ENLACE
  aunque se llame de otra forma
  → con la diferencia de que acumula valor,
    y eso hay que evaluarlo (Parte 21, clase 15)
```

## 🧮 Ejemplo guiado

**Situación.** Una plataforma de negociación y liquidación tokenizada solicita
autorización bajo un régimen piloto.

```text
DATOS
  instrumentos admitidos             bonos corporativos
  volumen previsto al año            180 000 000
  límite del régimen por instrumento  100 000 000
  límite total de la infraestructura  400 000 000
  participantes previstos                     14
  tramo de dinero              depósito tokenizado
  entidad receptora en el cese         no designada
```

**Paso 1 — comprueba los límites.**

```text
VOLUMEN PREVISTO        180 000 000
LÍMITE POR INSTRUMENTO  100 000 000

  → hay que repartir entre al menos dos
    emisiones distintas, o reducir

LÍMITE TOTAL            400 000 000
  → margen del 55 % sobre lo previsto

HALLAZGO
  el crecimiento previsto a tres años
  supuesto 520 000 000
  → superaría el límite total en el año 3
  → hay que planificar la salida del piloto
    hacia una autorización ordinaria
```

**Paso 2 — resuelve la finalidad.**

```text
¿ESTÁ EL SISTEMA DESIGNADO A EFECTOS
DE FIRMEZA?

  no, y el régimen piloto no lo designa
  automáticamente

  CONSECUENCIA
  una operación liquidada atómicamente
  puede impugnarse en el concurso de un
  participante

  OPCIONES
  a  solicitar la designación
  b  operar solo con prefinanciación
     total, de modo que no haya crédito
     que impugnar
  c  advertirlo a los participantes

  RECOMENDACIÓN: a y c
  la b elimina el riesgo y encarece
  la operación
```

**Paso 3 — evalúa el tramo de dinero.**

```text
DEPÓSITO TOKENIZADO DE UN BANCO SUPERVISADO

  el principio pide liquidar en dinero de
  banco central cuando sea practicable

  ¿ES PRACTICABLE?
  · no hay CBDC mayorista disponible
  · el depósito tokenizado es la mejor
    alternativa

  QUÉ HAY QUE ACREDITAR
  · que el banco emisor tiene bajo riesgo
    de crédito y de liquidez
  · límites de exposición al emisor
  · procedimiento si el banco falla

  HALLAZGO
  no hay límite de exposición al emisor
  → requerimiento
```

**Paso 4 — diseña la estrategia de transición.**

```text
ELEMENTOS EXIGIDOS

  1 ENTIDAD RECEPTORA
      no designada → BLOQUEANTE
      opciones: un depositario existente
      o un acuerdo con otra infraestructura

  2 PLAZO MÁXIMO
      propuesto: 20 días hábiles

  3 ACREDITACIÓN DE TITULARES
      copia diaria del registro en un tercero,
      con verificación de integridad

  4 CUSTODIA INTERINA
      el tercero conserva el registro;
      las posiciones quedan congeladas

  5 COSTE
      fondo de transición dotado por la
      infraestructura, supuesto 400 000

  6 COMUNICACIÓN
      a participantes en 24 horas

  Y UNA PRUEBA ANUAL DOCUMENTADA
```

**Paso 5 — evalúa el acceso.**

```text
CRITERIO DE PARTICIPACIÓN PROPUESTO
  «disponer de un nodo con la especificación
   técnica de la plataforma»

  COSTE DE CUMPLIRLO
  supuesto 180 000 de implantación
  más 60 000 al año

  EFECTO
  de los 40 participantes potenciales del
  mercado, supuesto 14 pueden asumirlo

  ¿ES PROPORCIONADO AL RIESGO?
  · un nodo propio no reduce el riesgo
    frente a un acceso por interfaz
  · y excluye al 65 % del mercado

  HALLAZGO
  ofrecer acceso indirecto por interfaz,
  con los mismos controles
```

**Paso 6 — resume los requerimientos.**

```text
BLOQUEANTES
  · entidad receptora de la transición
  · límite de exposición al emisor del dinero

RELEVANTES
  · solicitud de designación a efectos
    de firmeza, o advertencia expresa
  · acceso indirecto por interfaz
  · plan de salida del piloto antes del año 3

Y UNA CONSTATACIÓN
  de los diez principios, siete se cumplen
  con las prácticas ordinarias; los tres
  que exigen trabajo son finalidad, dinero
  de liquidación y transición.

  Son exactamente los tres que la clase
  anunció al empezar.
```

**Interpreta:** la plataforma había resuelto la tecnología y no la firmeza. **Una
liquidación atómica en un sistema no designado puede deshacerse en el concurso de
un participante**, y la atomicidad —que elimina el riesgo de principal— no
protege de eso.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Una plataforma autorizada | Si opera |
| Participante | Un nodo de 180 000 | Si entra |
| Excluido | Un requisito técnico | Si reclama |
| Banco | Exposición al emisor del dinero | Qué límite pide |
| Emisor | Un mercado para su instrumento | Si emite allí |
| Infraestructura | Límites del piloto | Cuándo sale de él |
| Supervisor | Firmeza no resuelta | Qué requiere |
| Auditor | Estrategia de transición sin probar | Qué observa |
| Administrador concursal | Operaciones impugnables | Qué deshace |
| Sociedad | Un mercado nuevo | Qué garantías exige |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Es atómico, es definitivo» | Sin firmeza legal puede deshacerse | 22, clase 10 |
| «Está en un régimen piloto» | Con límites y salida planificada | 22, clase 10 |
| «Cualquiera puede participar» | Con un nodo de 180 000 | 22, clase 10 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Finalidad técnica sin firmeza | Operaciones impugnadas en concurso | Designación o advertencia expresa |
| Sin entidad receptora | El cese se improvisa | Designarla antes de autorizar |
| Sin límite al emisor del dinero | Concentración de riesgo | Límite y procedimiento de fallo |
| Requisito técnico excluyente | Barrera de entrada de facto | Acceso indirecto con mismos controles |
| Límites del piloto ignorados | Se superan en el año 3 | Plan de salida planificado |
| Transición sin probar | No funciona cuando hace falta | Prueba anual documentada |

## 🧪 Práctica

En [`labs/lab-03.md`](../labs/lab-03.md):

1. Comprueba los límites del régimen frente al crecimiento previsto.
2. Determina si hay firmeza legal y qué opciones existen.
3. Diseña la estrategia de transición con sus seis elementos.
4. Evalúa el criterio de acceso por su proporcionalidad al riesgo.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Confundir finalidad técnica y jurídica | La operación «está cerrada» | La firmeza la da la designación |
| Ver el piloto como exención | Suena a permiso amplio | Exime lo tasado y exige más |
| Dejar la transición para el final | Nadie prevé el cese | Es la pieza que el régimen más mira |
| Requisitos técnicos como filtro | Parecen neutrales | Pueden ser barrera de entrada |
| Ignorar el emisor del dinero | Parece neutro | Es exposición concentrada |
| Planificar sin límites | Se mira el volumen del año 1 | Los límites llegan en el año 3 |

## ❓ Preguntas de comprobación

1. ¿Cuáles de los diez principios cambian con la tokenización y cuáles no?
2. ¿Qué diferencia hay entre finalidad técnica y jurídica?
3. ¿Qué exige un régimen piloto a cambio de sus exenciones?
4. ¿Qué seis elementos tiene una estrategia de transición?
5. ¿Cuándo un requisito técnico se convierte en barrera de entrada?

## 📥 Entregable

Guarda en `portfolio/parte-22/clase-10/`:

- la comprobación de límites frente al crecimiento previsto;
- el análisis de firmeza con sus opciones;
- la estrategia de transición con sus seis elementos;
- la evaluación del criterio de acceso.

## 🔗 Referencias cruzadas

- **Viene de:** clases 4 y 9; Parte 21, clases 2, 8 y 15.
- **Continúa en:** clases 14 y 15 de esta parte.
- **Se aplica en:** clase 18 de esta parte; Parte 23, clases 7 y 16.

## 📗 Fuentes y verificación

- CPMI e IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- Diario Oficial de la Unión Europea (2022). *Reglamento (UE) 2022/858 sobre el régimen piloto de infraestructuras del mercado basadas en DLT*. EUR-Lex. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32022R0858>
- Committee on Payments and Market Infrastructures (2024). *Tokenisation in the context of money and other assets*. BIS. <https://www.bis.org/cpmi/publ/d225.htm>
- Comisión para el Mercado Financiero. *Normativa sobre infraestructuras del mercado de valores*. CMF. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba qué sistemas están designados a efectos de firmeza en tu jurisdicción, cómo se solicita la designación y si existe un régimen piloto aplicable. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**
