# Parte 22: Regulación de mercados financieros digitales

## De qué trata esta parte

Las cinco partes anteriores de la etapa construyeron infraestructura: interfaces
de datos, rieles de pago, registros distribuidos, activos que circulan sobre
ellos y mercados donde se negocian. Esta parte hace la pregunta que faltaba: **de
todo eso, ¿qué alcanza una norma, y por qué esa frontera se dibuja donde se
dibuja?**

El cambio de registro es importante y conviene anticiparlo. Hasta aquí las
respuestas dependían de cómo funciona algo —cuánta profundidad tiene un libro,
qué tolera un consenso, qué cubre una reserva—. A partir de aquí dependen de qué
está haciendo alguien, y eso se responde con hechos observables y con la norma
citada, no con una descripción del producto.

El eje es un principio que se enuncia en una línea y que ordena toda la parte:

```text
LA REGULACIÓN SIGUE A LA ACTIVIDAD,
NO A LA TECNOLOGÍA

  «misma actividad, mismo riesgo, misma regulación»

  · si captas ahorro del público, hay un régimen
  · si custodias por cuenta de terceros, hay otro
  · si operas un mercado, hay otro
  · y el soporte técnico no cambia ninguno

LA PREGUNTA NO ES «¿ESTÁ REGULADO EL TOKEN?»
ES «¿QUÉ ESTÁ HACIENDO ESTA ENTIDAD?»
```

El principio es correcto y no es suficiente, y la parte dedica su segunda clase a
sus tres límites: hay actividades cuyo riesgo cambia al cambiar de
infraestructura, hay servicios sin un sujeto al que exigir cumplimiento, y hay
riesgos —la irreversibilidad, la composición automática, la dependencia de un
proveedor común— que ninguna norma anterior contempló porque no existían.

## Separación terminológica

Estas siete distinciones se usan con precisión en toda la parte. Confundirlas es
el origen de la mayor parte de los errores de determinación.

| Término | Qué es | Qué NO es |
|---|---|---|
| **Perímetro** | Conjunto de actividades sujetas a un régimen | No es una lista de tecnologías |
| **Autorización** | Permiso previo para ejercer una actividad | No es un registro informativo |
| **Registro** | Inscripción declarativa | No implica supervisión de solvencia |
| **Supervisión** | Vigilancia continua del cumplimiento | No es la autorización inicial |
| **Sandbox** | Espacio de prueba con requisitos adaptados | No es una exención de la norma |
| **Extraterritorialidad** | Aplicación a hechos fuera del territorio | No es cooperación entre autoridades |
| **Cumplimiento** | Conjunto de controles de la entidad | No es la conducta debida |

## Cómo se encadenan las veintidós clases

La secuencia no es una lista de temas: cada bloque responde una pregunta que el
anterior deja abierta, y saltarse uno deja el siguiente sin base.

**Clases 1 a 4 — qué haces, con qué y con qué permiso.** La clase 1 enseña a
determinar el perímetro con hechos observables, no con la descripción que da la
entidad. La 2 examina el principio que ordena la materia y sus tres límites. La 3
califica el instrumento, porque de eso dependen la información exigible y la
protección del tenedor. La 4 recorre el camino de la autorización y produce la
cifra que decide si el negocio existe: cuánto hay que facturar solo para sostener
la carga regulatoria.

**Clases 5 a 9 — qué protege al cliente.** Determinado el perímetro, la parte
mira al otro lado del mostrador. La 5 estudia qué se exige a quien emite; la 6
distingue la protección de conducta —que se audita en cada inspección— de la
patrimonial, que solo se comprueba cuando ya es tarde. La 7 resuelve las cuatro
decisiones jurídicas de una moneda digital de banco central; la 8 traduce la
exposición en capital y liquidez; la 9 comprueba qué exige la norma al custodio y
qué queda fuera.

**Clases 10 a 14 — qué hay que controlar.** La 10 aplica a una infraestructura
tokenizada el régimen escrito para los depositarios, y encuentra que la
liquidación atómica puede no tener firmeza legal. La 11 y la 12 tratan integridad
del mercado y prevención de lavado; la 13 resuelve la contradicción entre el
derecho a borrar, la obligación de conservar y un registro que no permite ni una
cosa ni la otra. La 14 cierra el bloque con el riesgo que no está en el perímetro
de nadie: veintidós entidades que cumplen su norma y un proveedor común que
concentra el 86 %.

**Clases 15 y 16 — el conjunto y la comparación.** La 15 cambia de escala y mira
al sistema. La 16 compara jurisdicciones y demuestra por qué el arbitraje
regulatorio ahorra menos de lo que parece; también fija el método que exige el
bloque siguiente: cada celda con su nivel, su referencia y su fecha.

