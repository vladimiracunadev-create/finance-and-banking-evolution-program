# Parte 20: Activos digitales, stablecoins y dinero programable

- **Etapa:** 5 — Finanzas digitales, infraestructura y mercados tokenizados
- **Clases:** 16
- **Horas:** 24
- **Laboratorios:** 8
- **Evaluaciones:** 2
- **Proyecto:** 1

## Descripción

La Parte 19 estudió el registro. Esta parte estudia **lo que circula sobre él** y,
sobre todo, **qué promesa lleva dentro**. La tecnología del registro no dice nada
sobre eso: dos instrumentos idénticos técnicamente pueden ser un depósito
bancario y una participación en un fondo sin derecho de redención.

El eje es una pregunta que la palabra «token» oculta:

```text
UN ACTIVO DIGITAL NO ES UNA TECNOLOGÍA:
ES UNA PROMESA ANOTADA EN UN REGISTRO

  ¿QUIÉN LA HACE?     el emisor, o nadie
  ¿QUÉ PROMETE?       un importe, un derecho, o nada
  ¿CON QUÉ RESPALDO?  activos, otro token, o expectativa
  ¿EXIGIBLE CUÁNDO?   a la vista, con plazo, o nunca
  ¿ANTE QUIÉN?        un juzgado, un comité, o nadie

SI LAS CINCO RESPUESTAS SON «NADIE» O «NADA»,
EL PRECIO LO SOSTIENE ÚNICAMENTE
QUE OTRO ESTÉ DISPUESTO A PAGARLO
```

## Separación terminológica

Esta parte trata como **distintos** cinco instrumentos que se confunden a diario:

| Instrumento | Quién debe | Qué es el saldo | Régimen típico |
|---|---|---|---|
| **Criptoactivo no respaldado** | Nadie | Ningún derecho frente a nadie | Genérico o específico |
| **Stablecoin** | El emisor, según su documentación | Un derecho contractual, si existe | Emisión de activos referenciados |
| **Dinero electrónico** | Un emisor autorizado | Un derecho de redención a la par | Régimen de dinero electrónico |
| **Depósito tokenizado** | Un banco | Un depósito bancario, con su garantía | Régimen bancario |
| **CBDC** | El banco central | Un pasivo del banco central | Norma monetaria |

La tabla no es un matiz académico: **decide quién quiebra, qué garantía aplica y
a quién reclama el cliente**. Ningún componente técnico la cambia.

## Prerrequisitos

| Parte | Clase | Qué aporta |
|---|---|---|
| 6 | Economía y sistema financiero | Creación de dinero y pasivos monetarios |
| 11 | Gestión integral de riesgos | Liquidez, mercado, contraparte y concentración |
| 14 | 9 · Criptoactivos y registro distribuido | Primera taxonomía |
| 18 | Pagos transfronterizos y liquidación | El uso al que se destinan muchas de estas piezas |
| 19 | 3, 8 y 9 · Claves, contratos y oráculos | Custodia, ejecución y dato externo |

## Resultados de aprendizaje

- Clasificar un activo digital por **la promesa que lleva**, no por la red donde
  vive ni por el nombre que use.
- Analizar una cartera de reservas por calidad, plazo y liquidez, y calcular si
  soporta una redención masiva.
- Reconstruir la anatomía de una pérdida de paridad y distinguir el detonante
  del mecanismo.
- Evaluar un modelo de custodia por sus modos de fallo y su régimen de
  segregación.
- Decidir si un caso de uso necesita dinero programable y qué **no** debe
  programarse nunca.

## Competencias

| Competencia | Nivel esperado |
|---|---|
| Clasificación de instrumentos | Justifica con la promesa y el régimen |
| Análisis de reservas | Calcula cobertura y descalce |
| Riesgo de liquidez y contagio | Modela una corrida y su propagación |
| Custodia y segregación | Diseña y audita |
| Diseño de condiciones programables | Distingue lo automatizable de lo que no debe serlo |

## Secuencia

