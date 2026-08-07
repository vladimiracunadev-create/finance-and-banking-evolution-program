# Parte 21: Tokenización, FX on-chain y mercados programables

- **Etapa:** 5 — Finanzas digitales, infraestructura y mercados tokenizados
- **Clases:** 16
- **Horas:** 24
- **Laboratorios:** 8
- **Evaluaciones:** 2
- **Proyecto:** 1

## Descripción

La Parte 19 estudió el registro y la Parte 20, lo que circula sobre él. Esta parte
estudia **el instrumento financiero** anotado en ese registro: un bono, una
acción, una participación, una divisa. Y su pregunta central es jurídica antes
que técnica:

```text
TOKENIZAR NO CREA UN DERECHO.
LO REPRESENTA.

  ¿QUÉ PASA SI EL REGISTRO DICE UNA COSA
   Y EL REGISTRO OFICIAL DICE OTRA?

  · si manda el registro oficial, el token es
    un espejo y todo el diseño es un sistema
    de conciliación
  · si manda el token, alguien tuvo que
    declararlo por norma, y esa norma existe
    en pocos sitios

NO HAY UNA TERCERA RESPUESTA,
y no responderla es el error que hunde
la mitad de los proyectos de tokenización.
```

## Separación terminológica

| Término | Qué es | Qué NO es |
|---|---|---|
| **Tokenización** | Representar un derecho existente en un registro | No es digitalizar, ni desmaterializar, ni emitir |
| **Emisión nativa** | Crear el instrumento directamente en el registro | No es tokenizar algo previo |
| **Entrega contra pago (DvP)** | Que la entrega y el pago ocurran juntos o no ocurran | No es que ocurran «casi a la vez» |
| **Atomicidad** | Propiedad de un conjunto de movimientos, no de una red | No la da la tecnología por sí sola |
| **FX on-chain** | Cambio de divisa entre dos activos anotados en registros | No es una operación FX del mercado mayorista |
| **Pago contra pago (PvP)** | Que las dos patas de un cambio se liquiden juntas | No es lo mismo que DvP |

## Prerrequisitos

| Parte | Clase | Qué aporta |
|---|---|---|
| 8 | Inversiones y mercados | Instrumentos, mercado primario y secundario |
| 18 | 7 y 15 · Liquidación y atomicidad | Finalidad y liquidación condicional |
| 19 | 8 y 9 · Contratos y oráculos | Ejecución programable y dato externo |
| 20 | 8, 10 y 12 · Dinero y custodia | El tramo de dinero y su custodia |

## Resultados de aprendizaje

- Determinar **quién es el registro de referencia** de un instrumento tokenizado
  y qué ocurre si diverge del token.
- Diseñar una entrega contra pago atómica y demostrar que lo es, incluidos sus
  modos de fallo.
- Calcular el ahorro real de una emisión tokenizada, separando lo que se debe a
  la tecnología de lo que se debe al proceso.
- Evaluar la liquidez prometida de un mercado secundario tokenizado con los
  criterios de la Parte 20, clase 13.
- Distinguir un cambio de divisa entre activos anotados de una operación FX, y
  medir qué riesgo elimina cada uno.

## Competencias

| Competencia | Nivel esperado |
|---|---|
| Diseño de emisión tokenizada | Especifica derechos, registro y ciclo de vida |
| Liquidación atómica | Diseña, prueba y documenta los modos de fallo |
| Análisis de liquidez secundaria | Mide en vez de suponer |
| FX y riesgo de liquidación | Calcula exposición y ventana |
| Evaluación de infraestructura | Compara con la alternativa, con números |

## Secuencia

