# Arquitectura de un mercado tokenizado

**Las nueve piezas de un mercado que emite, negocia y liquida instrumentos
tokenizados, y las cinco decisiones que ninguna tecnología resuelve.** Este
documento es el plano que la Parte 21 construye por clases y que la Parte 23
ensambla en un proyecto.

Conviene empezar por lo que este plano **no** dice. No dice que tokenizar sea
mejor: dice qué hace falta para que funcione si se decide hacerlo. La pregunta
previa —si el problema es de confianza, de coordinación, de datos, de proceso, de
regulación o de liquidez— se responde en la Parte 19, clase 1, y muchas veces la
respuesta correcta es no tokenizar.

---

## Las nueve piezas

```text
 1 · EMISOR
     quién asume la obligación y con qué
     patrimonio responde

 2 · REGISTRO DE REFERENCIA
     cuál de los registros determina la
     titularidad si dos difieren

 3 · REGISTRO DE INVERSIONISTAS
     identidad, elegibilidad y límites de
     transferencia

 4 · MERCADO PRIMARIO
     cómo se coloca, a quién y con qué
     documento de oferta

 5 · MERCADO SECUNDARIO
     dónde y cómo se negocia después

 6 · CUSTODIA
     quién tiene las llaves y cómo se
     segrega del patrimonio del custodio

 7 · TRAMO DE DINERO
     con qué se paga la pata de efectivo

 8 · LIQUIDACIÓN
     entrega contra pago, y con qué firmeza

 9 · EVENTOS CORPORATIVOS
     cupones, dividendos, amortización,
     vencimiento y sus incidencias
```

---

## Cómo encajan

```text
          EMISOR
             │  documento de oferta
             ▼
    MERCADO PRIMARIO ──── REGISTRO DE
             │            INVERSIONISTAS
             │            (elegibilidad,
             │             límites)
             ▼
      REGISTRO DE REFERENCIA
             │
      ┌──────┴──────┐
      ▼             ▼
  CUSTODIA     MERCADO SECUNDARIO
      │             │
      └──────┬──────┘
             ▼
       LIQUIDACIÓN ◄──── TRAMO DE DINERO
             │
             ▼
     EVENTOS CORPORATIVOS

LA PIEZA QUE MÁS PROYECTOS OLVIDAN
  el mercado secundario: sin él, la prima
  de iliquidez la paga el emisor durante
  toda la vida del instrumento
```

---

## Las cinco decisiones que la tecnología no resuelve

### 1. Cuál es el registro de referencia

```text
SI EL REGISTRO DISTRIBUIDO Y EL REGISTRO
OFICIAL DIFIEREN, ¿CUÁL MANDA?

  · si manda el oficial, el token es un
    reflejo y la atomicidad es aparente
  · si manda el distribuido, hace falta
    que la ley lo reconozca
  · y si nadie lo ha decidido, se decidirá
    en un tribunal, tarde
```

### 2. Qué otorga exactamente el token

```text
  TOKEN → ¿participación en una sociedad?
        → ¿derecho de crédito frente al
           emisor?
        → ¿derecho real sobre un activo?

  LA CADENA DE DERECHOS TIENE ESLABONES
  QUE NO ESTÁN EN LA CADENA DE BLOQUES,
  y el token vale lo que vale el más débil
```

### 3. Con qué se paga la pata de efectivo

```text
  · dinero de banco comercial · fuera del
    registro, liquidación no atómica
  · depósito tokenizado · atómica, con
    riesgo de banco comercial
  · ficha de dinero electrónico · atómica,
    con riesgo de emisor
  · moneda digital de banco central ·
    atómica, sin riesgo de emisor privado

  CADA OPCIÓN CAMBIA EL RIESGO, NO SOLO
  LA VELOCIDAD
```

### 4. Quién custodia y cómo se segrega

```text
  · segregación jurídica, no contable
  · esquema de firmas con independencia
    acreditada
  · plan de recuperación probado
  · y qué pasa en el concurso del custodio
```

### 5. Cómo se sale

```text
  · ¿qué ocurre si la infraestructura cesa?
  · ¿los tenedores conservan su derecho?
  · ¿quién ejecuta el registro si el
    operador desaparece?
  · ¿existe un plan de salida probado?

SI ESTAS CUATRO NO TIENEN RESPUESTA
ESCRITA, EL MERCADO NO ESTÁ DISEÑADO:
está montado.
```

---

## Qué mide un mercado tokenizado que funciona

| Indicador | Qué revela | Umbral de alarma |
|---|---|---|
| Operaciones en secundario por mes | Si existe mercado o solo emisión | Cero durante dos trimestres |
| Diferencial entre compra y venta | Coste real de salir | Superior a la prima de iliquidez asumida |
| Número de contrapartes activas | Profundidad real | Menos de cinco |
| Tiempo entre orden y liquidación | Si la atomicidad se usa | Superior al del mercado tradicional |
| Incidencias en eventos corporativos | Calidad del ciclo de vida | Cualquiera no prevista |
| Concentración de custodia | Riesgo de punto único | Más del 40 % en un custodio |

---

## Dónde se estudia cada pieza

| Pieza | Parte y clase |
|---|---|
| Emisor y documento de oferta | Parte 21, clases 1 y 4 |
| Registro de referencia | Parte 21, clase 2 |
| Registro de inversionistas y elegibilidad | Parte 21, clase 3 |
| Mercado primario | Parte 21, clase 4 |
| Mercado secundario | Parte 21, clase 6 |
| Custodia | Parte 21, clase 9; Parte 22, clase 9 |
| Tramo de dinero | Parte 21, clase 10 |
| Entrega contra pago | Parte 21, clase 8 |
| Pago contra pago | Parte 21, clase 12 |
| Eventos corporativos | Parte 21, clase 5 |
| Interoperabilidad | Parte 21, clase 15 |
| Régimen de la infraestructura | Parte 22, clase 10 |
| Ensamblaje completo | Parte 23, clases 10 a 14 |

---

## Qué se puede ejecutar

| Aplicación | Qué hace |
|---|---|
| [`apps/tokenization_platform/`](../apps/tokenization_platform/README.md) | Emisor, registro de inversionistas, reglas de cumplimiento, primario, secundario, custodia, liquidación y eventos |
| [`apps/onchain_fx_lab/`](../apps/onchain_fx_lab/README.md) | El tramo de dinero multidivisa y el pago contra pago |
| [`apps/digital_bank_capstone/`](../apps/digital_bank_capstone/README.md) | El conjunto integrado del proyecto final |

---

## Casos asociados

- [`case-studies/tokenization/bono-tokenizado.md`](../case-studies/tokenization/bono-tokenizado.md)
- [`case-studies/tokenization/proyecto-inmobiliario-tokenizado.md`](../case-studies/tokenization/proyecto-inmobiliario-tokenizado.md)
- [`case-studies/fx-onchain/deslizamiento-y-mev.md`](../case-studies/fx-onchain/deslizamiento-y-mev.md)

---

## Limitaciones

- Este plano es **didáctico**: describe las piezas necesarias, no una arquitectura
  lista para producción ni una recomendación de diseño.
- Las aplicaciones del repositorio son **simuladores**: no son un banco, ni un
  mercado, ni un custodio, y no operan con fondos reales.
- El régimen jurídico de cada pieza depende de la jurisdicción y **cambia**.

---

[🏠 Inicio](../README.md) · [📚 Documentación](README.md) · [📖 Programa](../SYLLABUS.md)
