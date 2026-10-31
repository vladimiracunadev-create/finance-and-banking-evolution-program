# Ejercicios y evaluación: crisis financiera digital

Complemento práctico de la [guía de crisis financiera digital](crisis-financiera-digital.md).
Cada ejercicio resuelto sigue el mismo orden: **fórmula → variables y unidad →
supuesto → cálculo → interpretación → límite**. Todos los importes son millones
de USD (MUSD) salvo que se indique; los datos son **sintéticos** y reproducibles
con `apps/custody_crisis_lab/` y los
[datasets](../datasets/README.md) `custody_crisis_*`. Una prueba de regresión
(`tests/test_custody_crisis_lab.py`) comprueba que las cifras de este documento
coincidan con el código.

## Parte A · Ejercicios resueltos

### Ejercicio 1 · Respaldo antes y después

**Datos.** `A_liq = 80 000`, `A_nl = 20 000`, `P = 100 000`. Un incidente
sustrae `S = 6 300` íntegramente de activos líquidos.

**Fórmulas.** `R_b = (A_liq + A_nl)/P`; `R_d = A_liq/P`; `B = P − (A_liq + A_nl)`.

| | Antes | Después |
|---|---:|---:|
| `R_b` | 100,00 % | (100 000 − 6 300)/100 000 = **93,70 %** |
| `R_d` | 80,00 % | (80 000 − 6 300)/100 000 = **73,70 %** |
| `B` | 0 | **6 300** |

**Interpretación.** Cada punto de `S/P` baja un punto de respaldo; como la
pérdida salió de lo líquido, el respaldo *disponible* cae lo mismo que el bruto
pero parte de una base más baja. **Límite.** Se supone que el 100 % inicial era
real: si no lo era, todo el cálculo parte de una cifra falsa.

### Ejercicio 2 · Sustraído, congelado y perdido

**Datos.** `S = 6 300`, `F = 3 000`, `p = 0,8`.

**Cálculo.** `U = S − F = 3 300`; `E[rec] = F·p = 2 400`; `D = S − F·p = 3 900`.

| `p` | `E[rec]` | `D` |
|---:|---:|---:|
| 0,5 | 1 500 | 4 800 |
| 0,8 | 2 400 | **3 900** |
| 1,0 | 3 000 | 3 300 |

**Interpretación.** Aun con restitución completa, `D ≥ U = 3 300`: lo no
congelado es pérdida salvo recuperación por otras vías. **Límite.** `p` no está
calibrado; la tabla es un análisis de sensibilidad, no una predicción.

### Ejercicio 3 · Retiros masivos

**Datos.** Tras el ejercicio 1: `r0 = 0,03`, `k = 1,0`, pausa de 2 días,
descuento `h = 5 %`.

**Cálculo del día 3.** `R_b = 0,937` → tasa = 0,03 + 1,0·(1 − 0,937) = **9,3 %**
→ `D_3 = 100 000 · 0,093 = 9 300`. La tasa máxima atendible sin vender nada es
`r* = A_liq/P = 73,7 %`, y con una demanda del 10 %,
`C = 73 700/(0,10 · 100 000) = 7,37`: la liquidez alcanza para 7,37 días de esa
demanda.

**Interpretación.** El deterioro del respaldo *eleva* la tasa (0,03 → 0,093).
**Límite.** `k = 1,0` es un supuesto; con `k = 3,0` la misma pérdida produce una
demanda del 21,9 % diario.

### Ejercicio 4 · Reposición

**Datos.** `N = 6 300`. Fuentes en orden: fondo de protección 800 (costo 0 %),
capital propio 5 000 (1 %), financiamiento externo hasta 50 000 (6 %).

**Cálculo.** 800 + 5 000 + 500 = 6 300. Costos: 0 + 50 + 30 = **80**.

**Compra con impacto.** Comprar `monto = 500` con `impacto = 0,02` y
`profundidad = 1 000` cuesta `0,02 · 500² / 1 000 = 5`; comprar el doble cuesta
**20**, no 10: el costo crece con el cuadrado del monto.

**Interpretación.** Reponer rápido y en grande es caro de forma no lineal.
**Límite.** En tensión la profundidad se contrae y el modelo subestima.

### Ejercicio 5 · Costo del incidente

**Datos.** `D = 3 900`; `C_rep = 80`; `C_for = 50`; ingreso diario 8 MUSD y 2 días
de pausa; compensaciones 0.

**Cálculo.** `C_op = 8 · 2 = 16`. `C_total = 3 900 + 80 + 50 + 16 + 0 =` **4 046**.
Con un seguro de cobertura 500 y pérdida asegurable 300:
`C_neto = 4 046 − min(500, 300) = 3 746`.

**Interpretación.** El costo (4 046) y lo sustraído (6 300) son preguntas
distintas con respuestas distintas. **Límite.** Faltan clientes futuros y
reputación.

## Parte B · Propuestas de cálculo para estudiantes

Sin solución en este documento; el docente dispone de la pauta en la guía
docente. Entrega: tabla, fórmula usada, supuesto declarado y una frase de límite.

1. **Sensibilidad de `p`.** Con el escenario `crd_003`, calcula `D` para
   `p = 0, 0,25, 0,5, 0,75, 1` y grafica. ¿A partir de qué `p` el costo total
   baja de 19 000?