1. [Qué es y qué no es tokenizar](classes/01-que-es-y-que-no-es-tokenizar.md)
2. [El registro de referencia](classes/02-el-registro-de-referencia.md)
3. [Derechos económicos y políticos del tenedor](classes/03-derechos-economicos-y-politicos-del-tenedor.md)
4. [Emisión: mercado primario tokenizado](classes/04-emision-mercado-primario-tokenizado.md)
5. [Ciclo de vida del instrumento](classes/05-ciclo-de-vida-del-instrumento.md)
6. [Mercado secundario y liquidez prometida](classes/06-mercado-secundario-y-liquidez-prometida.md)
7. [Fraccionamiento y acceso](classes/07-fraccionamiento-y-acceso.md)
8. [Entrega contra pago atómica](classes/08-entrega-contra-pago-atomica.md)
9. [Custodia de valores tokenizados](classes/09-custodia-de-valores-tokenizados.md)
10. [El tramo de dinero](classes/10-el-tramo-de-dinero.md)
11. [FX: del mercado mayorista al registro](classes/11-fx-del-mercado-mayorista-al-registro.md)
12. [Pago contra pago y riesgo de liquidación](classes/12-pago-contra-pago-y-riesgo-de-liquidacion.md)
13. [Creación de mercado automatizada](classes/13-creacion-de-mercado-automatizada.md)
14. [Colateral y garantías tokenizadas](classes/14-colateral-y-garantias-tokenizadas.md)
15. [Interoperabilidad entre infraestructuras](classes/15-interoperabilidad-entre-infraestructuras.md)
16. [Proyecto: mercado primario y secundario](classes/16-proyecto-mercado-primario-y-secundario.md)

## Laboratorios

| # | Laboratorio | Entregable principal |
|---:|---|---|
| 1 | [Registro de referencia y divergencia](labs/lab-01.md) | Detección y resolución de una discrepancia |
| 2 | [Emisión y ciclo de vida](labs/lab-02.md) | Instrumento con cupones y amortización |
| 3 | [Entrega contra pago atómica](labs/lab-03.md) | Prueba de que no hay estado intermedio |
| 4 | [Modos de fallo de la liquidación](labs/lab-04.md) | Cada fallo con su prueba negativa |
| 5 | [Liquidez del mercado secundario](labs/lab-05.md) | Profundidad medida frente a prometida |
| 6 | [Creación de mercado automatizada](labs/lab-06.md) | Pérdida por divergencia cuantificada |
| 7 | [FX y ventana de exposición](labs/lab-07.md) | Riesgo de liquidación con y sin PvP |
| 8 | [Colateral con llamada de margen](labs/lab-08.md) | Cascada de liquidaciones medida |

## Evaluaciones

- [Diagnóstico](assessments/diagnostic.md)
- [Evaluación final](assessments/final.md)

## Proyecto

- [Mercado primario y secundario de un instrumento tokenizado](project/README.md)

## Evidencias

- Determinación documentada del registro de referencia y su procedimiento de
  divergencia.
- Emisión con su ciclo de vida completo, incluidos cupones y amortización.
- Entrega contra pago con prueba de atomicidad y de sus modos de fallo.
- Medición de liquidez secundaria frente a la prometida en el folleto.
- Cálculo del riesgo de liquidación con y sin pago contra pago.
- Cascada de llamadas de margen con su punto de agotamiento.

## Mapa de dependencias

```text
Parte 19 — el registro
Parte 20 — el dinero que circula sobre él
   └── Parte 21 — el instrumento financiero tokenizado
          ├── Parte 22 · el régimen del mercado y de sus infraestructuras
          └── Parte 23 · el mercado completo, construido y defendido
```

## Aplicaciones asociadas

- [`apps/tokenization_platform/`](../../apps/tokenization_platform/README.md)
- [`apps/onchain_fx_lab/`](../../apps/onchain_fx_lab/README.md)

## Fuentes oficiales de referencia

- Committee on Payments and Market Infrastructures e IOSCO — principios para las
  infraestructuras del mercado financiero y su aplicación a la tokenización.
- IOSCO — recomendaciones sobre mercados de activos digitales y finanzas
  descentralizadas.
- Bank for International Settlements — informes sobre el libro unificado y la
  liquidación tokenizada.
- Comisión para el Mercado Financiero — normativa sobre oferta pública de
  valores y sobre infraestructuras de mercado.
- Diario Oficial de la Unión Europea — régimen piloto para infraestructuras de
  mercado basadas en tecnología de registro descentralizado.

## Limitaciones

- Los laboratorios implementan plataformas **didácticas**: no son seguras, no son
  eficientes y no deben usarse para nada real.
- **No se emite ningún valor, no se despliega nada en ninguna red pública y no se
  mueven fondos reales.**
- La parte **no recomienda ningún instrumento, plataforma ni estrategia**, y nada
  de lo que contiene es asesoría de inversión.
- El régimen jurídico de la tokenización difiere mucho entre jurisdicciones y
  cambia con rapidez: cada clase indica su fecha de verificación.
- La parte no cubre el régimen de mercados ni de sus infraestructuras: eso es la
  Parte 22.
