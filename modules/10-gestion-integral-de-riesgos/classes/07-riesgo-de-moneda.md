---
part: 11
class: 7
title: "Riesgo de moneda"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 07 · Riesgo de moneda

> [← 06 · Riesgo de mercado y valor en riesgo](06-riesgo-de-mercado-y-valor-en-riesgo.md) · [Índice de la parte](../README.md) · [08 · Riesgo país y de contraparte →](08-riesgo-pais-y-de-contraparte.md)

**Parte 11 — Gestión integral de riesgos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Medir y gestionar la exposición de un banco a los movimientos del tipo de cambio, incluyendo la forma
más dañina y menos evidente: **el riesgo de crédito inducido por el tipo de cambio**, cuando el banco
está calzado en su balance y sus deudores no lo están.

## 📚 Objetivos

Al finalizar podrás:

1. **Calcular** la posición neta por moneda y la posición global.
2. **Distinguir** exposición de transacción, de traslación y económica.
3. **Identificar** el riesgo de crédito inducido por el tipo de cambio.
4. **Aplicar** instrumentos de cobertura y evaluar su costo.
5. **Evaluar** la dolarización de una economía como factor de riesgo sistémico.

<!-- gen:agenda:start -->
## Agenda de 90 minutos

| Minutos | Bloque | Qué ocurre |
|---:|---|---|
| 0–10 | Activación | Pregunta diagnóstica y recuperación de la clase anterior. |
| 10–35 | Conceptos | Desarrollo guiado con la fuente oficial a la vista. |
| 35–55 | Ejemplo guiado | El docente resuelve el caso numérico paso a paso. |
| 55–80 | Práctica | El estudiante replica con datos propios o sintéticos. |
| 80–90 | Cierre | Preguntas de comprobación y registro en el portafolio. |
<!-- gen:agenda:end -->

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| `posición neta` | Activos menos pasivos en una moneda, incluidas las posiciones fuera de balance. |
| `posición larga` | Activos > pasivos. Gana si la moneda extranjera se aprecia. |
| `posición corta` | Pasivos > activos. Gana si la moneda extranjera se deprecia. |
| `exposición de transacción` | Flujos comprometidos en moneda extranjera. |
| `exposición de traslación` | Efecto contable de convertir estados financieros. |
| `exposición económica` | Efecto del tipo de cambio sobre el valor del negocio. |
| `riesgo de crédito inducido` | El deudor incumple porque el tipo de cambio lo dañó. |
| `descalce del deudor` | Ingresos en una moneda, deuda en otra. |

## 🧠 Modelo mental

```text
UN BANCO PUEDE ESTAR PERFECTAMENTE CALZADO
Y AUN ASÍ QUEBRAR POR EL TIPO DE CAMBIO

  activos en moneda extranjera:  créditos a empresas locales
  pasivos en moneda extranjera:  depósitos en esa moneda
  posición neta: CERO ✓

  la moneda local se deprecia 40 %
  las empresas deudoras tienen ingresos en moneda local
  su deuda sube 40 % medida en sus ingresos
  no pueden pagar

  el banco no tenía riesgo de MERCADO
  tenía riesgo de CRÉDITO disfrazado de calce
```

**Esta es la lección central de la clase** y la que explica la mayor parte de las crisis bancarias en
economías emergentes documentadas por el FMI y el BIS.

## 📖 Desarrollo

### 1. Posición por moneda

```text
POSICIÓN NETA EN LA MONEDA X =
  activos en X
  − pasivos en X
  + compras a término en X
  − ventas a término en X
  + delta de opciones en X
```

```text
POSICIÓN GLOBAL — dos criterios de agregación

AGREGACIÓN NETA        suma algebraica de todas las posiciones
                       supone compensación perfecta entre monedas

AGREGACIÓN BRUTA       mayor entre la suma de las largas
(criterio supervisor)  y la suma de las cortas, en valor absoluto
                       no supone compensación
```

| Moneda | Posición neta | Larga | Corta |
|---|---:|---:|---:|
| Dólar | +14 200 | 14 200 | |
| Euro | −8 600 | | 8 600 |
| Real | +3 400 | 3 400 | |
| Yen | −1 100 | | 1 100 |
| **Suma** | **+7 900** | **17 600** | **9 700** |

