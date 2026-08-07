# Solución de referencia — Laboratorio 5: liquidación de extremo a extremo

> Material docente.

## La quinta prueba es la que nadie escribe

Cuatro de las cinco pruebas de atomicidad son las que cualquiera escribiría. La quinta —el registro detenido— no se le ocurre a nadie porque no es un fallo de las partes sino del propio sistema, y es la que más veces se activa en producción.

## Las cinco pruebas

```text
1 sin estado intermedio observable
2 falla el activo → dinero intacto
3 falla el dinero → activo intacto
4 doble gasto imposible
5 REGISTRO DETENIDO → rechaza sin tocar nada
```

Las cinco se escriben una vez y valen para siempre. La quinta cubre el modo de fallo que el escenario de tensión del laboratorio 8 va a provocar de verdad.

## Rechazar antes de bloquear

```text
1 verificar el activo del vendedor
2 verificar el dinero del comprador
3 si falla cualquiera → RECHAZAR sin tocar
4 si no → los cuatro movimientos juntos
```

Rechazar no deja rastro. Bloquear y revertir sí, y ese rastro es un estado intermedio en el que alguien pudo actuar.

## El ahorro tras restarlo todo

```text
pérdida esperada evitada      4 950
coste de liquidez con neteo  −3 096
coste del fallo del ciclo    −1 200
NETO                            654
```

Seiscientos cincuenta y cuatro al año. Reconocerlo y justificar la arquitectura por el beneficio de producto es más sólido que inflar el argumento de riesgo, y además es cierto.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Bloquear y revertir | La reversión prueba que hubo estado intermedio |
| Probar solo el camino feliz | Cada fallo con su prueba |
| Ignorar el coste de liquidez | Se sobrestima el ahorro |
| No dimensionar el fallo del ciclo | Afecta a todas las operaciones |
| Inflar el argumento de riesgo | Declara el beneficio real |

## Límites

- El liquidador corre en un solo proceso: no modela concurrencia real ni latencias.
- La probabilidad de incumplimiento y la disponibilidad son **supuestos declarados**.
- El modelo no incluye el riesgo del emisor del dinero, que se analiza aparte.
