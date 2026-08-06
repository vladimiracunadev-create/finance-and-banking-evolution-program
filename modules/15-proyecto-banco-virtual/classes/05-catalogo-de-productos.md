---
part: 16
class: 5
title: "Catálogo de productos"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 05 · Catálogo de productos

> [← 04 · Arquitectura de datos y sistemas](04-arquitectura-de-datos-y-sistemas.md) · [Índice de la parte](../README.md) · [06 · Modelo de precios →](06-modelo-de-precios.md)

**Parte 16 — Proyecto Banco Virtual** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Diseñar los productos del Banco Austral: los mínimos necesarios para servir a sus dos segmentos, con la
estructura que hace posibles los compromisos de margen y de comisiones. Cada producto añadido tiene un
costo fijo permanente, y **el catálogo es donde se decide la complejidad futura del banco**.

## 📚 Objetivos

Al finalizar podrás:

1. **Diseñar** un catálogo mínimo viable para dos segmentos.
2. **Especificar** cada producto con su mercado objetivo positivo y negativo.
3. **Someter** cada producto al gobierno de productos.
4. **Proyectar** el aporte de comisiones al margen bruto.
5. **Verificar** la coherencia del catálogo con los compromisos.

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
| `catálogo mínimo viable` | El conjunto más pequeño que sirve a los segmentos. |
| `producto de entrada` | Aquel por el que el cliente inicia la relación. |
| `producto de profundización` | El que aumenta el valor de la relación. |
| `mercado objetivo` | Para quién sí y para quién no es adecuado el producto. |
| `costo fijo por producto` | Mantenimiento, control, formación y reportes. |
| `estructura de precio` | Componentes que el cliente paga. |
| `escalonamiento` | Límites crecientes según comportamiento verificado. |
| `gobierno de productos` | Proceso de diseño, aprobación y revisión. |

## 🧠 Modelo mental

```text
CADA PRODUCTO TIENE DOS COSTOS

  VISIBLE      su costo operativo por operación
  INVISIBLE    su costo fijo anual, aproximadamente 1,81
               (Parte 15, clase 8)

  un producto que aporta menos de 1,81 al año
  DESTRUYE VALOR, con independencia de su margen unitario

REGLA DE DISEÑO DEL CATÁLOGO
  cada producto debe justificar su costo fijo
  o cumplir una función que otro no cumple
  (entrada, cumplimiento normativo, retención)
```

## 📖 Desarrollo

### 1. Catálogo mínimo del Banco Austral

```text
SEGMENTO PERSONAS SIN HISTORIAL

  P1  CUENTA DE PAGOS
      producto de entrada; sin comisión de mantención
      medios de pago, transferencias, corresponsales
  P2  CRÉDITO ESCALONADO
      producto central; escalones de 0,4 a 6,0
  P3  AHORRO PROGRAMADO
      profundización; construye el colchón del cliente
  P4  SEGURO DE DESGRAVAMEN
      asociado a P2, obligatorio y con prima justificada

SEGMENTO PEQUEÑA EMPRESA

  E1  CUENTA EMPRESA CON RECAUDACIÓN
      producto de entrada; cobro por medios de pago
  E2  CAPITAL DE TRABAJO REVOLVENTE
      producto central; sobre flujo de ventas verificado
  E3  ANTICIPO DE LIQUIDACIONES
      profundización; convierte cobranza en caja
  E4  PAGO DE NÓMINA Y PROVEEDORES
      profundización; genera saldos y vincula

TOTAL: 8 PRODUCTOS
costo fijo anual: 8 × 1,81 = 14,5
```

```text
LO QUE NO ESTÁ, Y POR QUÉ
  tarjeta de crédito         inversión y riesgo (renuncia de la clase 2)
  hipotecario                plazo incompatible con el capital inicial
  depósito a plazo           se añadirá en el año 2, cuando haya
                             necesidad de financiamiento estable
  comercio exterior          renuncia declarada
  inversiones                fuera del alcance de la licencia inicial
```

