# Proyecto: expediente regulatorio de una entidad de activos digitales

## De qué se trata

Este proyecto reproduce lo que hace un equipo de cumplimiento cuando el
supervisor anuncia una revisión: reunir doce documentos que ya existen, cruzarlos
y descubrir que el conjunto dice cosas que ninguna de las piezas decía por
separado.

No es un ejercicio de redacción. Las doce piezas se elaboran con los métodos de
las diecisiete clases anteriores —determinar el perímetro por hechos, calificar
por criterios, verificar la salvaguarda con las cuatro preguntas— y el valor del
proyecto está en el paso final: **leer el expediente por parejas de piezas**, que
es como lo lee quien va a hacer las preguntas.

El proyecto **puede concluir que la actividad no procede como está planteada, y
esa conclusión vale lo mismo que la contraria** si está sostenida por las doce
piezas con su evidencia.

## Contexto

Una entidad de custodia y cambio de activos digitales, con 42 000 clientes,
68 000 000 en saldos de moneda y 121 000 000 en activos custodiados, ha recibido
la comunicación de una revisión supervisora en noventa días. Tú diriges la
preparación del expediente.

## Alcance

| Incluido | Excluido |
|---|---|
| Determinación de perímetro y calificación | Asesoría legal de ningún tipo |
| Vía de autorización y régimen por jurisdicción | Redacción de documentos vinculantes |
| Protección del cliente y de sus fondos | Uso de datos reales de personas |
| Programas de cumplimiento y vigilancia | Técnicas para eludir cualquier control |
| Resiliencia, terceros críticos y prudencial | Interlocución real con una autoridad |

## Las doce piezas

Cada una viene de una clase y se elabora con su método. La columna de la derecha
indica qué evidencia hay que adjuntar, porque una afirmación sin evidencia se
retira del expediente.

| # | Pieza | Clase | Evidencia exigida |
|---:|---|:---:|---|
| 1 | Perímetro determinado por hechos | 1 | Hechos con su fuente verificable |
| 2 | Calificación de los instrumentos | 3 | Material de promoción fechado |
| 3 | Vía de autorización y calendario | 4 | Requisitos con su forma de acreditación |
| 4 | Régimen por jurisdicción | 16 | Tabla con nivel, referencia y fecha |
| 5 | Salvaguarda y segregación | 6, 9 | Contratos y renuncia a compensar |
| 6 | Información y conducta | 6, 11 | Piezas comerciales vigentes |
| 7 | Programa de prevención de lavado | 12 | Análisis de riesgo escrito |
| 8 | Tratamiento de datos personales | 13 | Registro de actividades y bases |
| 9 | Vigilancia de conducta de mercado | 11 | Métricas del último trimestre |
| 10 | Resiliencia y terceros críticos | 14 | Mapa con subcontratación y pruebas |
| 11 | Capital, liquidez y prudencial | 8 | Cálculo por exposición |
| 12 | Hallazgos, remediación y revisión | 18 | Lectura cruzada y plan |

## Las cinco parejas críticas

El paso que da valor al proyecto. Cada pareja enfrenta lo que una pieza afirma
con lo que otra describe, y ahí es donde aparecen las contradicciones.

```text
perímetro     x resiliencia
calificación  x información y conducta
salvaguarda   x prevención de lavado
datos         x vigilancia de mercado
jurisdicción  x información y conducta
```

Si al cruzarlas no aparece ninguna contradicción, hay dos posibilidades: que el
expediente sea excelente o que las piezas se hayan escrito para coincidir. La
segunda es más frecuente, y se detecta comprobando si cada pieza fue elaborada
antes de conocer las demás.

## Datos de partida

Se proporcionan como conjunto sintético. Toda cifra adicional es un **supuesto
tuyo** y debe declararse junto al cálculo que la usa.

```text
ENTIDAD
  clientes                                42 000
  saldos en moneda                    68 000 000
  activos custodiados                121 000 000
  deuda con el banco depositario        4 200 000
  conciliación                           semanal
  esquema de claves        3-de-5, 4 en la sede
  jurisdicciones con clientes                  3
  proveedores declarados                       9

VIGILANCIA
  operaciones al mes                     412 000
  alertas                                  3 640
  casos confirmados                           44
  casos conocidos a posteriori                62

PRUDENCIAL
  capital de nivel 1                 320 000 000
  exposición directa declarada                 0
```

## Entregables

