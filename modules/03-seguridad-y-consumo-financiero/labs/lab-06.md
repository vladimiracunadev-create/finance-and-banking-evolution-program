# Laboratorio 6: Proyecto: protocolo personal de seguridad

## Propósito

Escribir el protocolo y **ejecutar el simulacro sin acceso a lo que se supone comprometido**.

Es el último laboratorio de la parte y el que valida todo lo anterior. Un protocolo que nunca se ha ensayado no se sabe si funciona, y el simulacro es donde falla lo que en el papel parecía resuelto.

## Escenario

El protocolo completo de una persona, sometido a un escenario en el que el correo de recuperación está comprometido.

## Datos

El inventario del laboratorio 1 y los controles configurados.

## Supuestos del ejercicio

- El simulacro se ejecuta sin acceso al correo principal ni al gestor de contraseñas.
- El protocolo tiene que ser alcanzable en esas condiciones.
- Los contactos de la entidad se verifican por canal inverso.

## Pasos

1. Escribe las seis secciones del protocolo con su contenido.
2. Registra la evidencia de cada control con su fecha de comprobación.
3. Calcula la pérdida máxima residual tras los controles.
4. Fija el calendario de vigencia y qué se revisa en cada fecha.
5. Ejecuta el simulacro sin acceso al correo ni al gestor.
6. Anota qué falló durante el simulacro y corrige el protocolo.
7. Vuelve a ejecutarlo y comprueba que el fallo desapareció.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Las seis secciones están completas | Sin ninguna vacía |
| 2 | Cada control tiene evidencia y fecha | No declarado |
| 3 | La pérdida máxima residual está calculada | Después de los controles |
| 4 | El simulacro se ejecutó en las condiciones dadas | Sin los accesos comprometidos |
| 5 | Lo que falló está corregido y reprobado | Con el segundo simulacro |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Guardar el protocolo en el gestor de contraseñas | Es lo primero que se pierde |
| Declarar controles sin evidencia | El simulacro los descubre |
| No ejecutar el simulacro | Un plan no ensayado no se sabe si funciona |
| Corregir sin volver a probar | La corrección puede no funcionar |

## Entregables

- `solution.md` con el protocolo de seis secciones.
- La evidencia de cada control con su fecha.
- La pérdida máxima residual calculada.
- El registro del simulacro, lo que falló y el segundo simulacro.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Protocolo completo | 25 |
| Controles con evidencia | 20 |
| Pérdida residual | 15 |
| Simulacro ejecutado | 25 |
| Corrección reprobada | 15 |
