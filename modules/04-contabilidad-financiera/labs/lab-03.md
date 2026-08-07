# Laboratorio 3: Registro de transacciones

## Propósito

Detectar seis asientos incorrectos **por sus consecuencias en los estados**, sin revisar el asiento.

El laboratorio 2 clasificó partidas. Este entra en la mecánica del registro, y su habilidad útil no es hacer asientos sino leerlos hacia atrás desde el efecto que producen.

## Escenario

Un juego de estados financieros con seis efectos anómalos, producidos por seis asientos concretos.

## Datos

Los estados con los efectos, y el libro diario del periodo.

## Supuestos del ejercicio

- Todos los asientos cuadran: el error no es de partida doble.
- Los documentos de respaldo están disponibles para tres de los seis.
- El periodo está cerrado y no se puede reabrir.

## Pasos

1. Identifica los seis efectos anómalos en los estados.
2. Deduce qué asiento pudo producir cada uno, antes de mirar el diario.
3. Comprueba tu deducción contra el libro diario.
4. Determina cuáles de los seis carecen de documento de respaldo.
5. Propón el asiento de corrección de cada uno.
6. Explica cuál de los seis podría no ser un error sino una decisión.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los seis efectos están identificados | En los estados |
| 2 | La deducción está escrita antes de mirar el diario | Y se contrasta |
| 3 | Los que carecen de respaldo están señalados | Tres de seis |
| 4 | Las correcciones están propuestas | Como asientos |
| 5 | El caso discutible está identificado | Con su razón |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Revisar el diario antes de deducir | Se pierde la habilidad que el ejercicio entrena |
| Suponer que si cuadra está bien | La partida doble no detecta clasificaciones erróneas |
| Corregir sin documento de respaldo | Un asiento sin respaldo es una afirmación |
| Tratar toda anomalía como error | Alguna puede ser una decisión legítima |

## Entregables

- `solution.md` con los seis efectos y su deducción previa.
- El contraste con el libro diario.
- Los asientos sin respaldo señalados.
- Las correcciones propuestas y el caso discutible.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Efectos identificados | 25 |
| Deducción previa | 25 |
| Respaldo verificado | 20 |
| Correcciones | 20 |
| Caso discutible | 10 |
