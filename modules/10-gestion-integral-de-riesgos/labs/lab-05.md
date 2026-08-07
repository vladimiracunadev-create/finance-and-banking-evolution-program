# Laboratorio 5: Pruebas de estrés

## Propósito

Diseñar un escenario coherente y **comprobar que rompe alguna métrica**, porque uno que el banco aguanta no informa.

Los laboratorios anteriores midieron riesgos por separado. Este los somete a un escenario común, que es donde aparecen las interacciones que ninguna medición individual captura.

## Escenario

Un banco con cartera concentrada en un sector cíclico, fondeo mayorista y exposición cambiaria indirecta por sus deudores.

## Datos

El balance completo, la composición de la cartera y los parámetros de riesgo actuales.

## Supuestos del ejercicio

- El escenario se construye desde una narrativa, no desde una lista de variables.
- Las acciones de gestión supuestas tienen que ser ejecutables en el escenario.
- El balance se proyecta estático salvo lo que el escenario cambie.

## Pasos

1. Escribe la narrativa del escenario adverso y comprueba su coherencia interna.
2. Traduce el escenario a parámetros de riesgo por segmento.
3. Proyecta el resultado, el balance y el capital bajo el escenario.
4. Comprueba qué métrica rompe primero y en qué trimestre.
5. Si ninguna rompe, endurece el escenario y repite.
6. Declara las acciones de gestión y evalúa si son ejecutables en ese contexto.
7. Ejecuta una prueba inversa: qué escenario haría inviable al banco.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La narrativa es coherente | Las variables se mueven juntas por una causa |
| 2 | La traducción a parámetros está hecha | Por segmento |
| 3 | La proyección cubre resultado, balance y capital | Trimestre a trimestre |
| 4 | Alguna métrica rompe | Con su trimestre |
| 5 | Las acciones son ejecutables en el escenario | Y se justifica |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Escenario que el banco aguanta | No informa de nada |
| Variables movidas sin narrativa | Producen combinaciones imposibles |
| Acciones de gestión no creíbles | Vender activos en un mercado sin compradores |
| No hacer la prueba inversa | Es la que más informa y la que menos se hace |

## Entregables

- `solution.md` con la narrativa y su coherencia.
- La traducción a parámetros y la proyección completa.
- La métrica que rompe y su trimestre.
- La prueba inversa con el escenario que haría inviable al banco.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Narrativa coherente | 20 |
| Traducción a parámetros | 20 |
| Proyección completa | 25 |
| Métrica que rompe | 20 |
| Prueba inversa | 15 |
