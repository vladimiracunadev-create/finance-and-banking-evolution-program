# Ejercicios y evaluación: Ueno Bank Paraguay

Material práctico del caso
[«Ueno Bank Paraguay: aprender sobre solvencia, riesgos, gobierno corporativo y
resolución bancaria»](../case-studies/bank-resolution/ueno-bank-paraguay.md).
Reúne dos ejemplos guiados, doce ejercicios con solución (cuatro básicos, cuatro
intermedios, cuatro avanzados), cinco preguntas abiertas, una actividad integradora
de comité de riesgos y la rúbrica de evaluación. Se puede hacer **sin programar**:
con lectura, calculadora y una hoja de trabajo. Las clases que lo usan están en la
[matriz e itinerario](ueno-bank-matriz-e-itinerario.md).

## Cómo leer este documento

Cada ejercicio sigue el mismo orden: **qué se pregunta → fórmula con variables y
unidades → datos → cálculo paso a paso → interpretación → límite**. Antes de cada
bloque de cálculo hay un párrafo que dice por qué aparece y cómo leerlo; después,
otro que extrae la consecuencia.

> 🔎 **Dos tipos de dato, nunca mezclados.** Las cifras marcadas **[H]**
> (histórico) provienen de comunicados o de prensa atribuida y figuran en el
> expediente del caso. Todo lo demás —los bancos *Yvyra* y *Tajy*, sus balances y
> sus depositantes— es **[S] sintético**: inventado para calcular y sin relación con
> ninguna entidad ni persona reales. Las unidades monetarias sintéticas son
> «millones de unidades monetarias» (**m.u.**); las cifras históricas están en
> guaraníes (**Gs**) salvo indicación.

Las fórmulas se usan con estos símbolos:

| Símbolo | Significado | Unidad |
|---|---|---|
| `E` | efectivo y equivalentes inmediatos | m.u. |
| `D` | depósitos del público | m.u. |
| `A` | activos totales | m.u. |
| `P` | patrimonio contable (`A − pasivos`) | m.u. |
| `K` | capital regulatorio (aquí: `P − intangibles`) | m.u. |
| `APR` | activos ponderados por riesgo | m.u. |
| `r = K / APR` | índice de solvencia | % |
| `r_min` | mínimo exigido (12 % en los ejercicios) | % |
| `G` | tope de la garantía por depositante y entidad | Gs |

El **supuesto** `K = P − intangibles` y el mínimo de 12 % son simplificaciones del
ejercicio. La definición real de capital regulatorio y su mínimo se verifican en la
norma del país (véase la clase 6 de la Parte 12).

---

## Parte A · Dos ejemplos guiados

### Ejemplo guiado 1 (introductorio): Marta quiere sus ahorros

**Situación.** Marta tiene ahorros en el *Banco Yvyra* **[S]** y quiere retirarlos.
Para entender si su dinero está en riesgo hay que distinguir dos preguntas que en
la calle se confunden: *¿el banco tiene dinero en la caja hoy?* y *¿el banco vale más
de lo que debe?* La primera es **liquidez**; la segunda, **solvencia**.

**Definiciones.** *Liquidez*: capacidad de pagar lo que se pide *hoy*, con efectivo
o activos que se convierten en efectivo sin pérdida. *Solvencia*: que los activos
valgan más que los pasivos, es decir, que el **patrimonio** (`P = A − pasivos`) sea
positivo. *Rentabilidad*: cuánto gana el banco; es una tercera cosa y no protege
por sí sola de las otras dos.

El balance se lee como una balanza: lo que el banco tiene a la izquierda, lo que
debe y lo que es de sus dueños a la derecha.

```text
BANCO YVYRA, versión mínima [S]     (m.u.)
  ACTIVOS                         PASIVOS Y PATRIMONIO
    efectivo            100         depósitos del público   940
    préstamos           900         patrimonio P             60
    TOTAL A           1 000         TOTAL                  1 000
```

**Paso 1: un día de retiros (problema de liquidez).** Suponga que los clientes
quieren retirar **150** pero hay **100** en caja.

```text
paga 100:  efectivo 100 → 0        depósitos 940 → 840
           préstamos 900            patrimonio P = 900 − 840 = 60   (sin cambio)
no puede pagar los otros 50 hoy aunque P > 0
```