```text
project/
├── 01-perimetro.md
├── 02-calificacion.md
├── 03-autorizacion.md
├── 04-regimen-por-jurisdiccion.md
├── 05-salvaguarda.md
├── 06-informacion-y-conducta.md
├── 07-prevencion-de-lavado.md
├── 08-datos-personales.md
├── 09-vigilancia-de-mercado.md
├── 10-resiliencia.md
├── 11-prudencial.md
├── 12-hallazgos-y-remediacion.md
├── supuestos.md            ← todos, en un solo sitio
├── lectura-cruzada.md      ← las cinco parejas
└── calculos/               ← los cuadernos o scripts usados
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Las doce piezas están presentes | Índice del expediente |
| 2 | Ninguna afirmación sin evidencia | Revisión pieza a pieza |
| 3 | El perímetro se determina por hechos con fuente | Sección 01 |
| 4 | La calificación analiza el material de promoción | Sección 02 |
| 5 | La salvaguarda responde las cuatro preguntas | Sección 05 |
| 6 | El programa de prevención deriva de un análisis escrito | Sección 07 |
| 7 | La vigilancia declara precisión y exhaustividad | Sección 09 |
| 8 | El mapa de terceros incluye subcontratación | Sección 10 |
| 9 | Las cinco parejas se cruzan | `lectura-cruzada.md` |
| 10 | Los hallazgos se priorizan por efecto sobre el cliente | Sección 12 |
| 11 | Cada remediación tiene medida provisional | Sección 12 |
| 12 | Toda norma citada lleva su fecha de verificación | Revisión completa |

## Hitos

| Semana | Entrega | Piezas |
|---:|---|---|
| 1 | Qué hacemos | 1, 2 |
| 2 | Con qué permiso | 3, 4 |
| 3 | Qué protege al cliente | 5, 6 |
| 4 | Qué controlamos | 7, 8, 9 |
| 5 | Con qué soporte | 10, 11 |
| 6 | Cruce, hallazgos y defensa | 12 |

## La defensa

Treinta minutos ante un comité con un supervisor invitado. Las preguntas salen de
las mismas piezas y son predecibles, que es justamente por lo que no hay excusa
para no tenerlas preparadas:

1. ¿Qué actividades ejercen y con qué hechos lo sostienen?
2. Si quiebran mañana, ¿qué recupera el cliente, cuándo y de quién?
3. ¿Cuántos clientes no pueden ejercer un derecho que su contrato les reconoce?
4. ¿De quién dependen y quién más depende de lo mismo?
5. ¿Qué casos de conducta anómala no detectan y por qué?
6. ¿Qué hallazgo no han corregido y qué protege al cliente mientras tanto?
7. ¿Qué han retirado del expediente por no poder sostenerlo?

Una respuesta que empiece por «creemos que» cuenta como no respondida. Una que
diga «hoy no puedo afirmarlo, y esta es la razón» cuenta como respondida.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Piezas 1 y 2 · perímetro y calificación | 15 |
| Piezas 3 y 4 · autorización y jurisdicciones | 10 |
| Piezas 5 y 6 · protección del cliente | 15 |
| Piezas 7, 8 y 9 · controles | 15 |
| Piezas 10 y 11 · soporte y prudencial | 10 |
| Lectura cruzada de las cinco parejas | 20 |
| Hallazgos priorizados con medida provisional | 10 |
| Supuestos declarados y normas fechadas | 5 |

### Penalizaciones

| Situación | Efecto |
|---|---|
| Falta una pieza | −10 por pieza |
| Afirmación sin evidencia mantenida | −10 por afirmación |
| Norma citada sin fecha de verificación | −5 por cita |
| Remediación sin medida provisional | −5 por hallazgo |
| Presentar el expediente como asesoría legal | Anula el proyecto |
| Incluir técnicas para eludir un control | Anula el proyecto |
| Uso de datos reales de personas | Anula el proyecto |
| Concluir que la actividad no procede, bien fundado | **Sin penalización**: vale igual |

## Restricciones

- **Nada de este proyecto constituye asesoría legal**, y el expediente debe
  decirlo en su primera página.
- Toda norma citada lleva **autoridad, identificador y fecha de verificación**,
  más la advertencia de comprobar en la fuente oficial vigente.
- Los datos son sintéticos. **No se usan datos reales de personas ni de
  entidades**, y las entidades reales que se citen se citan por sus documentos
  públicos con fecha de consulta.
- El proyecto **no produce ni describe técnicas para eludir controles, ocultar
  actividad o evitar la aplicación de una norma**.
- El expediente prepara una discusión con especialistas; no la sustituye.

## Referencias

- [Parte 22 — índice](../README.md)
- [`apps/regulatory_perimeter_engine/`](../../../apps/regulatory_perimeter_engine/README.md)
- [Metodología de verificación regulatoria](../../../docs/metodologia-verificacion-regulatoria.md)
- [Fichas normativas](../../../regulatory/README.md)
