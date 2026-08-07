# Laboratorio 6: Proyecto: calculadora financiera personal

## Propósito

Construir la calculadora del proyecto con **casos de prueba escritos antes que el código**.

Es el último laboratorio de la parte y la antesala del proyecto. Reúne los cinco anteriores en funciones que otra persona pueda usar y verificar.

## Escenario

Las cinco funciones que resuelven los laboratorios 1 a 5, con su interfaz y sus pruebas.

## Datos

Los casos numéricos ya resueltos a mano en los laboratorios anteriores.

## Supuestos del ejercicio

- Los valores esperados vienen de los cálculos manuales, no del propio código.
- La interfaz separa el cálculo de la presentación.
- Se rechaza toda entrada inválida con mensaje claro.

## Pasos

1. Escribe los casos de prueba desde los resultados de los laboratorios 1 a 5.
2. Implementa las funciones hasta que las pruebas pasen.
3. Añade validación de entrada: tasa negativa, plazo cero, capital no positivo.
4. Comprueba que la tabla de amortización generada cierra en cero.
5. Documenta cada función con su unidad de entrada y de salida.
6. Escribe la hoja de supuestos del conjunto.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Las pruebas se escribieron antes | Se ve en el orden del historial o se declara |
| 2 | Los valores esperados son independientes | Vienen de un cálculo manual |
| 3 | Las entradas inválidas se rechazan | Con mensaje, no con excepción cruda |
| 4 | La tabla cierra en cero | Comprobado por una prueba |
| 5 | Cada función declara sus unidades | En su documentación |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Probar el código contra sí mismo | No valida nada |
| Aceptar cualquier entrada | Una tasa negativa produce un resultado sin sentido |
| Mezclar cálculo y presentación | Impide probar el cálculo por separado |
| Omitir las unidades | Es el error que la clase 1 persigue |

## Entregables

- `solution.md` con las decisiones de diseño.
- El código con sus pruebas en verde.
- La hoja de supuestos con las unidades de cada función.
- La lista de lo que la calculadora no hace.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Pruebas antes que código | 25 |
| Valores esperados independientes | 20 |
| Validación de entrada | 20 |
| Documentación de unidades | 20 |
| Límites declarados | 15 |