El patrimonio *no* cambió: pagar un retiro reduce a la vez el efectivo y el
depósito, y la diferencia entre activos y pasivos se mantiene. El banco está
**solvente pero iliquido**: el problema es el calendario, no el valor.

**Paso 2: una pérdida de cartera (problema de solvencia).** Ahora suponga que se
reconoce que **70** de los préstamos no se cobrarán.

```text
préstamos 900 → 830     A = 100 + 830 = 930
pasivos (depósitos)  940
P = 930 − 940 = −10     ← patrimonio negativo
efectivo en caja sigue en 100: hoy aún puede pagar retiros hasta 100
```

El banco puede *pagar* hoy y, aun así, **valer menos de lo que debe**. Es iliquidez
la que se ve primero en la calle, pero es la insolvencia la que no se arregla con
más efectivo prestado.

**Interpreta.** Un retiro mueve el efectivo y los depósitos; una pérdida mueve el
patrimonio. Con solo mirar la caja no se sabe si el banco es solvente, y con solo
mirar el patrimonio no se sabe si podrá pagar el lunes. Marta, como depositante,
está cubierta por la garantía hasta un límite (véase el ejercicio B3), pero eso no
cambia el diagnóstico del banco. **Límite:** el balance mínimo omite capital
regulatorio, plazos y valor razonable.

### Ejemplo guiado 2 (profesional): de la carpeta de crédito al índice de solvencia

**Situación.** El comité de riesgos del *Banco Yvyra* **[S]** debe medir qué ocurre
con el índice de solvencia si la revisión de carpetas obliga a provisionar 60.
Este es el mecanismo que el expediente documenta como «previsiones adicionales»,
sin cifras **[H]**; aquí se calcula con números sintéticos.

**Fórmula y variables.** `r = K / APR`, con `K = P − intangibles`. Una provisión es
un gasto que **reduce la cartera neta y el patrimonio** en la misma cantidad.

```text
BALANCE INICIAL DEL BANCO YVYRA [S]                      (m.u.)
  efectivo                         120     depósitos                1 200
  inversiones                      180     otras deudas                60
  cartera bruta                  1 000     TOTAL PASIVOS            1 260
  (−) provisiones                  (40)    patrimonio P               140
  intangibles (software)            40
  otros activos                    100
  TOTAL ACTIVOS                  1 400     TOTAL                    1 400
  APR (supuesto)                   700     mínimo r_min              12 %
```

El balance se lee de arriba abajo: los activos suman 1 400 y los pasivos más el
patrimonio también, por lo que cuadra. Obsérvese que el **intangible de 40** forma
parte del patrimonio contable pero, en el supuesto del ejercicio, no cuenta como
capital regulatorio.

**Paso 1: situación inicial.**

```text
K = P − intangibles = 140 − 40 = 100
r = 100 / 700 = 14,29 %        ≥ 12 %: cumple
margen sobre el mínimo = 14,29 % − 12 % = 2,29 puntos porcentuales
```

**Paso 2: se reconoce una provisión adicional de 60.**

```text
provisiones 40 → 100        cartera neta 960 → 900
P = 140 − 60 = 80           (sin efecto fiscal, supuesto)
K = 80 − 40 = 40
r = 40 / 700 = 5,71 %       (con APR constante: supuesto conservador)
```

**Paso 3: compararlo con el mínimo, de tres maneras que no son iguales.**

```text
en puntos porcentuales:   12 − 5,71   = 6,29 pp por debajo del mínimo
como fracción del mínimo: 5,71 / 12   = 47,6 % del mínimo
umbral del 50 % del mínimo: 0,50 × 12 = 6,00 %  → 5,71 % < 6,00 % ✓
```

Este es el paso donde se equivoca la lectura apresurada. «Por debajo del 50 % del
mínimo» significa **por debajo de 6,00 %**, que es la mitad de 12 %. No significa
50 % del banco, 50 % de los depósitos ni «50 puntos» de nada.

**Paso 4: ¿cuánto capital falta?**

```text
K necesario para r = 12 %:   0,12 × 700 = 84      falta 84 − 40 = 44
K necesario para r = 6 %:    0,06 × 700 = 42      falta 42 − 40 = 2
```

**Paso 5: capitalización anunciada frente a integrada.** El grupo controlador
anuncia **100** en dos tramos de **50**. Solo el primero se ha pagado y registrado.

```text
anunciada, no integrada:          K = 40            r = 5,71 %
primer tramo integrado (50):      K = 90            r = 90/700 = 12,86 % ≥ 12 % ✓
ambos tramos (100):               K = 140           r = 20,00 %
```

