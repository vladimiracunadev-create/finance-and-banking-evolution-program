# Parte 23: Proyecto — banco digital y mercado tokenizado

- **Etapa:** 5 — Finanzas digitales, infraestructura y mercados tokenizados
- **Clases:** 18
- **Horas:** 27
- **Laboratorios:** 9
- **Evaluaciones:** 2
- **Proyecto:** 1

## De qué trata esta parte

Esta parte no enseña nada nuevo. Construye.

Las seis anteriores dieron las piezas: interfaces de datos con consentimiento,
rieles de pago que cruzan fronteras, registros distribuidos y su criterio de uso,
activos que circulan sobre ellos, instrumentos financieros tokenizados y el
régimen que alcanza a todo eso. Aquí se montan juntas, y el ejercicio descubre lo
que ninguna parte por separado podía mostrar: **las decisiones se contradicen
entre sí**.

Elegir liquidación atómica obliga a prefinanciar y encarece la liquidez. Bajar el
mínimo de entrada mejora el acceso y empeora la rentabilidad neta del pequeño.
Operar 24/7 genera crédito intradía entre bancos. Ninguna de esas tensiones
aparece al diseñar un componente; todas aparecen al integrarlos.

```text
LO QUE SE CONSTRUYE

  UN BANCO DIGITAL      capta, presta, custodia y paga
        +
  UN MERCADO TOKENIZADO emite, negocia y liquida
        +
  EL EXPEDIENTE         que lo sostiene ante un supervisor

Y LO QUE SE EVALÚA NO ES QUE FUNCIONE:
es que cada decisión tenga su alternativa
medida y que las contradicciones estén
resueltas y declaradas.
```

## Qué distingue a un capstone de un proyecto

Un proyecto integrador de una parte anterior pedía aplicar lo aprendido en esa
parte. Este pide algo distinto y más difícil: **sostener un sistema completo
frente a alguien que va a buscarle las costuras**. Por eso la mitad de las clases
son de construcción y la otra mitad, de defensa.

La diferencia práctica es que aquí no basta con que cada componente esté bien.
Un banco cuyo tramo de dinero está fuera del registro no puede prometer
liquidación atómica por mucho que su motor de liquidación sea impecable, y un
mercado con liquidez prometida y sin compromiso de cotización no la tiene aunque
el libro de órdenes esté perfectamente implementado.

## Prerrequisitos

Esta parte supone las seis anteriores completas. No es una recomendación: cada
clase invoca métodos concretos que se desarrollaron allí.

| Parte | Qué aporta | Dónde se usa aquí |
|---|---|---|
| 16 | Proyecto Banco Virtual | Estructura del capstone y método de defensa |
| 17 | Consentimiento y contratos de API | Clases 2 y 8 |
| 18 | Pagos y liquidación transfronteriza | Clases 5 y 11 |
| 19 | Criterio de registro distribuido | Clases 4 y 7 |
| 20 | Clasificación por promesa y contagio | Clases 6 y 14 |
| 21 | Registro de referencia y atomicidad | Clases 7, 9 y 10 |
| 22 | Perímetro, expediente y defensa | Clases 3, 13 y 16 |

## Resultados de aprendizaje

- **Integrar** los componentes de las seis partes anteriores en un sistema cuyas
  decisiones no se contradigan.
- **Resolver** las tensiones de diseño que solo aparecen al integrar, dejando
  constancia de qué se sacrificó y por qué.
- **Construir** el expediente que sostiene el sistema ante un supervisor, con
  evidencia por afirmación.
- **Someter** el diseño a escenarios adversos y medir qué aguanta y qué no.
- **Defender** las decisiones ante preguntas hostiles, incluidas las que no
  tienen buena respuesta.

## Competencias

| Competencia | Nivel esperado |
|---|---|
| Integración de arquitectura | Resuelve contradicciones y las declara |
| Análisis de tensiones de diseño | Cuantifica lo que se gana y lo que se pierde |
| Construcción de expediente | Cada afirmación con su evidencia |
| Prueba adversa | Diseña el escenario que rompe su propio sistema |
| Defensa | Responde con datos, o reconoce que no puede |

## Cómo se encadenan las 18 clases

La parte tiene tres bloques y cada uno cierra una fase del capstone.

**Clases 1 a 6 — la decisión de qué construir.** Antes de diseñar hay que
delimitar. La clase 1 fija el alcance y el modelo de negocio; la 2 determina qué
se construye y qué se integra de terceros; la 3 aplica el método de perímetro de
la Parte 22 al propio proyecto. Las clases 4 a 6 toman las tres decisiones de
arquitectura que condicionan todo lo demás: si hace falta un registro
distribuido, cómo se mueve el dinero y qué instrumentos se ofrecen.

**Clases 7 a 12 — la construcción y sus contradicciones.** Aquí se montan las
piezas y aparecen las tensiones. La 7 resuelve el registro de referencia y con él
si la atomicidad es alcanzable; la 8 y la 9, las interfaces y la custodia; la 10,
la liquidación; la 11, los pagos; la 12, el ciclo de vida completo. Cada clase
termina identificando qué decisión anterior queda comprometida.

**Clases 13 a 18 — la prueba y la defensa.** El expediente regulatorio, el
modelo de amenazas, el escenario de tensión, la continuidad y la resolución
ordenada. La parte —y el programa— cierra con la defensa ante un comité que
incluye a un supervisor, y con una clase dedicada a lo que el sistema **no**
puede hacer, que es la parte del expediente que más se omite y la que más
credibilidad da.

