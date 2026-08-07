# Mapa de regulación de mercados digitales

Guía de navegación de la Parte 22: dónde está cada concepto, con qué se conecta y
qué se puede ejecutar para comprobarlo.

## Qué hace distinta a esta parte

Las cinco partes anteriores de la Etapa 5 responden preguntas sobre cómo funciona
algo. Esta responde una pregunta sobre qué está haciendo alguien, y esa diferencia
cambia el método: los hallazgos ya no salen de una medición sino de contrastar lo
que una entidad declara con lo que sus propios documentos describen.

```text
LA REGULACIÓN SIGUE A LA ACTIVIDAD,
NO A LA TECNOLOGÍA

LA PREGUNTA NO ES «¿ESTÁ REGULADO EL TOKEN?»
ES «¿QUÉ ESTÁ HACIENDO ESTA ENTIDAD?»

Y se responde con hechos observables,
no con la calificación que el proyecto elija.
```

## Las seis preguntas del perímetro

Son el punto de entrada de la parte entera. Cada «sí» activa un régimen, y una
misma entidad puede activar varios sin haberse dado cuenta.

| Pregunta | Régimen que activa |
|---|---|
| ¿Recibe fondos del público con obligación de devolverlos? | Captación |
| ¿Custodia activos por cuenta de terceros? | Custodia |
| ¿Pone en contacto oferta y demanda de forma multilateral? | Mercado |
| ¿Ejecuta órdenes por cuenta ajena? | Intermediación |
| ¿Asesora o recomienda? | Asesoría |
| ¿Presta servicios de pago? | Pagos |

Y dos que aparecen al mirar lo accesorio y que casi nadie declara: el crédito
contra el saldo y el cambio de moneda con margen propio.

## Recorrido de la parte

```text
QUÉ HACES         1 · perímetro     2 · misma actividad
                        │
CON QUÉ           3 · calificación del instrumento
                        │
CON QUÉ PERMISO   4 · autorización, registro y supervisión
                        │
QUÉ PROTEGE       5 · emisores      6 · cliente y fondos
AL CLIENTE        7 · CBDC          8 · prudencial
                  9 · custodia en la norma
                        │
QUÉ CONTROLAS    10 · infraestructuras  11 · conducta
                 12 · prevención        13 · datos
                 14 · resiliencia y terceros críticos
                        │
EL CONJUNTO      15 · estabilidad   16 · comparada
                 17 · espacios de prueba
                        │
INTEGRACIÓN      18 · expediente regulatorio
```

## Dónde está cada concepto

| Concepto | Clase | Laboratorio | Código |
|---|:---:|:---:|---|
| Perímetro, calificación y autorización | 1 | 1 | `perimeter` |
| Hecho observable frente a declaración | 1 | 1 | `perimeter` |
| Las seis preguntas | 1 | 1 | `perimeter` |
| Actividad no declarada | 1 | 1 | `perimeter` |
| Lo que aplica sin régimen financiero | 1 | 1 | `perimeter` |
| Misma actividad, mismo riesgo | 2 | 1 | — |
| Los tres límites del principio | 2 | 1 | — |
| Proporcionalidad frente a exención | 2 | 1 | — |
| Los cuatro criterios de valor | 3 | 2 | `qualification` |
| La promoción como prueba | 3 | 2 | `qualification` |
| Utilidad genuina y aparente | 3 | 2 | `qualification` |
| Coste de una recalificación | 3 | 2 | `qualification` |
| Plazo real frente a plazo legal | 4 | 3 | — |
| Carga regulatoria anual | 4 | 3 | — |
| La prueba del caso concreto | 4 | 3 | — |
| Obligaciones del emisor | 5 | 4 | — |
| Plan de rescate y su ejecutor | 5 | 4 | — |
| Protección de conducta y patrimonial | 6 | 4 | `compliance` |
| Las cuatro preguntas de la salvaguarda | 6 | 4 | `compliance` |
| Renuncia a compensar | 6, 9 | 4 | `compliance` |
| Las cuatro decisiones de una CBDC | 7 | 3 | — |
| Curso legal e inclusión | 7 | 3 | — |
| Grupos prudenciales y límite | 8 | 5 | — |
| Exposición por servicios prestados | 8 | 5 | — |
| Las tres segregaciones | 9 | 4 | — |
| Reutilización del activo del cliente | 9 | 4 | — |
| Finalidad técnica y jurídica | 10 | 3 | — |
| Régimen piloto y transición | 10 | 3 | — |
| Las tres familias de abuso | 11 | 6 | `compliance` |
| Precisión y exhaustividad | 11 | 6 | `compliance` |
| Coste marginal frente a medio | 11 | 6 | `compliance` |
| Regla del viaje y resto no identificable | 12 | 5 | — |
| Enfoque basado en riesgo | 12 | 5 | — |
| Dato personal seudónimo | 13 | 5 | — |
| Supresión, conservación e inmutabilidad | 13 | 5 | — |
| Continuidad, resiliencia y ciberseguridad | 14 | 7 | — |
| Tolerancia al impacto | 14 | 7 | — |
| Concentración por infraestructura | 14 | 7 | `compliance` |
| Gradiente de pruebas | 14 | 7 | — |
| Micro frente a macroprudencial | 15 | 8 | — |
| Los cuatro canales de transmisión | 15 | 8 | — |
| Relevancia sistémica y sustituibilidad | 15 | 8 | — |
| Requisito, guía y práctica | 16 | 8 | — |
| Comercialización activa | 16 | 8 | — |
| Límites del arbitraje regulatorio | 16 | 8 | — |
| Hipótesis de un espacio de prueba | 17 | 9 | — |
| Lo que nunca se relaja | 17 | 9 | — |
| Las doce piezas del expediente | 18 | 9 | `dossier` |
| Las cinco parejas críticas | 18 | 9 | `dossier` |
| Medida provisional | 18 | 9 | `dossier` |

