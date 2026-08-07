# Laboratorio 3: Sistemas de amortización

## Propósito

Amortizar el mismo capital por cinco sistemas y **comprobar que el más barato en intereses no es el recomendable para todos los perfiles**.

El laboratorio 2 valoró series regulares. Este las estructura, y añade el criterio profesional: el sistema se elige por el flujo del deudor y no por su costo total.

## Escenario

Un capital de 30 000 000 a 5 años y 1,1 % mensual, y tres deudores con perfiles de flujo distintos: estable, estacional y creciente.

## Datos

El crédito y los tres perfiles de flujo.

## Supuestos del ejercicio

- El sistema de cuota creciente sube un 5 % anual.
- El fondo de amortización acumula al 0,6 % mensual.
- Los tres perfiles se entregan con su flujo mensual disponible.

## Pasos

1. Amortiza el capital por los cinco sistemas y tabula primera cuota, última e interés total.
2. Calcula la duración del crédito en cada sistema.
3. Compara la duración con el costo total y explica por qué no ordenan igual.
4. Contrasta cada sistema con los tres perfiles de flujo y marca los incompatibles.
5. Recomienda un sistema por perfil con su justificación.
6. Calcula el efecto de un prepago del 20 % en el mes 18 en los dos sistemas extremos.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los cinco sistemas están amortizados | Con sus tres cifras clave |
| 2 | La duración está calculada | Para los cinco |
| 3 | Duración y costo no ordenan igual | Y se explica |
| 4 | Los incompatibles están marcados | Perfil por perfil |
| 5 | La recomendación tiene justificación | Por flujo, no por costo |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Elegir por interés total | Un sistema barato con cuotas impagables incumple |
| Ignorar el perfil de flujo | Es lo que decide la recomendación |
| Confundir duración con plazo | La duración pondera por cuándo se recupera |
| No probar el prepago | Su efecto cambia mucho entre sistemas |

## Entregables

- `solution.md` con los cinco sistemas y sus cifras.
- La duración de cada uno y su contraste con el costo.
- La compatibilidad con los tres perfiles.
- El efecto del prepago en los dos sistemas extremos.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Cinco sistemas | 30 |
| Duración calculada | 20 |
| Contraste con costo | 15 |
| Recomendación por perfil | 25 |
| Prepago | 10 |
