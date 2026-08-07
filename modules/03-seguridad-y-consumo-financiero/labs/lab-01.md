# Laboratorio 1: Amenazas y hábitos seguros

## Propósito

Medir la superficie de exposición propia y **comprobar que los siete controles están activos**, no que se conocen.

Es el primer laboratorio de la parte y el que más riesgo reduce por el tiempo que cuesta. Todo lo demás supone que estos controles existen.

## Escenario

Una persona con cuatro cuentas, seis accesos, dos tarjetas y un correo que recupera todas las demás credenciales.

## Datos

El inventario sintético de accesos, o el propio si se prefiere.

## Supuestos del ejercicio

- El correo de recuperación se cuenta como acceso crítico.
- La pérdida máxima se calcula sobre lo alcanzable con un acceso, no sobre el patrimonio.
- Un control se da por activo solo con evidencia de su configuración.

## Pasos

1. Inventaria accesos, dispositivos y cuentas alcanzables desde cada uno.
2. Calcula la superficie de exposición y la pérdida máxima por acceso.
3. Identifica el acceso que da entrada a más cuentas y por qué.
4. Comprueba los siete controles y marca cuáles están efectivamente activos.
5. Configura los que falten y registra la evidencia con su fecha.
6. Recalcula la pérdida máxima y mide la reducción obtenida.
7. Clasifica los controles restantes en preventivo, detectivo y correctivo.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El inventario está completo | Accesos, dispositivos y cuentas alcanzables |
| 2 | La pérdida máxima está calculada por acceso | No sobre el patrimonio total |
| 3 | El acceso crítico está identificado | Con las cuentas que abre |
| 4 | Los siete controles tienen evidencia | Con su fecha, no declarados |
| 5 | La reducción está medida | Antes y después |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Declarar un control sin comprobarlo | Casi la mitad de los que se creen activos no lo están |
| Calcular la pérdida sobre el patrimonio | Lo relevante es lo alcanzable desde un acceso |
| Olvidar el correo de recuperación | Es la llave de casi todo lo demás |
| Tener solo controles preventivos | Cuando fallan no hay nada que avise |

## Entregables

- `solution.md` con el inventario y la superficie medida.
- La pérdida máxima por acceso, antes y después.
- Los siete controles con su evidencia y su fecha.
- La clasificación de los controles en las tres categorías.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Inventario completo | 25 |
| Pérdida máxima por acceso | 20 |
| Controles con evidencia | 30 |
| Reducción medida | 15 |
| Clasificación | 10 |

> **Sobre los datos.** Si usas tu propio inventario, no sale de tu equipo y
> nunca se comparte. El ejercicio se puede resolver con el perfil sintético.
