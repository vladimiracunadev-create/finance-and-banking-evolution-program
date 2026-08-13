# Caso · Migrar el formato sin migrar el dato

**Tema:** ISO 20022 · **Parte relacionada:** 18 · **Naturaleza:** caso sintético
compuesto · **Fecha de verificación:** 2026-08-12

Un banco completa su migración a mensajería estructurada en plazo y sin
incidencias técnicas. Seis meses después, su tasa de procesamiento automático es
peor que antes de migrar. El proyecto fue un éxito y el resultado un retroceso, y
la razón está en un solo campo.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · migración completada en plazo
  · mensajes válidos contra el esquema:
    100 %
  · tasa de procesamiento automático
      antes de migrar            88,4 %
      seis meses después         81,7 %

CAUSA IDENTIFICADA
  · el sistema de origen guardaba nombre y
    dirección del beneficiario en un solo
    campo de texto de 140 caracteres
  · la migración lo volcó íntegro en el
    campo de nombre del nuevo formato
  · el mensaje es válido: el campo admite
    texto
  · pero el cribado, el enrutamiento y la
    conciliación esperaban un nombre

SUPUESTO DEL EJERCICIO
  · pagos mensuales             340 000
  · coste de una reparación manual  9,80
```

**Un mensaje válido no es un mensaje útil.** El esquema comprueba la forma; el
proceso de destino necesita el significado, y entre esas dos cosas cabe un
proyecto entero.

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Equipo de migración | Cumplir el plazo y el esquema | Los criterios de aceptación firmados |
| Operaciones | Menos reparaciones manuales | Solo después de migrar |
| Cumplimiento | Cribar bien | Nombres con dirección dentro |
| Bancos corresponsales | Recibir datos utilizables | Mensajes válidos y sucios |
| Clientes corporativos | Conciliación automática | Extractos peores que antes |
| Patrocinador del proyecto | Cerrar en plazo | Un tablero en verde |

## Decisiones

```text
FASE DE DISEÑO
  criterio de aceptación:
  «100 % de mensajes válidos contra el
   esquema»
  DECISIÓN QUE DEFINE EL FRACASO
  seis meses antes de que ocurra

FASE DE PRUEBAS
  se prueba validez, no utilidad
  no se mide tasa de procesamiento
  automático en el entorno de pruebas

DECISIÓN DESCARTADA
  limpiar los datos de origen antes de
  migrar
  RAZÓN: añadía cuatro meses
  COSTE ESTIMADO ENTONCES     380 000

PUESTA EN PRODUCCIÓN
  éxito declarado
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Criterio de aceptación por forma | Desde el diseño | Sí |
| Datos de origen no estructurados | Previo | Sí |
| Falsos positivos de cribado | Desde el día 1 | Sí |
| Conciliación degradada del cliente | Desde el día 1 | Sí |
| Coste de reparación manual | Desde el día 1 | Sí |
| Pérdida de confianza del corresponsal | A medio plazo | Parcialmente |

## Regulación

```text
QUÉ ALCANZA

  CALIDAD DE DATOS EN PAGOS
    la regla del viaje exige información
    del ordenante y del beneficiario; si
    va mezclada en un campo libre, puede
    considerarse incompleta

  MIGRACIÓN A MENSAJERÍA ESTRUCTURADA
    los calendarios de migración de las
    infraestructuras suelen exigir datos
    estructurados, no solo formato válido

  CONDUCTA CON EL CLIENTE
    degradar un servicio existente tras
    un cambio técnico tiene consecuencias
    contractuales

LÍMITE
  el calendario y las exigencias concretas
  dependen de la infraestructura y de la
  jurisdicción
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Validación contra esquema | Sí | Sí, y no bastó | Validación semántica |
| Criterio de aceptación | Sí | Sí, mal formulado | Tasa de procesamiento como criterio |
| Perfilado de datos de origen | No | — | Medir qué hay antes de mover |
| Pruebas con volumen real | Parcial | No | Con datos productivos anonimizados |
| Métrica posterior a la migración | No | — | Panel desde el día 1 |
| Plan de limpieza de datos | Descartado | — | Por fases, no todo o nada |

## Resultado

```text
COSTE DE LOS SEIS MESES (supuestos)

  caída de procesamiento automático
    88,4 % → 81,7 % = 6,7 puntos
  pagos afectados al mes
    340 000 × 6,7 % = 22 780
  coste mensual
    22 780 × 9,80 = 223 244
  SEIS MESES                 1 339 464

  proyecto de limpieza posterior
    (el que costaba 380 000 antes)
    ahora, con sistemas migrados
                               620 000

  TOTAL                      1 959 464
  FRENTE A 380 000 SI SE HUBIERA
  HECHO ANTES
```

## Lecciones

1. **El criterio de aceptación define el resultado.** «Mensajes válidos» produce
   mensajes válidos; «tasa de procesamiento automático igual o mejor» produce una
   migración útil.
2. **Migrar el formato no migra el dato.** Un campo libre volcado en un campo
   estructurado sigue siendo un campo libre con otro nombre.
3. **Limpiar antes es más barato que limpiar después**, y la diferencia crece con
   el número de sistemas que ya consumen el dato sucio.
4. **Una migración se mide en producción, no en pruebas**, y por eso el panel de
   métricas debe existir desde el primer día.

## Preguntas

1. ¿Cómo redactarías el criterio de aceptación de esta migración?
2. ¿Qué habrías medido en el perfilado de datos de origen, y con qué umbral
   habrías parado el proyecto?
3. ¿Es razonable que un mensaje con nombre y dirección mezclados pase la
   validación? ¿Debería el esquema impedirlo?
4. ¿Quién debía haber detectado el problema: el equipo técnico, operaciones o
   cumplimiento?
5. ¿Cómo se recupera la confianza de un corresponsal que ha recibido seis meses de
   datos degradados?

## Fuentes

- ISO 20022. *Message definitions and implementation guidelines*. <https://www.iso20022.org/>
- CPMI (2020). *Enhancing cross-border payments: building blocks of a global roadmap* (bloque sobre formatos de datos). BIS. <https://www.bis.org/cpmi/publ/d193.htm>
- GAFI. *Recomendación 16 e información del ordenante y del beneficiario*. FATF. <https://www.fatf-gafi.org/>
- Financial Stability Board. *G20 Roadmap for Enhancing Cross-border Payments*. <https://www.fsb.org/work-of-the-fsb/financial-innovation-and-structural-change/cross-border-payments/>
- Verificación local: caso sintético; cifras supuestas. Los calendarios y exigencias de migración dependen de cada infraestructura. **Fecha de verificación: 2026-08-12.** No constituye asesoría legal.
