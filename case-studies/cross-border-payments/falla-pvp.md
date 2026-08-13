# Caso · La pata que no llegó

**Tema:** pagos transfronterizos · **Parte relacionada:** 18 · **Naturaleza:**
caso sintético compuesto · **Fecha de verificación:** 2026-08-12

Dos bancos cierran una operación de cambio por 30 millones. Uno entrega su divisa
a las 09:15; el otro debía entregar la suya a las 15:00 de su propio huso, y no lo
hace. Entre esas dos horas hay seis horas y cuarenta y cinco minutos en las que un
banco tiene todo el riesgo y ninguna garantía. Es el riesgo Herstatt, y este caso
lo cuantifica.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · operación de cambio, valor mismo día
  · banco X entrega divisa A: 30 000 000
  · banco Y debe entregar divisa B:
    equivalente a 30 000 000
  · liquidación NO simultánea: cada pata
    por su propio sistema
  · X entrega a las 09:15 de su huso
  · Y no entrega: entra en resolución a
    las 13:00 de su huso

SUPUESTO DEL EJERCICIO
  · exposición de X                30 000 000
  · recuperación estimada en el
    procedimiento                        58 %
  · plazo estimado de recuperación   26 meses
```

Conviene ser preciso con lo que ocurrió: **no hubo un fallo de la operación de
cambio**. El precio era correcto, la confirmación era correcta y las
instrucciones eran correctas. Lo que faltó fue una condición: que ninguna pata se
entregara sin la otra.

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Banco X | Cerrar su posición de divisa | Que Y era contraparte habitual |
| Banco Y | Lo mismo | Su propia situación, que no comunicó |
| Mesa de X | Cumplir el mandato del cliente | El límite de contraparte, con holgura |
| Riesgo de crédito de X | Controlar la exposición | Exposición medida al cierre, no intradía |
| Autoridad de Y | Ordenar la resolución | La situación de Y |
| Cliente final de X | Su divisa | Nada |

## Decisiones

```text
D−1    la mesa cierra la operación
       LÍMITE DE CONTRAPARTE: consumido
       al 61 %, dentro de política

D 09:15 X entrega su pata
       DECISIÓN AUTOMÁTICA: así se opera
       siempre con esta contraparte

D 11:00 rumor de mercado sobre Y
       la mesa de X no puede hacer nada:
       ya entregó

D 13:00 Y entra en resolución

D 15:00 la pata de Y no llega

D+1    X reclama en el procedimiento
```

La decisión que decide el caso es la de las 09:15, y no la tomó nadie: la tomó un
proceso automático que llevaba años funcionando. **Los riesgos que se materializan
en operaciones rutinarias no tienen autor identificable, y por eso no tienen
control asociado.**

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Riesgo de liquidación (Herstatt) | Estructural | Sí |
| Exposición intradía no medida | Desde siempre | Sí |
| Límite de contraparte al cierre | Desde el diseño | Sí |
| Desfase de husos horarios | Estructural | Sí |
| Riesgo de reemplazo de la operación | Desde D+1 | Sí |
| Riesgo sistémico por contagio | Potencial | No en este caso |

## Regulación

```text
QUÉ ALCANZA

  PRINCIPIOS DE INFRAESTRUCTURAS
    los principios internacionales para
    infraestructuras del mercado financiero
    tratan de forma expresa el riesgo de
    liquidación y recomiendan mecanismos
    de pago contra pago

  SUPERVISIÓN PRUDENCIAL
    la exposición de liquidación se mide y
    consume capital; medirla solo al cierre
    subestima el riesgo real

  RECOMENDACIONES DE ORGANISMOS
    hay trabajo internacional sostenido
    sobre la reducción del riesgo de
    liquidación en operaciones de cambio

LÍMITE
  la exigencia concreta depende del marco
  prudencial y de la infraestructura
  disponible en cada divisa
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Pago contra pago | No | — | Liquidar ambas patas o ninguna |
| Límite de contraparte | Sí | Sí, mal calibrado | Medir exposición intradía |
| Neteo bilateral | No | — | Reduce el bruto expuesto |
| Escalonamiento de la entrega | No | — | Entregar por tramos, no todo |
| Vigilancia de señales de mercado | Parcial | No | Bloqueo automático ante alerta |
| Acuerdo marco con garantías | Parcial | No | Colateral para exposición intradía |

## Resultado

```text
PÉRDIDA (supuestos)

  exposición                  30 000 000
  recuperación 58 %           17 400 000
  PÉRDIDA BRUTA               12 600 000

  coste de reemplazo de la posición
    de cambio                    420 000
  coste financiero de 26 meses de
    espera sobre 17 400 000
    al 4 % anual                1 508 000

  PÉRDIDA ECONÓMICA TOTAL    ~14 528 000

COMPARACIÓN CON LIQUIDAR CON PVP
  coste anual del mecanismo
  (supuesto)                     380 000

  UN SOLO EPISODIO PAGA 38 AÑOS
  DEL MECANISMO
```

## Lecciones

1. **El riesgo de liquidación no es riesgo de mercado ni de crédito ordinario:**
   es la ausencia de simultaneidad, y solo se elimina condicionando una entrega a
   la otra.
2. **Medir la exposición al cierre esconde el riesgo entero**, porque el riesgo
   vive entre las 09:15 y las 15:00 y a las 23:59 ya no está.
3. **Las operaciones rutinarias no tienen autor y por eso no tienen control.**
   Conviene revisar periódicamente qué se ejecuta de forma automática y qué
   supuesto lo sostiene.
4. **El coste de un mecanismo de pago contra pago se compara con la pérdida de un
   episodio, no con la comisión de una operación.**

## Preguntas

1. ¿Por qué el límite de contraparte, consumido solo al 61 %, no evitó nada?
2. ¿Qué habría cambiado si X hubiera entregado en tres tramos a lo largo del día?
3. ¿Cuándo compensa un mecanismo de pago contra pago y cuándo no? ¿Qué divisas
   quedan fuera y qué se hace entonces?
4. ¿Debería la mesa haber podido bloquear la entrega a las 11:00 con solo un
   rumor? ¿Quién asume el coste si el rumor es falso?
5. ¿Qué diferencia hay entre este caso y una liquidación atómica sobre un registro
   compartido? ¿Qué problema resuelve y cuál no?

## Fuentes

- CPMI-IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- CPMI (2022). *Facilitating increased adoption of payment versus payment (PvP)*. BIS. <https://www.bis.org/cpmi/publ/d203.htm>
- Comité de Supervisión Bancaria de Basilea. *Supervisory guidance for managing risks associated with the settlement of foreign exchange transactions*. <https://www.bis.org/publ/bcbs241.htm>
- Financial Stability Board. *G20 Roadmap for Enhancing Cross-border Payments*. <https://www.fsb.org/work-of-the-fsb/financial-innovation-and-structural-change/cross-border-payments/>
- Verificación local: caso sintético; cifras supuestas. La disponibilidad de mecanismos de pago contra pago depende de la divisa y de la infraestructura. **Fecha de verificación: 2026-08-12.** No constituye asesoría legal.