**Interpreta.** Con estos datos, 60 de provisión sobre una cartera bruta de 1 000
(6 %) bastan para llevar el índice de 14,29 % a 5,71 %: **el apalancamiento
convierte una pérdida moderada en una caída grande del índice**, porque el capital
regulatorio es solo el 7,1 % de los activos. Y solo el capital **integrado** cambia
el índice: el anuncio, no. **Límites:** (a) se supuso `APR` constante; en el
ejercicio A2 se comprueba que esa elección puede cambiar el resultado; (b) no se
modelaron efectos fiscales ni la distribución del capital en tramos de calidad.

---

## Parte B · Doce ejercicios

### Ejercicios básicos

#### B1 · Retiro frente a pérdida

**Pregunta.** Con el balance inicial del ejemplo 2, calcula cuánto cambian
la liquidez (`E / D`) y la solvencia contable (`P / A`) en dos eventos separados:
(a) los clientes retiran 100; (b) se reconoce una pérdida de 60.

**Cálculo.**

```text
inicial:   E/D = 120/1200 = 10,00 %      P/A = 140/1400 = 10,00 %

(a) retiro de 100:   E = 20   D = 1100   A = 1300   P = 140
    E/D = 20/1100 = 1,82 %               P/A = 140/1300 = 10,77 %

(b) pérdida de 60:   E = 120  D = 1200   A = 1340   P = 80
    E/D = 120/1200 = 10,00 %             P/A = 80/1340 = 5,97 %
```

**Interpretación.** El evento (a) hunde la liquidez y *mejora* levemente
`P / A` (porque `A` baja y `P` no); el evento (b) deja intacta la liquidez y casi
parte por la mitad la solvencia contable. Son problemas distintos con remedios
distintos: al primero lo ataja efectivo (prestado, de tesorería); al segundo, solo
capital. **Respuesta orientativa de error típico:** decir que «el retiro redujo el
patrimonio». **Límite:** `P / A` es una medida contable simple; el índice regulatorio
se calcula sobre `APR`.

#### B2 · Qué quiere decir «por debajo del 50 % del mínimo»

**Pregunta.** La prensa atribuye al índice un valor de **5,56 %** frente a un mínimo
del **12 %** **[H, prensa: La Nación AR]**. Calcula (a) el índice como fracción del
mínimo; (b) la distancia al mínimo en puntos porcentuales; (c) si es coherente con
el comunicado «por debajo del 50 % del mínimo requerido» **[H, BCP]**; (d) qué
leería mal alguien que entendiera «50 %» como «50 % de los depósitos».

**Cálculo.**

```text
(a) 5,56 / 12      = 0,4633 = 46,3 % del mínimo
(b) 12 − 5,56      = 6,44 puntos porcentuales por debajo
(c) 50 % del mínimo = 0,5 × 12 = 6,00 %;  5,56 % < 6,00 %  → coherente
    (la coherencia no prueba que 5,56 % sea el dato oficial)
(d) los depósitos no intervienen en el índice: el denominador son los
    activos ponderados por riesgo, no los depósitos
```

**Interpretación.** Tres lecturas, tres números distintos: 46,3 % (relativo),
6,44 pp (absoluto) y 6,00 % (umbral). Mezclarlos es el error más común al leer un
comunicado. **Límite:** el 5,56 % es una cifra de prensa; el ejercicio comprueba
coherencia, no veracidad.

#### B3 · La garantía es por depositante y por entidad, no por cuenta

**Pregunta.** Con `G = 228,3` millones de Gs **[H]**, calcula lo cubierto y lo no
cubierto de: Ana, una cuenta de 150; Beto, dos cuentas (250 y 150) en la misma
entidad; Carla, 100 en la entidad en resolución y 100 en otro banco **[S]**.

**Cálculo.** `cubierto = mín(saldo total en la entidad, G)`.

```text
Ana:   saldo 150           cubierto 150,0       no cubierto 0
Beto:  saldo 250 + 150 = 400   cubierto 228,3   no cubierto 171,7   (57,1 % cubierto)
Carla: saldo 100 en la entidad cubierto 100,0   no cubierto 0
       (los 100 del otro banco no se suman: la garantía es por entidad)
```