### 2. Especificación de un producto

```text
P2 — CRÉDITO ESCALONADO

  MERCADO OBJETIVO POSITIVO
    personas de 21 a 68 años
    con ingreso verificable por al menos una fuente:
      pagos de servicios básicos a su nombre (12+ meses)
      flujo de cuenta en el propio banco (6+ meses)
      ventas por medios de pago (6+ meses)
    sin mora vigente > 60 días en el sistema

  MERCADO OBJETIVO NEGATIVO
    personas cuya carga financiera total supere el 45 %
      del ingreso verificado
    personas con menos de 6 meses de ingreso verificable
    personas identificadas como vulnerables sin capacidad
      de evaluación asistida
    → para estas últimas, el producto NO se ofrece
      hasta contar con el canal asistido

  ESTRUCTURA
    escalón 1: monto 0,4, plazo 6 meses
    escalón 2: monto 1,0, plazo 9 meses    (tras cumplir 1)
    escalón 3: monto 2,2, plazo 12 meses
    escalón 4: monto 4,0, plazo 18 meses
    escalón 5: monto 6,0, plazo 24 meses

    el ascenso exige: cumplimiento del escalón anterior
    Y capacidad verificada para el nuevo monto
    (Parte 14, clase 7)

  PRECIO
    tasa: 23,5 % anual  (clase 2, verificada contra tasa mínima)
    comisión de apertura: 0,0  → simplicidad y transparencia
    comisión por mora: costo real de la gestión, sin exceso
    prepago: sin comisión

  CÓMO GANA DINERO EL BANCO
    por el margen de intermediación del crédito
    NO por comisiones ni por errores del cliente
    → responde la pregunta de la Parte 12, clase 8
```

### 3. Gobierno de productos

```text
CADA PRODUCTO PASA POR EL COMITÉ, CON:
  1. mercado objetivo positivo y negativo
  2. necesidad que resuelve
  3. estructura de precio y su correspondencia con el costo
  4. escenarios: qué pasa si al cliente le va mal
  5. cómo se cancela y por qué canal
  6. cómo gana dinero el banco con él
  7. riesgos identificados y su tratamiento
  8. indicadores de seguimiento
  9. veto de riesgos y de cumplimiento

  SIN LOS NUEVE PUNTOS, EL PRODUCTO NO SE APRUEBA
```

```text
ESCENARIO ADVERSO DE P2 — "¿QUÉ PASA SI AL CLIENTE LE VA MAL?"

  pierde su ingreso en el mes 4 de un crédito de 9 meses

  QUÉ OFRECE EL PRODUCTO
    · reprogramación automática por una vez,
      sin costo, extendiendo el plazo
    · si el atraso persiste, contacto asistido antes
      de la gestión de cobranza
    · sin capitalización de intereses de mora
    · sin comisiones acumulativas

  POR QUÉ SE DISEÑA ASÍ
    el segmento es de ingreso variable por definición
    un producto que castiga la variabilidad
    convierte un atraso transitorio en un incumplimiento
```

### 4. Proyección de comisiones

```text
COMPROMISO: comisiones = 27 % del margen bruto
margen financiero proyectado: 46 187
→ comisiones necesarias: 17 083

FUENTES DE COMISIÓN DEL CATÁLOGO

  P1 cuenta de pagos
    sin comisión de mantención
    ingreso: intercambio de medios de pago
      68 000 clientes × 84 operaciones/año × 0,00042 = 2 399

  P3 ahorro programado
    sin comisión

  P4 seguro de desgravamen
    comisión de intermediación: 22 % de la prima
    (no 55 %: la prima se fija por siniestralidad esperada,
     Parte 12, clase 8)
    prima: 0,14 % mensual sobre saldo insoluto
    cartera P2: 118 048 → prima anual 1 983
    comisión: 436

  E1 cuenta empresa con recaudación
    comisión sobre monto recaudado: 0,22 %
    volumen recaudado: 9 200 empresas × 640 = 5 888 000... 
```

