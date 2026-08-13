# Caso · La remesa que costaba el 11 %

**Tema:** remesas · **Parte relacionada:** 18 · **Naturaleza:** caso sintético
compuesto · **Fecha de verificación:** 2026-08-12

Una persona envía 200 unidades a su familia cada mes. La comisión anunciada es de
4,99 y la receptora cobra el equivalente a 178. La diferencia entre esas dos
cifras —y no la comisión— es el objeto de este caso.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · importe enviado                200,00
  · comisión anunciada               4,99
  · tipo de cambio del operador  1 : 940
  · tipo de cambio de referencia
    del mercado ese día          1 : 985
  · importe recibido            183 300
    en moneda de destino
  · comisión de retiro en efectivo
    en el punto de pago              2 %

SUPUESTO DEL EJERCICIO
  · envíos al año                      12
  · el remitente compara operadores
    solo por la comisión anunciada
```

La aritmética completa:

```text
DESGLOSE REAL DEL COSTE

  comisión explícita              4,99
  diferencial de cambio
    195,01 × (985 − 940) / 985 =  8,91
  comisión de retiro
    183 300 × 2 % = 3 666
    ÷ 940 =                       3,90

  COSTE TOTAL                    17,80
  SOBRE 200 =                     8,9 %

  Y SI EL PUNTO DE PAGO ESTÁ A 40 KM
  añade transporte y tiempo:
  el coste efectivo supera el 11 %
```

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Remitente | Que llegue lo máximo posible | La comisión anunciada |
| Receptora | Cobrar cerca y sin esperar | El importe que le dan |
| Operador de envío | Margen por operación | Todo el desglose |
| Agente pagador | Comisión por retiro | Su propia tarifa |
| Banco corresponsal | Volumen | El corredor |
| Regulador del país receptor | Inclusión y transparencia | Datos agregados |

## Decisiones

```text
DEL REMITENTE
  elegir por comisión anunciada
  DECISIÓN RACIONAL CON LA INFORMACIÓN
  DISPONIBLE, Y EQUIVOCADA

DEL OPERADOR
  competir en la cifra visible y recuperar
  margen en la que no lo es
  DECISIÓN LEGAL EN MUCHOS MERCADOS
  Y ESTRUCTURALMENTE PROBLEMÁTICA

DE LA RECEPTORA
  retirar todo en efectivo
  RAZÓN: no tiene cuenta, o la cuenta
  cuesta más que el 2 %

DEL REGULADOR
  exigir publicación de comisión
  SIN EXIGIR PUBLICACIÓN DEL COSTE TOTAL
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Opacidad del coste total | Estructural | Sí |
| Diferencial de cambio no divulgado | Estructural | Sí |
| Coste de la última milla | Estructural | Sí |
| Exclusión financiera de la receptora | Previo | Sí |
| Desplazamiento a canales informales | A medio plazo | No en este caso |
| De-risking del corredor | Estructural | No |

## Regulación

```text
QUÉ ALCANZA

  TRANSPARENCIA
    varios regímenes exigen informar del
    importe que recibirá el beneficiario
    y del tipo aplicado, no solo de la
    comisión

  OBJETIVOS INTERNACIONALES
    existe un objetivo público global de
    reducción del coste medio de las
    remesas, y una serie estadística que
    lo sigue por corredor

  PROTECCIÓN DEL CONSUMIDOR
    la comparabilidad es un requisito
    típico: mostrar cifras no comparables
    entre sí puede constituir práctica
    engañosa

LÍMITE
  la exigencia concreta depende de la
  jurisdicción de envío y de la de destino
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Publicación de comisión | Sí | Sí, y no bastó | Importe final garantizado |
| Divulgación del tipo aplicado | Parcial | No | Comparación con referencia |
| Comparador independiente | No | — | Por corredor y por importe |
| Alternativa de abono en cuenta | No | — | Evita la comisión de retiro |
| Educación del remitente | No | — | Enseñar a comparar el recibido |
| Seguimiento del corredor | Parcial | No | Serie de coste total por corredor |

## Resultado

```text
COSTE ANUAL PARA ESTA FAMILIA

  17,80 × 12 =                 213,60
  sobre 2 400 enviados =         8,9 %

SI SE ELIGIERA POR IMPORTE RECIBIDO

  operador alternativo del ejercicio
    comisión anunciada           7,99
    tipo 1 : 972
    abono en cuenta, sin retiro
    coste total                 12,49
  AHORRO ANUAL                  63,72

  = 2,6 % del importe enviado

Y EL OPERADOR «CARO» POR COMISIÓN
ERA EL BARATO POR COSTE TOTAL.
```

## Lecciones

1. **La comisión anunciada no es el precio.** Compara siempre el importe que
   recibe la persona destinataria, que es el único número comparable.
2. **El diferencial de cambio es la partida mayor y la menos visible**, y por eso
   es donde se compite cuando la comisión es el único dato publicado.
3. **La última milla puede costar más que el envío.** Un abono en cuenta elimina
   la comisión de retiro, pero exige que la receptora tenga cuenta, y ese es un
   problema de inclusión, no de pagos.
4. **Publicar un dato no comparable es peor que no publicarlo**, porque produce
   decisiones equivocadas con apariencia de informadas.

## Preguntas

1. ¿Qué cifra única debería exigirse en la publicidad de una remesa, y por qué?
2. ¿Es el diferencial de cambio una comisión encubierta o una remuneración
   legítima del riesgo? ¿Cambia la respuesta según su tamaño?
3. ¿Qué haría falta para que la receptora pudiera cobrar en cuenta? ¿Quién paga
   esa cuenta?
4. Si un regulador fija un tope al coste total, ¿qué efectos secundarios
   esperarías en el corredor?
5. ¿Cómo diseñarías un comparador que no pudiera ser manipulado por los propios
   operadores?

## Fuentes

- Banco Mundial. *Remittance Prices Worldwide*. <https://remittanceprices.worldbank.org/>
- CPMI-Banco Mundial. *General Principles for International Remittance Services*. BIS. <https://www.bis.org/cpmi/publ/d76.htm>
- Naciones Unidas. *Objetivo de Desarrollo Sostenible 10.c sobre el coste de las remesas*. <https://sdgs.un.org/goals/goal10>
- Financial Stability Board. *G20 Roadmap for Enhancing Cross-border Payments*. <https://www.fsb.org/work-of-the-fsb/financial-innovation-and-structural-change/cross-border-payments/>
- Verificación local: caso sintético; cifras y tipos supuestos. Las obligaciones de transparencia dependen de la jurisdicción de envío y de destino. **Fecha de verificación: 2026-08-12.** No constituye asesoría financiera.