```text
posición global neta:   7 900
posición global bruta: 17 600  (el mayor entre largas y cortas)

el límite supervisor se aplica sobre la BRUTA
porque euro y dólar no se compensan entre sí en una crisis
```

### 2. Tres exposiciones

| Exposición | Horizonte | Se cubre con | Se ve en |
|---|---|---|---|
| Transacción | Corto, flujos ciertos | Forward, swap | Resultado |
| Traslación | Cierre contable | Cobertura de inversión neta | Patrimonio (otro resultado integral) |
| Económica | Largo, competitividad | Diversificación operativa | Ninguna cuenta, hasta que se materializa |

**La exposición económica es la que no se puede cubrir con derivados** y la que decide la viabilidad de
un negocio. Un banco cuyo país se aprecia sostenidamente pierde clientes exportadores aunque su balance
esté calzado.

### 3. Riesgo de crédito inducido

```text
CÓMO SE MIDE
  1. identifica los deudores con deuda en moneda extranjera
  2. clasifícalos por origen de ingresos:
       exportadores            → calce natural
       ingresos indexados      → calce parcial
       ingresos locales        → DESCALZADOS
  3. estima la PD de cada grupo bajo depreciación
  4. recalcula la pérdida esperada de la cartera
```

```text
EFECTO TÍPICO DE UNA DEPRECIACIÓN DEL 30 %
  sobre deudores descalzados con deuda en moneda extranjera:

  carga financiera / ingreso pasa de 28 % a 36 %
  PD estimada pasa de 2,1 % a 6,8 %    (× 3,2)

  y la LGD también empeora:
  la garantía está valorada en moneda local
```

**Doble efecto.** La depreciación aumenta la probabilidad de incumplimiento **y** reduce el valor
relativo de la garantía. Ambos factores se multiplican en la pérdida esperada.

### 4. Cobertura y su costo

| Instrumento | Qué hace | Costo |
|---|---|---|
| Forward | Fija el tipo de cambio de una fecha futura | Diferencial de tasas entre monedas |
| Swap de monedas | Intercambia flujos de principal e interés | Diferencial + prima de base |
| Opción | Derecho a cambiar a un tipo dado | Prima |
| Calce natural | Financiar activos en X con pasivos en X | Costo de oportunidad |
| Cláusula contractual | Trasladar el riesgo al cliente | Se convierte en riesgo de crédito |

```text
LA PARIDAD DE TASAS DE INTERÉS determina el precio del forward

  F = S × (1 + i_local) / (1 + i_extranjera)

  el forward NO predice el tipo de cambio futuro:
  refleja el diferencial de tasas
  cubrirse "cuesta" el diferencial, no el movimiento esperado
```

**La última fila de la tabla merece atención:** trasladar el riesgo cambiario al cliente por contrato no
elimina el riesgo, lo **transforma** en riesgo de crédito. Si el cliente no puede absorberlo, el banco
vuelve a tenerlo, ahora en forma de incumplimiento y con menos instrumentos para gestionarlo.

### 5. Dolarización y riesgo sistémico

```text
ECONOMÍA PARCIALMENTE DOLARIZADA
  · los depositantes ahorran en moneda extranjera (protección)
  · los bancos deben prestar en esa moneda (para calzar)
  · los deudores mayoritariamente tienen ingresos locales
  → el sistema entero acumula descalce en sus DEUDORES

  el banco central pierde parte de su capacidad
  de prestamista de última instancia:
  no puede emitir la moneda en que están denominados los pasivos
```

Las respuestas de política documentadas incluyen: requerimientos de encaje diferenciados por moneda,
límites de posición más estrictos, exigencia de calce del deudor, mayores ponderaciones de riesgo para
créditos en moneda extranjera a deudores no generadores, y reservas internacionales adecuadas.

## 🧮 Ejemplo guiado

**Situación.** Un banco en una economía parcialmente dolarizada evalúa su exposición real.

```text
BALANCE EN MONEDA EXTRANJERA (equivalente en moneda local)
  ACTIVOS
    créditos comerciales en ME        286 000
    créditos hipotecarios en ME        94 000
    inversiones en ME                  62 000
    disponible en ME                   38 000
    TOTAL                             480 000

  PASIVOS
    depósitos en ME                   412 000
    obligaciones con bancos del exterior 54 000
    TOTAL                             466 000

  FUERA DE BALANCE
    ventas a término netas             10 000

  patrimonio efectivo                 420 000
```

