# Laboratorio 5: Escenario de inflación

## Propósito

Someter el banco a un escenario inflacionario y **encontrar qué rompe primero**.

Los laboratorios anteriores construyeron el banco. Este lo somete a un escenario diseñado contra sus vulnerabilidades, que no son las de cualquier banco sino las suyas.

## Escenario

Una inflación que pasa del 3,4 % al 11,2 % en cuatro trimestres, con alza de la tasa de política y deterioro del empleo.

## Datos

El balance del banco, su cartera y su estructura de fondeo.

## Supuestos del ejercicio

- El banco tiene cartera en unidad indexada y fondeo mayorista.
- El traspaso de tasas a las colocaciones y a las captaciones difiere.
- El escenario se construye desde una narrativa coherente.

## Pasos

1. Escribe la narrativa del escenario y comprueba su coherencia.
2. Traduce la inflación y la tasa a parámetros de riesgo por segmento.
3. Calcula el efecto sobre el margen con el traspaso asimétrico.
4. Calcula el efecto sobre la mora de la cartera en unidad indexada.
5. Proyecta la liquidez con el comportamiento del fondeo mayorista.
6. Determina qué métrica rompe primero y en qué trimestre.
7. Declara las acciones de gestión y verifica que son ejecutables en ese escenario.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La narrativa es coherente | Las variables se mueven por una causa común |
| 2 | La traducción a parámetros está hecha | Por segmento |
| 3 | El efecto asimétrico del traspaso está calculado | Colocaciones y captaciones |
| 4 | La métrica que rompe está identificada | Con su trimestre |
| 5 | Las acciones son ejecutables en el escenario | Y se justifica |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Suponer traspaso simétrico | Las subidas se trasladan más rápido |
| Olvidar la cartera indexada | La cuota sube con la inflación y el sueldo no |
| Escenario que el banco aguanta | No informa |
| Acciones no ejecutables | Vender activos en un mercado sin compradores |

## Entregables

- `solution.md` con la narrativa y su traducción.
- El efecto sobre margen, mora y liquidez.
- La métrica que rompe primero y su trimestre.
- Las acciones de gestión con su viabilidad.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Narrativa coherente | 20 |
| Traducción a parámetros | 20 |
| Efecto asimétrico | 20 |
| Métrica que rompe | 25 |
| Acciones ejecutables | 15 |
