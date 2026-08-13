# Caso · Un consentimiento que no consentía

**Tema:** finanzas abiertas · **Parte relacionada:** 17 · **Naturaleza:** caso
sintético compuesto · **Fecha de verificación:** 2026-08-12

Un agregador financiero descubre, tras once meses de operación, que el
consentimiento con el que accedía a los datos de 84 000 clientes no cubría dos de
los tres usos que les estaba dando. Ninguna norma se incumplió el día del acceso:
se incumplió el día en que alguien decidió reutilizar los datos para otra cosa.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · el agregador obtuvo consentimiento para
    «consultar saldos y movimientos con el
    fin de mostrar una posición consolidada»
  · el consentimiento se otorgó por 12 meses
  · 84 000 clientes lo otorgaron
  · el agregador usó los datos para tres
    cosas: la posición consolidada, un
    modelo de scoring propio, y un informe
    agregado que vendía a terceros

SUPUESTO DEL EJERCICIO
  · ingreso anual por los tres usos:
      posición consolidada     0 (gratuito)
      scoring propio     1 900 000
      informe a terceros   740 000

INTERPRETACIÓN
  el producto gratuito era el que tenía
  consentimiento; los dos que generaban
  ingreso, no
```

La secuencia importa. El consentimiento se redactó cuando el único producto era
la posición consolidada, y era correcto entonces. Los otros dos usos aparecieron
después, se apoyaron en el mismo dato ya disponible, y nadie volvió a mirar el
texto que autorizaba el acceso. Es el modo habitual en que esto ocurre: no hay
una decisión de incumplir, hay una ausencia de decisión.

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Cliente | Ver todas sus cuentas en un sitio | El texto que aceptó, que no leyó |
| Agregador — producto | Lanzar productos con el dato disponible | Que el dato ya estaba |
| Agregador — cumplimiento | Que el consentimiento cubra el acceso | Lo revisó una vez, en el diseño |
| Banco proveedor de datos | Cumplir su obligación de entregar | Un consentimiento válido en forma |
| Comprador del informe | Datos agregados de mercado | Que venían «anonimizados» |
| Supervisor | Que la finalidad se respete | Nada, hasta la denuncia |

El banco proveedor merece una nota. Entregó los datos correctamente: recibió un
consentimiento formalmente válido y cumplió. Y aun así aparecerá en el expediente,
porque la pregunta que se le hará no es si entregó bien, sino si podía saber para
qué se usaban los datos que entregaba. La respuesta honesta —no podía— es
también la descripción de un problema estructural del modelo.

## Decisiones

```text
MES 0   se redacta el consentimiento para
        un solo uso
        DECISIÓN CORRECTA CON LA INFORMACIÓN
        DE ENTONCES

MES 4   producto propone el scoring
        «los datos ya los tenemos»
        NADIE PREGUNTA SI EL CONSENTIMIENTO
        LO CUBRE

MES 7   se lanza el informe a terceros
        cumplimiento pregunta si hay dato
        personal; le responden que va
        agregado
        LA PREGUNTA CORRECTA ERA OTRA:
        no si el dato de salida es personal,
        sino si la finalidad de entrada lo
        permitía

MES 11  un cliente pide el detalle de sus
        consentimientos y no reconoce dos
        de los usos
        SE ABRE LA REVISIÓN
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Finalidad excedida | Desde el mes 4 | Sí |
| Consentimiento no granular | Desde el diseño | Sí |
| Reidentificación del agregado | Desde el mes 7 | No comprobado |
| Ausencia de panel de consentimientos | Desde el mes 0 | Sí |
| Dependencia del agregador | Estructural | No |
| Responsabilidad del proveedor de datos | Desde el mes 0 | Parcialmente |

El tercero es el que más discusión genera en clase. Un informe agregado a partir
de 84 000 clientes puede ser irreversible o no serlo según el tamaño de las
celdas y el número de variables cruzadas, y en este caso nadie lo comprobó. Que
no se demostrara la reidentificación no significa que fuera imposible: significa
que no se midió.

## Regulación