**Paso 1 — calcula la posición neta.**

```text
posición = 480 000 − 466 000 − 10 000 = +4 000

posición / patrimonio efectivo = 4 000 / 420 000 = 0,95 %
límite supervisor habitual: 10–20 %  ✓ cumple con holgura

CONCLUSIÓN APARENTE: riesgo de moneda prácticamente nulo
```

**Paso 2 — clasifica a los deudores en moneda extranjera por origen de ingresos.**

```text
créditos comerciales en ME: 286 000
  exportadores (ingresos en ME)           98 000   34 %
  importadores (costos en ME, precio local) 74 000   26 %
  servicios locales (ingresos locales)     114 000   40 %

créditos hipotecarios en ME: 94 000
  personas con ingreso en ME                8 000    9 %
  personas con ingreso local               86 000   91 %

TOTAL DESCALZADO: 114 000 + 86 000 = 200 000
más los importadores, parcialmente:          74 000
```

**Paso 3 — mide la sensibilidad de los deudores descalzados.**

```text
DEPRECIACIÓN SUPUESTA: 30 %

hipotecarios con ingreso local (86 000):
  carga financiera / ingreso: 31 % → 40,3 %
  umbral de estrés del segmento: 38 %
  → 71 % de la subcartera supera el umbral

servicios locales (114 000):
  cobertura de servicio de deuda: 1,42 → 1,09
  umbral de covenant: 1,20
  → incumplimiento de covenant en el 63 % de los deudores
```

**Paso 4 — recalcula la pérdida esperada.**

```text
                       PD base   PD estresada   EAD      LGD    PE
exportadores            1,4 %      1,6 %       98 000   38 %    596
importadores            2,2 %      4,1 %       74 000   42 %  1 274
servicios locales       2,6 %      8,4 %      114 000   45 %  4 309
hipotecarios ME local   1,1 %      5,2 %       86 000   28 %  1 252
hipotecarios ME en ME   0,9 %      1,0 %        8 000   25 %     20
                                                       TOTAL  7 451

pérdida esperada en escenario base:
  (1,4×98+2,2×74+2,6×114+1,1×86+0,9×8)/100 × LGD medias ≈ 2 384

INCREMENTO POR LA DEPRECIACIÓN: 7 451 − 2 384 = 5 067
```

**Paso 5 — compara con la exposición de mercado.**

```text
RIESGO DE MERCADO (posición neta)
  4 000 × 30 % = 1 200 de efecto directo

RIESGO DE CRÉDITO INDUCIDO
  5 067 de pérdida esperada adicional

el riesgo de crédito inducido es 4,2 VECES el de mercado
y no aparece en ninguna medición de posición cambiaria
```

**Paso 6 — añade el efecto sobre la garantía.**

```text
hipotecarios en ME con garantía valorada en moneda local:
  saldo 86 000, valor de garantía 143 000 → relación 60 %

tras la depreciación, medida en ME:
  la garantía vale 143 000 / 1,30 = 110 000 en términos de la deuda
  relación préstamo/garantía: 86 000 / 110 000 = 78 %

  LGD recalculada: 28 % → 39 %
  pérdida esperada del segmento: 5,2 % × 86 000 × 39 % = 1 744
  (en vez de 1 252)

INCREMENTO ADICIONAL: 492
PÉRDIDA ESPERADA TOTAL EN ESCENARIO: 7 943
```

**Paso 7 — decisiones.**

```text
1. MEDICIÓN
   incorporar el riesgo de crédito inducido al marco de riesgo de moneda
   reportar posición neta Y exposición de deudores descalzados

2. ORIGINACIÓN
   suspender créditos hipotecarios en moneda extranjera
   a personas con ingreso local
   exigir calce de ingresos para nuevo crédito comercial en ME
   o aplicar una prueba de estrés cambiario en la admisión

3. CARTERA EXISTENTE
   ofrecer conversión voluntaria a moneda local a los 86 000
   de hipotecarios descalzados, con evaluación de capacidad de pago
   a la tasa local

4. CAPITAL
   reconocer en el Pilar 2 el riesgo de crédito inducido:
   5 559 de pérdida esperada adicional en el escenario

5. PRECIO
   los créditos en ME a deudores descalzados deben incluir
   la prima de riesgo cambiario en su tasa: no hacerlo
   equivale a subsidiarlos con el capital del banco
```

