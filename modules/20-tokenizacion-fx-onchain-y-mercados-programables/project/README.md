# Proyecto: mercado primario y secundario de un instrumento tokenizado

## Objetivo

Producir el **expediente de diseño** de una infraestructura completa: emitir un
instrumento, liquidarlo de forma atómica, darle mercado secundario y demostrar
que cada promesa del folleto se sostiene con un número.

El proyecto **puede concluir que no procede tokenizar y obtener la máxima
calificación**. Lo que se evalúa es si las doce decisiones están, si cada una
tiene su alternativa medida y si los supuestos están declarados.

## Contexto

Una empresa quiere emitir 40 000 000 en bonos a 3 años con cupón semestral del
6,4 %. Le proponen hacerlo tokenizado, con mercado secundario en la misma
plataforma. Tú preparas el expediente de diseño.

## Alcance

| Incluido | Excluido |
|---|---|
| Registro de referencia y divergencia | Emisión real de cualquier valor |
| Emisión, adjudicación y ciclo de vida | Despliegue en cualquier red |
| Liquidación atómica y sus fallos | Uso de fondos o credenciales reales |
| Mercado secundario y liquidez | Recomendación de inversión |
| Custodia, colateral e interoperabilidad | Asesoría legal o tributaria |

## Las doce decisiones

| # | Decisión | Viene de | Entregable |
|---:|---|---|---|
| 1 | Qué derecho se representa y su régimen | Clase 1 | Calificación con su fundamento |
| 2 | Registro de referencia y divergencia | Clase 2 | Configuración y procedimiento |
| 3 | Mecanismo de adjudicación | Clase 4 | Reglas y prorrateo |
| 4 | Tramo de dinero y su emisor | Clase 10 | Comparación de las cuatro opciones |
| 5 | Procedimiento de emisión desierta | Clase 4 | Mínimo y liberación automática |
| 6 | Eventos programables y no programables | Clase 5 | Clasificación completa |
| 7 | Función de inmovilización y su gobierno | Clase 5 | Quién, cómo y con qué registro |
| 8 | Estructura de mercado | Clase 6 | Continuo, subasta o fórmula |
| 9 | Compromisos de liquidez | Clase 6 | Cinco elementos y cláusulas |
| 10 | Custodia, segregación y sustitución | Clase 9 | Esquema y plan |
| 11 | Conexión con otras infraestructuras | Clase 15 | Modelo elegido |
| 12 | Promesas del folleto con su evidencia | Clase 16 | Tabla completa |

**Cada decisión necesita tres cosas: lo elegido, la alternativa descartada y el
número por el que se decidió.** Una decisión sin alternativa medida es una
preferencia, no una decisión.

## Datos de partida

Se proporcionan como conjunto sintético. Toda cifra adicional que necesites es un
**supuesto tuyo** y debe declararse junto al cálculo que la usa.

```text
INSTRUMENTO
  nominal                            40 000 000
  plazo                                  3 años
  cupón                       6,4 % semestral
  inversionistas objetivo                 1 200
  mínimo propuesto en el folleto          1 000

ENTORNO
  registro oficial disponible                sí
  depósito tokenizado disponible             sí
  CBDC mayorista                             no
  coste unitario de servicio         14 al año
  comisiones de la plataforma          0,9 % anual
  alternativa sin riesgo               4,3 % anual

MERCADO SECUNDARIO ESTIMADO
  volumen mensual                  900 000
  operación media                   22 000
  profundidad al 1 % estimada      180 000
```

## Entregables

```text
project/
├── 01-derecho-y-regimen.md
├── 02-registro-de-referencia.md
├── 03-emision-y-adjudicacion.md
├── 04-tramo-de-dinero.md
├── 05-ciclo-de-vida.md
├── 06-mercado-secundario.md
├── 07-custodia.md
├── 08-interoperabilidad.md
├── 09-folleto-y-evidencias.md
├── supuestos.md            ← todos, en un solo sitio
├── criterios-ejecutados.md ← los ocho, con su resultado
└── calculos/               ← los cuadernos o scripts usados
```

## Los ocho criterios de aceptación

Se **ejecutan**, no se documentan.

| # | Criterio | Cómo se demuestra |
|---:|---|---|
| 1 | Emisión completa, incluido el escenario desierto | Ejecución en pruebas |
| 2 | Pago de cupón con incidencias y reintento | Detalle por titular |
| 3 | Inmovilización con doble aprobación | Registro inmutable |
| 4 | Liquidación atómica con fallo de cada tramo | Estado sin cambios |
| 5 | Divergencia detectada, congelada y resuelta | Traza completa |
| 6 | Sustitución del custodio | Ejecutada sobre la copia |
| 7 | Vencimiento con destrucción solo de lo pagado | Unidades vivas |
| 8 | Medición de profundidad publicada | Serie con fecha |