**Interpretación.** Las dos cuentas de Beto se suman antes de aplicar el tope:
tener varias cuentas en la misma entidad **no multiplica** la garantía. Carla sí
tiene dos coberturas independientes porque son dos entidades. **Límite:**
el ejercicio ignora deudas vencidas y la regla de agregación de cuentas conjuntas,
que se verifican en la norma.

#### B4 · Concentración y partes relacionadas

**Pregunta.** En el *Banco Yvyra* **[S]**, la cartera bruta es 1 000 y los créditos
a empresas del mismo controlador suman 150. Calcula esa cifra como porcentaje de la
cartera y del capital regulatorio (100), y el exceso sobre un límite de ejercicio
del 20 % del capital.

**Cálculo.**

```text
150 / 1 000 = 15,0 % de la cartera
150 / 100   = 150 % del capital regulatorio
límite = 0,20 × 100 = 20        exceso = 150 − 20 = 130   (7,5 veces el límite)
```

**Interpretación.** Una exposición que es el 15 % de la cartera parece moderada;
medida contra el capital, que es lo que absorbe la pérdida, supera una vez y media
el capital completo. La unidad de comparación decide la conclusión. **Límite:** el
20 % es un supuesto; el límite real a partes relacionadas está en la ley.

### Ejercicios intermedios

#### I1 · Cartera, capital y capitalización anunciada (Banco Tajy)

**Datos [S].** Patrimonio contable `P = 90`; intangibles 30; `APR = 500`; `r_min =
12 %`. Se deben provisionar 20 adicionales. El grupo anuncia 30 en dos tramos de
15; solo el primero está integrado.

**Cálculo.**

```text
inicial:        K = 90 − 30 = 60      r = 60/500 = 12,0 %   (justo en el mínimo)
tras provisión: P = 70, K = 40        r = 40/500 =  8,0 %   (66,7 % del mínimo)
K para 12 %:    0,12 × 500 = 60       falta 20
con 1.er tramo: K = 55                r = 11,0 %   falta 5  → sigue bajo el mínimo
con 2 tramos:   K = 70                r = 14,0 %
```

**Interpretación.** Un banco *en* el mínimo no tiene margen alguno: cualquier
provisión lo deja en incumplimiento. Y una capitalización parcial puede dejarlo
casi, pero no del todo, en regla: el 11,0 % sigue siendo un incumplimiento aunque
parezca cercano. **Límite:** `APR` constante.

#### I2 · Patrimonio contable no es capital regulatorio

**Pregunta.** En el *Banco Tajy*, el supervisor concluye que la activación de un
software por 30 no tiene respaldo suficiente y debe reconocerse como gasto.
Calcula el efecto sobre `P` y sobre `K`, y repite el cálculo para un banco cuyo
supuesto fuera *no* deducir intangibles del capital.

**Cálculo.**

```text
Banco Tajy (deduce intangibles):
  antes:    P = 90, intangibles 30  → K = 60
  después:  P = 60, intangibles  0  → K = 60      K no cambia

Banco hipotético (NO deduce intangibles):
  antes:    K = P = 90
  después:  K = P = 60                            K cae 30
```

**Interpretación.** Revertir una activación reduce el patrimonio contable en 30
en ambos casos, pero el capital regulatorio solo cae si el intangible *contaba*
como capital. Aquí está la razón por la que el ajuste contable pesa distinto en
cada régimen y por la que no se pueden intercambiar los dos conceptos. Nota
conceptual: el ajuste documentado en el caso real trata de **respaldo contable**
(«no contaban con una justificación plenamente respaldada» **[D, BCP]**); no
permite inferir que el software fallara técnicamente. **Límite:** la deducción de
intangibles real depende de la norma local.

#### I3 · Liquidez bajo estrés

**Pregunta.** En el *Banco Yvyra* **[S]**, con efectivo 120 e inversiones 180 que se
venden con un recorte (*haircut*) del 10 %, calcula la liquidez disponible y la
cobertura frente a retiros del 5 %, 10 %, 20 % y 25 % de los depósitos (1 200).

**Fórmula.** Liquidez `L = E + (1 − h)·Inv`; cobertura `= L / retiros`.

```text
L = 120 + 0,90 × 180 = 120 + 162 = 282

retiro 5 %  = 60   → cobertura 282/60  = 4,70 veces
retiro 10 % = 120  → cobertura 2,35 veces
retiro 20 % = 240  → cobertura 1,175 veces
retiro 25 % = 300  → cobertura 0,94 veces → falta 18
retiro máximo soportable = 282/1200 = 23,5 % de los depósitos
```

