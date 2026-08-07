---
part: 21
class: 11
title: "FX: del mercado mayorista al registro"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [fx, liquidez, formacion-de-precio]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [BIS, CPMI, FSB]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 11 · FX: del mercado mayorista al registro

> [← 10 · El tramo de dinero](10-el-tramo-de-dinero.md) · [Índice de la parte](../README.md) · [12 · Pago contra pago y riesgo de liquidación →](12-pago-contra-pago-y-riesgo-de-liquidacion.md)

**Parte 21 — Tokenización, FX on-chain y mercados programables** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Distinguir un **cambio de divisa entre dos activos anotados en un registro** de
una operación del mercado FX mayorista. Se parecen en el resultado y se
diferencian en todo lo demás: quién provee el precio, qué profundidad hay y qué
riesgo queda.

## 📚 Objetivos

Al finalizar podrás:

1. **Explicar** cómo se forma el precio en el mercado FX mayorista y en un
   registro.
2. **Comparar** profundidad y diferencial entre ambos, con datos.
3. **Identificar** de dónde viene realmente el precio de un cambio en un
   registro.
4. **Calcular** el coste total de un cambio, incluidos los tramos ocultos.
5. **Determinar** cuándo un cambio en registro mejora y cuándo solo cambia de
   sitio el coste.

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
| `mercado FX mayorista` | Red de creadores de mercado y plataformas |
| `cambio en registro` | Intercambio de dos activos anotados |
| `precio de referencia importado` | El registro toma el precio de fuera |
| `diferencial` | Distancia entre compra y venta |
| `profundidad` | Importe absorbible sin mover el precio |
| `tramo oculto` | Coste que no aparece en el precio mostrado |
| `riesgo de liquidación` | Entregar una divisa y no recibir la otra |
| `ventana de exposición` | Tiempo entre entregar y recibir |

## 🧠 Modelo mental

```text
DE DÓNDE VIENE EL PRECIO

  MERCADO MAYORISTA
    cientos de participantes cotizan
    · el precio se forma por competencia
    · la profundidad es enorme en los pares
      principales
    · el diferencial es de fracciones de
      punto básico

  CAMBIO EN UN REGISTRO
    unos pocos participantes, o un algoritmo
    · el precio casi siempre se IMPORTA
      del mayorista mediante un oráculo
    · la profundidad es la del propio registro
    · el diferencial es varios órdenes
      de magnitud mayor

CONSECUENCIA
  el cambio en registro no forma precio:
  lo consume. Y le añade su propio coste.

DÓNDE SÍ APORTA
  no en el precio, sino en LA LIQUIDACIÓN:
  pago contra pago atómico entre dos activos
  del mismo registro (clase 12).
```

## 📖 Desarrollo

### 1. Formación del precio en el mayorista

```text
POR QUÉ EL DIFERENCIAL ES TAN ESTRECHO

  · muchos creadores de mercado compitiendo
  · volumen enorme que permite cubrir
    la posición al instante
  · información distribuida entre todos
  · infraestructura madura

  → en los pares principales, el diferencial
    se mide en fracciones de punto básico
    para importes grandes

Y ESE ES EL PRECIO CONTRA EL QUE HAY QUE
COMPARAR CUALQUIER ALTERNATIVA.
```

### 2. Formación del precio en un registro

```text
TRES MECANISMOS POSIBLES

  A · ORACULO QUE IMPORTA EL PRECIO
      el registro no forma precio: lo copia
      · hereda los problemas del oráculo
        (Parte 19, clase 9)
      · el retardo es explotable
      · y hay que añadir un margen sobre él

  B · LIBRO DE ÓRDENES PROPIO
      participantes que cotizan en el registro
      · profundidad muy inferior
      · pero forma precio de verdad

  C · CREADOR DE MERCADO AUTOMATIZADO
      una fórmula fija el precio según los
      saldos de dos reservas (clase 13)
      · no necesita contrapartes esperando
      · el precio se desvía del mayorista
        y el arbitraje lo corrige
      · quien aporta las reservas soporta
        la pérdida por divergencia

EN LA PRÁCTICA, CASI TODO ES A o C.
```