2. **Umbral de pausa.** Con `crd_002` y `k = 1,0`, busca el menor número de días
   de pausa tal que el respaldo del último día de la simulación (7) supere 90 %.
   ¿Cuánto cuesta esa pausa en `C_op`?
3. **Punto de quiebre de la corrida.** ¿Qué valor de `k` hace que, con `crd_002`
   y sin reposición, aparezca el primer día con `impagado > 0`?
4. **Fuentes de reposición.** Reordena las fuentes del ejercicio 4 de mayor a
   menor costo. ¿Cuánto más cuesta el plan? ¿Qué se gana en velocidad?
5. **Proof of Reserves.** Con el dataset de balance, diseña una tabla de PoR
   (activos por categoría, corte, alcance) y una de Proof of Liabilities. ¿Qué
   producto de los dos deja un hueco si se omite `bal_007`?
6. **Entidad estilizada.** En `cases.entidad_binance_estilizada()`, cambia la
   fracción líquida de 85 % a 60 %. ¿Cómo cambian `R_d` y la tasa máxima
   atendible después de `S = 6 300`?
7. **Extensión de código.** Añade a `costs.py` un componente de «costo de
   financiamiento durante la pausa» y una prueba que lo verifique.
8. **Discrepancia de fuentes.** Con `cases.CIFRAS_PUBLICAS`, calcula la
   diferencia entre las cifras de sustracción de las tres fuentes (en MUSD y en
   %) y entre la suma de emisores y lo congelado declarado. Escribe tres
   hipótesis que expliquen la diferencia.

## Parte C · Evaluación

Duración sugerida: 90 minutos. Total: 100 puntos. Se permite calculadora y el
laboratorio; no se permiten fuentes sin fecha.

**Entidad de la evaluación (sintética).** `P = 50 000`, `A_liq = 36 000`,
`A_nl = 9 000`, fondo de protección 500. Un incidente sustrae `S = 2 000` de
activos líquidos; `F = 1 200`, `p = 0,5`.

| # | Pregunta | Pts |
|---|---|---:|
| 1 | Calcula `R_b`, `R_d` y `B` antes y después del incidente | 15 |
| 2 | Calcula `U`, `E[rec]` y `D`; explica por qué `D ≠ S` | 15 |
| 3 | Calcula `r*` y la cobertura `C` para una demanda diaria del 8 % | 10 |
| 4 | Reposición a 100 %: `N` y costo con fuentes (500 al 0 %; 4 000 al 1 %; 20 000 al 5 %) | 15 |
| 5 | Costo total con `C_for = 20`, ingreso diario 3 y 4 días de pausa | 10 |
| 6 | Explica por qué un Proof of Reserves sin Proof of Liabilities no prueba respaldo | 10 |
| 7 | Distingue «transferencia sospechosa», «fondos congelados» y «pérdida definitiva» con un ejemplo | 10 |
| 8 | Enumera cinco controles de prevención y dos de detección, cada uno con su pregunta de auditoría | 10 |
| 9 | Ordena las siete fases del plan de recuperación y da la condición de salida de la fase 2 | 5 |

### Rúbrica

| Nivel | Criterio |
|---|---|
| Logrado (100 %) | Fórmula, variables, unidad, supuesto, cálculo correcto e interpretación |
| Parcial (60 %) | Cálculo correcto sin supuesto ni interpretación, o error aritmético con método correcto |
| Insuficiente (20 %) | Cifra sin método, o método que mezcla sustraído, congelado y perdido |

### Pauta de corrección

1. Antes: `R_b = 45 000/50 000 = 90 %`; `R_d = 72 %`; `B = 5 000`. Después:
   `R_b = 43 000/50 000 = 86 %`; `R_d = 34 000/50 000 = 68 %`; `B = 7 000`.
2. `U = 800`; `E[rec] = 600`; `D = 1 400`. `D ≠ S` porque parte de lo congelado
   se restituye (con probabilidad `p`).
3. `r* = 68 %`; `C = 34 000/(0,08 · 50 000) = 8,5`.
4. `N = 50 000 − 43 000 = 7 000`. Aportes: 500 + 4 000 + 2 500; costos:
   0 + 40 + 125 = **165**.
5. `C_op = 3 · 4 = 12`. `C_total = 1 400 + 165 + 20 + 12 + 0 =` **1 597**.
6. Numerador sin denominador: los activos observados no se comparan con las
   obligaciones, y la omisión de productos (rendimiento, préstamos) oculta
   pasivos.
7. Sospechosa: indicio sin determinación; congelada: inmovilizada sin
   restitución; pérdida definitiva: lo no recuperado al cierre del proceso.
8. Respuesta abierta; se valora la pregunta de auditoría de la sección 3 de la
   guía.
9. Contención, cuantificación, comunicación, reposición, reapertura,
   verificación, aprendizaje. Salida de la fase 2: brecha firmada y revisada por
   segunda línea.

## Parte D · Para el docente

- Entrega primero la sección 1 de la guía y deja que el grupo calcule antes de
  ejecutar el laboratorio; la discusión nace de la diferencia.
- Usa el [caso Binance 2026](../case-studies/custody/binance-2026.md) en dos
  rondas: primero solo los hechos con una fuente, luego con las tres.
- La [guía docente](guia-docente.md) y la
  [guía de laboratorios digitales](guia-laboratorios-digitales.md) describen la
  evaluación del programa; esta evaluación **no reemplaza** ninguna de las 46
  existentes.
