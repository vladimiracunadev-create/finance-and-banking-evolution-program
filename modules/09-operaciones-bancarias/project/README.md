# Proyecto integrador: Simulador de operación de sucursal

## De qué se trata

Este proyecto construye la operación de una sucursal y la somete al día que
importa, que no es el día medio.

Casi todos los dimensionamientos se hacen por volumen promedio, y por eso casi
todas las sucursales tienen colas los días de mayor afluencia. Dimensionar por
pico cuesta más en capacidad instalada y menos en espera del cliente, y las dos
cifras se pueden calcular y comparar.

El proyecto **debe declarar el efecto de la migración de canal sobre quien no puede
migrar**. Un ahorro que se obtiene excluyendo a una parte del segmento no es un
ahorro: es un traslado de costo al cliente.

## Contexto

Una sucursal atiende cinco procesos críticos con volumen estacional. El día de
pago de pensiones cuadruplica la afluencia y produce esperas de más de una hora.
La dirección pide una propuesta que reduzca el costo sin empeorar el servicio.

## Alcance

| Incluido | Excluido |
|---|---|
| Dimensionamiento por proceso y por volumen | Datos reales de clientes |
| Conciliación diaria con independencia | Decisiones sobre personal real |
| Costo por transacción y por canal | Datos de sucursales identificables |
| Migración de canal con su accesibilidad | Cierre de sucursales reales |
| Continuidad de los procesos críticos | Datos personales de cualquier tipo |

## Entregables

| # | Entregable | Qué debe contener |
|---:|---|---|
| 1 | Mapa de procesos críticos | Los cinco, con su efecto sobre el cliente y su criticidad |
| 2 | Dimensionamiento por media | Capacidad necesaria y costo |
| 3 | Dimensionamiento por pico | Capacidad necesaria, costo y espera evitada |
| 4 | Comparación de ambos | Costo de capacidad frente a costo de espera |
| 5 | Diseño de la conciliación | Con independencia, frecuencia y escalamiento |
| 6 | Propuesta de migración | Operaciones a migrar, ahorro y clientes que no pueden migrar |
| 7 | Plan de continuidad | De un proceso crítico, con su tolerancia y su nivel de prueba |
| 8 | Indicadores de operación | Con su frecuencia y su umbral |

## Rúbrica

| Criterio | Puntos | Qué se valora |
|---|---:|---|
| Dimensionamiento por pico | 25 | Con la comparación frente a la media |
| Costo de la espera cuantificado | 15 | Aunque no se facture |
| Conciliación con independencia | 15 | Diseñada, no descrita |
| Migración con accesibilidad | 20 | El efecto sobre quien no migra, declarado |
| Continuidad con nivel declarado | 15 | En el gradiente de cinco |
| Indicadores con umbral | 10 | Accionables |

**Total:** 100 puntos. **Aprobación:** 70.

## Restricciones

- **No** se usan datos reales de clientes ni de sucursales identificables.
- **No** se toman decisiones sobre personal real.
- Todos los volúmenes y tiempos son sintéticos y están declarados.
- El efecto de la migración sobre la accesibilidad se declara siempre.
- El nivel de prueba de continuidad se declara en el gradiente de cinco.

## Aviso

Material **docente**. Los volúmenes, tiempos y costos son sintéticos. No
constituye una recomendación de dimensionamiento ni de reorganización para
ninguna entidad real.
