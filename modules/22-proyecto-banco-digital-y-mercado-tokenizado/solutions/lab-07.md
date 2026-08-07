# Solución de referencia — Laboratorio 7: modelo de amenazas

> Material docente.

## El punto más barato no era el más protegido

Priorizar por sofisticación habría llevado a reforzar la criptografía del registro, que ya estaba bien. El atacante racional mira otra cosa: dónde está el mayor valor detrás del control más débil, y eso apuntaba a la autenticación del cliente.

## El criterio

```text
valor acumulado en el objetivo
coste de comprometer el control
probabilidad de ser detectado

Y LA PREGUNTA
  ¿dónde está el mayor valor detrás
   del control más débil?
```

Con 91,2 millones en saldos protegidos por autenticación y un registro que controla todo protegido por un 3-de-5 con independencia 4, el punto barato es el primero.

## Una prueba por control

```text
lista blanca con espera
  → alta de destino y retirada inmediata
    debe rechazarse

verificación de aprovisionamiento
  → pago con fondos insuficientes
    no debe pagar a nadie
```

Un control descrito y no probado es una intención. La prueba no tiene que ser compleja: tiene que fallar cuando el control falla.

## El riesgo residual se declara

```text
la amenaza y su efecto
por qué no hay control proporcionado
qué la detectaría a posteriori
qué se haría si ocurriera
quién lo aceptó, con fecha
```

La última línea es la que convierte un riesgo en una decisión. Sin ella, el riesgo queda flotando y nadie lo asumió.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Priorizar por sofisticación | Los escenarios complejos atraen |
| Control sin prueba | Es una intención |
| Componente sin amenazas | Suele significar que nadie lo miró |
| Riesgo residual oculto | Es lo que da credibilidad |
| Solo amenazas externas | La interna tiene acceso |

## Límites

- Los valores por componente son **sintéticos**; en un sistema real se recalculan cada trimestre.
- El coste de comprometer un control no se puede estimar con precisión: lo que sostiene el análisis es la comparación de órdenes de magnitud.
- El modelo no cubre amenazas a la cadena de suministro del software, que exigen su propio análisis.