### 3. Los tramos ocultos

```text
EL PRECIO MOSTRADO NO ES EL COSTE TOTAL

  · diferencial del cambio en el registro
  · margen sobre el precio importado
  · coste de entrar al registro
    (convertir dinero en activo anotado)
  · coste de salir
  · coste de operación en el registro
  · riesgo de que el emisor de cada activo
    no redima a la par (Parte 20)

LA COMPARACIÓN HONESTA
  suma los seis y los compara con el coste
  total de la alternativa tradicional,
  también con todos sus tramos
  (es exactamente el método de la
   Parte 18, clase 16)
```

### 4. Qué riesgo queda

```text
UN CAMBIO EN REGISTRO NO ELIMINA
EL RIESGO DE MERCADO

  entre que se decide cambiar y se ejecuta,
  el precio se mueve
  → eso es igual en los dos mundos

LO QUE SÍ PUEDE ELIMINAR
  el riesgo de LIQUIDACIÓN:
  entregar una divisa y no recibir la otra

  y eso solo si ambas patas están en el
  mismo registro y se liquidan de forma
  atómica (clase 12)

SI UNA PATA ESTÁ FUERA
  el riesgo de liquidación es el mismo
  que en el mercado tradicional,
  y este ya tiene mecanismos para acotarlo
```

### 5. Cuándo aporta y cuándo no

```text
APORTA
  · cuando las dos patas están en el mismo
    registro y se liquidan atómicamente
  · cuando el par es poco líquido en el
    mayorista y el registro concentra
    la poca liquidez que hay
  · cuando la alternativa tradicional tiene
    tramos de corresponsalía muy caros
    (Parte 18)

NO APORTA
  · en pares principales, donde el mayorista
    es imbatible en precio
  · cuando el precio se importa y se le añade
    margen
  · cuando entrar y salir del registro cuesta
    más que el diferencial que se ahorra

REGLA PRÁCTICA
  si el par tiene diferencial mayorista de
  menos de 2 puntos básicos, el registro
  no va a mejorarlo.
```

## 🧮 Ejemplo guiado

**Situación.** Una tesorería tiene que cambiar 3 000 000 de la moneda A a la
moneda B. Compara el mayorista con un cambio en registro.

```text
DATOS DEL MAYORISTA
  precio medio                         0,8420
  diferencial                          1,2 pb
  comisión del banco                   3,0 pb
  liquidación                          T+2
  riesgo de liquidación         cubierto por PvP

DATOS DEL REGISTRO
  precio importado del mayorista       0,8420
  margen del proveedor                 8,0 pb
  diferencial del registro             6,0 pb
  coste de entrada (A → A anotado)     4,0 pb
  coste de salida (B anotado → B)      4,5 pb
  operación en el registro             2 por operación
  liquidación                          atómica, T+0
```

**Paso 1 — calcula el coste en el mayorista.**

```text
DIFERENCIAL (mitad, por operar en un lado)
  1,2 / 2 = 0,6 pb

COMISIÓN
  3,0 pb

TOTAL = 3,6 pb
  3 000 000 × 3,6 / 10 000 = 1 080
```

**Paso 2 — calcula el coste en el registro.**

```text
MARGEN                8,0 pb
DIFERENCIAL (mitad)   3,0 pb
ENTRADA               4,0 pb
SALIDA                4,5 pb
                     ─────────
SUBTOTAL             19,5 pb
  3 000 000 × 19,5 / 10 000 = 5 850

OPERACIÓN EN EL REGISTRO         2

TOTAL = 5 852
```

**Paso 3 — compara.**

```text
MAYORISTA     1 080
REGISTRO      5 852

EL REGISTRO ES 5,4 VECES MÁS CARO

  y la diferencia son 4 772
  sobre una operación de 3 000 000
  = 15,9 puntos básicos
```