1. [Taxonomía de los activos digitales](classes/01-taxonomia-de-los-activos-digitales.md)
2. [Criptoactivos no respaldados](classes/02-criptoactivos-no-respaldados.md)
3. [Stablecoins: tipologías y mecánica de la paridad](classes/03-stablecoins-tipologias-y-mecanica-de-la-paridad.md)
4. [Reservas: composición, calidad y verificación](classes/04-reservas-composicion-calidad-y-verificacion.md)
5. [Redención: el derecho, el proceso y la cola](classes/05-redencion-el-derecho-el-proceso-y-la-cola.md)
6. [Pérdida de paridad: anatomía de una corrida](classes/06-perdida-de-paridad-anatomia-de-una-corrida.md)
7. [Stablecoins algorítmicas y su modo de fallo](classes/07-stablecoins-algoritmicas-y-su-modo-de-fallo.md)
8. [Depósitos tokenizados y dinero de banco comercial](classes/08-depositos-tokenizados-y-dinero-de-banco-comercial.md)
9. [Dinero electrónico: el régimen que ya existía](classes/09-dinero-electronico-el-regimen-que-ya-existia.md)
10. [Monedas digitales de banco central](classes/10-monedas-digitales-de-banco-central.md)
11. [Dinero programable y sus límites](classes/11-dinero-programable-y-sus-limites.md)
12. [Custodia de activos digitales](classes/12-custodia-de-activos-digitales.md)
13. [Mercado, liquidez y formación de precio](classes/13-mercado-liquidez-y-formacion-de-precio.md)
14. [Contagio y riesgo sistémico](classes/14-contagio-y-riesgo-sistemico.md)
15. [Contabilidad, tributación y balance](classes/15-contabilidad-tributacion-y-balance.md)
16. [Proyecto: evaluación de un activo digital](classes/16-proyecto-evaluacion-de-un-activo-digital.md)

## Laboratorios

| # | Laboratorio | Entregable principal |
|---:|---|---|
| 1 | [Clasificador de activos digitales](labs/lab-01.md) | Ficha de instrumento con su promesa y su régimen |
| 2 | [Análisis de una cartera de reservas](labs/lab-02.md) | Cobertura, descalce y prueba de tensión |
| 3 | [Cola de redención](labs/lab-03.md) | Simulación de una corrida con prorrateo |
| 4 | [Anatomía de una pérdida de paridad](labs/lab-04.md) | Reconstrucción con detonante y mecanismo separados |
| 5 | [Modelo algorítmico y su espiral](labs/lab-05.md) | Punto de no retorno medido |
| 6 | [Custodia y segregación](labs/lab-06.md) | Modos de fallo y controles con prueba |
| 7 | [Liquidez y profundidad de mercado](labs/lab-07.md) | Impacto de una venta grande |
| 8 | [Grafo de contagio](labs/lab-08.md) | Exposición indirecta y orden de caída |

## Evaluaciones

- [Diagnóstico](assessments/diagnostic.md)
- [Evaluación final](assessments/final.md)

## Proyecto

- [Evaluación de un activo digital para tesorería](project/README.md)

## Evidencias

- Ficha de clasificación de un instrumento real, con su promesa y su régimen.
- Análisis de reservas con cobertura calculada y descalce identificado.
- Simulación de redención masiva con la cola y el prorrateo resueltos.
- Reconstrucción de una pérdida de paridad con fuentes citadas.
- Diseño de custodia con sus modos de fallo y una prueba por control.
- Grafo de contagio con la exposición indirecta cuantificada.

## Mapa de dependencias

```text
Parte 19 — el registro
   └── Parte 20 — lo que circula sobre él y qué promete
          ├── Parte 21 · el instrumento financiero tokenizado
          ├── Parte 22 · el régimen del emisor y del custodio
          └── Parte 23 · el activo dentro de una infraestructura completa
```

## Aplicación asociada

- [`apps/digital_assets_risk_lab/`](../../apps/digital_assets_risk_lab/README.md)

## Fuentes oficiales de referencia

- Financial Stability Board — recomendaciones sobre acuerdos globales de
  stablecoins y sobre activos criptográficos.
- Committee on Payments and Market Infrastructures e IOSCO — aplicación de los
  principios para infraestructuras del mercado financiero a los acuerdos de
  stablecoins.
- Basel Committee on Banking Supervision — tratamiento prudencial de las
  exposiciones a criptoactivos.
- Bank for International Settlements — informes sobre el sistema monetario y
  sobre monedas digitales de banco central.
- Banco Central de Chile y Comisión para el Mercado Financiero — publicaciones
  sobre medios de pago y sobre la Ley 21.521.

## Limitaciones

- La parte **no recomienda ningún activo, emisor, plataforma ni estrategia**, y
  nada de lo que contiene es asesoría de inversión.
- No se crea ningún activo destinado a uso real, no se despliega nada en una red
  pública y no se mueven fondos reales.
- **No contiene herramientas para ocultar fondos, evadir controles ni eludir
  obligaciones de cumplimiento**, ni las contendrá.
- Los datos de mercado son sintéticos y los casos históricos se citan por sus
  fuentes públicas; ninguna cifra debe usarse como dato operativo.
- El régimen jurídico cambia: cada clase indica su fecha de verificación y
  ninguna sustituye la consulta de la fuente oficial vigente.
