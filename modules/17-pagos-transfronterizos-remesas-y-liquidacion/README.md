# Parte 18: Pagos transfronterizos, remesas y liquidación internacional

## De qué trata esta parte

La Parte 10 explicó cómo se mueve el dinero dentro de un país. Esta parte cruza
la frontera, y allí aparece la distinción que ordena todo el material: **un
mensaje no es un movimiento de fondos**. La red transporta instrucciones, el
dinero se mueve en cuentas, la liquidación ocurre en un sistema de pagos y la
finalidad la da la norma.

Confundir esas cuatro cosas es el origen de casi todos los errores de esta
materia, y por eso la parte las modela por separado desde la primera clase.

El eje es una distinción que casi todo el mundo pasa por alto:

```text
UN MENSAJE NO ES UN MOVIMIENTO DE FONDOS

  SWIFT transporta INSTRUCCIONES
  los fondos se mueven en CUENTAS
  la liquidación ocurre en un SISTEMA DE PAGOS

  confundir los tres es el origen de la mitad
  de los errores de esta materia
```

## Prerrequisitos

| Parte | Clase | Qué aporta |
|---|---|---|
| 6 | Economía y sistema financiero | Tipo de cambio y balanza de pagos |
| 10 | Operaciones bancarias | Pagos, compensación y tesorería |
| 12 | Regulación y cumplimiento | AML/CFT, sanciones, KYC |
| 14 | 2 · Pagos digitales | Concepto de infraestructura de pagos |
| 17 | 8 y 10 · Contratos e iniciación | Idempotencia y estados de un pago |

## Resultados de aprendizaje

- Distinguir pago transfronterizo, remesa, transferencia internacional y
  operación de cambio, y explicar por qué no son la misma cosa.
- Trazar los cuatro flujos de un pago —mensaje, fondos, contable y
  cumplimiento— e identificar dónde se rompe cada uno.
- Leer y construir mensajes ISO 20022 de la familia de pagos, con sus campos
  obligatorios y sus códigos de propósito.
- Calcular el coste total de un pago separando comisión explícita, comisiones de
  intermediarios y diferencial de cambio.
- Evaluar arquitecturas alternativas —corresponsalía, interconexión de pagos
  inmediatos, stablecoins, depósitos tokenizados— con criterios medibles y sin
  atribuir a la tecnología mejoras que vienen del proceso.

## Competencias

| Competencia | Nivel esperado |
|---|---|
| Arquitectura de pagos internacionales | Diseña y compara rutas |
| Mensajería financiera | Construye y valida ISO 20022 |
| Gestión de liquidez multidivisa | Modela prefinanciación y netting |
| Análisis de coste y transparencia | Descompone y audita |
| Cumplimiento en pagos | Aplica screening, Travel Rule y reparaciones |

## Cómo se encadenan las 16 clases

La secuencia sigue el recorrido de un pago, y cada bloque añade una capa de
realidad que la anterior había simplificado.

**Clases 1 a 5 — la anatomía del pago.** Los cuatro flujos, la corresponsalía y
las cuentas nostro y vostro, la mensajería ISO 20022 y las ventanas horarias.
Al terminar este bloque se puede reconstruir por dónde pasa un pago y qué ocurre
en cada tramo.

**Clases 6 a 10 — lo que puede salir mal.** Sanciones, prevención de lavado y la
regla del viaje; después la liquidación, la finalidad y el riesgo que dio nombre
al problema en 1974. Es el bloque donde el pago deja de ser un flujo y pasa a ser
una exposición.

**Clases 11 a 16 — el coste y las alternativas.** Liquidez, neteo, el diferencial
de cambio y su trampa de base, las remesas, la interconexión de sistemas
inmediatos y la ruta con stablecoin. La parte cierra demostrando que el ahorro de
esa ruta no viene del registro: viene de eliminar tramos de corresponsalía.

## Secuencia