**Paso 4 — valora lo que el registro sí elimina.**

```text
RIESGO DE LIQUIDACIÓN

  en el mayorista ya está cubierto por
  el mecanismo de pago contra pago:
  el ahorro es CERO

SI NO LO ESTUVIERA
  exposición = 3 000 000 durante 2 días
  probabilidad de incumplimiento en 2 días:
  supuesto 0,004 %
  recuperación 45 %
  pérdida esperada
  = 3 000 000 × 0,00004 × 0,55 = 66

  → 66 FRENTE A 4 772 DE SOBRECOSTE

INCLUSO SIN PvP, EL REGISTRO NO COMPENSA
EN ESTE PAR.
```

**Paso 5 — cambia el par.**

```text
PAR POCO LÍQUIDO, MONEDA C CONTRA D

  DATOS DEL MAYORISTA
    diferencial                     45 pb
    comisión                        18 pb
    dos tramos de corresponsalía    22 pb
    TOTAL                        62,5 pb
    (diferencial a la mitad + comisión
     + corresponsalía)

  DATOS DEL REGISTRO
    margen                          12 pb
    diferencial (mitad)              9 pb
    entrada                          4 pb
    salida                         4,5 pb
    TOTAL                         29,5 pb

  AHORRO: 33 pb
  sobre 3 000 000 = 9 900

AQUÍ SÍ APORTA, Y POR UNA RAZÓN
QUE NO ES TECNOLÓGICA: elimina dos tramos
de corresponsalía, que es la conclusión
de la Parte 18, clase 16.
```

**Paso 6 — comprueba la profundidad.**

```text
EL AHORRO DE 33 pb SUPONE QUE SE PUEDE
EJECUTAR 3 000 000 AL PRECIO MOSTRADO

  profundidad del registro en ese par
  supuesto: 5 200 000 al 1 % de impacto

  3 000 000 / 5 200 000 = 0,58 veces
  → de golpe, el impacto sería de 58 pb
    y se comería el ahorro entero

EJECUTANDO EN SEIS TRAMOS DE 500 000
  impacto por tramo
  500 000 / 5 200 000 × 100 pb = 9,6 pb

  con reposición del 70 %, cada tramo deja
  un residuo del 30 %:
  9,6 × [1 + 5 × 0,30] = 24,0 pb

  AHORRO REAL = 33 − 24 = 9 pb
  = 2 700 sobre 3 000 000
```

**Paso 7 — decide.**

```text
CONCLUSIÓN POR PAR

  PAR PRINCIPAL
    mayorista, sin discusión
    el registro es 5,4 veces más caro

  PAR POCO LÍQUIDO
    el registro ahorra 9 pb reales,
    no 33 como sugería el precio mostrado
    → conviene, con ejecución escalonada
      y midiendo la profundidad antes

Y LA REGLA GENERAL
  el registro no compite en precio:
  compite en topología, eliminando tramos.
  Igual que la ruta con stablecoin de la
  Parte 18: el ahorro no venía del registro,
  venía de quitar intermediarios.
```

