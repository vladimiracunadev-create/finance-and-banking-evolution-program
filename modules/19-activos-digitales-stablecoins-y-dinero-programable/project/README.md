# Proyecto: evaluación de un activo digital para tesorería

## Objetivo

Producir el **expediente de decisión** completo de un activo digital, con dieciséis
piezas calculadas, y llevarlo a un comité simulado que lo aprobará, lo
condicionará o lo rechazará.

El proyecto **puede concluir que el instrumento no es apto y obtener la máxima
calificación**. Lo que se evalúa es si las dieciséis piezas están, si los cálculos son
correctos y si los supuestos están declarados.

## Contexto

Una entidad con 420 000 000 de capital quiere mantener saldo operativo en un
activo digital. Su apetito declarado es del **2 % del capital en instrumentos sin
garantía estatal**. Tú preparas el expediente.

## Alcance

| Incluido | Excluido |
|---|---|
| Clasificación y régimen | Recomendación de inversión |
| Análisis de reservas y redención | Ejecución de operaciones reales |
| Mercado, custodia y contagio | Conexión a redes o plataformas |
| Límites, alertas y plan de salida | Uso de credenciales o fondos reales |
| Tratamiento contable y prudencial | Asesoría legal o tributaria |

## Las dieciséis piezas

| # | Pieza | Viene de | Entregable |
|---:|---|---|---|
| 1 | Ficha de cinco preguntas | Clase 1 | Tabla con las cinco respuestas |
| 2 | Clasificación y perímetro | Clases 1, 9 | Régimen aplicable y qué exige |
| 3 | Reservas y descalce | Clase 4 | Coberturas y composición |
| 4 | Canal de redención | Clases 3, 5 | Quién puede redimir y con qué mínimo |
| 5 | Punto de no retorno | Clase 6 | Porcentaje de circulante |
| 6 | Profundidad y límite | Clase 13 | Medición del libro |
| 7 | Fuente de precio | Clases 13, 19.9 | Método de composición |
| 8 | Custodia | Clase 12 | Esquema e independencia efectiva |
| 9 | Controles de retirada | Clase 12 | Cadena de siete, con tiempos |
| 10 | Exposición indirecta | Clase 14 | Grafo y dependencias comunes |
| 11 | Contable y prudencial | Clases 2, 15 | Tratamiento y su diferencia |
| 12 | Recomendación | Clase 16 | Límites, alertas y salida |
| 13 | Ledger y pasivo completo | Clases 12, 15 | Roll-forward por activo |
| 14 | Conciliación externa | Clase 12 | Banco, exchange y blockchain |
| 15 | Trading y liquidez | Clases 12–15 | Spot, margin, futures y derivatives por libro |
| 16 | Gobernanza | Clase 12 | Seis roles, excepciones y auditoría |

## Datos de partida

Se proporcionan como conjunto sintético. Toda cifra adicional que necesites es un
**supuesto tuyo** y debe declararse junto al cálculo que la usa.

```text
INSTRUMENTO
  circulante                     6 200 000 000
  cobertura declarada                  101,8 %
  informe externo                    mensual, atestación
  mínimo de redención                  250 000
  participantes autorizados                  7
  cláusula de suspensión      «circunstancias extraordinarias»

COMPOSICIÓN DE LA RESERVA
  efectivo y equivalentes                18 %
  letras ≤ 3 meses                       47 %
  deuda 1–2 años                         26 %
  pactos inversos                         9 %

MERCADO
  volumen diario publicado         142 000 000
  profundidad al 1 % (medida)        3 100 000
  volatilidad diaria                     3,8 %

ENTIDAD
  capital                          420 000 000
  saldo operativo objetivo           8 000 000
  apetito                    2 % del capital
```

## Entregables

