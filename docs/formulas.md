# Formulario

Las fórmulas que el programa usa, con su significado y su trampa habitual. Cada una
indica la parte donde se desarrolla.

> **⚠️ La regla que evita la mitad de los errores**
>
> **Convierte siempre la tasa a la misma periodicidad de los flujos**, y **verifica la
> escala antes de sumar o multiplicar**. Las clases del programa incluyen esa
> verificación de forma explícita porque es donde se producen los errores más caros.

---

## 1 · Valor del dinero en el tiempo

<sub>Parte 1 · Matemática financiera básica</sub>

| Concepto | Fórmula | Trampa habitual |
|---|---|---|
| Interés simple | `VF = VP × (1 + i × n)` | Usarlo para plazos largos |
| Interés compuesto | `VF = VP × (1 + i)ⁿ` | No convertir la tasa a la periodicidad |
| Valor presente | `VP = VF / (1 + i)ⁿ` | Descontar con una tasa que no refleja el riesgo |
| Tasa efectiva anual | `TEA = (1 + i/m)^m − 1` | Comparar una nominal con una efectiva |
| Tasa equivalente | `i₂ = (1 + i₁)^(n₁/n₂) − 1` | Dividir la anual por 12 |
| Tasa real | `r = (1 + i)/(1 + π) − 1` | Restar la inflación en lugar de dividir |

## 2 · Anualidades y amortización

<sub>Parte 1</sub>

| Concepto | Fórmula |
|---|---|
| Valor presente de una anualidad | `VP = C × [1 − (1+i)⁻ⁿ] / i` |
| Valor futuro de una anualidad | `VF = C × [(1+i)ⁿ − 1] / i` |
| Cuota fija (sistema francés) | `C = P × i(1+i)ⁿ / [(1+i)ⁿ − 1]` |
| Saldo insoluto tras *k* cuotas | `S_k = C × [1 − (1+i)^-(n−k)] / i` |
| Perpetuidad | `VP = C / i` |
| Perpetuidad creciente | `VP = C / (i − g)`, con `g < i` |

> **Trampa:** en el sistema francés, la primera cuota amortiza poco capital. Un prepago
> temprano ahorra mucho más interés que uno tardío (Parte 2).

## 3 · Evaluación de proyectos

<sub>Parte 13 · Finanzas corporativas</sub>

| Concepto | Fórmula | Regla |
|---|---|---|
| Valor presente neto | `VPN = Σ FC_t/(1+k)^t − I₀` | Aceptar si > 0 |
| Tasa interna de retorno | `k tal que VPN = 0` | Aceptar si > costo de capital |
| Índice de rentabilidad | `IR = VP(flujos) / I₀` | Aceptar si > 1 |
| Valor terminal (crecimiento) | `VT = FC_(n+1) / (WACC − g)` | `g` ≤ crecimiento de la economía |

> **Trampa:** entre proyectos mutuamente excluyentes, **decide por VPN**. La TIR es un
> porcentaje y no sabe sobre cuánto capital se aplica.

## 4 · Costo de capital

<sub>Parte 13</sub>

| Concepto | Fórmula |
|---|---|
| Costo del patrimonio | `ke = rf + β × (rm − rf) [+ primas]` |
| Costo de la deuda | `kd × (1 − t)` |
| Costo promedio ponderado | `WACC = ke × E/(D+E) + kd(1−t) × D/(D+E)` |
| Desapalancar beta | `βu = βL / [1 + (1−t) × D/E]` |
| Apalancar beta | `βL = βu × [1 + (1−t) × D/E]` |

> **Trampa:** usa **valores de mercado** como pesos, no contables. Y el costo de la deuda
> relevante es el **marginal**, no el histórico.

## 5 · Renta fija

<sub>Parte 7 · Matemática financiera avanzada</sub>

| Concepto | Fórmula |
|---|---|
| Precio de un bono | `P = Σ C/(1+y)^t + VN/(1+y)ⁿ` |
| Duración de Macaulay | `D = Σ [t × VP(FC_t)] / P` |
| Duración modificada | `D_mod = D / (1 + y)` |
| Cambio de precio aproximado | `ΔP/P ≈ −D_mod × Δy + ½ × C × (Δy)²` |
| Convexidad | `C = Σ [t(t+1) × VP(FC_t)] / [P(1+y)²]` |

> **Trampa:** la duración sola subestima la caída ante alzas grandes. La convexidad
> corrige, y siempre a favor del tenedor del bono.

## 6 · Carteras

<sub>Parte 8 · Inversiones y mercados</sub>

| Concepto | Fórmula |
|---|---|
| Rendimiento de la cartera | `E(Rp) = Σ w_i × E(R_i)` |
| Varianza (dos activos) | `σp² = w₁²σ₁² + w₂²σ₂² + 2w₁w₂ρσ₁σ₂` |
| Índice de Sharpe | `S = (Rp − rf) / σp` |
| Beta de un activo | `β = Cov(R_i, R_m) / σm²` |

