# Caso · Los datos que viajaron a ninguna parte

**Tema:** regulación de mercados · **Parte relacionada:** 22 · **Naturaleza:**
caso sintético compuesto · **Fecha de verificación:** 2026-08-12

Un proveedor de servicios cumple la regla del viaje: envía los datos del ordenante
con cada transferencia. Una inspección encuentra que el 44 % de esos envíos fue a
destinatarios que no podían recibirlos, y que nadie comprobó nunca si llegaban.
Cumplir el procedimiento no es cumplir la obligación.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · transferencias salientes al mes  61 000
  · con datos del ordenante enviados 61 000  (100 %)
  · destinatarios que confirmaron
    recepción                        34 160  (56 %)
  · sin confirmación                 26 840  (44 %)

DESGLOSE DEL 44 %
  · destinatario con protocolo distinto
    e incompatible                   14 900
  · destinatario no identificado como
    proveedor                         7 200
  · dirección autoalojada             4 740

Y EN LOS TRES CASOS
  la transferencia se ejecutó igual

SUPUESTO DEL EJERCICIO
  · importe medio                     2 100
  · valor mensual sin trazabilidad
    de destino              56 364 000
```

**El indicador que la entidad publicaba era el de envío, no el de recepción**, y
esos dos números difieren en cuarenta y cuatro puntos. Medir lo que se hace en
lugar de lo que se consigue es el patrón de fondo de este caso.

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Proveedor emisor | Cumplir la obligación | Su tasa de envío |
| Cliente | Que su transferencia salga | Nada de esto |
| Proveedor receptor | Recibir lo que pueda procesar | Su propio protocolo |
| Proveedor de la solución técnica | Vender interoperabilidad | La cobertura real de su red |
| Inspector | Que la información llegue | Los dos indicadores |
| Unidad de análisis financiero | Trazabilidad | Reportes agregados |

## Decisiones

```text
DISEÑO DEL PROGRAMA
  indicador: «% de transferencias con
  datos enviados»
  DECISIÓN QUE DEFINE EL FALLO

CONTRATACIÓN
  se elige una solución de mensajería
  con cobertura declarada del 70 %
  del mercado
  NO SE COMPRUEBA LA COBERTURA EFECTIVA
  DE LOS DESTINATARIOS PROPIOS

POLÍTICA DE EJECUCIÓN
  ejecutar aunque el destinatario no
  confirme
  RAZÓN COMERCIAL: no frenar al cliente
  DECISIÓN NO DOCUMENTADA NI APROBADA

DIRECCIONES AUTOALOJADAS
  no se aplica ninguna medida específica
  RAZÓN: «no hay proveedor al otro lado»
  CONCLUSIÓN INCORRECTA: la ausencia de
  proveedor no elimina la obligación,
  la cambia
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Indicador que mide el envío | Desde el diseño | Sí |
| Incompatibilidad de protocolos | Estructural | Sí |
| Ejecución sin contraparte identificada | Desde la política | Sí |
| Direcciones autoalojadas sin medida | Desde el diseño | Sí |
| Trazabilidad rota en la cadena | Estructural | Sí |
| Sanción y requerimiento | Latente | Sí |

## Regulación

```text
QUÉ ALCANZA

  REGLA DEL VIAJE
    la obligación es que la información
    acompañe a la transferencia y esté
    disponible para el proveedor receptor;
    enviarla a un destino que no puede
    recibirla no la cumple

  DIRECCIONES AUTOALOJADAS
    varios regímenes exigen medidas
    reforzadas —verificación del control de
    la dirección, umbrales— en lugar de
    exención

  POLÍTICA ANTE INFORMACIÓN INCOMPLETA
    los regímenes suelen exigir una
    política escrita sobre si se ejecuta,
    se retiene o se rechaza

LÍMITE
  el umbral, la exigencia sobre
  autoalojadas y el régimen sancionador
  dependen de la jurisdicción y de la fecha
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Envío de datos | Sí | Sí | No es el objetivo |
| Confirmación de recepción | No | — | Indicador y umbral |
| Mapa de cobertura de contrapartes | No | — | Por volumen, no por número |
| Política de información incompleta | No | — | Escrita, aprobada y aplicada |
| Medidas para autoalojadas | No | — | Verificación de control |
| Revisión periódica del programa | Parcial | No | Con métrica de resultado |

El tercero es el control que convierte el problema en manejable: **la cobertura no
se mide por número de contrapartes sino por volumen.** Cubrir el 70 % de los
proveedores puede significar cubrir el 30 % del valor, y ese es el dato que
importa.

## Resultado

```text
RESULTADO DE LA INSPECCIÓN

  requerimiento de remediación en 6 meses
  · alcanzar 90 % de confirmación por
    volumen
  · política escrita de información
    incompleta
  · medidas específicas para autoalojadas

COSTE DE LA REMEDIACIÓN (supuestos)
  segunda solución de mensajería  340 000
  desarrollo de verificación de
    control de direcciones        210 000
  revisión de 6 meses de operativa
    pasada                        180 000
  TOTAL                           730 000

EFECTO COMERCIAL
  transferencias que pasan a requerir
  verificación                     4 740/mes
  fricción adicional para el cliente
  y caída estimada del 9 % en ese segmento
```

## Lecciones

1. **Medir el envío no mide el cumplimiento.** El indicador debe ser la
   disponibilidad de la información para quien debe tenerla.
2. **La cobertura se mide por volumen.** Un porcentaje de contrapartes no dice
   nada sobre el valor cubierto.
3. **La ausencia de proveedor al otro lado no elimina la obligación**, la
   transforma en una medida distinta.
4. **Ejecutar pese a información incompleta es una decisión de política** y debe
   estar escrita, aprobada y ser defendible; tomarla por defecto comercial no lo
   es.

## Preguntas

1. ¿Qué indicador propondrías, y con qué umbral de aceptación?
2. ¿Cómo se verifica que un cliente controla una dirección autoalojada, y qué
   fricción añade?
3. ¿Debe ejecutarse una transferencia cuando el destinatario no puede recibir los
   datos? Justifica la respuesta en ambos sentidos.
4. ¿Qué haces con los seis meses de operativa pasada?
5. ¿Cómo se resuelve la incompatibilidad de protocolos sin duplicar proveedores?

## Fuentes

- GAFI. *Recomendación 16 y actualizaciones sobre activos virtuales*. FATF. <https://www.fatf-gafi.org/en/topics/virtual-assets.html>
- Diario Oficial de la Unión Europea (2023). *Reglamento (UE) 2023/1113*. EUR-Lex. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32023R1113>
- Unidad de Análisis Financiero de Chile. *Normativa sobre sujetos obligados*. <https://www.uaf.cl/>
- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- Verificación local: caso sintético; cifras supuestas. Los umbrales y el tratamiento de las direcciones autoalojadas dependen de la jurisdicción y de la fecha. **Fecha de verificación: 2026-08-12.** No constituye asesoría legal.