```text
project/
├── 01-ficha-y-clasificacion.md
├── 02-reservas.md
├── 03-redencion-y-punto-de-no-retorno.md
├── 04-mercado-y-limite.md
├── 05-custodia.md
├── 06-contagio.md
├── 07-contable-y-prudencial.md
├── 08-recomendacion.md
├── 09-ledger-y-conciliacion.md
├── 10-trading-liquidez-y-gobernanza.md
├── supuestos.md            ← todos, en un solo sitio
└── calculos/               ← los cuadernos o scripts usados
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Las dieciséis piezas están presentes | Índice del expediente |
| 2 | La clasificación se justifica por la promesa | Ficha completa |
| 3 | Las coberturas se calculan con descuentos declarados | Cálculo reproducible |
| 4 | El punto de no retorno usa escalera creciente | Comparación con el plano |
| 5 | El límite de posición cuelga de la profundidad | No del volumen |
| 6 | La independencia efectiva se mide | Cuatro factores |
| 7 | La exposición indirecta se calcula | Grafo con fuentes |
| 8 | Cada límite tiene valor, método, frecuencia y disparador | Tabla de límites |
| 9 | El plan de salida incluye el escenario de canal cerrado | Sección explícita |
| 10 | Todo supuesto está declarado | `supuestos.md` y en cada cálculo |
| 11 | Hecho, supuesto e interpretación están separados | Sección de recomendación |
| 12 | No hay ninguna recomendación de inversión | Revisión del texto |
| 13 | Activos propios y custodiados no se netean | Dos ecuaciones separadas |
| 14 | Bruto, disponible y diferencia se calculan por activo | Conciliación a la hora de corte |
| 15 | Los cuatro tipos de trading se atribuyen a su libro | P/L, pasivos, colateral y mandato |
| 16 | Ninguna persona concentra funciones incompatibles | Matriz de seis roles |

## Hitos

| Semana | Entrega | Piezas |
|---:|---|---|
| 1 | Identificación | 1, 2 |
| 2 | Solidez del instrumento | 3, 4, 5 |
| 3 | Mercado y operación | 6, 7, 8, 9 |
| 4 | Encaje y decisión | 10, 11, 12 |
| 5 | Defensa ante el comité | Todo |

## La defensa

Quince minutos ante un comité simulado. Las preguntas que se harán:

1. ¿Qué pasa si el emisor suspende la redención mañana?
2. ¿Cuánto tardamos en salir y cuánto cuesta?
3. ¿Qué exposición tenemos si no compramos nada?
4. ¿De dónde sale ese descuento del 1,4 %?
5. ¿Qué pasa si el proveedor de precios se equivoca?
6. ¿Por qué el balance no coincide con el capital regulatorio?
7. ¿Qué tendría que ocurrir para que revirtamos esta decisión?

Una respuesta que empiece por «es seguro» sin una cifra detrás cuenta como no
respondida.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Piezas 1 y 2 · clasificación y perímetro | 8 |
| Piezas 3, 4 y 5 · solidez del instrumento | 15 |
| Piezas 6 y 7 · mercado y precio | 10 |
| Piezas 8 y 9 · custodia y controles | 12 |
| Pieza 10 · exposición indirecta | 8 |
| Pieza 11 · contable y prudencial | 7 |
| Pieza 12 · recomendación con límites y salida | 7 |
| Piezas 13 y 14 · ledger y conciliación externa | 15 |
| Pieza 15 · trading y liquidez | 10 |
| Pieza 16 · gobernanza y excepciones | 4 |
| Supuestos declarados y capas separadas | 4 |

### Penalizaciones

| Situación | Efecto |
|---|---|
| Falta una pieza | −10 por pieza |
| Límite sin disparador | −5 por límite |
| Supuesto usado y no declarado | −5 por supuesto |
| Recomendación de inversión | Anula el proyecto |
| Uso de datos reales de personas o entidades | Anula el proyecto |
| Conclusión de rechazo bien fundada | **Sin penalización**: vale igual |

## Restricciones

- **No se usa ninguna credencial, cuenta, clave ni fondo real.** Todo el trabajo
  se hace con los datos sintéticos proporcionados o con datos públicos.
- **No se crea ningún activo, ni se despliega nada en ninguna red.**
- **No se produce ninguna herramienta para ocultar fondos, evadir controles ni
  eludir obligaciones de cumplimiento.**
- El expediente **no constituye asesoría de inversión, legal ni tributaria**, y
  debe decirlo en su primera página.
- Los emisores reales que se citen se citan por sus documentos públicos, con
  fecha de consulta.

## Aplicación transversal opcional: GAMECO

El mismo expediente puede aplicarse al [caso GAMECO](../../../case-studies/virtual-economies/gameco.md)
sin alterar las dieciséis piezas: la ficha distingue GEM, item y token; el canal
de redención se reemplaza por cash-out/payout cuando exista; mercado y custodia
se aplican al P2P; y el bloque contable separa bookings, net receipts, revenue,
contract liability y breakage. La conclusión puede ser «unidad interna fuera
del perímetro financiero en la fase A» y debe reabrirse en cada fase posterior.

## Referencias

- [Parte 20 — índice](../README.md)
- [`apps/digital_assets_risk_lab/`](../../../apps/digital_assets_risk_lab/README.md)
- [Metodología de verificación regulatoria](../../../docs/metodologia-verificacion-regulatoria.md)
- [Guía de laboratorios digitales](../../../docs/guia-laboratorios-digitales.md)