**Interpretación.** El banco aguanta una corrida del 20 % pero no del 25 %. El
punto de ruptura (23,5 %) es la cifra que hay que comparar con un escenario
plausible, y la difusión de información sensible **[D, BCP]** es lo que puede
llevar un escenario de 5 % a uno de 20 %. **Límite:** se ignoran plazos
intradía y el acceso a líneas de liquidez del banco central.

#### I4 · Primer desembolso, total cubierto y deudas vencidas

**Pregunta.** Con `G = 228,3` millones de Gs y un anticipo de hasta **40 salarios
mínimos** (= 40 × 3,044 = 121,76 millones de Gs, **salario implícito derivado**)
descontando deudas vencidas **[H]**, calcula para tres depositantes **[S]** el
anticipo neto, el remanente cubierto y lo no cubierto: D1, cuentas de 90, 70 y 150
con una deuda vencida de 20; D2, 60 sin deudas; D3, 500 sin deudas.

**Cálculo.**

```text
D1: saldo 310; cubierto = mín(310; 228,3) = 228,3; no cubierto = 81,7
    anticipo bruto = mín(121,76; 228,3) = 121,76; neto = 121,76 − 20 = 101,76
    cubierto neto total = 228,3 − 20 = 208,3; remanente = 208,3 − 101,76 = 106,54

D2: saldo 60; cubierto 60; anticipo = mín(121,76; 60) = 60; remanente 0

D3: saldo 500; cubierto 228,3; no cubierto 271,7
    anticipo 121,76; remanente 228,3 − 121,76 = 106,54
```

**Interpretación.** El anticipo es **una fracción** del total cubierto (53,3 % para
D1 y D3) y puede ser **todo** para un depositante pequeño (D2). Para D3, la mayor
parte de su saldo (54,3 %) no está cubierta. La palabra «cubierto» y la palabra
«depositado» se refieren a cantidades distintas. **Límite:** el orden en que se
descuentan las deudas y la reconciliación entre el primer desembolso de Gs 10 M y
el anticipo de 40 salarios mínimos informados **no están aclarados** en las
fuentes; el ejercicio fija un supuesto.

### Ejercicios avanzados

#### A1 · Comparar alternativas de resolución

**Pregunta.** El valor realizable de los activos del *Banco Yvyra* **[S]** tras las
revisiones es 1 000. Los pasivos son: depósitos cubiertos 700, depósitos no
cubiertos 500 y otras deudas 60. Compara cuatro alternativas con el **principio de
no perjuicio** (ningún acreedor recibe menos que en la liquidación) y una **regla
de menor costo** (el fondo no gasta más que el pago directo).

**Cálculo.** Supuestos: depositantes de igual rango; el fondo se subroga en lo que
paga; otras deudas cobran después de los depósitos.

```text
(1) LIQUIDACIÓN Y PAGO DIRECTO
    recuperación de depósitos = 1 000 / 1 200 = 83,33 %
    el fondo paga 700, recupera 0,8333 × 700 = 583,3  → costo neto 116,7
    no cubiertos reciben 0,8333 × 500 = 416,7  (pierden 83,3)
    otras deudas: 0

(2) VENTA DE TODO: adquirente asume 1 200 de depósitos y recibe 1 000 de activos
    brecha 200 → costo para el fondo 200 > 116,7  ✗ viola la regla de menor costo
    no cubiertos: 100 %

(3) TRANSFERENCIA DE CUBIERTOS CON 700 DE LOS MEJORES ACTIVOS
    costo del fondo 0; quedan 300 de activos para 500 no cubiertos
    → 300/500 = 60 % < 83,3 %  ✗ viola el principio de no perjuicio

(4) TRANSFERENCIA DE CUBIERTOS CON ACTIVOS PROPORCIONALES
    activos transferidos 0,8333 × 700 = 583,3; fondo aporta 116,7
    no cubiertos: 416,7 (83,3 %)   ✓ ambos criterios; las cuentas no se interrumpen
```

**Interpretación.** Las alternativas (1) y (4) cuestan lo mismo al fondo y dejan
igual a los no cubiertos; (4) además **preserva el servicio** de las cuentas y
pagos. (2) protege a todos pero a un costo mayor; (3) parece barata para el fondo
a costa de los no cubiertos. La elección no es técnica solamente: pondera costo
público, trato de acreedores y continuidad. **Límite:** el catálogo de
instrumentos y la prelación son los de la ley paraguaya y no se asumen aquí.

