# Caso · El oráculo que dijo la verdad de un mercado vacío

**Tema:** blockchain y DLT · **Parte relacionada:** 19 · **Naturaleza:** caso
sintético compuesto · **Fecha de verificación:** 2026-08-12

Un contrato de préstamo colateralizado liquida posiciones por 6,4 millones en
noventa segundos. El precio que usó era correcto: era el precio real de un mercado
en el que, en ese momento, casi no había nadie. El oráculo no falló. Falló la idea
de que un precio es un hecho.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · el contrato liquida cuando el colateral
    cae por debajo del 130 % del préstamo
  · el precio lo aporta un oráculo que toma
    la mediana de tres mercados
  · a las 03:14, dos de los tres mercados
    tenían profundidad muy reducida
  · una orden de venta de 900 000 movió el
    precio un 19 % en uno de ellos
  · la mediana cayó un 11 %
  · el precio se recuperó en 4 minutos

SUPUESTO DEL EJERCICIO
  · posiciones liquidadas         6 400 000
  · penalización de liquidación         8 %
  · pérdida de los prestatarios     512 000
  · beneficio de los liquidadores   512 000
```

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Prestatario | Mantener su posición | Un umbral del 130 % |
| Protocolo | Que el préstamo esté siempre cubierto | El precio del oráculo |
| Oráculo | Reportar un precio verificable | Tres precios reales |
| Liquidador | Beneficio por liquidar | Todo, y más rápido |
| Mercado con poca profundidad | Volumen | Su propio libro |
| Diseñador del protocolo | Robustez | La mediana como defensa |

## Decisiones

```text
DISEÑO
  usar mediana de tres fuentes
  DECISIÓN RAZONABLE Y INSUFICIENTE:
  la mediana protege del error de una
  fuente, no de la falta de profundidad
  de dos

DISEÑO
  no ponderar por volumen ni por
  profundidad
  RAZÓN: complejidad y coste de datos

DISEÑO
  no usar media temporal
  RAZÓN: retrasa la liquidación y aumenta
  el riesgo de infracolateralización
  ESTA ES LA COMPENSACIÓN REAL DEL CASO

03:14
  el contrato ejecuta lo que se le dijo
  NO HAY FALLO DE SOFTWARE
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Precio correcto en mercado ilíquido | Estructural | Sí |
| Falta de ponderación por profundidad | Desde el diseño | Sí |
| Ausencia de media temporal | Desde el diseño | Sí |
| Manipulación deliberada del precio | Posible | No demostrada |
| Irreversibilidad de la liquidación | Estructural | Sí |
| Concentración de liquidadores | Estructural | Sí |

## Regulación

```text
QUÉ ALCANZA

  FORMACIÓN DE PRECIOS Y ABUSO
    mover un precio para provocar
    liquidaciones ajenas encaja en la
    descripción de manipulación en los
    regímenes que la tipifican para estos
    mercados

  DILIGENCIA DEL DISEÑADOR
    donde existe un sujeto responsable del
    protocolo, la elección de la fuente de
    precio es una decisión con consecuencias
    exigibles

  PROTECCIÓN DEL USUARIO
    la información sobre cómo se determina
    el precio de liquidación es material

LÍMITE
  cuando no hay sujeto identificable, no
  hay a quién exigir: es el límite que
  este programa señala desde el inicio
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Mediana de tres fuentes | Sí | Sí, e insuficiente | Ponderar por profundidad |
| Media temporal | No | — | Ventana corta, con su coste |
| Umbral de desviación | No | — | Pausar si el precio salta un X % |
| Liquidación parcial | No | — | Liquidar lo mínimo necesario |
| Interruptor de emergencia | No | — | Y quién puede accionarlo |
| Divulgación del método | Parcial | No | Que el usuario sepa el riesgo |

El cuarto control es el que más pérdida habría evitado. Liquidar la posición
entera cuando basta con restablecer el ratio convierte un ajuste en una pérdida
del 8 % sobre el total.

## Resultado

```text
LO QUE OCURRIÓ

  liquidado                    6 400 000
  penalización 8 %               512 000
  precio recuperado en           4 min
  posiciones que no habrían sido
    liquidadas con media de 10 min
                               5 900 000  (92 %)

  PÉRDIDA EVITABLE               472 000

REPARTO
  prestatarios          −512 000
  liquidadores          +512 000
  protocolo                    0
  → NO ES UNA PÉRDIDA DEL SISTEMA,
    ES UNA TRANSFERENCIA
  Y ESO IMPORTA: hay un incentivo
  permanente a que vuelva a pasar
```

## Lecciones

1. **Un precio no es un hecho: es el resultado de un mercado en un momento.** Un
   oráculo que reporta fielmente un mercado vacío reporta fielmente un dato que no
   debe usarse para liquidar.
2. **La mediana protege del error, no de la iliquidez.** Son dos fallos distintos
   y necesitan defensas distintas.
3. **La liquidación total cuando basta la parcial es un defecto de diseño**, no
   una consecuencia del mercado.
4. **Cuando la pérdida de unos es la ganancia de otros, el incentivo persiste.**
   Un control que no cambia el incentivo no cierra el caso.

## Preguntas

1. ¿Qué ventana de media temporal elegirías, y qué riesgo aceptas al retrasar la
   liquidación?
2. ¿Cómo se pondera por profundidad sin crear una nueva superficie de
   manipulación?
3. ¿Fue esto manipulación? ¿Qué evidencia harías falta para afirmarlo?
4. ¿Quién responde ante los prestatarios si el protocolo no tiene sujeto?
5. ¿Qué información sobre el método de precio debería recibir un usuario antes de
   depositar colateral?

## Fuentes

- IOSCO (2023). *Policy Recommendations for Decentralized Finance*. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD754.pdf>
- Financial Stability Board (2023). *The Financial Stability Risks of Decentralised Finance*. <https://www.fsb.org/2023/02/the-financial-stability-risks-of-decentralised-finance/>
- BIS (2023). *Annual Economic Report*, capítulo sobre el sistema monetario futuro. <https://www.bis.org/publ/arpdf/ar2023e3.htm>
- CPMI-IOSCO (2012). *Principles for Financial Market Infrastructures*. <https://www.bis.org/cpmi/publ/d101.htm>
- Verificación local: caso sintético; cifras supuestas. La tipificación de la manipulación en mercados de criptoactivos depende de la jurisdicción. **Fecha de verificación: 2026-08-12.** No constituye asesoría de inversión.
