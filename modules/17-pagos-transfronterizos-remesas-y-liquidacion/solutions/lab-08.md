# Solución de referencia — Laboratorio 8: ruta mediante stablecoin

> Material docente. La stablecoin del ejercicio es **sintética**.

## La respuesta escrita a la dirección

> La afirmación «reduce el coste un 78 %» no se sostiene en nuestros corredores.
> En el caso base —cadena clásica con un intermediario— la ruta con stablecoin
> cuesta **2,40 %** frente al **2,29 %** de la ruta clásica: es más cara.
>
> La ruta gana cuando la cadena clásica tiene dos o más intermediarios: ahí pasa
> a 2,40 % frente a 3,10 %, con un ahorro de 0,70 puntos.
>
> Del ahorro observado en ese caso, el **2,7 %** es atribuible al registro
> distribuido. El 97 % restante viene de evitar intermediarios y de no
> prefinanciar, y lo produciría cualquier arquitectura con la misma topología —
> incluido un enlace de pagos inmediatos, que además no añade riesgo de emisor.
>
> Recomendación: usarla solo en corredores sin enlace directo y con cadena larga,
> con los seis controles adjuntos.

## Los cinco tramos y dónde está el coste

Envío de 20 000 USD:

| Tramo | Coste | % del total |
|---|---:|---:|
| Entrada (comisión + diferencial) | 190,00 | 39,7 % |
| Transferencia (comisión de red) | 0,04 | 0,01 % |
| Tenencia (riesgo, no coste directo) | — | — |
| Salida (comisión + diferencial) | 280,00 | 58,4 % |
| Última milla (retiro local) | 9,00 | 1,9 % |
| **Total** | **479,04** | **100 %** |

```text
ENTRADA + SALIDA = 98,1 % DEL COSTE
EL TRAMO «TECNOLÓGICO» = 0,01 %
```

Comparar el 0,01 % con la ruta clásica completa es el error que el laboratorio
está diseñado para hacer visible.

## La comparación honesta

```text
                         clásica    stablecoin
comisiones y diferencial   444,00      479,04
prefinanciación imputada    14,00        0,00
TOTAL                      458,00      479,04

la ruta con stablecoin es 21,04 USD MÁS CARA
```

Cifras reproducibles con:

```bash
python apps/cross_border_payments_lab/cli.py compare-routes --amount 20000
```

La prefinanciación se imputa porque la ruta clásica exige mantener saldo en el
nostro y la otra no. Omitirla favorece artificialmente a la clásica; incluirla
sin decirlo, a la otra.

## Sensibilidad al número de intermediarios

```text
intermediarios   clásica   stablecoin   diferencia
       1          458,00      479,04      −21,04
       2          620,00      479,04     +140,96
       3          782,00      479,04     +302,96
```

Cada intermediario adicional añade **comisión y diferencial**: 22,00 de comisión
más 70 pb sobre el importe. Por eso el coste crece más deprisa que el número de
eslabones, y por eso el punto de cruce llega antes de lo que sugiere contar
comisiones.

**El punto de cruce está entre uno y dos intermediarios.** Ese es el resultado
del laboratorio: la ventaja de la ruta es proporcional a los eslabones que evita,
no a la tecnología que usa.

## Descomposición del ahorro (caso de dos intermediarios)

| Fuente | USD | % del ahorro |
|---|---:|---:|
| Menor diferencial | 200,00 | 141,9 % |
| Intermediarios evitados | 40,16 | 28,5 % |
| Prefinanciación no necesaria | 14,00 | 9,9 % |
| Mensajería frente a coste de red | 3,80 | 2,7 % |
| Comisiones de servicio (peor en la ruta nueva) | −117,00 | −83,0 % |
| **Total** | **140,96** | **100 %** |

```text
ATRIBUIBLE AL REGISTRO: 2,7 %
ATRIBUIBLE A LA TOPOLOGÍA Y AL MODELO: 97,3 %
```

Dos lecturas que la tabla obliga a hacer:

- **las partes suman el ahorro total.** Una descomposición cuyas partes no suman
  el total no es una descomposición: es una lista de cifras favorables;
- **una de las partes es negativa.** Las comisiones de servicio de la ruta con
  stablecoin son 117 USD peores que las de la clásica, porque son porcentuales
  sobre el importe y las otras son fijas. Ocultar esa fila para que el resultado
  luzca mejor es el error que la clase 16 llama atribución errónea.

## Exposición durante la tenencia

```python
def exposicion(importe: Decimal, minutos: int) -> Decimal:
    # La exposición NO es la planificada: es la que resulte.
    # Si la salida se bloquea, los 22 minutos previstos
    # se convierten en el tiempo que tarde el desbloqueo.
    return importe * Decimal(minutos) / Decimal(60 * 24)
```

```text
ESCENARIO PLANIFICADO   22 minutos    exposición baja
SALIDA BLOQUEADA         3 días       exposición ×196

Y el bloqueo puede venir de:
  · congestión de la red
  · control de cumplimiento del proveedor de salida
  · decisión del propio emisor
  · falta de liquidez de salida en destino
```

Por eso el límite de tenencia con alerta es un control obligatorio, no una buena
práctica.

## La regla de enrutamiento

```text
SI existe enlace de pagos inmediatos en el corredor
   → usarlo (más barato, sin riesgo de emisor)

SI NO, Y la cadena clásica tiene ≤ 1 intermediario
   → ruta clásica

SI NO, Y la cadena tiene ≥ 2 intermediarios
   Y hay mercado líquido de salida en destino
   Y la tenencia estimada es < 60 minutos
   Y el emisor está dentro del límite aprobado
   → ruta con stablecoin

CONTROLES OBLIGATORIOS
  1. límite de exposición por emisor
  2. límite de tenencia con alerta a los 60 min
  3. procedimiento si la salida se bloquea
  4. lista blanca de direcciones de destino
  5. cumplimiento de la regla del viaje en el tramo
  6. evaluación del emisor según los criterios de la Parte 20

CONDICIÓN DE REVISIÓN
  si aparece un enlace de pagos inmediatos en el corredor,
  la regla lo prioriza automáticamente
```

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Comparar el tramo de red con la ruta entera | Es la comparación que el laboratorio desmonta |
| No imputar la prefinanciación | Favorece artificialmente a una ruta |
| Suponer la tenencia planificada | La exposición es la que resulte |
| Atribuir el ahorro al registro | El 97 % viene de la topología |
| Omitir la condición del enlace directo | Elige lo peor cuando hay algo mejor |

## Límites

- La stablecoin es sintética; su diseño, reservas y regulación son materia de la
  Parte 20 y aquí no se modelan.
- No se modela un episodio de pérdida de paridad: se trata como riesgo declarado,
  no cuantificado.
- Los costes de entrada y salida son los que más varían por corredor y por mes:
  el resultado del laboratorio depende de ellos y se declara como tal.