```text
VERIFICACIÓN DE ESCALA
  9 200 empresas pequeñas con ventas medias anuales
  de 640 (miles) → ventas agregadas 5 888 000
  sobre un producto interno bruto del país que el proyecto
  no ha definido: la cifra es grande pero no imposible
  para 9 200 empresas de 2 a 30 empleados

  volumen recaudado POR EL BANCO: no todas sus ventas
  penetración de recaudación: 38 % de sus ventas
  volumen: 2 237 440
  comisión 0,22 %: 4 922
```

```text
  E3 anticipo de liquidaciones
    volumen anticipado: 2 237 440 × 32 % × (2/365) = 3 923
      (saldo medio anticipado)
    tasa implícita: 28 % anual
    ingreso: 1 098

  E4 pago de nómina y proveedores
    volumen: 1 840 000
    comisión 0,18 %: 3 312

  OTRAS COMISIONES
    transferencias fuera de cupo, corresponsales,
    reposición de medios de pago: 1 240

  TOTAL COMISIONES: 2 399 + 436 + 4 922 + 1 098 + 3 312 + 1 240
                  = 13 407

  NECESARIAS: 17 083
  BRECHA: 3 676
```

### 5. Cierre de la brecha

```text
OPCIONES
  a) añadir un producto (costo fijo 1,81, ingreso incierto)
  b) aumentar la penetración de E1 de 38 % a 52 %
     ingreso adicional: 1 814
  c) aumentar la penetración de E4
     de 1 840 000 a 2 600 000 de volumen: +1 368
  d) revisar el compromiso del 27 %

  DECISIÓN: (b) y (c)
    penetración de recaudación: 38 % → 50 %
      la propuesta de valor de E1 es la velocidad
      de disponibilidad de los fondos recaudados
      ingreso: 6 476
    volumen de pagos: +42 %
      integrado con la recaudación
      ingreso: 4 703

  COMISIONES REVISADAS: 16 352
  BRECHA RESIDUAL: 731  (4,3 %)

  se declara como brecha y se asigna al plan
  de la clase 14, no se cierra con supuestos optimistas
```

## 🧮 Ejemplo guiado

**Situación.** Someter el producto P4 (seguro de desgravamen) al gobierno de productos.

```text
CONTEXTO
  el caso de la Parte 12, clase 8 mostró un seguro
  de desgravamen con siniestralidad del 6 %
  y comisión del banco del 55 % de la prima

  el Banco Austral debe diseñarlo bien desde el inicio
```

**Paso 1 — determina la prima técnicamente correcta.**

```text
COBERTURA: saldo insoluto en caso de fallecimiento
o invalidez total y permanente del deudor

SINIESTRALIDAD ESPERADA
  población: personas de 21 a 68 años
  tasa de mortalidad media ponderada por edad
  de la cartera esperada: 0,42 % anual
  invalidez total y permanente: 0,18 % anual
  TOTAL: 0,60 % anual sobre el saldo cubierto

PRIMA TÉCNICA
  siniestralidad esperada          0,60 %
  gastos de la aseguradora         0,18 %
  margen de la aseguradora         0,12 %
  comisión de intermediación       0,22 %
  PRIMA ANUAL                      1,12 %  → 0,093 % mensual
```

**Paso 2 — compara con la práctica del mercado.**

```text
PRIMA DE MERCADO OBSERVADA: 0,68 % mensual = 8,16 % anual
PRIMA TÉCNICA CALCULADA:    1,12 % anual

  la prima de mercado es 7,3 veces la técnica
  siniestralidad implícita del mercado: 7,4 %
  → coincide con el caso de la Parte 12, clase 8
```

**Paso 3 — decide la prima del Banco Austral.**

