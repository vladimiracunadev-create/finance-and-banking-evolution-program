<!-- portada:inicio -->
<div align="center">

# 🪙 Mapa de activos digitales y stablecoins

**Dónde está cada concepto de la Parte 20 y las seis afirmaciones que la parte desmonta.**

[![parte](https://img.shields.io/badge/parte-20%20%C2%B7%20activos%20digitales-7c5cff?style=flat-square)](../modules/19-activos-digitales-stablecoins-y-dinero-programable/README.md)
[![lab](https://img.shields.io/badge/lab-digital__assets__risk__lab-3776AB?style=flat-square)](../apps/digital_assets_risk_lab/)

[⬅️ Mapa anterior](mapa-blockchain-dlt.md) ·
[🏠 Inicio](../README.md) ·
[📘 Parte 20](../modules/19-activos-digitales-stablecoins-y-dinero-programable/README.md) ·
[➡️ Mapa siguiente](mapa-tokenizacion.md)

</div>
<!-- portada:fin -->

---

Guía de navegación de la Parte 20: dónde está cada concepto, con qué se conecta
y qué se puede ejecutar para comprobarlo.

## 🎯 El eje de la parte

```text
UN ACTIVO DIGITAL NO ES UNA TECNOLOGÍA:
ES UNA PROMESA ANOTADA EN UN REGISTRO

  ¿QUIÉN LA HACE?     el emisor, o nadie
  ¿QUÉ PROMETE?       un importe, un derecho, o nada
  ¿CON QUÉ RESPALDO?  activos, otro token, o expectativa
  ¿EXIGIBLE CUÁNDO?   a la vista, con plazo, o nunca
  ¿ANTE QUIÉN?        un juzgado, un comité, o nadie

SI LAS CINCO RESPUESTAS SON «NADIE» O «NADA»,
EL PRECIO LO SOSTIENE ÚNICAMENTE
QUE OTRO ESTÉ DISPUESTO A PAGARLO
```

Ninguna de las cinco preguntas es técnica. La red, el estándar de contrato y la
billetera no aparecen, y esa ausencia es el contenido de la parte.

## 🧩 Los cinco instrumentos que no son sinónimos

| Instrumento | Quién debe | Qué es el saldo | Clase |
|---|---|---|:---:|
| Criptoactivo no respaldado | Nadie | Ningún derecho frente a nadie | 2 |
| Stablecoin | El emisor, según su documentación | Un derecho contractual, si existe | 3 |
| Dinero electrónico | Un emisor autorizado | Redención a la par | 9 |
| Depósito tokenizado | Un banco | Un depósito, con su garantía | 8 |
| CBDC | El banco central | Un pasivo soberano | 10 |

La tabla decide **quién quiebra, qué garantía aplica y a quién reclama el
cliente**. Ningún componente técnico la cambia.

## 🧭 Recorrido de la parte

```text
IDENTIFICACIÓN   1 · taxonomía por la promesa
                        │
SIN OBLIGADO     2 · criptoactivos no respaldados
                        │
LA PARIDAD       3 · mecánica    4 · reservas    5 · redención
                        │
CUANDO FALLA     6 · corrida     7 · espiral algorítmica
                        │
LAS ALTERNATIVAS 8 · depósito tokenizado   9 · dinero electrónico
                       10 · CBDC          11 · dinero programable
                        │
OPERACIÓN       12 · custodia   13 · mercado   14 · contagio
                        │
BALANCE         15 · contabilidad, tributación y prudencial
                        │
INTEGRACIÓN     16 · expediente de decisión
```

## 🗺️ Dónde está cada concepto

| Concepto | Clase | Laboratorio | Código |
|---|:---:|:---:|---|
| Ficha de cinco preguntas | 1 | 1 | `classification` |
| Activo digital, criptoactivo y token | 1 | 1 | — |
| Respaldo circular | 1, 7 | 1, 5 | `classification` |
| Sustancia sobre forma | 1, 9 | 1 | `classification` |
| Capital desplazado por una exposición | 2 | 1 | — |
| Escasez y reflexividad | 2 | — | — |
| Arbitraje de redención | 3 | 4 | `depeg` |
| Banda de no arbitraje | 3 | 4 | `depeg` |
| Participante autorizado | 3 | 4 | — |
| Paridad de derecho y de mercado | 3 | 1, 4 | `classification` |
| Cobertura contable y líquida | 4 | 2 | `reserves` |
| Descalce de plazo | 4 | 2 | `reserves` |
| Descuento por venta forzada | 4, 6 | 2 | `reserves` |
| Atestación frente a auditoría | 4 | 2 | — |
| Las siete etapas de una redención | 5 | 3 | `redemption` |
| Orden de llegada y prorrateo | 5 | 3 | `redemption` |
| Comisión antidilución | 5 | 3 | `redemption` |
| Tramo mínimo íntegro | 5 | 3 | `redemption` |
| Las cinco fases de una corrida | 6 | 4 | `depeg` |
| Punto de no retorno | 6 | 2, 4 | `reserves` |
| Recuperación aparente | 6 | 4 | `depeg` |
| Respaldo endógeno y espiral | 7 | 5 | `algorithmic` |
| Rendimiento por dilución | 7 | 5 | `algorithmic` |
| Cobertura de un híbrido | 7 | 5 | `algorithmic` |
| Singularidad del dinero | 8 | 1 | — |
| Crédito intradía por operar 24/7 | 8 | 1 | — |
| Tres elementos del dinero electrónico | 9 | 1 | `classification` |
| Salvaguarda de fondos | 9 | 1 | — |
| Modelo de dos niveles | 10 | 1 | — |
| Desintermediación y límite de tenencia | 10 | 1 | — |
| Pago frente a dinero programable | 11 | 6 | — |
| Fungibilidad y mercado gris | 11 | 6 | — |
| Vía de excepción | 11 | 6 | — |
| Independencia efectiva | 12 | 6 | `custody` |
| Recuperación sin puerta trasera | 12 | 6 | `custody` |
| Los siete controles de retirada | 12 | 6 | `custody` |
| Segregación jurídica | 12, 15 | 6 | — |
| Volumen, amplitud, profundidad, resiliencia | 13 | 7 | `market` |
| Impacto de mercado | 13 | 7 | `market` |
| Límite de posición | 13 | 7 | `market` |
| Exposición de segundo grado | 14 | 8 | `contagion` |
| Dependencia común | 14 | 8 | `contagion` |
| Venta correlacionada | 14 | 8 | — |
| Asimetría del intangible | 15 | 2 | — |
| Balance frente a capital regulatorio | 2, 15 | 2 | — |
| Las doce piezas del expediente | 16 | proyecto | — |

## 🚫 Las seis afirmaciones que la parte desmonta

1. **«La cobertura subió, vamos mejor.»** Sube mientras la composición empeora y
   el efectivo llega a cero.
2. **«La corrida la causó el pánico.»** La causa el orden de la cola: si ser el
   primero vale algo, todos solicitan.
3. **«El ratio de absorción está sano.»** Sube durante todo el colapso del
   sistema que mide.
4. **«Es un 3 de 5, es robusto.»** Cinco guardianes con el mismo dispositivo son
   uno.
5. **«Mueve 184 millones al día.»** Absorbe 2 con un 1 % de impacto.
6. **«No tenemos exposición.»** Cero directo y 117 millones de necesidad de
   liquidez.

Las seis tienen una prueba en
[`tests/test_digital_assets_risk_lab.py`](../tests/test_digital_assets_risk_lab.py),
y las seis **documentan defectos y deben pasar**.

## 🧪 Qué se puede ejecutar

```bash
python apps/digital_assets_risk_lab/cli.py reserves --redemption 0.35
```

```bash
python apps/digital_assets_risk_lab/cli.py queue
```

```bash
python apps/digital_assets_risk_lab/cli.py spiral --rounds 5
```

```bash
python apps/digital_assets_risk_lab/cli.py custody
```

```bash
python apps/digital_assets_risk_lab/cli.py market --position 12000000
```

```bash
python apps/digital_assets_risk_lab/cli.py contagion
```

```bash
python -m pytest tests/test_digital_assets_risk_lab.py -q
```

## ✅ La conclusión que la parte permite

Un expediente de esta parte **puede concluir que el instrumento no es apto, y eso
es la máxima calificación**. Lo que se evalúa no es la decisión: es si las doce
piezas están, si los cálculos son correctos y si los supuestos están declarados.

## ➡️ Hacia dónde sigue

| De esta parte | A | Qué se profundiza |
|---|---|---|
| Clasificación y promesa (1) | Parte 21 | El instrumento financiero tokenizado |
| Depósito tokenizado y CBDC (8, 10) | Parte 21 | El tramo de dinero en una entrega contra pago |
| Custodia (12) | Parte 21 | La custodia de valores tokenizados |
| Régimen y perímetro (1, 9) | Parte 22 | El régimen del emisor y del custodio |
| Contagio (14) | Parte 22 | La supervisión de la interconexión |
| Todo | Parte 23 | El activo dentro de una infraestructura completa |

---

**Ver también:** [Parte 20](../modules/19-activos-digitales-stablecoins-y-dinero-programable/README.md) ·
[Etapa 5](etapa-5-finanzas-digitales.md) ·
[Digital Assets Risk Lab](../apps/digital_assets_risk_lab/README.md) ·
[Glosario de finanzas digitales](glosario-finanzas-digitales.md)

<!-- pie:inicio -->
---

<div align="center">

[⬅️ Mapa anterior](mapa-blockchain-dlt.md) · [🏠 Inicio](../README.md) · [📘 Parte 20](../modules/19-activos-digitales-stablecoins-y-dinero-programable/README.md) · [➡️ Mapa siguiente](mapa-tokenizacion.md)

</div>
<!-- pie:fin -->