1. [Qué es un pago transfronterizo](classes/01-que-es-un-pago-transfronterizo.md)
2. [Arquitectura de participantes y responsabilidades](classes/02-arquitectura-de-participantes.md)
3. [Corresponsalía bancaria](classes/03-corresponsalia-bancaria.md)
4. [Cuentas nostro, vostro y loro](classes/04-cuentas-nostro-vostro-y-loro.md)
5. [Mensajería frente a movimiento de fondos](classes/05-mensajeria-frente-a-movimiento-de-fondos.md)
6. [SWIFT, CBPR+ e ISO 20022](classes/06-swift-cbpr-e-iso-20022.md)
7. [Compensación, liquidación y finalidad](classes/07-compensacion-liquidacion-y-finalidad.md)
8. [Liquidez, prefinanciación, netting y horarios](classes/08-liquidez-prefinanciacion-y-netting.md)
9. [El cambio de divisa dentro de un pago](classes/09-fx-dentro-de-un-pago-transfronterizo.md)
10. [Remesas y corredores internacionales](classes/10-remesas-y-corredores-internacionales.md)
11. [Pagos empresariales y comercio exterior](classes/11-pagos-empresariales-y-comercio-exterior.md)
12. [AML, sanciones y regla del viaje](classes/12-aml-sanciones-y-regla-del-viaje.md)
13. [Interconexión de sistemas de pagos inmediatos](classes/13-interconexion-de-pagos-inmediatos.md)
14. [Stablecoins y pagos internacionales](classes/14-stablecoins-y-pagos-internacionales.md)
15. [Payment versus Payment y liquidación atómica](classes/15-payment-versus-payment-y-liquidacion-atomica.md)
16. [Proyecto: red de pagos transfronterizos](classes/16-proyecto-red-de-pagos-transfronterizos.md)

## Laboratorios

| # | Laboratorio | Entregable principal |
|---:|---|---|
| 1 | [Transferencia con corresponsales](labs/lab-01.md) | Trazado de los cuatro flujos |
| 2 | [Motor de rutas](labs/lab-02.md) | Selección con coste, plazo y riesgo |
| 3 | [Mensajes ISO 20022](labs/lab-03.md) | `pacs.008` válido y su cadena de estados |
| 4 | [Screening y reparaciones](labs/lab-04.md) | Cola de investigación con tasa de STP |
| 5 | [Comparador de remesas](labs/lab-05.md) | Coste total por corredor |
| 6 | [Interconexión de pagos inmediatos](labs/lab-06.md) | Enlace bilateral con FX y liquidación |
| 7 | [Payment versus Payment](labs/lab-07.md) | Liquidación condicional sin riesgo Herstatt |
| 8 | [Ruta mediante stablecoin](labs/lab-08.md) | Comparación honesta contra la ruta clásica |

## Evaluaciones

- [Diagnóstico](assessments/diagnostic.md)
- [Evaluación final](assessments/final.md)

## Proyecto

- [Red de pagos transfronterizos](project/README.md)

## Evidencias

- Trazado completo de los cuatro flujos de un pago con corresponsales.
- Mensajes ISO 20022 validados, incluidos los de rechazo y devolución.
- Descomposición del coste total con el diferencial de cambio aislado.
- Modelo de liquidez con prefinanciación, netting y horarios.
- Comparación de cuatro arquitecturas con métricas, no con adjetivos.
- Registro de decisiones con la alternativa descartada.

## Mapa de dependencias

```text
Parte 10 (operaciones bancarias)
   └── Parte 18 — pagos transfronterizos
          ├── Parte 20 · stablecoins como activo de liquidación
          ├── Parte 21 · PvP y liquidación atómica multidivisa
          ├── Parte 22 · normativa de cambios y de pagos
          └── Parte 23 · capa transfronteriza del banco digital
```

## Aplicación asociada

- [`apps/cross_border_payments_lab/`](../../apps/cross_border_payments_lab/README.md)

## Fuentes oficiales de referencia

- Committee on Payments and Market Infrastructures (BIS) — informes sobre pagos transfronterizos y corresponsalía.
- Financial Stability Board — hoja de ruta del G20 y sus informes de avance.
- SWIFT / ISO 20022 — catálogo de mensajes y guías de uso CBPR+.
- Banco Mundial — *Remittance Prices Worldwide*.
- Grupo de Acción Financiera Internacional — Recomendación 16.
- Banco Central de Chile — Compendio de Normas de Cambios Internacionales.

## Limitaciones

- Las cifras de coste, plazo y volumen del material son **ilustrativas** salvo
  cuando se cita la fuente: los valores reales cambian por corredor y por mes.
- Los proyectos institucionales citados están en distintos estados; cada clase
  indica qué demostró cada uno y qué **no** demostró.
- El entorno simulado no se conecta con ninguna red de pagos real ni mueve
  fondos. No sustituye la normativa de cambios internacionales aplicable.