```text
OPCIÓN A — cobrar la prima de mercado
  ingreso de comisión: 118 048 × 8,16 % × 55 % = 5 298
  → cerraría la brecha de comisiones por sí sola

OPCIÓN B — cobrar la prima técnica
  ingreso de comisión: 118 048 × 1,12 % × 22 % = 291

DIFERENCIA: 5 007 anuales

  Y LA PREGUNTA DEL GOBIERNO DE PRODUCTOS
    "¿cómo gana dinero el banco con este producto?"

    opción A: por la diferencia entre la prima cobrada
              y el riesgo cubierto
    opción B: por intermediar un seguro que efectivamente
              transfiere un riesgo

  la opción A es exactamente lo que la Parte 12, clase 8
  identificó como riesgo de conducta
```

**Paso 4 — decide y asume la consecuencia.**

```text
DECISIÓN: opción B, prima técnica

  CONSECUENCIA
    5 007 anuales menos de comisiones
    la brecha de comisiones sube de 731 a 5 738

  ¿ES SOSTENIBLE ESA DECISIÓN?
    el compromiso de comisiones del 27 % no se alcanza
    comisiones proyectadas: 11 345
    sobre margen bruto: 19,7 %

  → EL COMPROMISO DEBE REVISARSE
    no la decisión del producto
```

**Paso 5 — revisa el compromiso y su efecto.**

```text
COMPROMISO REVISADO
  comisiones sobre margen bruto: 19,7 %  (era 27 %)

EFECTO EN EL RESULTADO
  margen financiero:        46 187
  comisiones:               11 345
  margen bruto:             57 532
  gastos (55 %):           −31 643
  costo de riesgo (4,2 %): −17 259
  resultado antes de imp.:   8 630
  resultado neto:            6 300
  rentabilidad sobre patrimonio: 6 300 / 50 000 = 12,60 %

  costo del capital: 17,68 %
  BRECHA: 5,08 puntos  (era 1,31)

  LA DECISIÓN CORRECTA SOBRE EL PRODUCTO
  ABRIÓ UNA BRECHA DE 3,77 PUNTOS
```

**Paso 6 — busca dónde cerrarla sin repetir el error.**

```text
FUENTES LEGÍTIMAS DE CIERRE

  1. EFICIENCIA
     el compromiso es 55 %; un banco digital
     sin sucursales puede alcanzar 48 %
     ahorro: 57 532 × 7 % = 4 027

  2. COSTO DE RIESGO
     el 4,2 % supone el modelo actual
     con datos alternativos y escalonamiento
     bien diseñado (clase 8): 3,6 % alcanzable
     ahorro: 410 940 × 0,6 % = 2 466

  3. MARGEN
     E3 (anticipo de liquidaciones) tiene margen alto
     y baja penetración proyectada
     duplicar su penetración: +1 098

  4. VOLUMEN
     el capital permite 421 245 de cartera
     y el plan proyecta 410 940
     usar la holgura: +1 168 de margen
```

**Paso 7 — recalcula.**

```text
  margen financiero:        47 355  (+1 168)
  comisiones:               12 443  (+1 098)
  margen bruto:             59 798
  gastos (48 %):           −28 703
  costo de riesgo (3,6 %): −14 794
  resultado antes de imp.:  16 301
  resultado neto:           11 900
  rentabilidad sobre patrimonio: 11 900 / 50 000 = 23,80 %

  costo del capital: 17,68 %
  MARGEN SOBRE EL COSTO DEL CAPITAL: 6,12 puntos
```

**Paso 8 — verifica que las nuevas cifras sean sostenibles.**

```text
¿SON REALISTAS LOS NUEVOS COMPROMISOS?

  eficiencia del 48 %
    exige: sin sucursales, trastienda automatizada,
    asistente conversacional, catálogo de 8 productos
    → todo está en el diseño; ES ALCANZABLE
    → y las clases 9 y 14 deberán demostrarlo

  costo de riesgo del 3,6 %
    exige: modelos con datos alternativos,
    escalonamiento disciplinado, cobranza temprana
    → las clases 7, 8 y 12 deberán demostrarlo

  COMPROMISOS FINALES DEL BANCO AUSTRAL
    margen de intermediación:       9,45 %
    comisiones sobre margen bruto: 20,8 %
    índice de eficiencia:          48,0 %
    costo de riesgo:                3,60 %
    rentabilidad sobre patrimonio: 23,8 %
```