#### A2 · Estrés inverso con una hipótesis que cambia la respuesta

**Pregunta.** Calcula cuánta provisión adicional `h` lleva al *Banco Yvyra* **[S]**
(a) por debajo del mínimo de 12 % y (b) por debajo del 50 % del mínimo (6 %), bajo
dos hipótesis: `APR` constante y `APR` que baja `h` (porque la cartera neta cae).

**Cálculo.**

```text
APR constante:   K − h = r · APR
  12 %:  100 − h = 84  → h = 16        (1,6 % de la cartera bruta)
   6 %:  100 − h = 42  → h = 58        (5,8 %)

APR = 700 − h:   (100 − h)/(700 − h) = r
  12 %:  100 − h = 84 − 0,12h  → 16 = 0,88h → h = 18,18
   6 %:  100 − h = 42 − 0,06h  → 58 = 0,94h → h = 61,70

con h = 60:  APR constante → 40/700 = 5,71 %  (< 6 %)
             APR = 640     → 40/640 = 6,25 %  (> 6 %)
```

**Interpretación.** Con la misma provisión de 60, una hipótesis deja al banco *por
debajo* del umbral y la otra *por encima*. La conclusión «cruza el 50 % del mínimo»
depende de un supuesto sobre `APR` que parece menor. Un informe responsable da el
resultado bajo ambas hipótesis y dice cuál usó. **Límite:** las ponderaciones de
riesgo reales no son uniformes.

#### A3 · Concentración por grupo

**Pregunta.** La cartera de 1 000 del *Banco Yvyra* **[S]** contiene: empresas E1 =
60, E2 = 40, E3 = 30, E4 = 20 (todas del mismo controlador); diez deudores
independientes de 20; el resto (650) atomizado. Calcula las cinco mayores
exposiciones **por nombre** y **por grupo**, el índice de Herfindahl (suma de
cuadrados de las cuotas en puntos porcentuales) sobre los 14 deudores grandes y la
pérdida de capital si el grupo pierde el 40 %.

**Cálculo.**

```text
por nombre:  60, 40, 30, 20, 20  → suma 170 = 17,0 % de la cartera
por grupo:   150 (E1..E4), 20, 20, 20, 20 → suma 230 = 23,0 %
cuotas por nombre (%): 6, 4, 3, 2 y diez de 2
  HHI nombre = 36 + 16 + 9 + 4 + 10×4 = 105
por grupo: 15 y diez de 2:  HHI = 225 + 40 = 265    (×2,52)
grupo / capital = 150/100 = 150 %; límite supuesto 25 % → 25; exceso 125
pérdida con 40 % = 0,40 × 150 = 60 → K = 40, r = 5,71 % (con APR constante)
```

**Interpretación.** Mirar prestatario por prestatario subestima la concentración
2,5 veces; y esa pérdida de 60 es **exactamente** la provisión del ejemplo guiado
2: la cartera a vinculadas puede explicar por sí sola la caída del índice. Es una
**ilustración sintética del mecanismo**: no se afirma que esa fuera la composición
del caso real. **Límite:** la agrupación por vinculación exige criterios (control,
dependencia económica) que el ejercicio da por conocidos.

#### A4 · Línea de tiempo de liquidez y capitalización

**Pregunta.** Con la liquidez disponible de 282 (ejercicio I3), salidas diarias
sobre los depósitos iniciales: 3 %, 5 %, 8 %, 8 %, 6 % en los días 1 a 5. ¿En qué
día se agota la liquidez? ¿Qué cambia si el grupo integra 50 en el día 3, o 100?
¿Qué cambia si solo lo anuncia?

**Cálculo.**

```text
salidas:   d1 36   d2 60   d3 96   d4 96   d5 72
acumulado: 36      96      192     288     360

sin ayuda:              282 → se agota el día 4 (288 > 282; falta 6)
anunciado, no integrado: igual: se agota el día 4
integra 50 el día 3:    332 → aguanta el día 4 (288), se agota el día 5 (360 > 332; falta 28)
integra 100 el día 3:   382 → aguanta hasta el día 5 (360), sobran 22
```

