# Solución de referencia — Laboratorio 3: registro de referencia y atomicidad

> Material docente.

## La ventana la fija el cliente más activo, no la media

El cálculo de la ventana de conciliación se hace casi siempre con la media de operaciones por cliente, y esa media no protege a nadie: quien puede provocar la divergencia es el que opera tres veces al mes, no el que opera media vez.

## El registro de referencia se decide dato a dato

```text
saldo de cuenta        el propio
colateral pignorado    el propio mientras
                       está pignorado
saldo de liquidación   el del banco
posición del cliente   el propio
```

Con bloqueo de origen no hay dos versiones activas del mismo dato en ningún momento, y por eso la divergencia estructural desaparece.

## La cadena de decisiones

```text
dinero DENTRO del registro
  → atomicidad alcanzable
  → el registro de colateral se justifica
  → y hay que prefinanciar

dinero FUERA
  → no hay atomicidad
  → el registro no aporta nada
```

No hay una tercera rama, y por eso la clase 4 dejó su conclusión pendiente de la 5 en vez de resolverla por adelantado para que saliera como se quería.

## La distinción que hay que escribir

```text
NO ES  «usamos blockchain»
ES     «el colateral y su tramo de dinero
        viven en un registro común operado
        por nosotros»
```

La primera frase es la que se entiende y la que no dice nada. La segunda es más larga y precisa qué componente, con qué dinero y quién lo opera.

## El ahorro es pequeño y aun así cierra la decisión

```text
pérdida esperada evitada    13 200
coste de prefinanciar        6 192
neto                         7 008
```

Siete mil al año no justifican una arquitectura. Lo que la justifica es que el colateral se libera en el acto, y eso es un beneficio de producto que hay que declarar como tal.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Un registro de referencia para todo | Se decide dato a dato |
| Ventana por la media | Decide el cliente más activo |
| Prometer atomicidad sin el dinero dentro | La arquitectura lo impide |
| Dejar la dependencia abierta | La clase 4 depende de esta |
| Decir «usamos blockchain» | Precisa qué componente y por qué |

## Límites

- La distribución de operaciones por cliente es **sintética**; en un sistema real hay que medirla.
- El modelo supone que el banco emisor concilia a diario; si no lo hace, la ventana es la suya.
- El ahorro de 7 008 depende de la probabilidad de incumplimiento supuesta, que es una estimación de cartera.