## Criterios de aceptación del expediente

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Las doce decisiones están presentes | Índice |
| 2 | Cada una tiene su alternativa medida | Revisión decisión a decisión |
| 3 | El registro de referencia está decidido por escrito | Sección 02 |
| 4 | La atomicidad se promete solo si es alcanzable | Coherencia 02 con 04 |
| 5 | El mínimo del folleto es el de equilibrio | Cálculo en 06 |
| 6 | La liquidez declarada es la medida | Serie en 06 |
| 7 | La independencia efectiva de la custodia se mide | Sección 07 |
| 8 | Los ocho criterios se ejecutaron | `criterios-ejecutados.md` |
| 9 | Cada promesa del folleto tiene evidencia o se retira | Sección 09 |
| 10 | Todo supuesto está declarado | `supuestos.md` y en cada cálculo |
| 11 | Hay contingencia por componente con plazo | Sección 08 |
| 12 | No hay ninguna recomendación de inversión | Revisión del texto |

## Hitos

| Semana | Entrega | Decisiones |
|---:|---|---|
| 1 | Derecho, régimen y registro | 1, 2 |
| 2 | Emisión y dinero | 3, 4, 5 |
| 3 | Ciclo de vida y mercado | 6, 7, 8, 9 |
| 4 | Custodia e interoperabilidad | 10, 11 |
| 5 | Folleto, criterios y defensa | 12 |

## La defensa

Veinte minutos ante un comité simulado con un supervisor invitado. Las preguntas
que se harán:

1. ¿Quién manda si el registro del token y el oficial dicen cosas distintas?
2. ¿Puedes prometer liquidación atómica? Demuéstralo.
3. ¿Cuántos días de los últimos seis meses hubo operaciones en el secundario?
4. ¿De dónde sale el mínimo de 1 000?
5. ¿Qué pasa si el custodio pierde la autorización mañana?
6. ¿Quién paga si la emisión queda desierta?
7. ¿Qué promesa del folleto has retirado y por qué?

Una respuesta que empiece por «es más adecuado» sin un número detrás cuenta como
no respondida.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Decisiones 1 y 2 · derecho y registro | 15 |
| Decisiones 3, 4 y 5 · emisión y dinero | 20 |
| Decisiones 6 y 7 · ciclo de vida | 10 |
| Decisiones 8 y 9 · mercado y liquidez | 15 |
| Decisiones 10 y 11 · custodia e interoperabilidad | 15 |
| Decisión 12 · folleto con evidencias | 10 |
| Los ocho criterios ejecutados | 10 |
| Supuestos declarados y alternativas medidas | 5 |

### Penalizaciones

| Situación | Efecto |
|---|---|
| Falta una decisión | −10 por decisión |
| Decisión sin alternativa medida | −5 por decisión |
| Supuesto usado y no declarado | −5 por supuesto |
| Criterio documentado pero no ejecutado | −5 por criterio |
| Promesa sin evidencia mantenida | −10 por promesa |
| Recomendación de inversión | Anula el proyecto |
| Uso de datos reales de personas o entidades | Anula el proyecto |
| Conclusión de que no procede tokenizar, bien fundada | **Sin penalización**: vale igual |

## Restricciones

- **No se emite ningún valor, no se despliega nada en ninguna red y no se mueven
  fondos reales.** Todo el trabajo se hace con los datos sintéticos
  proporcionados.
- **No se usa ninguna credencial, cuenta ni clave real.**
- El expediente **no constituye asesoría de inversión, legal ni tributaria**, y
  debe decirlo en su primera página.
- Las plataformas y emisores reales que se citen se citan por sus documentos
  públicos, con fecha de consulta.
- Ninguna sección puede afirmar que una promesa se cumple sin la evidencia que
  lo demuestre.

## Referencias

- [Parte 21 — índice](../README.md)
- [`apps/tokenization_platform/`](../../../apps/tokenization_platform/README.md)
- [`apps/onchain_fx_lab/`](../../../apps/onchain_fx_lab/README.md)
- [Metodología de verificación regulatoria](../../../docs/metodologia-verificacion-regulatoria.md)
- [Guía de laboratorios digitales](../../../docs/guia-laboratorios-digitales.md)
