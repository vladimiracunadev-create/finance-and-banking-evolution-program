# Solución de referencia — Laboratorio 5: programa de cumplimiento

> Material docente.

## Prohibir parecía más barato y solo desplazaba la actividad

El 32 % de destinos no identificables no era un fallo del programa: es una consecuencia estructural de que el registro no transporta la identidad. Lo que define la calidad del programa no es llevar ese resto a cero —no se puede— sino cómo lo gestiona.

## El resto es estructural

```text
transferencias salientes            28 400
a destinos no identificables         9 100  (32,0 %)
importe                         29 120 000
```

Antes de transferir hay que determinar si la dirección de destino pertenece a un sujeto obligado, y el registro no lo dice. Ninguna lista compartida ni protocolo de descubrimiento es completo, y el resto siempre existe.

## La comparación que engaña

```text
prohibir     pérdida   72 800 al mes
por tramos   coste    103 400 al mes

  → PROHIBIR PARECE MÁS BARATO
```

Y es la conclusión equivocada. No cuenta el riesgo de que el cliente se vaya a un proveedor sin controles, ni la pérdida del cliente completo, ni el valor de la información que el tramo intermedio genera.

## El tratamiento por tramos

```text
hasta 1 000       declaración del cliente
1 000 – 15 000    declaración + análisis de
                  procedencia del destino
más de 15 000     medidas reforzadas y aprobación
```

Los umbrales derivan del análisis de riesgo escrito, no al revés. Un enfoque basado en riesgo sin ese análisis no es un enfoque: es una elección de umbrales que no se puede justificar ante nadie.

## Los datos personales y el registro

```text
QUÉ VA AL REGISTRO
  identificador sin significado, importe,
  momento, referencia

QUÉ NO VA NUNCA
  nombre, documento, domicilio,
  concepto libre escrito por el cliente
```

La pregunta que hay que responder antes de escribir el primer dato es «si mañana alguien pide que lo borremos, ¿qué le contestamos?». Cuesta una reunión antes de empezar y no tiene respuesta después de cuatro millones de operaciones.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Enfoque de riesgo sin análisis | El análisis justifica el umbral |
| Prohibir por simplicidad | Desplaza la actividad |
| Cotejar solo el nombre | Las listas incluyen direcciones |
| Dato personal en el registro | Validación en la entrada |
| Ignorar la custodia en el prudencial | Consume capital operacional |

## Límites

- Los costes por medida reforzada son **supuestos declarados** y dependen mucho del grado de automatización.
- El análisis de procedencia hasta N saltos tiene un coste que crece con N y un rendimiento decreciente; el laboratorio no optimiza N.
- Nada de este material describe cómo eludir controles: el objetivo es cumplir y detectar.
