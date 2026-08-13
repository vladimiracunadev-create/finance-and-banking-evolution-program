# Caso · Un mercado con mucho volumen y poca gente

**Tema:** regulación de mercados · **Parte relacionada:** 22 · **Naturaleza:**
caso sintético compuesto · **Fecha de verificación:** 2026-08-12

Una plataforma publica un volumen diario de 240 millones y aparece entre las
primeras de su categoría. Un análisis posterior encuentra que el 63 % de ese
volumen se produce entre cuentas que comparten origen de fondos. El volumen es
real en el sentido de que las operaciones existen; no lo es en el sentido de que
alguien haya cambiado de posición.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · volumen diario publicado    240 000 000
  · cuentas activas al día            3 100
  · el 63 % del volumen se concentra en
    41 cuentas
  · esas 41 cuentas recibieron su fondeo
    inicial desde 4 orígenes comunes
  · operan entre sí, con posiciones netas
    casi planas al cierre de cada día
  · comisión efectiva para esas cuentas:
    0, por un programa de creadores de
    mercado

SUPUESTO DEL EJERCICIO
  · volumen económico real       88 800 000
  · ingreso por comisiones          124 000
  · coste del programa de incentivos 96 000
```

El detalle que hace posible el patrón es el último de la lista de hechos: **el
programa de incentivos hacía que operar consigo mismo fuera gratis o rentable.**
Un diseño de incentivos que no penaliza la operación circular la produce.

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Operador de las 41 cuentas | Incentivos y apariencia de liquidez | Su propia estructura |
| Plataforma | Aparecer en los primeros puestos | Los datos de fondeo, si los miraba |
| Inversor que elige plataforma | Liquidez real | Un ranking por volumen |
| Agregador de datos | Publicar rankings | Volumen declarado |
| Creador de mercado legítimo | Competir | Un mercado con volumen falso |
| Supervisor | Integridad y transparencia | Nada, hasta el análisis |

## Decisiones

```text
DE LA PLATAFORMA
  lanzar un programa de incentivos por
  volumen sin límite de contraparte
  DECISIÓN COMERCIAL QUE CREA EL PATRÓN

DE LA PLATAFORMA
  no cruzar origen de fondos entre cuentas
  RAZÓN: coste y fricción en el alta

DEL OPERADOR
  abrir 41 cuentas y operar entre ellas
  DECISIÓN RACIONAL DADO EL INCENTIVO

DEL AGREGADOR
  publicar el ranking por volumen declarado
  SIN MÉTRICA DE CALIDAD

DEL INVERSOR
  elegir por ranking
  DECISIÓN INFORMADA CON UN DATO MALO
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Incentivos que premian el volumen circular | Desde el programa | Sí |
| Ausencia de cruce de origen de fondos | Desde el alta | Sí |
| Ranking sin métrica de calidad | Estructural | Sí |
| Decisión del inversor con dato falso | Desde el ranking | Sí |
| Desplazamiento de creadores legítimos | Estructural | Sí |
| Riesgo de sanción a la plataforma | Latente | Sí |

## Regulación

```text
QUÉ ALCANZA

  ABUSO DE MERCADO
    las operaciones que no producen cambio
    de titularidad económica real y dan
    apariencia de actividad encajan en las
    descripciones de manipulación de la
    mayoría de los regímenes

  RESPONSABILIDAD DE LA PLATAFORMA
    quien opera un mercado suele tener
    obligación de vigilar y de comunicar
    operaciones sospechosas; no basta con
    no participar

  INFORMACIÓN AL PÚBLICO
    publicar volumen sin metodología ni
    controles puede constituir información
    engañosa

LÍMITE
  el régimen aplicable a la plataforma
  depende de su calificación y de la
  jurisdicción
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Vigilancia de operaciones | Parcial | No | Detección de operativa circular |
| Cruce de origen de fondos | No | — | Grafo de fondeo entre cuentas |
| Límite de contraparte en incentivos | No | — | No premiar operar consigo mismo |
| Métrica de calidad del volumen | No | — | Volumen con cambio neto de posición |
| Auditoría del programa | No | — | Revisión trimestral de su efecto |
| Comunicación de operaciones sospechosas | No | — | Procedimiento y responsable |

La métrica del cuarto control es la que resuelve el problema de raíz y es sencilla
de definir: **volumen que produce cambio neto de posición al cierre.** Publicar
esa cifra junto al volumen bruto hace inútil el patrón.

## Resultado

```text
CUANDO SE PUBLICA LA MÉTRICA DE CALIDAD

  volumen bruto            240 000 000
  volumen con cambio neto   88 800 000
  proporción                    37 %

  POSICIÓN EN EL RANKING
    por volumen bruto             4.ª
    por volumen con cambio       19.ª

CONSECUENCIAS (supuestos)
  · el operador de las 41 cuentas se retira
  · el volumen cae a 91 000 000
  · el ingreso por comisiones sube a
    139 000 (se retira el incentivo)
  · entran dos creadores de mercado que
    antes no competían

EL MERCADO SE HACE MÁS PEQUEÑO
Y MÁS ÚTIL.
```

## Lecciones

1. **Un incentivo mal diseñado produce exactamente la conducta que premia.** Si se
   premia el volumen sin condición, se obtiene volumen sin contenido.
2. **El volumen bruto no mide liquidez.** La métrica útil es la que refleja cambio
   neto de posición, y es fácil de calcular.
3. **La plataforma responde aunque no participe.** Operar un mercado conlleva
   vigilar el mercado que se opera.
4. **Un ranking sin metodología traslada el error a quien decide con él**, y ese
   es el daño principal del caso.

## Preguntas

1. ¿Cómo definirías «volumen con cambio neto de posición» de forma que no se pueda
   eludir?
2. ¿Qué límites pondrías al programa de incentivos sin desincentivar la
   provisión legítima de liquidez?
3. ¿Debe la plataforma comunicar estas operaciones como sospechosas? ¿Desde qué
   momento?
4. ¿Qué responsabilidad tiene el agregador que publica el ranking?
5. ¿Es siempre ilícito operar entre cuentas del mismo titular? ¿Dónde está el
   límite?

## Fuentes

- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- IOSCO. *Investigating and Prosecuting Market Manipulation*. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD103.pdf>
- Diario Oficial de la Unión Europea (2023). *Reglamento (UE) 2023/1114*, título sobre abuso de mercado. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32023R1114>
- CMF. *Normativa sobre conducta de mercado*. <https://www.cmfchile.cl/>
- Verificación local: caso sintético; cifras supuestas. La calificación de la operativa circular depende de la jurisdicción y de los hechos concretos. **Fecha de verificación: 2026-08-12.** No constituye asesoría legal.
