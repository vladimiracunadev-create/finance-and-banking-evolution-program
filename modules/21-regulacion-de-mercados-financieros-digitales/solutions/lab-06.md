# Solución de referencia — Laboratorio 6: detección de conducta anómala

> Material docente.

## El coste marginal supera al medio y aun así se justifica

La vigilancia detectaba el 71 % de los casos, y el mayor grupo de los no detectados —la anticipación de órdenes— no tenía ningún indicador. No por descuido: los indicadores se habían copiado de un mercado donde las órdenes pendientes no son visibles antes de ejecutarse.

## El estado inicial

```text
alertas                  3 640
confirmados                 44
casos reales                62

precisión               1,21 %
exhaustividad          70,97 %
coste mensual           65 520
```

Precisión baja y exhaustividad media es el perfil habitual: se revisa mucho ruido y aun así se escapa uno de cada tres casos. Optimizar la precisión reduce el trabajo y empeora la protección.

## El indicador que faltaba

```text
de los 18 casos no detectados
  11 anticipación de órdenes
   5 operaciones circulares
   2 uso de información

EL PRIMER GRUPO ERA EL MAYOR
y no había ningún indicador para él
```

Es la consecuencia directa de una particularidad del registro: las órdenes pendientes son visibles antes de ejecutarse, y quien decide el orden puede colocarse delante. La anticipación deja de ser la conducta de un intermediario desleal y pasa a ser una propiedad del sistema.

## La decisión correcta

```python
assert decision["coste_marginal_por_caso"] > decision["coste_medio_por_caso"]
assert decision["se_justifica"]
```

**Esta prueba documenta el error de razonamiento.** El coste marginal de 1 880 por caso supera al medio de 1 489, y comparar ambos llevaría a rechazar el indicador. La comparación correcta es el marginal frente al valor del caso, que es 45 000.

## Lo que hay que discutir en el comité

```text
9 casos × 45 000 = 405 000 al año
coste adicional           203 040

→ el indicador se justifica

Y EL SUPUESTO DE 45 000 ES LO QUE
HAY QUE DISCUTIR, no el umbral
```

El equipo de vigilancia puede calcular todo lo demás; lo que no puede decidir solo es cuánto vale detectar un caso. Ese número es una decisión de apetito de riesgo y corresponde al comité.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Copiar indicadores | El abuso aquí es distinto |
| Optimizar la precisión | La exhaustividad es lo que protege |
| Decidir con el coste medio | Decide el marginal |
| Conflictos «gestionados» | La separación funciona mejor |
| Mejor ejecución afirmada | Hay que demostrarla con datos |

## Límites

- Los casos conocidos a posteriori son la referencia de exhaustividad y siempre son una cota inferior: los que nadie descubrió no están.
- El valor de detectar un caso es un supuesto del comité y no se estima aquí.
- El modelo no incluye el coste reputacional ni el sancionador, que en un episodio grave dominan sobre lo calculado.
