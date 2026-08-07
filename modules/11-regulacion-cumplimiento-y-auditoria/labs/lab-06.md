# Laboratorio 6: Proyecto: sistema de cumplimiento

## Propósito

Integrar los tres ciclos de hallazgos y **comprobar que dejan de duplicarse**.

Es el último laboratorio de la parte y la antesala del proyecto. Cumplimiento, auditoría interna y supervisión producen hallazgos sobre lo mismo, y gestionarlos por separado duplica trabajo y pierde información.

## Escenario

Una entidad con 40 hallazgos abiertos: 18 de cumplimiento, 14 de auditoría interna y 8 de supervisión, con solapamientos.

## Datos

Los 40 hallazgos con su origen, su área, su criticidad y su plan de acción.

## Supuestos del ejercicio

- Los solapamientos no están identificados en el estado inicial.
- Cada hallazgo tiene un plan de acción y un responsable declarados.
- Seis planes de acción están vencidos.

## Pasos

1. Identifica los hallazgos que se refieren al mismo defecto desde orígenes distintos.
2. Consolida los solapamientos en un hallazgo único con sus tres orígenes.
3. Prioriza el conjunto por criticidad y por clientes afectados.
4. Detecta los planes de acción vencidos y clasifica la razón del retraso.
5. Verifica que cada plan tiene medida provisional para el intervalo.
6. Diseña el ciclo único: cómo entra un hallazgo, quién lo prioriza y cómo se cierra.
7. Construye el informe mensual al comité con lo que necesita para decidir.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los solapamientos están identificados | Con sus orígenes |
| 2 | La consolidación reduce el número | Con la cifra antes y después |
| 3 | La priorización usa efecto sobre el cliente | No solo criticidad formal |
| 4 | Los vencidos están clasificados por causa | No solo listados |
| 5 | Cada plan tiene medida provisional | O se señala que falta |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Gestionar tres ciclos separados | Duplica trabajo y pierde información |
| Priorizar por criticidad formal | El efecto sobre el cliente ordena mejor |
| Plan sin medida provisional | El intervalo de corrección deja al cliente expuesto |
| Informe que lista hallazgos | El comité necesita decidir, no leer una lista |

## Entregables

- `solution.md` con los solapamientos identificados y consolidados.
- La priorización por efecto sobre el cliente.
- Los vencidos clasificados por causa.
- El diseño del ciclo único y el informe al comité.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Solapamientos identificados | 25 |
| Consolidación | 20 |
| Priorización | 20 |
| Medidas provisionales | 20 |
| Ciclo único | 15 |