```text
QUÉ ALCANZA CADA TRAMO

  ACCESO AL DATO
    régimen de finanzas abiertas y de
    protección de datos: el consentimiento
    debe ser informado, específico y
    revocable

  USO POSTERIOR
    principio de finalidad: el uso debe
    ser compatible con aquel para el que
    se recogió

  CESIÓN A TERCEROS
    exige base propia; que el dato salga
    agregado no elimina la pregunta sobre
    la licitud de la entrada

LÍMITE DE ESTE BLOQUE
  el régimen concreto depende de la
  jurisdicción y de la fecha; este caso
  enseña el mecanismo, no la norma
  aplicable a tu entidad
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Revisión legal en el diseño | Sí | Sí | Que se repitiera con cada uso nuevo |
| Registro de finalidades por uso | No | — | Un inventario vivo, no un documento |
| Panel de consentimientos del cliente | No | — | Visibilidad y revocación granular |
| Prueba de reidentificación | No | — | Umbral de celda y variables cruzadas |
| Aprobación de nuevos usos del dato | No | — | Puerta obligatoria antes del lanzamiento |
| Auditoría de accesos por finalidad | Parcial | No | Trazar el uso, no solo el acceso |

El control que habría evitado todo es el quinto y cuesta poco: ningún producto
nuevo puede usar un dato ya disponible sin declarar bajo qué finalidad se recogió.
Es una casilla en el proceso de lanzamiento, no un departamento.

## Resultado

```text
LO QUE OCURRIÓ

  · se suspenden los dos usos no cubiertos
  · se rehace el consentimiento con tres
    casillas separadas
  · se pide de nuevo a los 84 000 clientes

  RESULTADO DE LA RESOLICITUD (supuesto)
    aceptan la posición consolidada   91 %
    aceptan el scoring                38 %
    aceptan el informe a terceros     12 %

  INGRESO ANUAL RECONSTRUIDO
    scoring    1 900 000 × 0,38 =   722 000
    informe      740 000 × 0,12 =    88 800
    TOTAL                            810 800
    frente a 2 640 000 anteriores

  PÉRDIDA DE INGRESO             1 829 200
  COSTE DE LA REMEDIACIÓN          310 000
```

La cifra que hay que discutir no es la pérdida: es la diferencia entre el 38 % y
el 12 %. El consentimiento granular no destruyó el negocio, lo redimensionó a lo
que los clientes realmente autorizaban. **El ingreso previo no era ingreso: era
una deuda con vencimiento indeterminado.**

## Lecciones

1. **El consentimiento envejece con el producto, no con el calendario.** Un
   consentimiento de doce meses sigue siendo válido durante doce meses para el uso
   que describe, y deja de serlo el día en que aparece un uso nuevo.
2. **La pregunta correcta es sobre la entrada, no sobre la salida.** Que el
   resultado sea agregado no legitima la finalidad del dato de origen.
3. **Un panel de consentimientos es un control, no una función de producto.** Es
   lo que convierte la revocación en real y lo que permite detectar el desajuste
   antes de que lo detecte un cliente.
4. **El proveedor de datos también aparece en el expediente**, aunque haya
   cumplido, y eso condiciona a quién abre sus interfaces y con qué exigencias.

## Preguntas

1. ¿En qué momento exacto se produjo el incumplimiento, y quién estaba en
   posición de detectarlo?
2. ¿Habría cambiado algo si el informe a terceros se hubiera vendido de forma
   verdaderamente irreversible? ¿Y cómo se demuestra esa irreversibilidad?
3. ¿Qué obligación, si alguna, tiene el banco proveedor de datos sobre el uso
   posterior que hace el agregador?
4. Si el 12 % de aceptación del informe hace inviable ese producto, ¿es un fallo
   del producto o una señal de mercado?
5. ¿Qué habrías puesto en el proceso de lanzamiento para que el mes 4 hubiera
   salido distinto, sin frenar el desarrollo?

## Fuentes

- Ley N.º 21.521 de Chile y normativa de la CMF sobre el Sistema de Finanzas Abiertas. <https://www.bcn.cl/leychile>
- OpenID Foundation. *Financial-grade API (FAPI) security profiles*. <https://openid.net/wg/fapi/>
- IETF. *RFC 6749, The OAuth 2.0 Authorization Framework*. <https://www.rfc-editor.org/rfc/rfc6749>
- OCDE. *Recommendation of the Council concerning Guidelines Governing the Protection of Privacy and Transborder Flows of Personal Data*. <https://legalinstruments.oecd.org/>
- Verificación local: caso sintético; las cifras son supuestos del ejercicio. El régimen de consentimiento y de finalidad depende de la jurisdicción y cambia. **Fecha de verificación: 2026-08-12.** No constituye asesoría legal.