## 7 · Riesgo de crédito

<sub>Parte 9 · Análisis y gestión de crédito</sub>

| Concepto | Fórmula |
|---|---|
| Pérdida esperada | `PE = PD × LGD × EAD` |
| LGD | `LGD = 1 − (recuperación − costos) × factor de descuento` |
| EAD de una línea | `EAD = saldo usado + FCC × parte no usada` |
| Capital IRB (cartera granular) | `K = LGD × [N((N⁻¹(PD) + √ρ·N⁻¹(0,999))/√(1−ρ)) − PD] × ajuste de plazo` |
| Índice de Herfindahl | `HHI = Σ wᵢ²` · número efectivo `= 1/HHI` |

> **Trampa:** el factor de conversión observado en el incumplimiento **supera** al
> regulatorio: quien va a incumplir usa toda la línea disponible (Parte 16, clase 8).

## 8 · Riesgo de mercado y de tasa

<sub>Parte 11 · Gestión integral de riesgos</sub>

| Concepto | Fórmula |
|---|---|
| Valor en riesgo (paramétrico) | `VaR = z × σ × √h × V` |
| Escalamiento temporal | `VaR_h = VaR_1 × √h` |
| Déficit esperado | `ES = E[pérdida \| pérdida > VaR]` |
| Volatilidad de cartera | `σp = √(Σ Σ σᵢ σⱼ ρᵢⱼ)` |
| Sensibilidad del margen | `Δmargen ≈ Σ brecha_t × Δi × (días/365)` |
| Sensibilidad del valor económico | `ΔVEP ≈ −brecha de duración × Δi × activos` |
| Brecha de duración | `D_A − D_P × (Pasivos/Activos)` |

> **Trampa:** el escalamiento por `√h` supone independencia entre días. La volatilidad se
> agrupa, así que **subestima**.

## 9 · Liquidez y capital

<sub>Partes 11 y 12</sub>

| Concepto | Fórmula |
|---|---|
| Cobertura de liquidez | `LCR = HQLA / salidas netas a 30 días ≥ 100 %` |
| Financiamiento estable neto | `NSFR = disponible / requerido ≥ 100 %` |
| Ratio de capital | `CET1 / activos ponderados por riesgo` |
| Ratio de apalancamiento | `capital nivel 1 / exposición total ≥ 3 %` |
| Conversión a activos ponderados | `APR = requerimiento / 8 % = requerimiento × 12,5` |
| RAROC | `resultado ajustado por riesgo / capital económico asignado` |
| Valor económico añadido | `VEA = resultado ajustado − capital × costo del capital` |

## 10 · Precio de un crédito

<sub>Partes 11, 15 y 16</sub>

```text
tasa mínima = costo de fondos del plazo
            + pérdida esperada (PD × LGD)
            + costo operativo
            + costo del capital × capital asignado / exposición
            + margen objetivo
```

> **Trampa:** el costo de fondos corresponde al **plazo conductual**, no al contractual.
> Un hipotecario a 20 años con prepago medio de 8,2 años se financia a 8 años.

## 11 · Análisis de empresas

<sub>Parte 13</sub>

| Concepto | Fórmula |
|---|---|
| Descomposición del ROE | `ROE = margen neto × rotación de activos × apalancamiento` |
| Ciclo de conversión de efectivo | `días inventario + días cobro − días pago` |
| Necesidad operativa de fondos | `existencias + cobros + caja mínima − proveedores` |
| Fondo de maniobra | `(patrimonio + deuda LP) − activo no corriente` |
| Cobertura del servicio de la deuda | `flujo disponible / servicio de la deuda` |
| Crecimiento sostenible | `g = ROE × (1 − tasa de reparto)` |

## 12 · Eficiencia y desempeño

<sub>Parte 15</sub>

| Concepto | Fórmula |
|---|---|
| Índice de eficiencia | `gastos operativos / ingresos operativos` |
| Margen de intermediación | `margen financiero / activos productivos medios` |
| Resultado antes de provisiones / activos | La medida de capacidad de generación real |
| Ratio de cobertura óptimo | `h* = ρ × (σ_S / σ_F)` |

---

## Verificaciones que el programa exige siempre

1. **Periodicidad** — la tasa y los flujos en la misma unidad de tiempo.
2. **Escala** — verifica el orden de magnitud antes de sumar o multiplicar.
3. **Signo** — un pasivo que baja de valor es ganancia; un activo, pérdida.
4. **Supuesto** — declara de qué depende el resultado antes de calcularlo.
5. **Holgura sospechosa** — si un resultado es mucho mejor de lo esperado, falta un costo.

---

**Ver también:** [Glosario](glosario.md) · [Fuentes](fuentes.md) ·
[Calculadoras](../apps/financial_calculators) · [Índice del programa](../SYLLABUS.md)
