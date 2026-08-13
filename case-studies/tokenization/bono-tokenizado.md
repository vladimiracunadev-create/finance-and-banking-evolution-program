# Caso · Un bono tokenizado sin mercado secundario

**Tema:** tokenización · **Parte relacionada:** 21 · **Naturaleza:** caso
sintético compuesto · **Fecha de verificación:** 2026-08-12

Una emisión de 60 millones se coloca entera en once horas, liquida en el mismo
día y paga sus cupones de forma automática. Todo funciona. Y a los catorce meses,
cuando un inversor necesita vender, descubre que no hay a quién. El caso trata de
la diferencia entre emitir y crear un mercado.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · importe emitido           60 000 000
  · plazo                          5 años
  · cupón                          4,80 %
  · inversores en la colocación         23
  · liquidación entrega contra pago,
    en el día
  · pago de cupones automático, sin
    incidencias en 3 vencimientos
  · transferencias restringidas a una lista
    de inversores elegibles

SUPUESTO DEL EJERCICIO
  · operaciones en secundario a los 14 meses
                                        2
  · volumen negociado             1 400 000
  · descuento sobre valor razonable    6,2 %
```

Los ahorros de la emisión fueron reales: menos intermediarios, liquidación el
mismo día, cupones sin conciliación manual. **Lo que no se creó fue la otra mitad
del mercado**, y la iliquidez resultante costó más que todo lo ahorrado.

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Emisor | Financiarse más barato | El ahorro de la emisión |
| Inversor institucional | Rendimiento y poder salir | El folleto y la promesa de secundario |
| Agente de la lista de elegibles | Cumplir las restricciones | Los criterios |
| Creador de mercado potencial | Margen razonable | Un universo de 23 contrapartes |
| Custodio | Custodiar y conciliar | Su parte |
| Supervisor | Que el instrumento tenga régimen | El expediente |

## Decisiones

```text
DISEÑO
  restringir transferencias a inversores
  elegibles
  RAZÓN CORRECTA: cumplimiento y perímetro
  EFECTO NO EVALUADO: reduce el universo
  de compradores a 23

DISEÑO
  no contratar creador de mercado
  RAZÓN: coste
  «el secundario surgirá solo»

DISEÑO
  denominación mínima de 250 000
  EFECTO: excluye al inversor mediano,
  que es quien da profundidad

MES 14
  un inversor necesita vender 1 400 000
  encuentra un comprador de los 23
  y acepta un 6,2 % de descuento
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Universo de contrapartes reducido | Desde el diseño | Sí |
| Ausencia de creador de mercado | Desde el diseño | Sí |
| Denominación mínima excluyente | Desde el diseño | Sí |
| Valoración sin precio observable | Desde el mes 1 | Sí |
| Dependencia del agente de elegibilidad | Estructural | No |
| Riesgo de que el emisor recompre | Latente | No |

El cuarto merece atención porque afecta a todos los tenedores, no solo al que
vende: sin operaciones observables, **cada inversor valora el bono con un modelo
propio**, y esas valoraciones divergen justo cuando alguien necesita que
converjan.

## Regulación

```text
QUÉ ALCANZA

  RÉGIMEN DE VALORES
    un instrumento que da derecho a un
    flujo periódico es un valor; el
    soporte no lo cambia

  RESTRICCIONES DE TRANSFERENCIA
    son lícitas y a menudo necesarias;
    su efecto sobre la liquidez es una
    consecuencia de diseño, no un defecto
    jurídico

  INFORMACIÓN AL INVERSOR
    la ausencia de mercado secundario es
    un riesgo material y debe declararse
    de forma destacada

LÍMITE
  el régimen concreto depende de la
  jurisdicción y del tipo de oferta
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Lista de inversores elegibles | Sí | Sí | Ampliarla activamente |
| Advertencia de iliquidez | Parcial | No | Destacada y cuantificada |
| Creador de mercado | No | — | Contratado, con obligaciones |
| Ventana periódica de casación | No | — | Subasta mensual con todos |
| Metodología de valoración común | No | — | Publicada por el agente de cálculo |
| Denominación accesible | No | — | Fraccionamiento hasta un mínimo bajo |

La ventana periódica de casación es la solución más barata y la que casi nunca se
diseña: una subasta mensual entre los veintitrés concentra la oferta y la demanda
en un momento y produce un precio observable, que es exactamente lo que faltaba.

## Resultado

```text
BALANCE A LOS 14 MESES (supuestos)

  AHORRO DE LA EMISIÓN
    intermediación evitada     420 000
    liquidación y conciliación 180 000
    TOTAL                      600 000

  COSTE DE LA ILIQUIDEZ
    descuento en la venta
      1 400 000 × 6,2 % =       86 800
    prima de iliquidez exigida por
      los inversores en la emisión,
      estimada en 35 pb sobre 60 M
      y 5 años                1 050 000

    TOTAL                    1 136 800

  RESULTADO NETO            −536 800

EL AHORRO DE LA EMISIÓN LO PAGÓ
EL EMISOR EN EL CUPÓN.
```

## Lecciones

1. **Emitir es la mitad del trabajo.** Un instrumento sin mercado secundario se
   financia más caro, y la prima de iliquidez la paga el emisor durante toda la
   vida del bono.
2. **Las restricciones de transferencia tienen un coste medible**, y ese coste
   debe compararse con el riesgo que evitan, no darse por supuesto.
3. **Sin precio observable no hay valoración común**, y sin valoración común no
   hay contrapartes dispuestas.
4. **Una subasta periódica crea mercado con muy poca infraestructura**, y produce
   el dato que todos necesitan.

## Preguntas

1. ¿Cómo cuantificarías la prima de iliquidez antes de emitir?
2. ¿Qué obligaciones exigirías a un creador de mercado en una emisión de 60
   millones con 23 inversores?
3. ¿Se puede ampliar la lista de elegibles sin relajar el cumplimiento? ¿Cómo?
4. ¿Qué frecuencia tendría la ventana de casación, y cómo se fija el precio en
   ella?
5. ¿Habría sido mejor no tokenizar? ¿Qué habría cambiado y qué no?

## Fuentes

- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- BIS (2023). *Annual Economic Report*, capítulo sobre tokenización. <https://www.bis.org/publ/arpdf/ar2023e3.htm>
- Diario Oficial de la Unión Europea (2022). *Reglamento (UE) 2022/858, régimen piloto DLT*. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32022R0858>
- CMF. *Normativa sobre oferta pública de valores y sistemas alternativos de transacción*. <https://www.cmfchile.cl/>
- Verificación local: caso sintético; cifras supuestas. El régimen aplicable a un valor tokenizado depende de la jurisdicción. **Fecha de verificación: 2026-08-12.** No constituye asesoría de inversión.
