# Laboratorio 5: Análisis técnico: prueba dentro y fuera de muestra

## Propósito

Probar una regla técnica dentro y fuera de muestra, y **medir cuánto se deteriora**.

Los laboratorios anteriores usaron métodos con fundamento. Este somete uno discutido a la prueba que decide, y el resultado es consistente y por eso convincente.

## Escenario

Una serie de precios de diez años y una regla de cruce de medias móviles con parámetros optimizables.

## Datos

La serie completa, dividida en un periodo de ajuste y otro posterior.

## Supuestos del ejercicio

- El periodo de ajuste son los primeros siete años y el de prueba los tres últimos.
- Los costos de transacción se entregan como dato y se aplican.
- La regla no puede usar información posterior a cada decisión.

## Pasos

1. Optimiza los parámetros de la regla en el periodo de ajuste.
2. Calcula el resultado dentro de muestra con costos de transacción.
3. Aplica los mismos parámetros al periodo posterior sin reoptimizar.
4. Compara los dos resultados y mide el deterioro.
5. Comprueba que la regla no usa información futura en ningún punto.
6. Compara con la estrategia de comprar y mantener en el mismo periodo.
7. Escribe qué habrías concluido si solo hubieras visto el periodo de ajuste.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los parámetros están optimizados | En el periodo de ajuste |
| 2 | Los costos están aplicados | En ambos periodos |
| 3 | El periodo posterior no se reoptimiza | Mismos parámetros |
| 4 | El deterioro está medido | En porcentaje |
| 5 | La ausencia de información futura está comprobada | Punto por punto |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Optimizar sobre todo el periodo | Es sobreajuste y el resultado no vale |
| Omitir los costos de transacción | Suelen consumir todo el resultado aparente |
| Usar el cierre del día para decidir ese día | Es sesgo de anticipación |
| Concluir con el periodo de ajuste | Es exactamente lo que el laboratorio desmonta |

## Entregables

- `solution.md` con los parámetros optimizados y ambos resultados.
- El deterioro medido entre periodos.
- La comprobación de ausencia de información futura.
- La comparación con comprar y mantener y la conclusión.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Optimización correcta | 20 |
| Costos aplicados | 20 |
| Prueba fuera de muestra | 30 |
| Sin información futura | 15 |
| Conclusión honesta | 15 |
