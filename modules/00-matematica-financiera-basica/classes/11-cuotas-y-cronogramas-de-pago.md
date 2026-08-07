---
part: 1
class: 11
title: "Cuotas y cronogramas de pago"
level: fundamento
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 11 · Cuotas y cronogramas de pago

> [← 10 · Valor futuro](10-valor-futuro.md) · [Índice de la parte](../README.md) · [12 · Amortización básica →](12-amortizacion-basica.md)

**Parte 01 — Matemática financiera básica** · **Nivel:** Fundamento — sin conocimientos previos · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir, entender y auditar el documento más importante de cualquier crédito: la **tabla de
desarrollo**. Aquí se ve, línea por línea, cuánto de cada cuota paga interés y cuánto reduce la
deuda. Es también la clase donde se descubre por qué las primeras cuotas casi no bajan el saldo, y
por qué prepagar temprano tiene un efecto desproporcionado.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** la cuota fija de un crédito con la fórmula del sistema francés.
2. **Construir** una tabla de desarrollo completa y verificar que cierre en cero.
3. **Descomponer** cualquier cuota en interés y amortización.
4. **Cuantificar** el efecto de un prepago según el momento en que se hace.
5. **Auditar** una tabla entregada por un tercero y detectar inconsistencias.

<!-- gen:agenda:start -->
## Agenda de 90 minutos

La clase dura noventa minutos y se recorre en cinco tramos. No es un horario
rígido: es el orden en que los bloques de esta página se sostienen unos a otros, y
por eso conviene respetarlo aunque cambien los tiempos.

Los **diez primeros minutos** se dedican a recuperar la clase anterior, porque casi
todo lo que aquí se explica supone algo que ya se vio. Los **veinticinco
siguientes** desarrollan los conceptos con la fuente oficial a la vista: las
referencias del final de la página no son un adorno bibliográfico, se consultan
mientras se estudia. Del **minuto 35 al 55** se resuelve el ejemplo guiado paso a
paso, sin saltarse ninguno, porque el error típico vive precisamente en el paso que
parece obvio. Los **veinticinco minutos siguientes** son de práctica con datos
propios o sintéticos —nunca reales de terceros—, que es cuando se comprueba si se
entendió. Los **diez últimos** cierran con las preguntas de comprobación y el
registro del entregable.

Si el tiempo aprieta, lo que se recorta es la práctica y se traslada al
laboratorio de la parte; lo que no se recorta nunca es el ejemplo guiado.
<!-- gen:agenda:end -->

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| `cuota` | Pago periódico total. En el sistema francés es constante; su **composición** cambia cada periodo. |
| `interés del periodo` | `saldo anterior × tasa periódica`. Se calcula **antes** de amortizar. |
| `amortización` | `cuota − interés`. Es la parte que efectivamente reduce la deuda. |
| `saldo insoluto` | Capital que aún se debe. Es la base del interés del periodo siguiente. |
| `tabla de desarrollo` | Cronograma completo, cuota por cuota. Documento contractual y auditable. |
| `prepago` | Pago extraordinario aplicado a capital. Su efecto depende críticamente de cuándo se hace. |
| `cierre en cero` | Control obligatorio: el saldo tras la última cuota debe ser 0 salvo el ajuste de centavos. |

## 🧠 Modelo mental

Cada cuota atraviesa **dos puertas en orden fijo**:

```text
cuota  →  [1. paga el interés devengado]  →  [2. lo que sobra reduce el capital]
```

Si el interés se lleva casi toda la cuota, el saldo baja poco. Eso ocurre al principio, cuando el
saldo —y por lo tanto el interés— es máximo. No es un truco del banco: es aritmética, y se puede
verificar línea por línea.

## 📖 Desarrollo

### 1. La fórmula de la cuota (sistema francés)

```text
        i (1+i)^n              i
A = P ------------- = P ----------------
       (1+i)^n − 1        1 − (1+i)^-n
```

Donde `P` es el capital, `i` la tasa **periódica** (mensual si las cuotas son mensuales) y `n` el
número de cuotas.

Crédito de 5 000 000, tasa 1,45 % mensual, 36 cuotas:

```text
(1,0145)^36 = 1,675737
A = 5 000 000 × 0,0145 × 1,675737 / (1,675737 − 1)
A = 5 000 000 × 0,024298 / 0,675737 = 121 490 / 0,675737 = 179 787
```

**Cuota: 179 787 pesos.** Total pagado: `179 787 × 36 = 6 472 332`, de los cuales 1 472 332 son
intereses (29,4 % del capital).

### 2. La tabla de desarrollo