## Las seis afirmaciones que la parte desmonta

1. **«Somos tecnología, no finanzas.»** Siete regímenes activados y ninguno
   declarado.
2. **«Es un token de utilidad.»** Cuatro criterios de valor cumplidos, y el que
   los activa es una frase del material comercial.
3. **«Los fondos están en cuenta segregada.»** Falta la renuncia del banco a
   compensar, y con ella se van 4,2 millones.
4. **«Decidir con el coste por caso.»** El medio dice que no y el marginal frente
   al valor dice que sí.
5. **«Trabajamos con 41 proveedores.»** Que se apoyan en tres infraestructuras,
   una con el 86,4 %.
6. **«Las doce piezas están correctas.»** Y el conjunto tiene cuatro hallazgos
   bloqueantes que aparecen al leerlo por parejas.

Las seis tienen una prueba en
[`tests/test_regulatory_perimeter_engine.py`](../tests/test_regulatory_perimeter_engine.py),
y las seis **documentan defectos o errores de razonamiento y deben pasar**.

## Qué se puede ejecutar

```bash
python apps/regulatory_perimeter_engine/cli.py perimeter
```

```bash
python apps/regulatory_perimeter_engine/cli.py qualification
```

```bash
python apps/regulatory_perimeter_engine/cli.py compliance
```

```bash
python apps/regulatory_perimeter_engine/cli.py dossier
```

```bash
python -m pytest tests/test_regulatory_perimeter_engine.py -q
```

## La conclusión que la parte permite

Un expediente de esta parte **puede concluir que la actividad no procede como
está planteada, y eso vale lo mismo que la conclusión contraria** si está
sostenido por las doce piezas con su evidencia.

Y hay una regla que resume la parte entera: **una afirmación sin evidencia se
retira del expediente**, porque un supervisor que encuentra una sin respaldo
revisa las demás con otra actitud.

## Hacia dónde sigue

| De esta parte | A | Qué se profundiza |
|---|---|---|
| Perímetro y calificación (1, 3) | Parte 23 | El régimen del banco digital completo |
| Protección del cliente (6, 9) | Parte 23 | Las garantías del mercado tokenizado |
| Resiliencia y terceros (14) | Parte 23 | La continuidad de la infraestructura |
| Expediente (18) | Parte 23 | La defensa ante el supervisor |

---

**Ver también:** [Parte 22](../modules/21-regulacion-de-mercados-financieros-digitales/README.md) ·
[Etapa 5](etapa-5-finanzas-digitales.md) ·
[Regulatory Perimeter Engine](../apps/regulatory_perimeter_engine/README.md) ·
[Verificación regulatoria](metodologia-verificacion-regulatoria.md) ·
[Glosario de finanzas digitales](glosario-finanzas-digitales.md)
