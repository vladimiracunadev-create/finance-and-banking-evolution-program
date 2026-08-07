<!-- portada:inicio -->
<div align="center">

# 🏛️ Mapa de tokenización y FX sobre registros

**Dónde está cada concepto de la Parte 21 y las seis afirmaciones que la parte desmonta.**

[![parte](https://img.shields.io/badge/parte-21%20%C2%B7%20tokenizaci%C3%B3n%20y%20FX-7c5cff?style=flat-square)](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/README.md)
[![labs](https://img.shields.io/badge/labs-tokenization__platform%20%C2%B7%20onchain__fx__lab-3776AB?style=flat-square)](../apps/tokenization_platform/)

[⬅️ Mapa anterior](mapa-activos-digitales.md) ·
[🏠 Inicio](../README.md) ·
[📘 Parte 21](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/README.md) ·
[➡️ Mapa siguiente](mapa-regulatorio.md)

</div>
<!-- portada:fin -->

---

Guía de navegación de la Parte 21: dónde está cada concepto, con qué se conecta
y qué se puede ejecutar para comprobarlo.

## 🎯 El eje de la parte

```text
TOKENIZAR NO CREA UN DERECHO.
LO REPRESENTA.

  ¿QUÉ PASA SI EL REGISTRO DICE UNA COSA
   Y EL REGISTRO OFICIAL DICE OTRA?

  · si manda el registro oficial, el token es
    un espejo y todo el diseño es un sistema
    de conciliación
  · si manda el token, alguien tuvo que
    declararlo por norma

NO HAY UNA TERCERA RESPUESTA,
y no responderla es el error que hunde
la mitad de los proyectos de tokenización.
```

Y la respuesta decide algo más que la conciliación: **decide si el único
beneficio exclusivo de la tokenización —la liquidación atómica— es alcanzable.**

## ❓ Las cuatro preguntas de viabilidad

| Pregunta | Qué decide |
|---|---|
| ¿Qué derecho se representa? | El régimen aplicable |
| ¿Dónde vive ese derecho hoy? | Qué registro hay que coordinar |
| **¿Quién manda si divergen?** | **Si la atomicidad es posible** |
| ¿Qué se gana que no se pueda ganar sin tokenizar? | Si el proyecto procede |

De cinco promesas habituales, **dos resisten**: la operación fuera del horario
del sistema de pagos y la liquidación atómica contra el dinero, esta última solo
si ambos tramos están en el mismo registro.

## 🧭 Recorrido de la parte

```text
IDENTIFICACIÓN   1 · qué es y qué no es tokenizar
                        │
                 2 · el registro de referencia
                        │
EL INSTRUMENTO   3 · derechos del tenedor
                        │
CICLO COMPLETO   4 · emisión    5 · ciclo de vida
                        │
MERCADO          6 · liquidez prometida   7 · fraccionamiento
                        │
LIQUIDACIÓN      8 · entrega contra pago atómica
                 9 · custodia   10 · el tramo de dinero
                        │
DIVISAS         11 · FX    12 · pago contra pago
                        │
MECANISMOS      13 · creación de mercado automatizada
                14 · colateral y garantías
                        │
CONEXIÓN        15 · interoperabilidad
                        │
INTEGRACIÓN     16 · expediente de diseño
```

## 🗺️ Dónde está cada concepto

| Concepto | Clase | Laboratorio | Código |
|---|:---:|:---:|---|
| Tokenizar, digitalizar, desmaterializar | 1 | 1 | — |
| Emisión nativa | 1 | 1 | — |
| Envoltorio y sus obligados | 1 | 1 | — |
| Las cuatro preguntas de viabilidad | 1 | 1 | — |
| Configuración espejo | 2 | 1 | `registry` |
| Bloqueo de origen | 2 | 1 | `registry` |
| Las seis causas de divergencia | 2 | 1 | `registry` |
| Conciliación y ventana | 2 | 1 | `registry` |
| Autoridad de resolución | 2 | 1 | `registry` |
| Derechos económicos, políticos y de información | 3 | 2 | — |
| Umbrales y fraccionamiento | 3, 7 | 2 | — |
| Redondeo del voto | 3 | 2 | — |
| Derecho de rescate | 3 | 1 | `registry` |
| Las nueve etapas de una emisión | 4 | 2 | `issuance` |
| Adjudicación y prorrateo | 4 | 2 | `issuance` |
| Sobredemanda artificial | 4 | 2 | `issuance` |
| Bloqueo del importe | 4 | 2 | `issuance` |
| Emisión desierta | 4 | 2 | `issuance` |
| Fecha de corte e instantánea | 5 | 2 | `lifecycle` |
| Verificación del aprovisionamiento | 5 | 2 | `lifecycle` |
| Función de inmovilización | 5 | 2 | `lifecycle` |
| Vencimiento y destrucción | 5 | 2 | `lifecycle` |
| Transferibilidad, negociabilidad, liquidez | 6 | 5 | — |
| Compromiso de cotización | 6 | 5 | — |
| Subasta frente a continuo | 6 | 5 | — |
| Coste unitario de servicio | 7 | 5 | — |
| Importe de equilibrio | 7 | 5 | — |
| Acceso sin salida | 6, 7 | 5 | — |
| Atomicidad y estado intermedio | 8 | 3 | `settlement` |
| Rechazar antes de bloquear | 8 | 3 | `settlement` |
| Los cinco riesgos | 8 | 4 | `settlement` |
| Neteo con liquidación atómica | 8 | 3 | `settlement` |
| Ómnibus frente a segregada | 9 | 4 | — |
| Conciliación a tres bandas | 9 | 4 | — |
| Plan de sustitución del custodio | 9 | 4 | — |
| Las cuatro opciones de dinero | 10 | 3 | `settlement` |
| Saldo prefinanciado y horario | 10 | 3 | `settlement` |
| Formación de precio en el registro | 11 | 7 | `pricing` |
| Los seis tramos del coste | 11 | 7 | `pricing` |
| Corrección por profundidad | 11 | 7 | `pricing` |
| Ventana de exposición | 12 | 7 | `settlement` (FX) |
| Neteo, límites y PvP | 12 | 7 | `settlement` (FX) |
| Oponibilidad del acuerdo de neteo | 12 | 7 | `settlement` (FX) |
| Producto constante y deslizamiento | 13 | 6 | `amm` |
| Pérdida por divergencia | 13 | 6 | `amm` |
| Recorte y colchón | 14 | 8 | `collateral` |
| Cascada de liquidaciones | 14 | 8 | `collateral` |
| Liquidación parcial y pausa | 14 | 8 | `collateral` |
| Puente, enlace, participante común | 15 | 4 | — |
| Umbral efectivo y valor acumulado | 15 | 4 | — |
| Las doce decisiones del expediente | 16 | proyecto | — |

## 🚫 Las seis afirmaciones que la parte desmonta

1. **«Liquidación atómica con el registro oficial de referencia.»** Un espejo lo
   impide por construcción.
2. **«Hubo 3,75 veces de demanda.»** La mayor parte es artificial si pedir de más
   no cuesta nada.
3. **«El cupón es automático, no falla.»** Falla si el emisor no aprovisiona, y
   pagar por orden hasta agotar los fondos discrimina.
4. **«Ahorra 33 puntos básicos.»** Nueve, tras medir la profundidad del libro.
5. **«Tenemos acuerdo de neteo.»** Solo reduce la exposición si es oponible en el
   concurso de la contraparte.
6. **«El recorte es del 5 %, hay margen.»** Lo que rompe el sistema es liquidar
   posiciones enteras contra un mercado menos profundo que el volumen a vender.

Las seis tienen una prueba en
[`tests/test_tokenization_platform.py`](../tests/test_tokenization_platform.py) y
[`tests/test_onchain_fx_lab.py`](../tests/test_onchain_fx_lab.py); cinco de ellas
**documentan defectos y deben pasar**.

## 🧪 Qué se puede ejecutar

```bash
python apps/tokenization_platform/cli.py registry
```

```bash
python apps/tokenization_platform/cli.py issuance
```

```bash
python apps/tokenization_platform/cli.py coupon
```

```bash
python apps/tokenization_platform/cli.py settlement
```

```bash
python apps/tokenization_platform/cli.py collateral --drop 0.12
```

```bash
python apps/onchain_fx_lab/cli.py pricing
```

```bash
python apps/onchain_fx_lab/cli.py amm --rounds 4
```

```bash
python apps/onchain_fx_lab/cli.py settlement
```

## ✅ La conclusión que la parte permite

Un expediente de esta parte **puede concluir que no procede tokenizar, y eso es
la máxima calificación**. Lo que se evalúa es si las doce decisiones están, si
cada una tiene su alternativa medida y si los supuestos están declarados.

Y hay una regla que resume la parte entera: **una decisión sin alternativa
medida es una preferencia, no una decisión.**

## ➡️ Hacia dónde sigue

| De esta parte | A | Qué se profundiza |
|---|---|---|
| Registro de referencia (2) | Parte 22 | El régimen de la infraestructura |
| Derechos y fraccionamiento (3, 7) | Parte 22 | La protección del inversionista |
| Liquidación y custodia (8, 9) | Parte 22 | La supervisión de las infraestructuras |
| Interoperabilidad (15) | Parte 22 | El régimen transfronterizo |
| Todo | Parte 23 | El mercado completo, construido y defendido |

---

**Ver también:** [Parte 21](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/README.md) ·
[Etapa 5](etapa-5-finanzas-digitales.md) ·
[Tokenization Platform](../apps/tokenization_platform/README.md) ·
[Onchain FX Lab](../apps/onchain_fx_lab/README.md) ·
[Glosario de finanzas digitales](glosario-finanzas-digitales.md)

<!-- pie:inicio -->
---

<div align="center">

[⬅️ Mapa anterior](mapa-activos-digitales.md) · [🏠 Inicio](../README.md) · [📘 Parte 21](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/README.md) · [➡️ Mapa siguiente](mapa-regulatorio.md)

</div>
<!-- pie:fin -->