| Cuota | Saldo inicial | Cuota | Interés | Amortización | Saldo final |
|---:|---:|---:|---:|---:|---:|
| 1 | 5 000 000 | 179 787 | 72 500 | 107 287 | 4 892 713 |
| 2 | 4 892 713 | 179 787 | 70 944 | 108 843 | 4 783 870 |
| 3 | 4 783 870 | 179 787 | 69 366 | 110 421 | 4 673 449 |
| 12 | 3 733 566 | 179 787 | 54 137 | 125 650 | 3 607 916 |
| 24 | 2 176 471 | 179 787 | 31 559 | 148 228 | 2 028 243 |
| 35 | 356 496 | 179 787 | 5 169 | 174 618 | 181 878 |
| 36 | 181 878 | 179 815 | 2 637 | 177 178 | 0 |

Observaciones que hay que saber leer:

- En la cuota 1, el **60 %** de lo pagado es interés. En la cuota 36, el **1,5 %**.
- Tras 12 cuotas (un tercio del plazo) el saldo bajó solo un **27,8 %**.
- La última cuota difiere en 28 pesos: es la **cuota de ajuste** de la clase 2. Debe estar declarada.

### 3. Punto de equilibrio de la cuota

El momento en que la amortización supera al interés:

```text
se cumple cuando  saldo × i < A/2
```

En este crédito ocurre ya en la cuota 1 (107 287 > 72 500), porque el plazo es corto. En un
hipotecario a 240 meses al 0,45 % mensual, la amortización recién supera al interés cerca de la
**cuota 96**: durante ocho años, más de la mitad de cada cuota es interés puro.

### 4. Prepago: por qué el momento lo es todo

Un prepago a capital de 500 000 en el crédito del ejemplo:

| Prepago en la cuota | Intereses ahorrados | Cuotas que se evitan (manteniendo cuota) |
|---:|---:|---:|
| 1 | 172 850 | 3,7 |
| 12 | 108 240 | 3,3 |
| 24 | 45 190 | 2,9 |
| 30 | 21 630 | 2,8 |

El mismo dinero ahorra **cuatro veces más** en la cuota 1 que en la cuota 30. Motivo: el prepago
evita todos los intereses futuros sobre ese capital, y quedan más periodos por delante. Regla
práctica: **prepagar sirve mucho al principio y poco al final**.

Existen dos modalidades y hay que elegir explícitamente:

| Modalidad | Qué hace | Cuándo conviene |
|---|---|---|
| Reducción de plazo | Mantiene la cuota, acorta el crédito | Maximiza el ahorro de intereses |
| Reducción de cuota | Mantiene el plazo, baja la cuota | Alivia el flujo mensual; ahorra menos |

### 5. Auditar una tabla ajena

Cinco controles que detectan casi cualquier error o abuso:

```text
1. saldo final de cada fila = saldo inicial − amortización
2. interés de cada fila = saldo inicial × tasa periódica declarada
3. cuota = interés + amortización     (en todas las filas)
4. Σ amortizaciones = capital original
5. saldo tras la última cuota = 0 (±0,01)
```

Si el control 2 falla de manera sistemática, la tasa aplicada no es la declarada. Si el control 4
falla, hay cargos incorporados al capital que no se informaron. Ambos hallazgos son materia de la
Parte 4, clase 8, sobre lectura de contratos.

## 🧮 Ejemplo guiado

**Situación.** Un banco ofrece a Rocío 3 200 000 en 24 cuotas de 158 900 y declara "tasa 1,25 %
mensual". Rocío quiere verificar si la cuota corresponde a esa tasa.

**Paso 1 — calcula la cuota teórica al 1,25 %.**

```text
(1,0125)^24 = 1,347351
A = 3 200 000 × 0,0125 × 1,347351 / 0,347351
A = 3 200 000 × 0,016842 / 0,347351 = 53 894 / 0,347351 = 155 158
```

**Paso 2 — compara.**

```text
cuota ofrecida  158 900
cuota teórica   155 158
diferencia        3 742 por cuota → 89 808 en total
```

**Paso 3 — encuentra la tasa implícita.** Se busca `i` tal que la cuota sea 158 900. Por tanteo:

| i mensual | Cuota resultante |
|---:|---:|
| 1,25 % | 155 158 |
| 1,45 % | 157 987 |
| 1,52 % | 158 984 |
| **1,515 %** | **158 913** |

La tasa efectivamente aplicada es ≈ **1,515 % mensual**, no 1,25 %.

**Paso 4 — investiga la brecha.** Al revisar el contrato aparecen: comisión de apertura de 45 000 y
seguro de desgravamen de 42 000, ambos financiados dentro del crédito. Entonces:

```text
capital real financiado = 3 200 000 + 45 000 + 42 000 = 3 287 000
cuota al 1,25 % sobre 3 287 000 = 159 377
```

Muy cerca de 158 900. **La tasa declarada era correcta; lo que no se explicó fue que la base incluía
cargos.** Rocío recibe 3 200 000 y paga intereses sobre 3 287 000.

**Paso 5 — el número que importa.** El costo total anual equivalente considera lo recibido, no lo
firmado:

```text
tasa que iguala 3 200 000 con 24 cuotas de 158 900 ≈ 1,515 % mensual
equivalente anual: (1,01515)^12 − 1 = 19,80 %
```

**Ese 19,80 %** es el número comparable entre ofertas, y es justamente lo que la Parte 3, clase 13,
formaliza como carga anual equivalente.

## 🏦 Del cliente al banco

| Elemento | Cliente | Banco |
|---|---|---|
| Tabla de desarrollo | Papel que se archiva | Documento contractual, base contable y de auditoría |
| Interés de la primera cuota | "Casi no bajó la deuda" | Devengo sobre saldo máximo; ingreso reconocido en el periodo |
| Prepago | "Quiero pagar antes" | Reduce ingreso futuro; sujeto a comisión de prepago regulada |
| Cuota de ajuste | 28 pesos de diferencia | Política de redondeo declarada y auditada |

## 🧪 Práctica

En `labs/lab-06.md`:

1. Construye la tabla de desarrollo completa de un crédito propio o sintético en planilla o Python.
2. Aplica los cinco controles de auditoría y documenta el resultado de cada uno.
3. Simula un prepago en tres momentos distintos y compara el ahorro.
4. Compara las modalidades reducción de plazo y reducción de cuota sobre el mismo prepago.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El saldo final no llega a cero | Se redondeó cada fila | Usa precisión completa y ajusta solo la última cuota. |
| El interés se calculó sobre el saldo después de amortizar | Orden invertido | Interés primero, sobre el saldo **inicial** del periodo. |
| La cuota no coincide con la tasa declarada | Cargos financiados dentro del capital | Recalcula la tasa implícita sobre el monto **recibido**. |
| Se usó tasa anual con cuotas mensuales | Unidades incompatibles | Convierte a tasa periódica antes de aplicar la fórmula. |
| El prepago no reduce lo esperado | Se aplicó a cuotas futuras y no a capital | Exige por escrito que el prepago se impute a capital. |
| Se cree que la mitad del plazo baja la mitad de la deuda | Composición de la cuota mal entendida | Revisa la tabla: en la mitad del plazo el saldo suele superar el 55 %. |

## ❓ Preguntas de comprobación

1. Calcula la cuota de 2 000 000 a 18 meses con tasa de 1,3 % mensual.
2. ¿Por qué en la primera cuota la amortización es la parte menor?
3. ¿Qué cinco controles aplicarías para auditar una tabla de desarrollo ajena?
4. ¿Por qué el mismo prepago ahorra más en la cuota 3 que en la cuota 30?
5. Un crédito declara 1,2 % mensual pero la cuota implica 1,5 %. ¿Qué hipótesis investigas primero?

## 📥 Entregable

Guarda en `portfolio/parte-01/clase-11/`:

- la tabla de desarrollo completa con los cinco controles documentados;
- la comparación de prepagos en tres momentos;
- la comparación entre reducción de plazo y reducción de cuota;
- una auditoría de una oferta real o sintética con la tasa implícita calculada.

<!-- gen:etica:start -->
## 🔐 Seguridad, ética y límites

Trabaja siempre con datos sintéticos o propios: nunca uses datos reales de terceros,
números de cuenta, documentos de identidad ni antecedentes crediticios ajenos. Este
material es formativo y **no constituye asesoría financiera, tributaria ni legal**; las
tasas, comisiones, límites y normas citados cambian y deben verificarse en la fuente
oficial vigente del país donde se aplique. Cuando un cálculo alimente una decisión que
afecte a otra persona, registra los supuestos y quién los aprobó.
<!-- gen:etica:end -->

## 📗 Fuentes y verificación

- Kellison, S. (2008). *The Theory of Interest* (3.ª ed.). McGraw-Hill/Irwin. Capítulo 6: amortización y construcción de tablas.
- Broverman, S. (2017). *Mathematics of Investment and Credit* (7.ª ed.). ACTEX. Capítulo 3: sistema francés, prepagos y saldo insoluto.
- Ross, S., Westerfield, R. y Jordan, B. (2022). *Fundamentos de finanzas corporativas* (12.ª ed.). McGraw-Hill. Capítulo 6: préstamos amortizables.
- IFRS Foundation (2014). *NIIF 9 Instrumentos Financieros*. Método del interés efectivo aplicado a préstamos con comisiones incorporadas.
- World Bank (2017). *Good Practices for Financial Consumer Protection*. Banco Mundial. Estándares sobre entrega y contenido de la tabla de desarrollo.
- Verificación local: revisa si tu legislación obliga a entregar la tabla de desarrollo antes de firmar y qué comisión máxima de prepago permite.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 10 · Valor futuro](10-valor-futuro.md) | [Parte 01](../README.md) · [Programa](../../../SYLLABUS.md) | [12 · Amortización básica →](12-amortizacion-basica.md) |
<!-- gen:footer:end -->
