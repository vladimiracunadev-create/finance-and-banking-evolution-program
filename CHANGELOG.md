<!-- portada:inicio -->
<div align="center">

# 📜 Historial de cambios

**Todo lo que ha cambiado en el programa, versión a versión, con el formato Keep a Changelog.**

[![versión](https://img.shields.io/badge/versi%C3%B3n-2.2.0-e67e22?style=flat-square)](CHANGELOG.md)
[![formato](https://img.shields.io/badge/formato-Keep%20a%20Changelog%20%C2%B7%20SemVer-1f6feb?style=flat-square)](https://keepachangelog.com/es-ES/1.1.0/)

[🏠 Inicio](README.md) ·
[📊 Estado](STATUS.md) ·
[🗺️ Roadmap](ROADMAP.md)

</div>
<!-- portada:fin -->

---

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y el
versionado sigue [SemVer](https://semver.org/lang/es/).

---

## [2.2.0] — 2026-08-12

Regulación con nombre propio y la biblioteca de casos. Hasta esta versión, la
Parte 22 enseñaba a determinar un perímetro sin decir en qué país; el método
estaba completo y nunca se aplicaba a una norma concreta. Esta versión cierra esa
brecha con cuatro clases sobre dos regímenes reales, y añade los veintiséis casos
que el repositorio declaraba pendientes desde la 1.0.0.

### ✨ Añadido

- **Parte 22 · cuatro clases nuevas** que leen regímenes concretos en lugar de
  describir principios:
  - clase 17 · **MiCA I: perímetro, activos y participantes** — el embudo de tres
    filtros, las tres categorías y por qué el libro blanco no es una autorización;
  - clase 18 · **MiCA II: obligaciones, reservas y supervisión** — las cuatro
    reglas de la reserva, el reembolso a la par y la diferencia entre el plan de
    recuperación y el plan de reembolso;
  - clase 19 · **Regímenes europeos conexos** — régimen piloto DLT, resiliencia
    operativa y regla del viaje, con el reparto de coste que demuestra que MiCA
    suele ser la quinta parte de la carga regulatoria;
  - clase 20 · **El Salvador: bitcoin, Chivo y activos digitales** — tres
    decisiones en una sola ley y siete resultados que no se promedian.
- **Biblioteca de casos** en `case-studies/`: **26 casos** en 13 temas, todos con
  la misma estructura de diez bloques —hechos, actores, decisiones, riesgos,
  regulación, controles, resultado, lecciones, preguntas y fuentes— y con la
  separación explícita entre hecho verificado, supuesto del ejercicio e
  interpretación.
- **Cinco fichas normativas** nuevas en `regulatory/`: Ley Bitcoin de El Salvador
  y su reforma, Ley de Emisión de Activos Digitales, resiliencia operativa
  digital de la Unión Europea, reglamento europeo sobre la información que
  acompaña a las transferencias, y la norma de carácter general chilena de
  prestadores de servicios financieros.
- **Siete documentos** en `docs/`:
  - `mapa-stablecoins.md` — la ruta transversal completa, de diseño a resolución;
  - `mapa-fx-onchain.md` — el cambio de divisas sobre infraestructura programable;
  - `arquitectura-mercado-tokenizado.md` — las nueve piezas y las cinco
    decisiones que ninguna tecnología resuelve;
  - `mapa-regulatorio-chile.md` — matriz de actividad, norma, autoridad y clase;
  - `mapa-regulatorio-internacional.md` — el método de comparación y quién
    produce qué;
  - `guia-docente-etapa-5.md` — qué cambia al enseñar las Partes 17 a 23;
  - `referencias-oficiales-digitales.md` — dónde verificar cada cosa.

### 🔧 Cambiado

- La Parte 22 pasa de **18 a 22 clases**. Las dos últimas se renumeran: espacios
  de prueba pasa de la 17 a la 21, y el proyecto de expediente regulatorio de la
  18 a la 22. Las referencias cruzadas del resto de la parte se actualizaron en
  consecuencia.
- El programa pasa de **352 a 356 clases** y de **528 a 534 horas** de sesión.
  Todas las cifras de `STATUS.md`, `SYLLABUS.md`, `FILE_INDEX.md` y el glosario
  maestro se regeneraron desde los archivos.
- `tools/progress.py` actualiza el plan de la Parte 22 a 22 clases, para que el
  avance declarado no supere el cien por cien.
- `ROADMAP.md` cierra la línea «Biblioteca de casos», que figuraba como abierta.
- `docs/README.md` incorpora los siete documentos nuevos y la biblioteca de casos.

### 📚 Documentación

- El glosario maestro pasa de 2 175 a **2 198 términos**.
- El índice del manual pasa de 380 a **384 entradas**.

### 🔐 Seguridad

- Las cuatro clases nuevas y los veintiséis casos declaran de forma expresa que
  los regímenes citados **no son derecho aplicable en Chile** cuando son
  extranjeros, y que sus cifras son sintéticas.
- Ningún caso atribuye a una entidad identificable un fallo, una pérdida o una
  infracción.

### 🧭 Notas de migración

- Quien tenga enlaces a `modules/21-.../classes/17-espacios-de-prueba-*.md` o a
  `18-proyecto-expediente-regulatorio.md` debe apuntarlos a `21-` y `22-`
  respectivamente. Los enlaces internos del repositorio ya se actualizaron y
  `tools/check_links.py` los verifica.

---

## [2.1.0] — 2026-08-07

Portal de estudio propio, aplicaciones para teléfono y escritorio, y el primer
release del repositorio.

### ✨ Añadido

- **Portal de estudio** con portada propia, temario de las 352 clases y buscador
  que indexa títulos, niveles y los 2 629 conceptos centrales. Instalable en el
  teléfono: manifiesto, iconos y trabajador de servicio para releer sin conexión
  lo ya visitado.
- **Aplicación de Android** (`mobile/`): WebView sobre el HTML del portal,
  embebido en el APK. El manifiesto no declara `android.permission.INTERNET`,
  de modo que la ausencia de telemetría se puede comprobar desde los ajustes.
- **Aplicación de Windows** (`desktop/`): lector en PySide6 con QtWebEngine
  sobre el mismo HTML, portable y sin instalador.
- **Flujo `apps.yml`**: genera el sitio una vez y de ahí salen las tres piezas.
  Antes de publicar abre cada artefacto y cuenta las clases que contiene.
- Portada, insignias y navegación en los 29 documentos, también en los cuatro
  que se generan.
- El manual se publica como descarga del portal, en PDF, HTML y Markdown.

### 🐛 Corregido

- **El manual titulaba «🎯 Propósito» las 352 clases**: el generador leía el
  título del cuerpo, pero el H1 vive dentro del bloque generado que se limpia.
  Además se perdía esa sección en todas las clases.
- **El PDF salía sin marcadores ni numeración**. Ahora lleva 380 marcadores en
  tres niveles y folio al pie.
- **La impresión del PDF fallaba en silencio**: el navegador imprime en segundo
  plano y sale con código 0 en décimas de segundo.
- **El portal servía el README sin convertir** desde su rediseño: faltaba
  `md_in_html`, así que todo lo que va dentro de `<div>` salía como texto plano.
- **El APK compilaba sin firmar**, y Android no instala un APK sin firma.
- Cifras obsoletas en la documentación: «240 clases» y «360 horas».
- «periodo de gracia» figuraba dos veces en el glosario, con y sin tilde.

### 🔄 Cambiado

- La entrada del portal es la portada, no el README volcado.
- El despliegue verifica las tres descargas del manual por código y por peso.

---

## [2.0.0] — 2026-08-07

Séptima y última parte de la **Etapa 5**, y cierre del programa. Con ella existen
las siete partes de la etapa, y por eso se libera la versión que estaba reservada
desde la 1.2.0: **el programa pasa de 240 clases en 16 partes a 352 clases en 23
partes**, agrupadas en cinco etapas que se recorren en orden.

La Parte 23 no introduce ningún concepto nuevo, y esa es su dificultad. Reúne los
métodos de las veintidós anteriores y los somete a la única prueba que ninguna de
ellas podía aplicar: hacerlos funcionar juntos. Al integrarlos aparecen
contradicciones entre decisiones que eran correctas por separado, y esas
contradicciones son el contenido de la parte.

### Añadido

**Parte 23 — Proyecto: banco digital y mercado tokenizado**

- 18 clases de 90 minutos organizadas en tres bloques: qué construir (1-6),
  construirlo y encontrar las contradicciones (7-12), y probarlo y defenderlo
  (13-18).
- Una **cadena de decisiones** explícita —alcance, registro, dinero, producto—
  donde la clase 4 deja su conclusión pendiente de la 5 en vez de resolverla por
  adelantado. Cerrar la cadena al revés es el error de capstone más difícil de
  detectar, porque el resultado parece coherente.
- 9 laboratorios con solución de referencia comentada.
- Evaluación diagnóstica y final. La final califica algo distinto de las
  anteriores: **no si se sabe cada tema, sino si el conjunto se sostiene ante
  alguien que busca dónde se contradice**.
- Proyecto capstone en tres fases, con doce entregables y la restricción de que
  una tensión sin resolver bloquea la operación.

**Aplicación `apps/digital_bank_capstone/`**

- `scope`: las cuatro preguntas por función, exclusiones que exigen razón escrita
  y el cálculo de la carga regulatoria y la facturación necesaria.
- `build`: construir, integrar o comprar, con la salida real por encima del coste
  y la medición de la concentración del sector.
- `tensions`: decisiones, tolerancias que solo el consejo puede fijar y tensiones
  que exigen declarar y cuantificar el sacrificio.
- `stress`: fuente de correlación, escenario que debe afectar a más de un
  componente y punto de rotura medido en desviaciones.
- 24 pruebas, cuatro de las cuales **documentan razonamientos del capstone y
  deben pasar**.

**Documentación**

- `docs/mapa-capstone.md` con la cadena de decisiones, la tabla de dónde está
  cada cosa y las cinco afirmaciones que la parte desmonta.
- Seis términos nuevos en el glosario digital, en una sección propia de diseño de
  sistemas completos.

### Cambiado

- **El programa deja de estar en ampliación activa.** El README raíz, la ficha
  técnica y la hoja de ruta describen ahora un programa completo de cinco etapas
  y veintitrés partes, en vez de una etapa en curso.
- La cifra publicada pasa a **352 clases en 23 partes** (528 horas), con 150
  laboratorios, 46 evaluaciones, 23 proyectos y 11 aplicaciones.
- El trabajo transversal que sigue abierto —biblioteca de casos, bloques «para
  profundizar» en las partes antiguas y más fichas normativas— se separa en la
  hoja de ruta del trabajo de la etapa, que está cerrado.

---

## [1.7.0] — 2026-08-06

Sexta parte de la **Etapa 5**: el régimen que alcanza a la infraestructura
construida en las cinco anteriores. Cambia el registro del programa —las
respuestas dejan de depender de cómo funciona algo y pasan a depender de qué está
haciendo alguien— y por eso esta entrega incorpora además la corrección
pedagógica que faltaba en toda la etapa.

### Añadido

**Parte 22 — Regulación de mercados financieros digitales**

- 18 clases de 90 minutos, con el eje de que **la regulación sigue a la
  actividad, no a la tecnología**, y con la clase 2 dedicada íntegramente a los
  tres límites de ese principio: el riesgo cambia, el sujeto puede no existir y
  hay riesgos sin precedente.
- 9 laboratorios con solución de referencia comentada.
- Evaluación diagnóstica y final, con un criterio transversal nuevo: una
  afirmación regulatoria sin la norma citada y su fecha **no puntúa, aunque sea
  correcta**.
- Proyecto integrador «expediente regulatorio» de doce piezas, cuyo valor está en
  la lectura cruzada por parejas: las contradicciones no están dentro de ninguna
  pieza, están entre dos.

**Aplicación `apps/regulatory_perimeter_engine/`**

- `perimeter`: las seis preguntas aplicadas sobre hechos con fuente obligatoria;
  un hecho sin fuente se rechaza, porque es una declaración disfrazada.
- `qualification`: los cuatro criterios, con análisis del material de promoción
  en vez de pregunta al emisor.
- `compliance`: las cuatro preguntas de la salvaguarda con su cuantificación,
  vigilancia con coste marginal frente a medio, y concentración medida por
  proveedor y por infraestructura para poder contrastarlas.
- `dossier`: las doce piezas, las cinco parejas críticas, la priorización por
  efecto sobre el cliente y la remediación que exige medida provisional.
- 29 pruebas, seis de las cuales **documentan defectos o errores de razonamiento
  y deben pasar**.

**Documentación y metadatos**

- `docs/mapa-regulatorio.md` con las seis preguntas del perímetro, la tabla de
  dónde está cada concepto y las seis afirmaciones que la parte desmonta.
- 21 términos nuevos en el glosario digital, cada uno con su «qué NO significa».

### Cambiado

- **Prosa pedagógica en todo el material de la etapa.** El README de cada parte
  abre con una explicación narrativa de qué trata y una sección que explica **por
  qué cada clase lleva a la siguiente**; las clases incorporan párrafos que
  presentan cada bloque y extraen su consecuencia, y los laboratorios abren con
  el porqué del ejercicio. La estructura de secciones no cambia: la prosa se
  añade.
- **README raíz coherente.** Las cinco etapas se presentan con el mismo formato y
  el mismo nivel de detalle, en vez de destacar la ampliación más reciente sobre
  las demás.
- La cifra publicada pasa a **334 clases en 22 partes** (501 horas).

---

## [1.6.0] — 2026-08-06

Quinta parte de la **Etapa 5**: el instrumento financiero anotado en el registro.
Su pregunta central es jurídica antes que técnica, y decide si el único beneficio
exclusivo de la tokenización es alcanzable.

### Añadido

**Parte 21 — Tokenización, FX on-chain y mercados programables**

- 16 clases de 90 minutos, con el eje de que **tokenizar no crea un derecho: lo
  representa**, y que si el registro oficial sigue mandando, la liquidación
  atómica es imposible por construcción.
- De cinco promesas habituales de la tokenización, la parte demuestra que **dos
  resisten**: la operación fuera del horario del sistema de pagos y la
  liquidación atómica contra el dinero, esta última solo si ambos tramos están
  en el mismo registro.
- 8 laboratorios con solución de referencia comentada.
- Evaluación diagnóstica y final con rúbrica que no puntúa las decisiones
  justificadas por «es más adecuado».
- Proyecto integrador de doce decisiones, cada una con su alternativa medida, que
  **puede concluir que no procede tokenizar y obtener la máxima calificación**.

**Aplicación `apps/tokenization_platform/`**

- `registry`: espejo frente a bloqueo de origen, con las seis causas de
  divergencia, conciliación completa, congelación simultánea y autoridad de
  resolución obligatoria.
- `issuance`: libro de órdenes, tres mecanismos de adjudicación, coste del
  bloqueo del importe y emisión desierta con liberación automática.
- `lifecycle`: cupón que verifica el aprovisionamiento **antes** de pagar,
  inmovilización con doble aprobación y vencimiento que destruye solo lo
  confirmado.
- `settlement`: entrega contra pago que rechaza antes de bloquear, con
  `observar()` para poder probar la ausencia de estado intermedio, y que se niega
  a operar si el tramo de dinero está fuera del registro.
- `collateral`: recorte, colchón, cascada de liquidaciones y la corrección que la
  apaga sin tocar ningún parámetro de riesgo.

**Aplicación `apps/onchain_fx_lab/`**

- `pricing`: coste total por ruta con los seis tramos y corrección por
  profundidad del libro.
- `amm`: producto constante, deslizamiento y pérdida por divergencia, con la
  razón crítica resuelta por bisección.
- `settlement`: ventana de irrevocable a confirmado, y comparación de neteo,
  límites y pago contra pago **contra la misma base**, con la oponibilidad del
  acuerdo como parámetro explícito.

- 62 pruebas entre ambas aplicaciones, cinco de las cuales **documentan defectos
  o errores de razonamiento y deben pasar**.

**Documentación y metadatos**

- `docs/mapa-tokenizacion.md` con las cuatro preguntas de viabilidad, la tabla de
  dónde está cada concepto y las seis afirmaciones que la parte desmonta.
- 20 términos nuevos en el glosario digital, cada uno con su «qué NO significa».
- Fichas normativas del régimen piloto DLT de la Unión Europea y de los
  Principios para las Infraestructuras del Mercado Financiero.

### Cambiado

- La cifra publicada pasa a **316 clases en 21 partes** (474 horas).
- `README.md`, `MANIFEST.md` y `ROADMAP.md` reflejan cinco de las siete partes de
  la Etapa 5 publicadas. La versión `2.0.0` sigue reservada para cuando existan
  las siete.

---

## [1.5.0] — 2026-08-06

Cuarta parte de la **Etapa 5**: lo que circula sobre el registro. El eje es que
un activo digital no es una tecnología sino una promesa anotada, y que
clasificarlo no exige mirar ni una línea de código.

### Añadido

**Parte 20 — Activos digitales, stablecoins y dinero programable**

- 16 clases de 90 minutos, con la ficha de cinco preguntas —quién promete, qué
  promete, con qué respaldo, exigible cuándo y ante quién— como criterio único
  de clasificación. Ninguna de las cinco es técnica.
- Separación estricta de cinco instrumentos que se confunden a diario:
  criptoactivo no respaldado, stablecoin, dinero electrónico, depósito
  tokenizado y CBDC. La distinción decide quién quiebra, qué garantía aplica y
  a quién reclama el cliente.
- 8 laboratorios con solución de referencia comentada.
- Evaluación diagnóstica y final con guía de corrección y rúbrica que penaliza
  el supuesto oculto el doble de lo que valía la cifra.
- Proyecto integrador «expediente de decisión» de doce piezas, que **puede
  concluir que el instrumento no es apto y obtener la máxima calificación**.

**Aplicación `apps/digital_assets_risk_lab/`**

- `classification`: ficha de cinco preguntas y rastreo del respaldo hasta un
  activo externo, con detección de circularidad.
- `reserves`: cobertura contable, cobertura líquida a 24 horas, escalera de
  descuentos creciente y punto de no retorno.
- `redemption`: orden de llegada frente a prorrateo, comisión antidilución y
  tramo mínimo íntegro, con la ventaja del primero como métrica.
- `depeg`: banda de no arbitraje, vigilancia de desvío persistente y las cinco
  fases de una corrida.
- `algorithmic`: espiral de dos tokens, con el ratio de absorción y la emisión
  por unidad retirada calculados en paralelo.
- `custody`: independencia efectiva por cuatro factores, recuperación con
  retardo y los siete controles de retirada.
- `market`: libro con importe acumulado, profundidad, impacto y límite de
  posición colgado de la profundidad, no del volumen.
- `contagion`: grafo de exposición, segundo grado, dependencias comunes y
  cascada de liquidez.
- 49 pruebas, seis de las cuales **documentan defectos y deben pasar**.

**Documentación y metadatos**

- `docs/mapa-activos-digitales.md` con el recorrido, la tabla de dónde está cada
  concepto y las seis afirmaciones que la parte desmonta.
- 24 términos nuevos en el glosario digital, cada uno con su «qué NO significa».
- Fichas normativas del Reglamento (UE) 2023/1114, de la norma prudencial SCO60
  de Basilea y de las recomendaciones del FSB sobre stablecoins globales.

### Cambiado

- La cifra publicada pasa a **300 clases en 20 partes** (450 horas).
- `README.md`, `MANIFEST.md` y `ROADMAP.md` reflejan cuatro de las siete partes
  de la Etapa 5 publicadas. La versión `2.0.0` sigue reservada para cuando
  existan las siete.

---

## [1.4.0] — 2026-08-06

Tercera parte de la **Etapa 5**: el registro distribuido. Se estudia como una
opción de arquitectura, no como una conclusión, y la parte enseña sobre todo a
decidir cuándo **no** hace falta.

### Añadido

**Parte 19 — Blockchain y DLT para instituciones financieras**

- 14 clases de 90 minutos, con el eje de que un registro distribuido resuelve un
  problema —que partes que no confían entre sí ni en un tercero común mantengan
  un registro que ninguna controla— y lo resuelve caro: redundancia total,
  lentitud e irreversibilidad.
- Seis preguntas de criterio, de las que **solo la de confianza** justifica por
  sí sola la arquitectura; las otras cinco se resuelven mejor de otra forma.
- 6 laboratorios con solución de referencia comentada.
- Evaluación diagnóstica y final con guía de corrección.
- Proyecto integrador «expediente de decisión», que **puede concluir que no hace
  falta un registro distribuido y obtener la máxima calificación**.

**Aplicación `apps/dlt_financial_lab/`**

- Cadena con estado, instantáneas, número de orden por cuenta y reescritura
  completa: `recalcular_desde` devuelve la cadena a un estado válido, que es
  justo lo que el laboratorio quiere demostrar.
- Árbol de Merkle con prefijos distintos para hoja y nodo, sumas por nodo,
  prueba de inclusión y prueba de exclusión sobre un orden total. El nodo suelto
  de un nivel impar se **promueve** en vez de duplicarse: duplicarlo sumaría su
  valor dos veces y la raíz dejaría de declarar la suma real.
- Consenso con nodos honestos, silenciosos, mentirosos y **con defecto común**,
  más `independencia_efectiva` para medir cuántos comparten implementación.
- Contrato de depósito en garantía con y sin reentrada, e interruptor que solo
  detiene: no altera saldos ni transfiere.
- Oráculo con mediana, banda de descarte y mínimo de fuentes vivas.
- Firma múltiple con análisis de correlación entre guardianes.
- 38 pruebas, tres de las cuales **documentan defectos y deben pasar**:
  `test_recalcular_toda_la_cadena_NO_se_detecta`,
  `test_un_fallo_comun_produce_acuerdo_erroneo` y
  `test_el_ataque_de_reentrada_vacia_el_contrato_defectuoso`.

**Documentación**

- `docs/mapa-blockchain-dlt.md` con el recorrido de la parte, la tabla de dónde
  está cada concepto y las cinco afirmaciones que desmonta.
- Ampliación del glosario digital con los 12 términos de la parte, cada uno con
  su «qué NO significa».

### Cambiado

- La cifra publicada pasa a **284 clases en 19 partes** (426 horas).
- `README.md`, `MANIFEST.md` y `ROADMAP.md` reflejan tres de las siete partes de
  la Etapa 5 publicadas. La versión `2.0.0` sigue reservada para cuando existan
  las siete: declararla antes contradiría el principio del repositorio de que la
  documentación nunca declara más de lo que existe.

---

## [1.3.0] — 2026-08-06

Segunda parte de la **Etapa 5**: la infraestructura por la que un pago cruza una
frontera. Continúa desde la Parte 10 hacia la corresponsalía, la mensajería
ISO 20022, la liquidación y las arquitecturas que intentan sustituirla.

### Añadido

**Parte 18 — Pagos transfronterizos, remesas y liquidación internacional**

- 16 clases de 90 minutos, con el eje de que **un mensaje no es un movimiento de
  fondos**: la red transporta instrucciones, el dinero se mueve en cuentas, la
  liquidación ocurre en un sistema de pagos y la finalidad la da la norma.
- 8 laboratorios con solución de referencia comentada.
- Evaluación diagnóstica y final con guía de corrección y cálculos resueltos.
- Proyecto integrador «red de pagos transfronterizos» con seis corredores, cada
  uno diseñado para forzar una decisión distinta del motor de rutas.

**Aplicación `apps/cross_border_payments_lab/`**

- Los cuatro flujos modelados por separado, con husos, ventanas y calendarios.
- Motor de rutas con tres filtros y tres factores: un filtro de cumplimiento no
  se compensa con precio, y hay una prueba que lo demuestra.
- Construcción y validación de `pacs.008`, `pacs.002` y la máquina de estados
  que impide devolver antes de liquidar.
- Screening con precisión, exhaustividad y prueba retrospectiva.
- Liquidación con pago contra pago, incluidos los dos escenarios de fallo.
- Enlace de pagos inmediatos con resolución de alias y subasta de liquidez.
- Comparación honesta de la ruta con stablecoin, con el ahorro descompuesto por
  fuente.
- 56 pruebas, cada una asociada a una afirmación concreta de una clase.

**Herramientas**

- `tools/validate_iso20022.py`: campos obligatorios, formato de importe, divisa
  ISO, direcciones estructuradas, códigos de propósito y **referencia estable**
  entre reintentos. Es independiente del espacio de nombres del esquema, para
  que no deje de funcionar en la siguiente versión.

**Datos y metadatos**

- `datasets/synthetic/remittance_corridors.csv` (36 rutas, 9 corredores) y
  `sanctions_screening_alerts.csv` (12 000 alertas con resolución etiquetada),
  ambos con ficha, supuestos y **limitaciones explícitas**.
- Fichas normativas de la Recomendación 16 del GAFI y de la hoja de ruta del G20.

**Documentación**

- `docs/mapa-pagos-transfronterizos.md` y ampliación del glosario digital con
  los 12 términos de la parte.

### Cambiado

- La CI valida los mensajes ISO 20022 en cada cambio.
- `tools/build_file_index.py` usa `--cached --others --exclude-standard`: el
  índice ya no depende de si se generó antes o después de `git add`.
- `tools/build_site.py` descubre los adjuntos enlazados leyendo los enlaces
  reales, en lugar de una lista mantenida a mano.

### Corregido

- **Base del diferencial de cambio (Parte 18, clase 9).** El material medía el
  diferencial sobre la cotización inversa (28/950 = 2,947 %) cuando la pérdida
  del cliente es 1 − 950/978 = 2,863 %. Con la base equivocada, la composición
  del diferencial cruzado no cuadraba con el cálculo directo. La clase explica
  ahora la diferencia y el laboratorio la comprueba.
- **Descomposición del ahorro de la ruta con stablecoin.** Las partes no sumaban
  el ahorro total, lo que producía porcentajes sin sentido. Ahora suman, incluida
  una componente negativa que el análisis honesto no puede ocultar.
- `CHANGELOG.md`: 66 líneas con codificación corrompida en la entrada 1.1.0.

### Seguridad

- Las listas de sanciones y los nombres del laboratorio son sintéticos y se
  declara en cada salida. El módulo **no sirve para calibrar un sistema real**.
- El screening nunca descarta un caso por **falta** de información: lo escala.
  Descartar por ausencia de dato es el falso negativo que la Parte 18 persigue.

### Notas de migración

- Las Partes 1 a 17 no cambian.
- Quien tuviera un guion contra `tools/build_file_index.py` debe saber que ahora
  incluye los archivos sin rastrear que no están ignorados.

---

## [1.2.0] — 2026-08-06

Comienza la **Etapa 5 — Finanzas digitales, infraestructura y mercados
tokenizados**, que continúa el programa desde la introducción fintech de la
Parte 14 hacia la infraestructura financiera. Esta versión publica la primera de
sus siete partes.

> **Sobre la numeración.** La ampliación completa de la Etapa 5 se publicará como
> `2.0.0` cuando existan sus siete partes. Declarar `2.0.0` con una de siete
> contradiría el principio que sostiene el repositorio: `STATUS.md` describe lo
> que hay, no lo que se planea.

### Añadido

**Parte 17 — Finanzas abiertas, APIs y economía de datos**

- 14 clases de 90 minutos, con el eje de que las finanzas abiertas no son una
  API sino un régimen de consentimiento con soporte técnico.
- 6 laboratorios reproducibles, cada uno con escenario, supuestos, criterios de
  aceptación, amenazas, rúbrica y **solución de referencia comentada**.
- Evaluación diagnóstica y evaluación final con rúbrica, escala y guía de
  corrección con los cálculos resueltos.
- Proyecto integrador «agregador financiero regulado», con expediente de doce
  piezas y guion de defensa.

**Aplicación `apps/open_finance_sandbox/`**

- Entorno simulado completo: servidor de autorización con PKCE, API de cuentas,
  panel de consentimientos, iniciación de pagos y proveedor tercero.
- Contrato `openapi.json` validado en integración continua.
- 28 pruebas, en su mayoría **negativas**, y batería de conformidad de 16 casos
  en cuatro familias, con sus limitaciones declaradas.
- Modelo de amenazas priorizado por impacto × probabilidad, con la prueba que
  verifica cada control.

**Herramientas de validación**

- `tools/validate_metadata.py`: falla si una clase cita un instrumento normativo
  sin declarar su fecha de verificación.
- `tools/validate_openapi.py`: alcances declarados, respuestas de error,
  referencias resueltas, importes que no son coma flotante y enumerados con
  cláusula de compatibilidad.
- `tools/validate_datasets.py`: todo conjunto de datos con ficha, toda columna
  con diccionario.
- `tools/detect_secrets.py` y `tools/detect_pii.py`: credenciales reales y datos
  personales, distinguiendo el valor de ejemplo del secreto.

**Metadatos regulatorios**

- Directorio `regulatory/` con una ficha por instrumento: autoridad, número,
  fechas, estado, alcance, fuente oficial y `last_verified`.
- Encabezado YAML ampliado en las clases de la Etapa 5: `jurisdictions`,
  `regulatory_topics`, `regulation_last_verified`, `regulatory_status`,
  `primary_authorities` y `requires_legal_review`.

**Datos**

- `datasets/synthetic/open_finance_consents.csv`: 1 200 consentimientos con los
  patrones que las clases analizan (revocación temprana, fatiga).
- Separación `raw/`, `processed/`, `synthetic/`, `schemas/`.
- Ficha con diccionario, supuestos, calidad y límites para **los cuatro**
  conjuntos, incluidos los tres históricos que no la tenían.

**Documentación**

- `docs/etapa-5-finanzas-digitales.md`, `docs/mapa-finanzas-abiertas.md`,
  `docs/metodologia-verificacion-regulatoria.md`,
  `docs/guia-laboratorios-digitales.md` y
  `docs/glosario-finanzas-digitales.md`, este último con el campo «qué NO
  significa» en cada término.

### Cambiado

- `tools/progress.py` cuenta los componentes no curriculares sobre los archivos
  reales en lugar de declararlos a mano.
- `tools/build_syllabus.py` reconoce la Etapa 5 y calcula el número de proyectos
  y la clase final desde el contenido.
- `tools/build_site.py` deriva el número de partes y clases del repositorio: el
  pie del portal ya no puede quedar desactualizado.
- `datasets/README.md` documenta la organización y las cinco reglas de datos.

### Corregido

- `CHANGELOG.md` tenía 66 líneas con codificación corrompida (mojibake) en la
  entrada 1.1.0. Reparadas a UTF-8 correcto.
- Las cifras «240 clases» y «16 partes» escritas a mano en generadores y
  documentación quedaban desactualizadas al crecer el programa; ahora se
  calculan.

### Seguridad

- Las claves del entorno simulado son de juguete y están versionadas a
  propósito; `tools/detect_secrets.py` distingue ese caso del secreto real.
- Ningún dato personal, ningún fondo real, ninguna red externa y ninguna
  herramienta reutilizable de ataque: los ataques existen solo como pruebas que
  deben fallar.

### Notas de migración

- Las clases de las Partes 1 a 16 **no cambian**. El encabezado ampliado y las
  secciones adicionales solo se exigen a partir de la parte 17.
- La regla «toda cita de un instrumento lleva línea de verificación» sí se
  aplica a todo el repositorio; las 15 clases anteriores que citan instrumentos
  ya la cumplían.
- Quien tuviera un guion propio contra `tools/progress.py` debe saber que
  `PLANNED` incluye ahora las siete partes de la Etapa 5.

---

## [1.1.0] — 2026-08-06

Portal de estudio publicado y endurecimiento de la integración continua siguiendo las
convenciones del resto de los programas del autor.

### Añadido

**Portal de estudio**

- `tools/build_site.py` genera un sitio navegable con las 467 páginas del material:
  240 clases, documentación, laboratorios, evaluaciones y proyectos.
- El sitio espeja la estructura del repositorio (`X.md` → `X.html` en la misma ruta),
  de modo que cualquier enlace del material funciona dentro del portal.
- Diagramas mermaid renderizados, tema claro y oscuro, navegación por migas y diseño
  adaptable.
- Publicado en GitHub Pages y verificado tras el despliegue.

**Flujos de integración continua**

- `ci.yml` reemplaza a `validate.yml`: añade estilo de Markdown, matriz de
  compatibilidad (3 sistemas × 3 versiones de Python), auditoría de los propios
  workflows con `actionlint` y `zizmor`, y puerta de calidad final.
- `security.yml`: `pip-audit` sobre las dependencias, `bandit` sobre el código y
  escaneo de secretos con `gitleaks` sobre el historial completo.
- `codeql.yml`: análisis semántico del código Python.
- `pages.yml`: genera, publica y verifica el portal.
- `enlaces-externos.yml`: revisa semanalmente los enlaces a fuentes oficiales y abre
  un issue si alguno cae. Informativo: no bloquea la CI.
- `release.yml`: al etiquetar una versión publica el programa completo, las clases por
  separado, el SBOM en formato CycloneDX y las sumas de verificación.

**Configuración**

- `.markdownlint-cli2.jsonc` con las reglas de estilo y la razón de cada excepción.
- `.lycheeignore` con los dominios que bloquean agentes automáticos.
- `requirements-site.txt` con las dependencias del portal.

### Cambiado

- Acciones de terceros **fijadas por SHA de commit**, con su versión en comentario.
- `persist-credentials: false` en todos los checkout, para no dejar el token en `.git`.
- `timeout-minutes` en todos los jobs.
- Ninguna expresión `${{ }}` se interpola dentro de un `run`: los valores entran por
  `env` y el script los lee como variables de shell. Es la vía de inyección que señala
  `zizmor`, y el repositorio cierra su auditoría **sin un solo hallazgo**.
- La publicación usa `gh release`, ya incluido en el runner, en lugar de una acción de
  terceros: una dependencia externa menos que fijar, auditar y renovar.
- `pytest` sube a `>=9.0.3` para resolver la vulnerabilidad PYSEC-2026-1845.
- README con las insignias de los cuatro flujos y el enlace al portal.

### Corregido

- Seis errores de estilo de Markdown detectados por `markdownlint`: un nivel de
  encabezado saltado, tres tablas con celdas de más por barras verticales sin escapar,
  una almohadilla sin espacio interpretada como encabezado y un enlace vacío.

---

## [1.0.0] — 2026-08-06

Primera versión completa del programa: **las 240 clases redactadas, verificadas y con
bibliografía oficial**.

### Añadido

**Contenido — 240 clases en 16 partes**

- Partes 1–4 · *Fundamentos* (56 clases): matemática financiera, finanzas personales,
  productos y servicios, seguridad y consumo financiero.
- Partes 5–8 · *Analista* (60 clases): contabilidad, economía y sistema financiero,
  matemática financiera avanzada, inversiones y mercados.
- Partes 9–12 · *Bancario* (64 clases): crédito, operaciones, gestión integral de
  riesgos, regulación y cumplimiento.
- Partes 13–16 · *Dirección* (60 clases): finanzas corporativas, fintech y datos,
  estrategia y dirección, y el proyecto integrador «Banco Virtual».

**Estructura pedagógica**

- Trece secciones por clase, incluidas ejemplo numérico guiado paso a paso, puente
  «del cliente al banco», errores frecuentes con causa y corrección, preguntas de
  comprobación y entregable de portafolio.
- Mínimo de cuatro fuentes verificables por clase, con línea de verificación local en
  todo contenido normativo.
- 96 laboratorios, 32 evaluaciones y 16 proyectos integradores.

**Herramientas de verificación**

- `tools/validate_program.py` — estructura, secciones obligatorias y fuentes.
- `tools/render_program.py` — genera navegación, agenda docente y bloque de ética,
  con modo `--check` idempotente.
- `tools/build_syllabus.py` — genera `SYLLABUS.md` con el índice de las 240 clases.
- `tools/progress.py` — genera `STATUS.md` desde los archivos reales.
- `tools/check_links.py` — verifica los ~2 000 enlaces relativos del repositorio.

**Documentación**

- `README.md` reescrito con navegación, insignias, diagramas y anatomía de una clase.
- `docs/fuentes.md` — bibliografía consolidada de manuales, marcos institucionales y
  artículos fundacionales.
- `docs/glosario.md` — definiciones operativas indexadas por parte.
- `docs/formulas.md` — formulario por dominio, con la trampa habitual de cada fórmula.
- `docs/guia-docente.md` — sesión de 90 minutos, rúbricas y adaptación por contexto.
- `docs/ruta-aprendizaje.md` — progresión, puntos de entrada y cadenas de dependencia.
- `docs/mapa-competencias.md` — competencias por nivel con listas de autoevaluación.
- `docs/etica-y-limitaciones.md` — alcance, uso de datos, modelos y contenidos sensibles.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` y `SECURITY.md` ampliados.

**Integración continua**

- Flujo `Validate program` con trabajos de validación, enlaces y calidad de Markdown.
- Permisos mínimos, control de concurrencia y caché de dependencias.

### Cambiado

- `SYLLABUS.md` pasa de ser una tabla escrita a mano a un índice generado desde los
  archivos: incluye las 240 clases con su nivel y su enlace.
- `STATUS.md` se genera desde los archivos y nunca declara más contenido del que existe.
- Nombres de archivo normalizados a ASCII para compatibilidad entre sistemas y URL.
- Finales de línea unificados a LF mediante `.gitattributes`.

---

## [0.1.0] — 2026-08-05

Versión inicial: estructura del programa y herramientas base.

### Añadido

- Arquitectura curricular de 16 partes y 240 clases.
- 96 laboratorios y 32 evaluaciones estructurados.
- Calculadoras financieras con interfaz de línea de comandos.
- Modelo de scoring crediticio con métricas.
- Banco virtual sobre SQLite.
- Conjuntos de datos sintéticos.
- Validación estructural inicial.

---

[2.0.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v2.0.0
[1.7.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v1.7.0
[1.6.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v1.6.0
[1.5.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v1.5.0
[1.4.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v1.4.0
[1.3.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v1.3.0
[1.2.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v1.2.0
[1.1.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v1.1.0
[1.0.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v1.0.0
[0.1.0]: https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/tag/v0.1.0

<!-- pie:inicio -->
---

<div align="center">

[🏠 Inicio](README.md) · [📊 Estado](STATUS.md) · [🗺️ Roadmap](ROADMAP.md)

</div>
<!-- pie:fin -->