**Interpreta:** diseñar el seguro correctamente **abrió una brecha de 3,77 puntos** y obligó a revisar
todo el modelo económico del banco. Ese es el efecto que el proyecto persigue: la decisión ética sobre
un producto no se toma «además» del modelo económico, **lo modifica**, y el trabajo consiste en cerrar
la diferencia con fuentes legítimas en lugar de revertir la decisión.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El seguro me cuesta muy poco» | Prima técnica, no de mercado | 12, clase 8 |
| «Empecé con un crédito pequeño» | Escalonamiento por capacidad | 14, clase 7 |
| «Me reprogramaron sin costo» | Escenario adverso diseñado | 16, clase 5 |
| «El banco tiene pocos productos» | Catálogo mínimo viable | 15, clase 8 |
| «No me cobran mantención» | El banco gana por el margen | 16, clase 5 |

## 🧪 Práctica

En `labs/lab-03.md`:

1. Diseña el catálogo mínimo viable para tus segmentos, con su costo fijo.
2. Especifica un producto con los nueve puntos del gobierno de productos.
3. Calcula la prima técnica de un seguro y compárala con la de mercado.
4. Proyecta las comisiones y verifica el compromiso, revisándolo si procede.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Catálogo amplio en un banco nuevo | Costo fijo por producto | Mínimo viable. |
| Producto sin mercado objetivo negativo | Se venderá a quien no debe | Define para quién no. |
| Prima de seguro por referencia de mercado | Puede no transferir riesgo | Calcula la prima técnica. |
| Escenario adverso del cliente no diseñado | El producto castiga la variabilidad | Diséñalo. |
| Se cierra la brecha con la decisión incorrecta | Ética subordinada a la cifra | Cierra con fuentes legítimas. |
| Compromisos que no se revisan | Incoherencia | Revísalos cuando una decisión los cambia. |

## ❓ Preguntas de comprobación

1. ¿Por qué cada producto debe justificar su costo fijo?
2. ¿Qué revela la pregunta «cómo gana dinero el banco con este producto»?
3. ¿Cómo se calcula la prima técnica de un seguro de desgravamen?
4. ¿Por qué el escenario adverso del cliente es parte del diseño del producto?
5. ¿Qué se hace cuando una decisión correcta abre una brecha en el modelo económico?

## 📥 Entregable

Guarda en `portfolio/parte-16/clase-05/`:

- el catálogo mínimo viable con su costo fijo y sus exclusiones;
- la especificación completa de un producto con los nueve puntos;
- el cálculo de la prima técnica y su comparación;
- la proyección de comisiones y los compromisos finales revisados.

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

- European Banking Authority (2015). *Guidelines on product oversight and governance arrangements*. EBA.
- OECD (2022). *G20/OECD High-Level Principles on Financial Consumer Protection*. OECD.
- Rejda, G. y McNamara, M. (2016). *Principles of Risk Management and Insurance* (13.ª ed.). Pearson. Cálculo de primas.
- World Bank y CGAP (2019). *Alternative Data Transforming SME Finance*. World Bank Group.
- Financial Conduct Authority (2022). *Consumer Duty* (PS22/9). FCA.
- Verificación local: revisa las obligaciones de gobierno de productos, los límites a seguros asociados a crédito y las reglas de información precontractual de tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 04 · Arquitectura de datos y sistemas](04-arquitectura-de-datos-y-sistemas.md) | [Parte 16](../README.md) · [Programa](../../../SYLLABUS.md) | [06 · Modelo de precios →](06-modelo-de-precios.md) |
<!-- gen:footer:end -->
