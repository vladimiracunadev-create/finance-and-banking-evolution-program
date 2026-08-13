# Caso · Cuarenta y una horas de cola

**Tema:** stablecoins · **Parte relacionada:** 20 · **Naturaleza:** caso sintético
compuesto · **Fecha de verificación:** 2026-08-12

Un emisor atiende todas las peticiones de reembolso que recibe. Ninguna se
rechaza. Y aun así, a las cuarenta y una horas ha perdido el 61 % de su
circulante y ha tenido que vender activos con pérdida. Este caso trata de por qué
cumplir la promesa puede destruir al que la cumple.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · fichas en circulación        3 100 000 000
  · reserva                      3 100 000 000
    · 30 % vencimiento < 7 días
    · 45 % vencimiento < 90 días
    · 25 % vencimiento 1 a 3 años
  · desencadenante: un informe crítico sobre
    la calidad del 25 % largo
  · el emisor responde publicando la
    composición completa, que era correcta

CURVA DE REEMBOLSOS (supuesto del ejercicio)
  hora  0–6    240 000 000
  hora  6–12   420 000 000
  hora 12–24   610 000 000
  hora 24–41   621 000 000
  TOTAL      1 891 000 000   (61 %)
```

La publicación de la composición no calmó nada: la aceleró. El informe decía que
el 25 % largo era ilíquido; la publicación confirmó que existía; y quien leyó
ambas cosas concluyó, correctamente, que **quien reembolsara antes cobraría del
tramo corto y quien reembolsara después dependería del largo.** La prima de
prioridad es lo que convierte una duda en una corrida.

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Tenedor grande | Salir el primero | Todo, y rápido |
| Tenedor pequeño | Entender qué pasa | Titulares |
| Emisor | Sostener la paridad y el negocio | Su propia escalera de vencimientos |
| Autor del informe | Señalar un riesgo real | Datos públicos |
| Compradores de los activos largos | Comprar barato | Que el emisor tenía que vender |
| Supervisor | Que no se contagie | Informes con retraso |

## Decisiones

```text
HORA 0
  el emisor decide atender todo sin límite
  DECISIÓN CORRECTA JURÍDICAMENTE
  y la que agota el tramo corto primero

HORA 9
  se agota el tramo de 7 días
  DECISIÓN: empezar a liquidar el de 90
  días con descuento

HORA 18
  se plantea suspender temporalmente
  DECISIÓN: no suspender
  RAZÓN: suspender confirma la insolvencia
  aparente y destruye la franquicia

HORA 24
  se contrata una línea de liquidez
  garantizada con el tramo largo
  COSTE: elevado, porque se negocia
  en el peor momento

HORA 41
  la curva se aplana
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Prima de prioridad | Estructural | Sí |
| Desajuste de plazos | Desde el diseño | Sí |
| Venta forzada de activos | Desde la hora 9 | Sí |
| Publicación que acelera la salida | Desde la hora 2 | Sí |
| Contagio a otras fichas | Estructural | Parcialmente |
| Pérdida permanente de circulante | Desde la hora 12 | Sí |

## Regulación

```text
QUÉ ALCANZA

  RESERVA Y LIQUIDEZ
    los regímenes exigen composición con
    instrumentos muy líquidos y de riesgo
    mínimo; el tramo largo de este caso
    habría sido cuestionable bajo varios
    de ellos

  PLANES PARA EL DÍA MALO
    plan de recuperación —cómo vuelvo a
    cumplir— y plan de reembolso —cómo
    devuelvo a todos si cierro— son
    exigibles en algunos regímenes

  SUSPENSIÓN DEL REEMBOLSO
    su admisibilidad y sus condiciones son
    una de las cuestiones más discutidas:
    protege al conjunto y perjudica a quien
    llega tarde

LÍMITE
  depende de la jurisdicción y de la fecha
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Escalera de vencimientos | Sí | Insuficiente | Peso mayor en el tramo corto |
| Publicación periódica | No | — | Antes del episodio, no durante |
| Línea de liquidez contratada | No | — | Antes, no en la hora 24 |
| Plan de reembolso ordenado | No | — | Con prelación y calendario |
| Prueba de estrés con esta curva | No | — | 60 % en 48 h como escenario base |
| Comunicación diferenciada | No | — | Al minorista, en su lenguaje |

## Resultado

```text
BALANCE DEL EPISODIO (supuestos)

  reembolsado                1 891 000 000
  circulante restante        1 209 000 000
  pérdida por venta forzada
    tramo 90 días, descuento 1,8 %
      sobre 900 000 000        16 200 000
    tramo largo, descuento 6,4 %
      sobre 430 000 000        27 520 000
  coste de la línea de liquidez  8 900 000

  PÉRDIDA TOTAL                52 620 000

  Y LA RESERVA SIGUE CUBRIENDO
  AL 100 % LO QUE QUEDA

EL EMISOR CUMPLIÓ Y PERDIÓ
EL 61 % DE SU NEGOCIO.
```

## Lecciones

1. **La prima de prioridad convierte cualquier duda en corrida.** Mientras salir
   antes sea mejor que salir después, la respuesta racional individual es salir
   ya.
2. **Publicar durante el episodio confirma; publicar antes previene.** La misma
   información tiene efecto opuesto según el momento.
3. **La liquidez se contrata cuando no hace falta.** Una línea negociada en la
   hora 24 se paga a precio de hora 24.
4. **Suspender es una decisión de política, no técnica**, y conviene tenerla
   decidida y escrita antes: quién puede, con qué umbral, por cuánto tiempo y con
   qué prelación al reanudar.

## Preguntas

1. ¿Cómo se elimina o se reduce la prima de prioridad? ¿Qué instrumentos existen?
2. ¿Habrías suspendido en la hora 18? Justifica la decisión ante los dos grupos
   afectados.
3. ¿Qué composición de reserva habría soportado esta curva sin pérdida?
4. ¿Qué habrías publicado, y cuándo, para que la publicación no acelerara la
   salida?
5. ¿Es este episodio un problema de solvencia, de liquidez o de diseño del
   producto?

## Fuentes

- Financial Stability Board (2023). *High-level Recommendations for Global Stablecoin Arrangements*. <https://www.fsb.org/2023/07/high-level-recommendations-for-the-regulation-supervision-and-oversight-of-global-stablecoin-arrangements-final-report/>
- Comité de Supervisión Bancaria de Basilea (2013). *Basel III: The Liquidity Coverage Ratio*. <https://www.bis.org/publ/bcbs238.htm>
- CPMI-IOSCO (2022). *Application of the PFMI to stablecoin arrangements*. <https://www.bis.org/cpmi/publ/d206.htm>
- Fondo Monetario Internacional. *Global Financial Stability Report*, capítulos sobre activos digitales. <https://www.imf.org/en/Publications/GFSR>
- Verificación local: caso sintético; cifras y curva supuestas. La admisibilidad de la suspensión del reembolso depende de la jurisdicción. **Fecha de verificación: 2026-08-12.** No constituye asesoría de inversión.
