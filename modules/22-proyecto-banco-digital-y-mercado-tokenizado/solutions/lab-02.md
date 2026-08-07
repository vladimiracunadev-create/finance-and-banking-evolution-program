# Solución de referencia — Laboratorio 2: perímetro y calificación del proyecto

> Material docente.

## Dos regímenes entraron por dos líneas de diseño

El equipo creía construir cuatro funciones y estaba activando seis regímenes. Los dos que sobraban no venían de una decisión consciente: venían de guardar unas claves y de ordenar unas opciones en pantalla.

## Los hechos de diseño

```text
«el saldo queda en nuestra cuenta»    captación
«guardamos las claves»                CUSTODIA
«ordenamos las opciones»              ASESORÍA
«convertimos con margen propio»       cambio
«adelantamos contra el saldo»         crédito
```

Cada una es una línea de código y un régimen. Y la pregunta útil en esta fase no es «¿qué régimen nos aplica?» sino «¿qué decisión de diseño lo activó y podemos tomar otra?».

## La custodia se delega

```text
carga de asumirla        180 000 al año
coste de delegarla        19 200 al año

  24 000 000 × 0,08 % de comisión
```

El colateral tiene que estar inmovilizado durante el crédito, pero no tiene por qué estarlo en las claves de la entidad. Un custodio autorizado lo resuelve por una novena parte del coste.

## La asesoría se evita sin quitar valor

```text
ANTES  «mejor tipo» destacado
DESPUÉS ordenado por coste total para el
        cliente, criterio publicado, y la
        entidad gana lo mismo con cualquiera

  EL CLIENTE NO PIERDE NADA
  EL RÉGIMEN NO SE ACTIVA
```

Este es el ajuste legítimo. El que no vale es evitar un régimen quitando una función que el cliente necesita: eso no es ajustar el diseño, es empeorar el producto.

## Lo que costó descubrirlo a tiempo

```text
dos ajustes de diseño = una reunión

los mismos dos ajustes en la clase 13,
con el sistema construido = rediseño de
dos componentes
```

El perímetro se determina antes de construir precisamente por esto. Después no desaparece: solo se vuelve caro.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Perímetro supuesto | Se cree saber qué se construye |
| Régimen descubierto tarde | Obliga a rediseñar |
| Ajustar quitando valor | Si el cliente pierde, se asume el régimen |
| Asumir todo régimen activado | Compara carga con aporte |
| No revisar al cambiar el diseño | El perímetro se fijó una vez |

## Límites

- La lista de ocho regímenes cubre los habituales; cada jurisdicción tiene la suya y es la que manda.
- La carga incremental por régimen es un **supuesto**: varía con el tamaño y con la actividad.
- La determinación del perímetro prepara un informe jurídico y **no lo sustituye**.
