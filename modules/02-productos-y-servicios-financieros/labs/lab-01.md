# Laboratorio 1: Mapa del sistema financiero

## Propósito

Verificar seis entidades reales y **determinar dónde quedaría el dinero en cada una si quebraran**.

Es el primer laboratorio de la parte y el que evita el error más caro del consumo financiero: entregar dinero a una entidad que no es lo que parece.

## Escenario

Seis entidades que ofrecen productos parecidos: dos bancos, una cooperativa, una emisora de tarjetas, una plataforma de inversión y una entidad no supervisada.

## Datos

Las seis fichas sintéticas, con su nombre comercial y su descripción de producto.

## Supuestos del ejercicio

- La verificación se hace contra los registros públicos del supervisor.
- Ningún producto se contrata: el ejercicio es documental.
- La garantía de depósitos se aplica según su alcance declarado.

## Pasos

1. Clasifica cada entidad por lo que puede hacer legalmente.
2. Determina qué organismo la supervisa, o si ninguno lo hace.
3. Comprueba si sus productos están cubiertos por garantía de depósitos.
4. Clasifica sus productos por función y no por su nombre comercial.
5. Determina dónde quedaría el dinero si cada entidad quebrara.
6. Aplica la comprobación de dos minutos y señala cuál de las seis no la pasa.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Cada entidad tiene tipo y supervisor | Tabla completa |
| 2 | La cobertura de garantía está determinada | Con su alcance |
| 3 | Los productos están clasificados por función | No por nombre |
| 4 | El destino del dinero en quiebra está determinado | Para las seis |
| 5 | La entidad que no pasa la comprobación está identificada | Con su razón |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Clasificar por el nombre del producto | «Cuenta» y «depósito» significan cosas distintas según quién los ofrezca |
| Suponer que toda entidad está supervisada | Es el supuesto que sostiene la mayoría de los fraudes |
| Confundir supervisión con garantía | Estar supervisado no implica que el dinero esté garantizado |
| No comprobar el registro público | Es una consulta de dos minutos |

## Entregables

- `solution.md` con las seis entidades clasificadas y verificadas.
- La tabla de productos por función.
- El destino del dinero en caso de quiebra, entidad por entidad.
- La entidad que no pasa la comprobación, con su razón.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Clasificación y supervisor | 25 |
| Cobertura determinada | 20 |
| Productos por función | 20 |
| Destino en quiebra | 20 |
| Entidad detectada | 15 |