## Secuencia

1. [Alcance y modelo de negocio](classes/01-alcance-y-modelo-de-negocio.md)
2. [Construir, integrar o comprar](classes/02-construir-integrar-o-comprar.md)
3. [Perímetro del propio proyecto](classes/03-perimetro-del-propio-proyecto.md)
4. [Decisión de arquitectura: ¿hace falta un registro?](classes/04-decision-de-arquitectura-registro.md)
5. [Decisión de arquitectura: el dinero](classes/05-decision-de-arquitectura-el-dinero.md)
6. [Decisión de producto: qué se ofrece](classes/06-decision-de-producto-que-se-ofrece.md)
7. [El registro de referencia del sistema](classes/07-el-registro-de-referencia-del-sistema.md)
8. [Interfaces, consentimiento y terceros](classes/08-interfaces-consentimiento-y-terceros.md)
9. [Custodia y gestión de claves](classes/09-custodia-y-gestion-de-claves.md)
10. [Liquidación y sus modos de fallo](classes/10-liquidacion-y-sus-modos-de-fallo.md)
11. [Pagos y conexión con el exterior](classes/11-pagos-y-conexion-con-el-exterior.md)
12. [Ciclo de vida y operación diaria](classes/12-ciclo-de-vida-y-operacion-diaria.md)
13. [Expediente regulatorio del sistema](classes/13-expediente-regulatorio-del-sistema.md)
14. [Modelo de amenazas priorizado](classes/14-modelo-de-amenazas-priorizado.md)
15. [Escenario de tensión y continuidad](classes/15-escenario-de-tension-y-continuidad.md)
16. [Resolución ordenada y salida](classes/16-resolucion-ordenada-y-salida.md)
17. [Lo que el sistema no puede hacer](classes/17-lo-que-el-sistema-no-puede-hacer.md)
18. [Defensa ante el comité](classes/18-defensa-ante-el-comite.md)

## Laboratorios

Los nueve laboratorios siguen el orden de construcción y se apoyan en
`apps/digital_bank_capstone/`, que integra las aplicaciones de las seis partes
anteriores en un solo sistema.

| # | Laboratorio | Entregable principal |
|---:|---|---|
| 1 | [Alcance y decisiones de arquitectura](labs/lab-01.md) | Tres decisiones con su alternativa medida |
| 2 | [Perímetro y calificación del proyecto](labs/lab-02.md) | Regímenes activados y su evidencia |
| 3 | [Registro de referencia y atomicidad](labs/lab-03.md) | Prueba de si es alcanzable |
| 4 | [Custodia integrada](labs/lab-04.md) | Independencia efectiva del sistema completo |
| 5 | [Liquidación de extremo a extremo](labs/lab-05.md) | Ciclo completo con sus modos de fallo |
| 6 | [Tensiones de diseño](labs/lab-06.md) | Contradicciones cuantificadas y resueltas |
| 7 | [Modelo de amenazas](labs/lab-07.md) | Amenazas priorizadas con una prueba por control |
| 8 | [Escenario de tensión](labs/lab-08.md) | Qué aguanta y qué no, con números |
| 9 | [Expediente y defensa](labs/lab-09.md) | Documento que resiste las siete preguntas |

## Evaluaciones

- [Diagnóstico](assessments/diagnostic.md)
- [Evaluación final](assessments/final.md)

## Proyecto

- [Banco digital y mercado tokenizado](project/README.md)

## Evidencias

- Tres decisiones de arquitectura, cada una con su alternativa medida.
- Perímetro del propio proyecto con los regímenes que activa.
- Determinación del registro de referencia y prueba de atomicidad.
- Liquidación de extremo a extremo con cada modo de fallo probado.
- Tabla de tensiones de diseño con lo que se sacrificó en cada una.
- Modelo de amenazas priorizado con una prueba por control.
- Escenario de tensión con el punto de rotura medido.
- Expediente completo y defensa grabada.

## Mapa de dependencias

```text
Partes 17 a 22 — las piezas
   └── Parte 23 — el sistema completo
          · construido
          · probado contra escenarios adversos
          · sostenido por un expediente
          · y defendido ante un comité
```

## Aplicación asociada

- [`apps/digital_bank_capstone/`](../../apps/digital_bank_capstone/README.md)

## Fuentes oficiales de referencia

- Committee on Payments and Market Infrastructures e IOSCO — principios para las
  infraestructuras del mercado financiero.
- Basel Committee on Banking Supervision — gobierno corporativo, resiliencia
  operativa y tratamiento prudencial.
- Financial Stability Board — marco global para las actividades con
  criptoactivos y planificación de resolución.
- IOSCO — recomendaciones sobre mercados de activos digitales.
- Comisión para el Mercado Financiero y Banco Central de Chile — normativa
  aplicable y Ley 21.521.

## Limitaciones

- El sistema es **didáctico**: no es seguro, no es eficiente y no debe usarse
  para nada real. En producción se usan componentes auditados.
- **No se emite ningún valor, no se despliega nada en ninguna red pública, no se
  usan credenciales ni cuentas reales y no se mueven fondos.**
- El capstone **no constituye asesoría financiera, legal ni tributaria** y no
  recomienda ningún instrumento, plataforma ni estrategia.
- **No contiene técnicas para eludir controles, ocultar fondos ni evitar la
  aplicación de una norma.**
- Todo dato es sintético. Las entidades reales que se citen se citan por sus
  documentos públicos, con fecha de consulta.