**Interpretación.** Una inyección **efectiva y rápida** compra días, pero no
resuelve la corrida si las salidas continúan: solo la cambia de fecha. Y un
anuncio sin dinero integrado no compra ni un día. En la vida real, la garantía de
depósitos modifica el cálculo porque los depositantes cubiertos tienen menos
razones para retirar. **Límite:** tasas de salida sintéticas; el efecto de la
garantía y el crédito de última instancia no se modelan.

---

## Parte C · Cinco preguntas abiertas

No tienen respuesta única. Se evalúan por el uso de las fuentes, la separación de
niveles **H · D · P · I · S** y el reconocimiento de límites.

1. Una autoridad actúa cinco meses después de detectar un problema. ¿Qué
   información falta para decir si fue tardía, prudente o inevitable? ¿Por qué una
   reacción rápida también tiene costos?
2. ¿Debe el supervisor comunicar el valor exacto del índice de solvencia al
   iniciar una resolución? Compara transparencia, riesgo de corrida y deber de
   informar.
3. ¿Qué diferencia hay entre una investigación sobre administradores y una
   condena? ¿Cómo debe hablar un docente de un caso con investigaciones abiertas?
4. Los fondos mutuos son patrimonios separados del banco. ¿Por qué podrían verse
   afectados igualmente? ¿Qué debe saber un inversor antes de comprar un fondo
   ofrecido en una ventanilla bancaria?
5. Si el programa de estudios cambia de régimen (de Paraguay a Chile o a la Unión
   Europea), ¿qué partes del caso se transfieren y cuáles no?

**Respuestas orientativas.** (1) Falta saber qué se pidió al banco en cada etapa,
qué plazos tenía, si había alternativas privadas; actuar rápido puede forzar una
resolución evitable. (2) A favor: confianza, comparabilidad; en contra: puede
precipitar retiros; la práctica habitual es comunicar la insuficiencia y diferir el
detalle cuando se verifique. (3) Una investigación es un procedimiento abierto; una
condena es una decisión judicial; hay que usar «se investiga», «se atribuye». (4)
Pueden perder valor por el activo que el banco emitió y por suspensión de rescates;
hay que preguntar composición y diversificación. (5) Se transfieren los conceptos
(liquidez, capital, jerarquía); no los instrumentos ni los límites.

---

## Parte D · Actividad integradora: comité de riesgos del Banco Yvyra

**Rol.** Eres el comité de riesgos del *Banco Yvyra* **[S]** un viernes por la
tarde. Debes decidir, por escrito, qué recomiendas a un directorio para el lunes.

**Paquete de datos [S].** Balance inicial del ejemplo guiado 2; provisión
adicional necesaria 60; cartera a vinculadas 150 (E1..E4); liquidez 282; salidas
esperadas de 3 %, 5 %, 8 % por día si el rumor se difunde; capitalización anunciada
de 100 en dos tramos de 50, el primero «en los próximos días»; banco sin acceso
confirmado a líneas del banco central.

**Informe requerido** (extensión máxima de dos páginas), con estas secciones:

1. **Qué ocurrió según las fuentes.** Cinco líneas con etiquetas **H · D · P · I · S**.
2. **Conceptos que lo explican.** Liquidez, solvencia, capital regulatorio frente a
   patrimonio, concentración, partes relacionadas (con una definición propia).
3. **Cálculos e interpretación.** Índice antes y después; faltante; días de
   liquidez; concentración por grupo; todo con fórmula, variables y unidad.
4. **Alternativas y decisión justificada.** Al menos tres alternativas
   (por ejemplo: exigir integración del primer tramo antes del lunes; limitar
   retiros; pedir apoyo al supervisor; vender cartera) con ventajas, costos y
   riesgos; una decisión con criterio explícito.
5. **Consecuencias para los clientes.** Depositantes por debajo y por encima del
   tope de garantía; empresas con pagos en curso; qué se les comunica.
6. **Incertidumbres y límites.** Qué dato falta, qué supuesto es más sensible
   (por ejemplo `APR`), qué no se puede afirmar.

**Apoyo para principiantes.** Entregar solo las secciones 1, 3 y 4 con las
fórmulas escritas; usar la tabla de la clase 4 de la Parte 11 y el ejemplo guiado 1.

**Extensión para avanzados.** Añadir el estrés inverso con ambas hipótesis de
`APR`, la comparación A1 con cifras propias y un breve comunicado de 120 palabras
para depositantes sin mencionar causas no comprobadas.