**Interpreta:** el cambio en registro perdía por 5,4 veces en el par principal y
ganaba en el poco líquido, **y en ambos casos por la misma razón: los tramos de
corresponsalía**. La profundidad redujo el ahorro anunciado de 33 a 9 puntos
básicos, y ese dato no estaba en ninguna comparación comercial.

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Un precio de cambio | Si acepta |
| Tesorería | Coste total con tramos | Por dónde ejecuta |
| Banco | Un servicio FX en competencia | Qué precio ofrece |
| Proveedor del registro | Un margen sobre el importado | Cuánto carga |
| Creador de mercado | Profundidad que aportar | Si participa |
| Infraestructura | Liquidación de dos patas | Si es atómica |
| Oráculo | Un precio que publicar | Con qué retardo |
| Supervisor | Precio importado con margen | Qué transparencia exige |
| Auditor | Coste total frente a mostrado | Qué revela |
| Sociedad | Cambio de divisa más barato | En qué corredores |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El precio es el mismo» | Más margen, diferencial, entrada y salida | 21, clase 11 |
| «Ahorra 33 puntos básicos» | 9 tras medir la profundidad | 21, clase 11 |
| «Es más moderno» | Compite en topología, no en precio | 21, clase 11 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Comparar solo el precio mostrado | Se ignoran cuatro tramos | Sumar los seis costes |
| Profundidad no medida | El ahorro anunciado no se ejecuta | Medir antes de comprometer |
| Precio importado con retardo | Se opera contra un precio viejo | Publicación forzada por desviación |
| Margen sobre el importado | No aparece desglosado | Exigir el desglose |
| Riesgo de emisor de cada pata | Un activo no redime a la par | Aplicar la ficha de la Parte 20 |
| Suponer que el registro forma precio | Casi siempre lo copia | Verificar el mecanismo |

## 🧪 Práctica

En [`labs/lab-07.md`](../labs/lab-07.md):

1. Calcula el coste total en ambos mundos, con los seis tramos.
2. Repite con un par poco líquido y compara.
3. Mide la profundidad y corrige el ahorro anunciado.
4. Identifica el mecanismo de formación de precio de un caso real.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Comparar precios mostrados | Es lo visible | Suma entrada, salida y margen |
| Suponer profundidad | No se publica | Mídela y escalona la ejecución |
| Creer que el registro forma precio | Suena a mercado | Casi siempre lo importa |
| Ignorar el riesgo de cada pata | Se ven como dinero | Cada una tiene emisor |
| Generalizar de un par | El principal y el exótico difieren | Concluye por par |
| Atribuir el ahorro al registro | Viene de quitar tramos | Igual que la Parte 18 |

## ❓ Preguntas de comprobación

1. ¿Cómo se forma el precio en el mayorista y cómo en un registro?
2. ¿Cuáles son los seis tramos del coste total de un cambio en registro?
3. ¿Qué riesgo puede eliminar y cuál no?
4. En el ejemplo, ¿por qué el ahorro pasó de 33 a 9 puntos básicos?
5. ¿En qué compite realmente un cambio en registro?

## 📥 Entregable

Guarda en `portfolio/parte-21/clase-11/`:

- el coste total de ambos mundos para dos pares distintos;
- la medición de profundidad y el ahorro corregido;
- la identificación del mecanismo de formación de precio;
- la conclusión por par, con su justificación.

## 🔗 Referencias cruzadas

- **Viene de:** Parte 18, clases 9 y 16; Parte 20, clase 13.
- **Continúa en:** clases 12 y 13 de esta parte.
- **Se aplica en:** Parte 22, clase 10; Parte 23, clase 11.

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

- Bank for International Settlements (2022). *Triennial Central Bank Survey of foreign exchange and OTC derivatives markets*. BIS. <https://www.bis.org/statistics/rpfx22.htm>
- Global Foreign Exchange Committee (2021). *FX Global Code*. GFXC. <https://www.globalfxc.org/fx_global_code.htm>
- Committee on Payments and Market Infrastructures (2024). *Tokenisation in the context of money and other assets*. BIS. <https://www.bis.org/cpmi/publ/d225.htm>
- Financial Stability Board (2020). *Enhancing Cross-border Payments: Stage 3 roadmap*. FSB. <https://www.fsb.org/2020/10/enhancing-cross-border-payments-stage-3-roadmap/>
- Verificación local: comprueba qué régimen aplica en tu jurisdicción a la intermediación cambiaria y si un cambio entre activos anotados queda dentro de él. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 10 · El tramo de dinero](10-el-tramo-de-dinero.md) | [Parte 21](../README.md) · [Programa](../../../SYLLABUS.md) | [12 · Pago contra pago y riesgo de liquidación →](12-pago-contra-pago-y-riesgo-de-liquidacion.md) |
<!-- gen:footer:end -->
