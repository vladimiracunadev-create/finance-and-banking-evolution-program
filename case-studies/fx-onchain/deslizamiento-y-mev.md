# Caso · Una orden de cambio y los tres que la vieron llegar

**Tema:** FX on-chain · **Parte relacionada:** 21 · **Naturaleza:** caso sintético
compuesto · **Fecha de verificación:** 2026-08-12

Una tesorería corporativa cambia 4 millones entre dos fichas estables usando un
creador de mercado automático. El precio de pantalla era 1,0002. El precio de
ejecución fue 1,0139. La diferencia no fue una comisión: fue el resultado de que
la orden se hizo pública antes de ejecutarse.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · importe                       4 000 000
  · pool con profundidad          9 400 000
  · precio antes de la orden         1,0002
  · precio de ejecución medio        1,0139
  · precio 3 bloques después         1,0011

DESCOMPOSICIÓN DEL COSTE
  impacto de precio propio
    (inevitable en ese pool)          0,84 %
  extracción por reordenación
    de la operación                   0,53 %
  comisión del pool                   0,05 %
  TOTAL                               1,42 %
                                   56 800

SUPUESTO DEL EJERCICIO
  · coste de la misma operación por
    solicitud de precio a tres
    proveedores: 0,11 %      →      4 400
```

Los dos primeros componentes son de naturaleza distinta y conviene no
confundirlos. **El impacto de precio es física del pool**: mover 4 millones en un
pool de 9,4 desplaza el precio y eso ocurriría igual sin nadie mirando. La
extracción por reordenación es otra cosa: alguien vio la orden pendiente, se puso
delante y detrás, y capturó la diferencia.

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Tesorería corporativa | Cambiar al precio de pantalla | El precio de pantalla |
| Pool de liquidez | Comisión por volumen | Su fórmula |
| Proveedores de liquidez | Rendimiento | Su posición |
| Extractor | Beneficio por reordenación | La orden pendiente, antes que nadie |
| Constructor de bloques | Comisión por ordenar | Todas las órdenes pendientes |
| Auditor interno, después | Explicar 56 800 | El extracto |

## Decisiones

```text
DE LA TESORERÍA
  ejecutar todo de una vez
  RAZÓN: simplicidad operativa
  EFECTO: el impacto crece más que
  proporcionalmente con el tamaño

DE LA TESORERÍA
  fijar tolerancia de deslizamiento en 2 %
  RAZÓN: «que no falle la operación»
  EFECTO: autoriza toda la extracción
  posible por debajo del 2 %

DE LA TESORERÍA
  enviar la orden al mempool público
  EFECTO: la orden es visible antes de
  ejecutarse

DEL EXTRACTOR
  comprar antes y vender después
  DECISIÓN RACIONAL Y, EN MUCHAS
  JURISDICCIONES, NO TIPIFICADA
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Impacto de precio por tamaño | Estructural | Sí |
| Extracción por reordenación | Estructural | Sí |
| Tolerancia de deslizamiento excesiva | Desde la configuración | Sí |
| Ausencia de comparación de canales | Desde el proceso | Sí |
| Riesgo de contraparte del pool | Estructural | No |
| Riesgo de que la operación falle | Latente | No |

## Regulación

```text
QUÉ ALCANZA

  MEJOR EJECUCIÓN
    donde existe el deber de mejor
    ejecución, elegir un canal sin comparar
    alternativas es una decisión que hay
    que poder justificar

  ABUSO DE MERCADO
    adelantarse a una orden conocida encaja
    en la descripción de conductas
    prohibidas en mercados regulados; su
    aplicación a estos entornos es
    desigual y está en discusión

  DEBER DE DILIGENCIA DEL TESORERO
    la política de tesorería debe fijar
    límites de deslizamiento y de tamaño
    por operación

LÍMITE
  la tipificación depende de la
  jurisdicción y del carácter del mercado
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Tolerancia de deslizamiento | Sí | Sí, mal calibrada | Ajustada al pool y al tamaño |
| Fraccionamiento de la orden | No | — | Trocear según profundidad |
| Comparación de canales | No | — | Solicitud de precio en paralelo |
| Envío por canal privado | No | — | Evita la visibilidad previa |
| Límite de tamaño sobre profundidad | No | — | Máximo 10 % del pool por operación |
| Registro de coste efectivo | No | — | Medir y comparar cada operación |

El quinto control es el más simple y el que más ahorra: **nunca mover más del 10 %
de la profundidad del pool en una sola operación.** Con 9,4 millones de
profundidad, eso son 940 000 por tramo, y el impacto habría bajado de 0,84 % a
cerca de 0,2 %.

## Resultado

```text
COMPARACIÓN DE CANALES (supuestos)

  CREADOR DE MERCADO AUTOMÁTICO,
  ORDEN ÚNICA
    coste 1,42 %          56 800

  MISMO CANAL, 5 TRAMOS,
  TOLERANCIA 0,3 %
    coste estimado 0,41 % 16 400

  SOLICITUD DE PRECIO A TRES
  PROVEEDORES
    coste 0,11 %           4 400

  AHORRO FRENTE A LO EJECUTADO
    troceando            40 400
    con solicitud de precio 52 400

Y NINGUNA DE LAS TRES OPCIONES
EXIGÍA TECNOLOGÍA NUEVA.
```

## Lecciones

1. **Precio de pantalla y precio de ejecución no son lo mismo** en un creador de
   mercado automático, y la diferencia crece con el tamaño relativo de la orden.
2. **La tolerancia de deslizamiento es un límite de pérdida, no un ajuste
   técnico.** Fijarla en 2 % autoriza a perder hasta el 2 %.
3. **Una orden visible antes de ejecutarse es una orden que otros pueden
   aprovechar**, y hay canales que evitan esa visibilidad.
4. **Comparar canales es parte del deber del tesorero**, y sin registro de coste
   efectivo nadie sabe si el canal elegido es el bueno.

## Preguntas

1. ¿Qué tolerancia de deslizamiento habrías fijado, y con qué criterio?
2. ¿Es la extracción por reordenación una conducta que deba prohibirse, cobrarse o
   simplemente evitarse por diseño?
3. ¿Cómo redactarías la política de tesorería para operaciones de este tipo?
4. ¿Qué información necesitarías para elegir entre solicitud de precio, libro de
   órdenes y creador de mercado automático?
5. ¿Quién responde de los 56 800: el tesorero, el proveedor del canal o nadie?

## Fuentes

- BIS (2023). *Annual Economic Report*, capítulo sobre el sistema monetario futuro. <https://www.bis.org/publ/arpdf/ar2023e3.htm>
- IOSCO (2023). *Policy Recommendations for Decentralized Finance*. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD754.pdf>
- Banco de Pagos Internacionales. *FX Global Code*. <https://www.globalfxc.org/fx_global_code.htm>
- Financial Stability Board (2023). *The Financial Stability Risks of Decentralised Finance*. <https://www.fsb.org/2023/02/the-financial-stability-risks-of-decentralised-finance/>
- Verificación local: caso sintético; cifras supuestas. La tipificación de la extracción por reordenación depende de la jurisdicción y del carácter del mercado. **Fecha de verificación: 2026-08-12.** No constituye asesoría de inversión.