**Clases 17 a 20 — dos regímenes con nombre.** Las quince primeras clases enseñan
a determinar sin decir en qué país. Este bloque hace lo contrario y es
deliberado: un método que nunca se aplica a una norma concreta no se comprueba
nunca. La 17 y la 18 leen MiCA por dentro —su perímetro, sus tres categorías, su
reserva, su reembolso y sus dos planes para el día malo—, porque es el primer
régimen que reguló la materia entera de una vez y por eso sus costuras se ven. La
19 añade las tres normas europeas sin las cuales MiCA no funciona, y produce el
dato que ningún plan de negocio incluye: MiCA suele ser la quinta parte del coste
regulatorio, no el total. Y la 20 estudia el único caso en que un Estado declaró
moneda de curso legal un activo sin emisor, con el método que impide el titular
fácil: siete resultados que se cuentan por separado y no se promedian.

**Clases 21 y 22 — el experimento y el expediente.** La 21 estudia los espacios de
prueba y por qué la mayoría no produce ni innovación ni conocimiento. Y la 22
ensambla las doce piezas del expediente, que es donde aparecen las
contradicciones que ninguna pieza mostraba por separado.

## Prerrequisitos

| Parte | Clase | Qué aporta |
|---|---|---|
| 12 | Regulación, cumplimiento y auditoría | Basilea, lavado, conducta, resolución |
| 18 | 6 y 12 · Sanciones y regla del viaje | Cumplimiento transfronterizo |
| 20 | 1, 9 y 16 · Taxonomía y perímetro | La clasificación por la promesa |
| 21 | 1, 2 y 16 · Registro de referencia | El régimen de la infraestructura |

## Resultados de aprendizaje

- Determinar el perímetro aplicable a una actividad a partir de **hechos
  observables**, no de la etiqueta que use el proyecto.
- Comparar regímenes de distintas jurisdicciones sin confundir requisito con
  guía ni con práctica de mercado.
- Diseñar un programa de cumplimiento proporcionado al riesgo y verificable.
- Evaluar la resiliencia operativa y la dependencia de terceros críticos.
- **Leer un régimen concreto** —MiCA y sus normas conexas— y deducir de él la
  autorización, la reserva y los planes que exige, con su referencia y su fecha.
- **Evaluar una política pública** de adopción separando sus resultados, sin
  promediarlos en un titular de éxito o de fracaso.
- Construir un expediente regulatorio que resista una revisión supervisora.

## Competencias

| Competencia | Nivel esperado |
|---|---|
| Determinación de perímetro | Justifica con hechos y con la norma citada |
| Comparación de regímenes | Distingue requisito, guía y práctica |
| Lectura de un régimen concreto | Deduce obligaciones del texto, no del resumen |
| Evaluación de política pública | Separa resultados y declara lo que no se puede medir |
| Diseño de cumplimiento | Proporcionado, verificable y probado |
| Resiliencia operativa | Identifica dependencias y prueba la continuidad |
| Relación con el supervisor | Documenta, anticipa y responde |

## Secuencia

1. [El perímetro regulatorio](classes/01-el-perimetro-regulatorio.md)
2. [Misma actividad, mismo riesgo, misma regulación](classes/02-misma-actividad-mismo-riesgo.md)
3. [Calificación de un instrumento digital](classes/03-calificacion-de-un-instrumento-digital.md)
4. [Autorización, registro y supervisión](classes/04-autorizacion-registro-y-supervision.md)
5. [Régimen de emisores](classes/05-regimen-de-emisores.md)
6. [Protección del cliente y de sus fondos](classes/06-proteccion-del-cliente-y-de-sus-fondos.md)
7. [Moneda digital de banco central: marco jurídico](classes/07-moneda-digital-de-banco-central-marco.md)
8. [Tratamiento prudencial de las exposiciones](classes/08-tratamiento-prudencial-de-las-exposiciones.md)
9. [Custodia y segregación en la norma](classes/09-custodia-y-segregacion-en-la-norma.md)
10. [Infraestructuras de mercado y su régimen](classes/10-infraestructuras-de-mercado-y-su-regimen.md)
11. [Conducta de mercado e integridad](classes/11-conducta-de-mercado-e-integridad.md)
12. [Prevención de lavado y financiamiento del terrorismo](classes/12-prevencion-de-lavado-y-financiamiento.md)
13. [Protección de datos y economía de la información](classes/13-proteccion-de-datos-y-economia-de-la-informacion.md)
14. [Resiliencia operativa y terceros críticos](classes/14-resiliencia-operativa-y-terceros-criticos.md)
15. [Estabilidad financiera y vigilancia macroprudencial](classes/15-estabilidad-financiera-y-vigilancia.md)
16. [Regulación comparada: Chile y el mundo](classes/16-regulacion-comparada-chile-y-el-mundo.md)
17. [MiCA I: perímetro, activos y participantes](classes/17-mica-perimetro-activos-y-participantes.md)
18. [MiCA II: obligaciones, reservas y supervisión](classes/18-mica-obligaciones-reservas-y-supervision.md)
19. [Regímenes europeos conexos: piloto DLT, DORA y regla del viaje](classes/19-regimenes-europeos-conexos.md)
20. [El Salvador: bitcoin, Chivo y activos digitales](classes/20-el-salvador-bitcoin-chivo-y-activos-digitales.md)
21. [Espacios de prueba y regulación experimental](classes/21-espacios-de-prueba-y-regulacion-experimental.md)
22. [Proyecto: expediente regulatorio](classes/22-proyecto-expediente-regulatorio.md)

