# Laboratorio 6: Proyecto: plataforma bancaria digital

## Propósito

Clasificar los casos de uso por su efecto sobre las personas y **definir controles proporcionales, no máximos**.

Es el último laboratorio de la parte y la antesala del proyecto. Aplicar el control máximo a todo es tan incorrecto como no aplicarlo, y la proporcionalidad es lo que se evalúa.

## Escenario

Una plataforma con seis casos de uso de modelos: ordenación de contenidos, detección de fraude, decisión de crédito, precio personalizado, asistente conversacional y priorización de cobranza.

## Datos

Los seis casos con su descripción y su efecto sobre el cliente.

## Supuestos del ejercicio

- Dos de los seis afectan directamente al acceso a un producto.
- Uno usa un sistema generativo.
- Los controles disponibles se entregan con su costo.

## Pasos

1. Clasifica los seis casos por su efecto sobre las personas.
2. Define los controles proporcionales de cada nivel de riesgo.
3. Determina cuáles exigen explicabilidad individual y cuáles no.
4. Para los de riesgo alto, define el humano en el circuito y su alcance.
5. Identifica los modos de fallo del caso generativo y sus controles propios.
6. Mide el sesgo de uno de los modelos con tres definiciones de equidad.
7. Elige una definición, justifícala y explica qué se sacrifica al elegirla.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Los seis están clasificados | Por efecto sobre las personas |
| 2 | Los controles son proporcionales | No máximos para todo |
| 3 | La explicabilidad individual está delimitada | Solo donde corresponde |
| 4 | El caso generativo tiene controles propios | Por sus modos de fallo |
| 5 | La definición de equidad está elegida y justificada | Con lo que sacrifica |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Aplicar controles máximos a todo | Hace inviable el uso y no protege más |
| Exigir explicabilidad donde no aporta | Consume esfuerzo sin beneficio |
| Tratar el sistema generativo como los demás | Sus modos de fallo son distintos |
| Buscar un modelo justo en todas las definiciones | Está demostrado que no existe |

## Entregables

- `solution.md` con los seis casos clasificados.
- Los controles proporcionales de cada nivel.
- Los modos de fallo del caso generativo con sus controles.
- La medición de sesgo y la definición elegida con su sacrificio.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Clasificación por efecto | 25 |
| Controles proporcionales | 25 |
| Explicabilidad delimitada | 15 |
| Caso generativo | 15 |
| Equidad justificada | 20 |