**Solución orientativa.** Un buen informe señala que el índice es 5,71 % (o 6,25 %
si `APR` baja), que no se puede esperar a que el primer tramo llegue «en los
próximos días» porque la liquidez se agota el día 4 (A4); que el 100 anunciado no
cuenta hasta integrarse; que la concentración por grupo supera el capital; que
exigir la integración inmediata del primer tramo, activar la liquidez disponible y
notificar al supervisor son las acciones de menor arrepentimiento; y que una
comunicación a depositantes debe decir qué está garantizado, hasta qué monto y
cuándo, sin prometer lo que no se controla. Acepta decisiones distintas si el
criterio es explícito.

---

## Parte E · Evaluación

### Ponderación

| Dimensión | Peso | Qué se evalúa en esta actividad |
|---|---:|---|
| **Conocimiento** | 20 % | Definiciones correctas de liquidez, solvencia, capital, garantía, resolución |
| **Aplicación** | 30 % | Los cálculos son correctos y cada uno lleva fórmula, variables y unidad |
| **Decisión argumentada** | 30 % | Alternativas comparadas, criterio explícito, sensibilidad |
| **Ética, documentación y límites** | 20 % | Niveles de dato separados, sin culpar a nadie, incertidumbres declaradas |

### Descriptores de desempeño

| Dimensión | 4 · Excelente | 3 · Competente | 2 · En desarrollo | 1 · Insuficiente |
|---|---|---|---|---|
| **Conocimiento (20 %)** | Distingue liquidez, solvencia y rentabilidad con ejemplos propios; separa patrimonio de capital | Define bien los conceptos; ejemplos prestados del texto | Define con imprecisiones (confunde retiro con pérdida) | Confunde los conceptos |
| **Aplicación (30 %)** | Cálculos correctos con unidades y comprobación; resuelve ambas hipótesis de `APR` | Cálculos correctos; faltan unidades o comprobaciones | Un error de procedimiento que cambia la conclusión | Cálculos incompletos o sin método |
| **Decisión (30 %)** | Compara ≥3 alternativas, criterio, supuestos y sensibilidad; acota la decisión | Decide con criterio y evidencia; sin sensibilidad | Decide y justifica sin declarar supuestos | Decide sin justificar o justifica sin decidir |
| **Ética y límites (20 %)** | Separa H · D · P · I · S; no atribuye culpa; declara qué no se sabe | Separa niveles con algún desliz; reconoce límites | Mezcla hechos y declaraciones; límites genéricos | Presenta investigaciones como condenas o inventa datos |

### Cómo convertir en nota

`nota = 0,20·C + 0,30·A + 0,30·D + 0,20·E`, donde cada letra es la puntuación (1 a
4) de su dimensión. Un 4 en las cuatro es 4,0 (excelente); 3,0 es el umbral de
competencia. Un estudiante que calcula perfecto (A = 4) pero decide sin criterio
(D = 1) y presenta una investigación como condena (E = 1), con conocimiento
correcto (C = 4), obtiene `0,8 + 1,2 + 0,3 + 0,2 = 2,5`: no alcanza el umbral. Es
intencional: la guía docente asigna el 50 % al criterio y a los límites.

### Errores de razonamiento para detectar

| Afirmación errónea | Por qué es errónea | Se trabaja en |
|---|---|---|
| «El banco tiene efectivo, luego es solvente» | Liquidez no implica solvencia | Ejemplo 1 |
| «El retiro redujo el patrimonio» | Reduce efectivo y depósitos | B1 |
| «5,56 % es el 50 % del mínimo» | Es 46,3 % del mínimo | B2 |
| «Tres cuentas, tres garantías» | La garantía es por depositante y entidad | B3, I4 |
| «El anticipo es lo que me cubren» | Es una fracción del total cubierto | I4 |
| «Capitalizaron 100, estamos a salvo» | Anunciada ≠ integrada | Ejemplo 2, A4 |
| «El ajuste del software redujo el capital» | Depende de la deducción | I2 |
| «Cuatro empresas, cuatro riesgos» | Un solo grupo | A3 |
| «Se investiga, luego es culpable» | Investigación ≠ condena | Parte C |

## Verificación

Las cifras de este documento se recalculan en `tests/test_ueno_bank_ejercicios.py`;
una discrepancia entre el texto y el cálculo hace fallar la prueba. La revisión
conceptual y pedagógica (si los ejercicios enseñan lo que dicen enseñar) es una
tarea humana que no cubre ningún validador.