## Laboratorios

Los nueve laboratorios siguen la misma secuencia que las clases y se apoyan en
`apps/regulatory_perimeter_engine/`. El primero fija el método —determinar la
actividad por hechos— y el último reproduce lo que hace un supervisor: leer el
expediente por parejas de piezas.

| # | Laboratorio | Entregable principal |
|---:|---|---|
| 1 | [Determinación de perímetro](labs/lab-01.md) | Actividades detectadas por hechos observables |
| 2 | [Calificación de instrumentos](labs/lab-02.md) | Matriz de calificación con su fundamento |
| 3 | [Vía de autorización](labs/lab-03.md) | Requisitos, plazos y facturación de equilibrio |
| 4 | [Salvaguarda y segregación](labs/lab-04.md) | Verificación con las cuatro preguntas |
| 5 | [Programa de cumplimiento](labs/lab-05.md) | Tratamiento del resto no identificable |
| 6 | [Detección de conducta anómala](labs/lab-06.md) | Precisión, exhaustividad y coste marginal |
| 7 | [Resiliencia y terceros críticos](labs/lab-07.md) | Concentración real frente a la aparente |
| 8 | [Comparación de regímenes](labs/lab-08.md) | Tabla comparada con nivel, fuente y fecha |
| 9 | [Expediente regulatorio](labs/lab-09.md) | Lectura cruzada de las cinco parejas |

## Evaluaciones

- [Diagnóstico](assessments/diagnostic.md)
- [Evaluación final](assessments/final.md)

## Proyecto

- [Expediente regulatorio de una entidad de activos digitales](project/README.md)

## Evidencias

- Determinación de perímetro con los hechos y las fuentes que la sostienen.
- Calificación de tres instrumentos con la norma citada y su fecha.
- Vía de autorización con plazo real, coste recurrente y facturación necesaria.
- Verificación de salvaguarda con las cuatro preguntas y su cuantificación.
- Vigilancia calibrada con coste marginal frente a valor del caso.
- Mapa de terceros con subcontratación y concentración por infraestructura.
- Expediente cruzado por parejas, con hallazgos priorizados y remediación.

## Mapa de dependencias

```text
Parte 12 — regulación bancaria
Partes 17 a 21 — la infraestructura construida
   └── Parte 22 — el régimen que la alcanza
          └── Parte 23 · el mercado completo, autorizado y defendido
```

## Aplicación asociada

- [`apps/regulatory_perimeter_engine/`](../../apps/regulatory_perimeter_engine/README.md)

## Fuentes oficiales de referencia

- Comisión para el Mercado Financiero y Banco Central de Chile — Ley 21.521 y su
  normativa de desarrollo.
- Financial Stability Board — marco global para las actividades con
  criptoactivos.
- IOSCO — recomendaciones sobre mercados de activos digitales y finanzas
  descentralizadas.
- Basel Committee on Banking Supervision — tratamiento prudencial y resiliencia.
- Diario Oficial de la Unión Europea — MiCA, DORA, el régimen piloto DLT y el
  reglamento sobre la información que acompaña a las transferencias.
- Autoridad Bancaria Europea y Autoridad Europea de Valores y Mercados — normas
  técnicas y directrices de desarrollo.
- Comisión Nacional de Activos Digitales de El Salvador y Banco Central de
  Reserva de El Salvador — régimen de activos digitales y estadísticas.
- Fondo Monetario Internacional — informes de país sobre El Salvador.
- GAFI — recomendaciones sobre activos virtuales y sus proveedores.

## Limitaciones

- **Nada de esta parte constituye asesoría legal.** Cada clase indica su fecha de
  verificación y ninguna sustituye la consulta de la fuente oficial vigente ni el
  criterio de un abogado.
- El régimen de los activos digitales **cambia con rapidez** y de forma desigual
  entre jurisdicciones: lo que la parte enseña es el método de determinación, no
  un catálogo estable.
- Los casos son sintéticos; los instrumentos y entidades reales que se citen se
  citan por sus documentos públicos, con fecha de consulta.
- **MiCA, DORA, el régimen piloto DLT, el reglamento europeo de transferencias y
  la legislación de El Salvador se estudian como referencia comparada y no son
  derecho aplicable en Chile.** Las clases 17 a 20 sirven para aprender a leer un
  régimen, no para operar bajo él sin asesoría local.
- Las cifras del caso de El Salvador proceden de fuentes con metodologías
  distintas y no son comparables entre sí; la clase 20 declara de forma expresa
  qué series no están disponibles con calidad suficiente.
- La parte **no proporciona técnicas para eludir controles, ocultar actividad ni
  evitar la aplicación de una norma**, y no lo hará.
- No cubre la construcción de la infraestructura: eso son las Partes 17 a 21.
