# Caso · Cuarenta minutos antes del cierre

**Tema:** regulación de mercados · **Parte relacionada:** 22 · **Naturaleza:**
caso sintético compuesto · **Fecha de verificación:** 2026-08-12

Un participante compra durante los últimos cuarenta minutos de la ventana de
cálculo de un índice. Las compras son reales, se pagan y se liquidan. El precio
del índice sube un 3,1 % y con él el valor de una posición que el mismo
participante tenía en otro mercado. Nadie mintió. El caso trata de por qué eso
puede seguir siendo manipulación.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · el índice se calcula con el precio medio
    ponderado de la última hora
  · volumen habitual en esa hora   1 900 000
  · volumen ese día                7 400 000
  · el 71 % del exceso viene de un
    participante
  · sus órdenes se ejecutan a precios
    crecientes
  · vende el 84 % de lo comprado en las
    dos sesiones siguientes, con pérdida

POSICIÓN EN OTRO MERCADO
  · derivado liquidado contra ese índice
  · nocional                     92 000 000
  · efecto de un 3,1 %            2 852 000

SUPUESTO DEL EJERCICIO
  · pérdida en las compras           410 000
  · beneficio neto                 2 442 000
```

El patrón que lo delata no es ninguna de esas cifras por separado: es la
combinación de **comprar caro, en la ventana que importa, y deshacer con pérdida
inmediatamente después**. Un comprador que quiere el activo no vende al día
siguiente con pérdida; un comprador que quiere el precio, sí.

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Participante | Que el índice cierre alto | Su posición en el derivado |
| Contraparte del derivado | Liquidar a precio correcto | El índice publicado |
| Administrador del índice | Calcular según su metodología | Los precios, no las intenciones |
| Mercado de contado | Volumen | Sus propias órdenes |
| Vigilancia del mercado | Detectar patrones | Datos con retraso |
| Supervisor | Integridad del mercado | La denuncia, meses después |

## Decisiones

```text
DEL PARTICIPANTE
  concentrar la compra en la ventana
  DECISIÓN QUE DEFINE EL CASO

DEL ADMINISTRADOR DEL ÍNDICE
  usar la última hora como ventana
  DECISIÓN DE DISEÑO QUE CREA EL INCENTIVO

DE LA VIGILANCIA
  alerta por volumen anómalo, revisada
  a los 6 días
  DEMASIADO TARDE PARA LA LIQUIDACIÓN

DE LA CONTRAPARTE
  liquidar según el índice publicado
  NO TENÍA ALTERNATIVA CONTRACTUAL
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Ventana de cálculo manipulable | Desde el diseño del índice | Sí |
| Ausencia de vigilancia entre mercados | Estructural | Sí |
| Alerta con revisión diferida | Desde el proceso | Sí |
| Liquidación sin cláusula de anomalía | Desde el contrato | Sí |
| Prueba de la intención | Estructural | Sí, como dificultad |
| Contagio a otros derivados del índice | Estructural | Parcialmente |

## Regulación

```text
QUÉ ALCANZA

  MANIPULACIÓN DE MERCADO
    los regímenes suelen describir como
    manipulación las operaciones que dan
    o pueden dar señales falsas sobre el
    precio, o que fijan el precio en un
    nivel artificial

  OPERACIONES REALES
    que las operaciones sean reales y se
    liquiden NO excluye la conducta: lo
    relevante es el efecto sobre el precio
    y el propósito

  ÍNDICES DE REFERENCIA
    varios regímenes regulan la elaboración
    de índices y exigen metodologías
    resistentes a la manipulación

LÍMITE
  la tipificación y la carga de la prueba
  dependen de la jurisdicción
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Alerta por volumen | Sí | Sí, tarde | Revisión en el día |
| Vigilancia entre mercados | No | — | Cruzar contado y derivados |
| Metodología del índice | Sí | Sí, vulnerable | Ventana aleatoria o más larga |
| Cláusula de precio anómalo | No | — | Recalcular si hay anomalía |
| Declaración de posiciones | Parcial | No | En el mercado que liquida |
| Registro de órdenes con identidad | Sí | Sí | Uso efectivo para cruzar |

El tercero es el control estructural: **una ventana de cálculo aleatoria dentro de
la sesión, o de varias horas, encarece la manipulación en proporción directa.**
Ningún control de vigilancia sustituye a un índice bien diseñado.

## Resultado

```text
BALANCE (supuestos)

  beneficio del participante  2 442 000
  pérdida de la contraparte   2 852 000
  diferencia absorbida por el
    mercado de contado          410 000

  SANCIÓN, SI SE PRUEBA
    depende del régimen; en varios
    incluye devolución del beneficio,
    multa y prohibición de operar

TIEMPO HASTA LA RESOLUCIÓN
  estimado 18 a 36 meses
  → la contraparte liquidó y pagó
    mucho antes
```

## Lecciones

1. **Operaciones reales pueden ser manipulación.** El criterio no es la
   veracidad de la operación, sino su efecto sobre el precio y su propósito.
2. **El patrón se ve en el conjunto, no en la operación.** Comprar caro y deshacer
   con pérdida solo tiene sentido si el beneficio está en otro sitio.
3. **La vigilancia que no cruza mercados no ve nada.** El contado y el derivado
   son el mismo caso.
4. **Un índice mal diseñado crea el incentivo.** La ventana de cálculo es una
   decisión de integridad de mercado, no una decisión técnica.

## Preguntas

1. ¿Qué evidencia harías falta para probar el propósito? ¿Basta el patrón?
2. ¿Cómo rediseñarías la ventana de cálculo del índice y qué coste tiene?
3. ¿Debería la contraparte poder impugnar la liquidación? ¿Con qué umbral?
4. ¿Qué señales incluirías en una vigilancia que cruce contado y derivados?
5. ¿Cambia el análisis si el participante alega que compraba por razones
   legítimas de cobertura?

## Fuentes

- IOSCO. *Principles for Financial Benchmarks*. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD415.pdf>
- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- Diario Oficial de la Unión Europea (2023). *Reglamento (UE) 2023/1114*, título sobre abuso de mercado. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32023R1114>
- CMF. *Normativa sobre conducta de mercado e información privilegiada*. <https://www.cmfchile.cl/>
- Verificación local: caso sintético; cifras supuestas. La tipificación de la manipulación y la carga de la prueba dependen de la jurisdicción. **Fecha de verificación: 2026-08-12.** No constituye asesoría legal.
