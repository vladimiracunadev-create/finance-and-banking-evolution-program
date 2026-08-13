# Caso · El contrato que hacía exactamente lo que decía

**Tema:** blockchain y DLT · **Parte relacionada:** 19 · **Naturaleza:** caso
sintético compuesto · **Fecha de verificación:** 2026-08-12

Un contrato de depósito en garantía libera 2,3 millones a la parte equivocada.
El código no tiene errores: implementa fielmente una especificación que estaba mal
escrita. El caso trata de la distancia entre lo que se quiso decir y lo que se
dijo, y de por qué en este entorno esa distancia no se corrige después.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · contrato de depósito en garantía para
    una compraventa de mercancía
  · condición de liberación al vendedor:
    «confirmación de entrega antes de la
     fecha límite»
  · la confirmación la aporta un tercero
    logístico mediante una llamada firmada
  · el logístico confirmó la entrega en el
    almacén del transportista, no en el
    del comprador
  · el contrato liberó los fondos

SUPUESTO DEL EJERCICIO
  · importe                     2 300 000
  · mercancía nunca recibida por el
    comprador
  · coste del litigio posterior    180 000
  · duración estimada del litigio  22 meses
```

La especificación decía «entrega». El código preguntaba al logístico si había
entrega. El logístico respondió con su propia definición de entrega. **Las tres
piezas eran correctas y el resultado fue incorrecto**, porque nadie definió el
término en un sitio donde las tres lo miraran.

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Comprador | Recibir la mercancía o su dinero | La cláusula, en lenguaje natural |
| Vendedor | Cobrar al entregar | La misma cláusula |
| Operador logístico | Registrar sus hitos | Su definición de entrega |
| Desarrollador del contrato | Implementar la especificación | La especificación |
| Auditor del código | Que el código haga lo especificado | El código y la especificación |
| Tribunal, después | Determinar la voluntad de las partes | Todo lo anterior, tarde |

## Decisiones

```text
NEGOCIACIÓN
  se pacta «entrega» sin definirla
  DECISIÓN HABITUAL EN CONTRATOS
  EN PAPEL, donde se resuelve después

IMPLEMENTACIÓN
  se elige el hito del logístico que se
  llama «delivered»
  DECISIÓN TÉCNICA CON CONSECUENCIA
  JURÍDICA, tomada por quien no la
  advierte

AUDITORÍA
  el código coincide con la especificación
  DICTAMEN CORRECTO

EJECUCIÓN
  el contrato libera
  NO HAY QUIEN LO PARE: no se previó
  ninguna facultad de suspensión
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Término no definido | Desde la negociación | Sí |
| Fuente de verdad con definición propia | Desde la implementación | Sí |
| Ausencia de facultad de suspensión | Desde el diseño | Sí |
| Irreversibilidad de la liberación | Estructural | Sí |
| Auditoría limitada a la coincidencia | Desde el alcance | Sí |
| Divergencia entre contrato y código | Estructural | Sí |

## Regulación

```text
QUÉ ALCANZA

  DERECHO DE CONTRATOS
    la voluntad de las partes prevalece;
    el código es un medio de ejecución,
    no la fuente de la obligación

  VALIDEZ DE LA EJECUCIÓN AUTOMÁTICA
    que el contrato se ejecute no impide
    que un tribunal declare que la
    liberación fue indebida; lo que impide
    es recuperar el dinero con facilidad

  RESPONSABILIDAD DEL TERCERO
    la fuente de datos puede responder si
    su información se usó para un efecto
    que conocía

LÍMITE
  el tratamiento varía por jurisdicción y
  depende del contrato marco entre las
  partes
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Especificación escrita | Sí | Sí, ambigua | Glosario de términos operativos |
| Auditoría de código | Sí | Sí, en su alcance | Verificar semántica de la fuente |
| Facultad de suspensión | No | — | Ventana de impugnación antes de liberar |
| Segunda fuente de confirmación | No | — | Dos hitos concordantes |
| Prueba con casos límite | Parcial | No | Entrega parcial, a tercero, tardía |
| Contrato marco que prevalece | Parcial | No | Qué manda si código y contrato difieren |

El tercero es el que convierte este caso en evitable: una ventana de setenta y dos
horas entre la condición y la liberación, con facultad de impugnar, no elimina la
automatización y sí elimina la irreversibilidad del error.

## Resultado

```text
SITUACIÓN

  fondos liberados             2 300 000
  mercancía no recibida
  litigio en curso                22 meses
  coste del litigio               180 000
  probabilidad de recuperación
    (supuesta)                        65 %

  VALOR ESPERADO DE LA RECUPERACIÓN
    2 300 000 × 0,65 = 1 495 000
    menos 180 000 de coste
    menos coste financiero de 22 meses
    ≈ 1 200 000

  PÉRDIDA ESPERADA           ~1 100 000

Y LO QUE EL CONTRATO PROMETÍA ERA
EXACTAMENTE EVITAR ESTE LITIGIO.
```

## Lecciones

1. **Automatizar una ambigüedad la convierte en un resultado.** En papel, un
   término indefinido se discute; en código, se ejecuta.
2. **La fuente de datos trae su propia definición**, y esa definición pasa a ser
   la del contrato aunque nadie lo haya querido.
3. **Una ventana de impugnación no destruye la automatización.** Es la diferencia
   entre un error corregible y una pérdida.
4. **El contrato manda sobre el código**, y conviene escribirlo así de forma
   expresa, porque la ejecución automática no cambia quién tiene razón, solo quién
   tiene el dinero.

## Preguntas

1. ¿Cómo habrías definido «entrega» para que las tres partes leyeran lo mismo?
2. ¿Qué duración tendría la ventana de impugnación, y quién puede accionarla?
3. ¿Responde el operador logístico? ¿Qué habría que probar?
4. ¿Qué casos límite habrías incluido en las pruebas? Enumera cinco.
5. Si el contrato marco dice una cosa y el código hace otra, ¿qué prevalece, y qué
   pasa con el dinero mientras se decide?

## Fuentes

- UNIDROIT. *Principles on Digital Assets and Private Law*. <https://www.unidroit.org/work-in-progress/digital-assets-and-private-law/>
- IOSCO (2023). *Policy Recommendations for Decentralized Finance*. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD754.pdf>
- NIST. *Blockchain Technology Overview (NISTIR 8202)*. <https://csrc.nist.gov/publications/detail/nistir/8202/final>
- CNUDMI. *Ley Modelo sobre Comercio Electrónico y textos sobre documentos transmisibles electrónicos*. <https://uncitral.un.org/es>
- Verificación local: caso sintético; cifras supuestas. El tratamiento jurídico de la ejecución automática depende de la jurisdicción y del contrato marco. **Fecha de verificación: 2026-08-12.** No constituye asesoría legal.