**Interpreta:** el banco cumplía su límite de posición con una holgura de veinte veces y **tenía cuatro
veces más riesgo cambiario del que medía**, porque estaba en el activo crediticio y no en la posición.
El indicador regulatorio de posición no es incorrecto: es **incompleto** para una economía dolarizada, y
esa es la razón por la que los supervisores de estas economías exigen medidas adicionales.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Me ofrecieron crédito en dólares con tasa menor» | Riesgo trasladado al cliente | 11, clase 7 |
| «Mi deuda subió 40 % sin que yo hiciera nada» | Descalce del deudor | 4, clase 7 |
| «Ahorro en dólares para protegerme» | Origen de la dolarización de pasivos | 2, clase 12 |
| «El banco me pide cubrirme» | Riesgo de crédito inducido reconocido | 13, clase 9 |
| «El banco central no pudo ayudar» | Límite del prestamista de última instancia | 6, clase 10 |

## 🧪 Práctica

En `labs/lab-04.md`:

1. Calcula la posición por moneda y la posición global neta y bruta.
2. Clasifica una cartera en moneda extranjera por origen de ingresos del deudor.
3. Recalcula la pérdida esperada bajo una depreciación del 30 %, con efecto en PD y LGD.
4. Compara el costo de cubrirse con forwards contra el costo del riesgo asumido.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Posición calzada y pérdidas por tipo de cambio | Riesgo de crédito inducido | Mide el descalce de los deudores. |
| Se agregan monedas netamente | Compensación supuesta | Usa la agregación bruta. |
| El riesgo se traslada por contrato al cliente | Se convierte en crédito | Evalúa la capacidad de absorción del cliente. |
| Se ignora el efecto sobre la garantía | Solo se mira la PD | La LGD también empeora. |
| El forward se ve como predicción | Confusión conceptual | Refleja el diferencial de tasas. |
| La exposición económica no se gestiona | No es cubrible con derivados | Diversificación operativa. |

## ❓ Preguntas de comprobación

1. ¿Cómo puede un banco perfectamente calzado quebrar por el tipo de cambio?
2. ¿Por qué el límite supervisor se aplica sobre la posición bruta y no la neta?
3. ¿Por qué una depreciación afecta a la vez la PD y la LGD de un deudor descalzado?
4. ¿Qué determina el precio de un forward de moneda?
5. ¿Por qué la dolarización limita al prestamista de última instancia?

## 📥 Entregable

Guarda en `portfolio/parte-11/clase-07/`:

- la posición por moneda con agregación neta y bruta;
- la clasificación de deudores por origen de ingresos;
- la pérdida esperada estresada con efecto en PD y en LGD;
- la comparación entre el costo de cobertura y el riesgo asumido.

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

- Basel Committee on Banking Supervision (2019). *Minimum capital requirements for market risk*, sección de riesgo de moneda. BIS.
- International Monetary Fund (2020). *Managing Foreign Exchange Risk in Emerging Markets*. IMF Working Papers.
- Bank for International Settlements (2020). *US dollar funding: an international perspective*. CGFS Papers 65. <https://www.bis.org/publ/cgfs65.htm>
- Ranciere, R., Tornell, A. y Vamvakidis, A. (2010). "Currency mismatch, systemic risk and growth in emerging Europe". *Economic Policy*, 25(64).
- Krugman, P., Obstfeld, M. y Melitz, M. (2018). *International Economics* (11.ª ed.). Pearson. Paridad de tasas de interés.
- Verificación local: revisa los límites de posición en moneda extranjera, los encajes diferenciados y las exigencias sobre crédito en moneda extranjera a no generadores en tu país.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 06 · Riesgo de mercado y valor en riesgo](06-riesgo-de-mercado-y-valor-en-riesgo.md) | [Parte 11](../README.md) · [Programa](../../../SYLLABUS.md) | [08 · Riesgo país y de contraparte →](08-riesgo-pais-y-de-contraparte.md) |
<!-- gen:footer:end -->
