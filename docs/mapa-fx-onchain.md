# Mapa de FX on-chain

**Una ruta propia, porque el cambio de divisas atraviesa tres partes y se estudia
mal si se toma solo desde una.** El FX tradicional está en las Partes 8 y 10; el
pago transfronterizo que lo contiene, en la 18; y la ejecución y liquidación sobre
infraestructura programable, en la 21. Este documento reúne la ruta.

Antes de recorrerla conviene fijar la definición que usa el programa, porque en el
mercado se usan al menos tres distintas:

```text
FX ON-CHAIN

  cotización, ejecución, compensación o
  liquidación de operaciones de cambio
  mediante infraestructura programable,
  activos tokenizados o registros
  distribuidos

LO QUE NO ES
  · no es «comprar cripto con pesos»
  · no es una casa de cambio con web
  · no es un mercado sin regulación por
    estar sobre un registro
```

---

## Las cuatro preguntas que ordenan la materia

```text
1 · ¿QUÉ SE CAMBIA?
    moneda fiduciaria contra ficha estable
    ficha estable contra ficha estable
    depósito tokenizado contra depósito
    tokenizado
    → cada combinación tiene un riesgo de
      contraparte distinto

2 · ¿CÓMO SE FORMA EL PRECIO?
    solicitud de precio · libro de órdenes
    creador de mercado automatizado
    → y cada mecanismo tiene su coste
      oculto propio

3 · ¿CÓMO SE LIQUIDA?
    secuencial · pago contra pago
    atómica
    → aquí vive el riesgo Herstatt

4 · ¿QUIÉN RESPONDE?
    intermediario identificable · protocolo
    sin sujeto
    → determina si hay a quién exigir
```

---

## La ruta, por orden de estudio

| Orden | Dónde | Qué aporta |
|---:|---|---|
| 1 | Parte 8, inversiones y mercados | Microestructura, libro de órdenes, formación de precio |
| 2 | Parte 10, operaciones bancarias | Mesa de cambio, spread, posición y su cobertura |
| 3 | Parte 18, clase 9 | FX dentro de un pago transfronterizo: los tres precios |
| 4 | Parte 18, clase 15 | Pago contra pago y liquidación atómica |
| 5 | Parte 21, clase 10 | El tramo de dinero: con qué se paga la pata |
| 6 | Parte 21, clase 11 | FX: del mercado mayorista al registro |
| 7 | Parte 21, clase 12 | Pago contra pago y riesgo de liquidación |
| 8 | Parte 21, clase 13 | Creación de mercado automatizada |
| 9 | Parte 21, clase 15 | Interoperabilidad entre infraestructuras |
| 10 | Parte 22, clase 19 | El régimen europeo conexo y sus límites |

---

## Los tres mecanismos de precio, comparados

```text
SOLICITUD DE PRECIO (RFQ)
  quién cotiza   proveedores identificados
  ventaja        precio en firme por tamaño
  coste oculto   depende del número de
                 proveedores consultados
  cuándo         importes grandes

LIBRO DE ÓRDENES (CLOB)
  quién cotiza   cualquiera
  ventaja        transparencia previa
  coste oculto   profundidad real distinta
                 de la mostrada
  cuándo         mercados con volumen

CREADOR DE MERCADO AUTOMATIZADO (AMM)
  quién cotiza   una fórmula sobre reservas
  ventaja        disponible 24/7 sin
                 contraparte activa
  coste oculto   impacto de precio, que
                 crece con el tamaño, y
                 extracción por reordenación
  cuándo         importes pequeños respecto
                 de la profundidad del pool

LA REGLA PRÁCTICA
  nunca mover más del 10 % de la
  profundidad en una sola operación
```

---

## El riesgo que da sentido a toda la ruta

```text
RIESGO DE LIQUIDACIÓN

  una pata entregada, la otra no

  EN EL MERCADO TRADICIONAL
    se mitiga con pago contra pago,
    donde existe infraestructura para
    ese par de divisas

  SOBRE UN REGISTRO COMPARTIDO
    la liquidación atómica lo elimina
    por construcción: o pasan las dos
    patas o no pasa ninguna

  Y AQUÍ ESTÁ LA PREGUNTA DIFÍCIL
    ¿tiene firmeza legal esa atomicidad?
    Parte 21, clase 12
    Parte 22, clase 10

SI LA RESPUESTA ES «TÉCNICAMENTE SÍ,
JURÍDICAMENTE NO CONSTA», el riesgo no se
eliminó: se trasladó al derecho concursal.
```

---

## Las seis afirmaciones que esta ruta desmonta

| Afirmación frecuente | Qué falta | Dónde se corrige |
|---|---|---|
| «El cambio on-chain no tiene comisiones» | El impacto de precio y la extracción no son comisiones y se pagan igual | Parte 21, clase 13 |
| «Es 24/7, luego siempre hay liquidez» | La profundidad cae fuera de horario y el impacto sube | Parte 21, clase 13 |
| «La liquidación atómica elimina el riesgo» | Solo si esa firmeza tiene reconocimiento jurídico | Parte 22, clase 10 |
| «Es más barato que la banca corresponsal» | Falta el tramo de entrada y salida a moneda local | Parte 18, clases 9 y 14 |
| «Con stablecoins no hay riesgo de cambio» | Se sustituye por riesgo de emisor y de paridad | Parte 20, clase 6 |
| «No hay controles de capital que aplicar» | La operación de cambio sigue estando sujeta donde lo esté | Parte 22, clases 1 y 16 |

---

## Qué se puede ejecutar

| Aplicación | Qué hace |
|---|---|
| [`apps/onchain_fx_lab/`](../apps/onchain_fx_lab/README.md) | Solicitud de precio, libro de órdenes, creador automatizado, pago contra pago y escenarios de riesgo |
| [`apps/cross_border_payments_lab/`](../apps/cross_border_payments_lab/README.md) | El FX dentro de la ruta de pago, con sus tres precios |
| [`apps/tokenization_platform/`](../apps/tokenization_platform/README.md) | Entrega contra pago sobre instrumentos tokenizados |

---

## Casos asociados

- [`case-studies/fx-onchain/deslizamiento-y-mev.md`](../case-studies/fx-onchain/deslizamiento-y-mev.md)
- [`case-studies/cross-border-payments/falla-pvp.md`](../case-studies/cross-border-payments/falla-pvp.md)
- [`case-studies/blockchain/falla-de-oraculo.md`](../case-studies/blockchain/falla-de-oraculo.md)

---

## Limitaciones

- Nada de esta ruta constituye asesoría de inversión ni recomendación sobre
  ningún mecanismo de ejecución.
- El programa **no proporciona técnicas para eludir controles de capital**, para
  ocultar el origen de fondos ni para explotar la ordenación de operaciones.
- La existencia de infraestructura de pago contra pago depende del par de divisas
  y de la jurisdicción: verifícalo antes de suponerlo.

---

[🏠 Inicio](../README.md) · [📚 Documentación](README.md) · [📖 Programa](../SYLLABUS.md)
