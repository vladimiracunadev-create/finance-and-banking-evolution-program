# Crisis financiera digital: custodia, respaldo y recuperación

Esta guía es una **especialización transversal**: no añade clases ni renumera
nada. Reúne en un solo recorrido lo que el programa ya enseña por separado —
riesgo operacional, custodia, conciliación, liquidez, fraude, AML, continuidad y
gobierno— y lo aplica a una pregunta concreta: **qué le ocurre a una entidad que
custodia activos de clientes cuando pierde una parte de ellos de golpe, y qué
tiene que demostrar, reponer y comunicar para seguir operando.**

El detalle técnico de blockchain, claves y puentes **no se repite aquí**: está en
la [Parte 19](../modules/18-blockchain-y-dlt-para-instituciones-financieras/README.md),
en el [mapa blockchain y DLT](mapa-blockchain-dlt.md) y en la
[guía de custodia, conciliación y gobernanza](custodia-conciliacion-y-gobernanza.md).
Aquí se usa su conclusión (una llave comprometida mueve fondos sin pasar por un
control humano) y se estudia lo que viene después en el balance de la entidad.

> ⚖️ **Material formativo.** Las cifras del caso de 2026 son **estimaciones
> públicas sujetas a revisión**, no un balance auditado. Los ejercicios usan
> datos sintéticos. Nada de esto es asesoría financiera, legal ni de inversión.

## Qué se aprende y dónde se ancla

| Pregunta | Qué se trabaja | Dónde está la base en el programa |
|---|---|---|
| ¿Qué falló y por qué? | Riesgo operacional y tecnológico, terceros | [11.10](../modules/10-gestion-integral-de-riesgos/classes/10-riesgo-operacional.md), [11.11](../modules/10-gestion-integral-de-riesgos/classes/11-riesgo-tecnologico-y-ciberseguridad.md), [23.14](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/14-modelo-de-amenazas-priorizado.md), [22.14](../modules/21-regulacion-de-mercados-financieros-digitales/classes/14-resiliencia-operativa-y-terceros-criticos.md) |
| ¿Qué tengo que devolver y qué tengo? | Custodia y segregación | [20.12](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/12-custodia-de-activos-digitales.md), [22.9](../modules/21-regulacion-de-mercados-financieros-digitales/classes/09-custodia-y-segregacion-en-la-norma.md), [23.9](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/09-custodia-y-gestion-de-claves.md) |
| ¿Cuadran activos y pasivos? | Conciliación | [10.8](../modules/09-operaciones-bancarias/classes/08-conciliacion-bancaria.md), [custodia y conciliación](custodia-conciliacion-y-gobernanza.md) |
| ¿Alcanza para pagar a todos? | Liquidez, solvencia, respaldo | [11.4](../modules/10-gestion-integral-de-riesgos/classes/04-riesgo-de-liquidez.md), [20.4](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/04-reservas-composicion-calidad-y-verificacion.md), [20.6](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/06-perdida-de-paridad-anatomia-de-una-corrida.md), [12.12](../modules/11-regulacion-cumplimiento-y-auditoria/classes/12-resolucion-bancaria-y-seguro-de-depositos.md) |
| ¿Cómo lo demuestro? | Proof of Reserves y de Liabilities | [20.4](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/04-reservas-composicion-calidad-y-verificacion.md), [custodia y conciliación](custodia-conciliacion-y-gobernanza.md) |
| ¿Cómo entró el fraude y cómo se detecta? | Fraude, transferencias no autorizadas | [4.12](../modules/03-seguridad-y-consumo-financiero/classes/12-prevencion-y-respuesta-ante-fraude.md), [4.13](../modules/03-seguridad-y-consumo-financiero/classes/13-analisis-de-incidentes.md) |
| ¿Qué hago con los fondos sospechosos? | AML, KYC, monitoreo, sanciones | [12.3](../modules/11-regulacion-cumplimiento-y-auditoria/classes/03-prevencion-de-lavado-de-activos.md), [12.4](../modules/11-regulacion-cumplimiento-y-auditoria/classes/04-conozca-a-su-cliente.md), [12.5](../modules/11-regulacion-cumplimiento-y-auditoria/classes/05-sanciones-internacionales.md), [18.12](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/12-aml-sanciones-y-regla-del-viaje.md) |
| ¿Cómo sigo operando? | Continuidad y crisis | [10.16](../modules/09-operaciones-bancarias/classes/16-continuidad-y-eficiencia-operativa.md), [15.13](../modules/14-estrategia-y-direccion-bancaria/classes/13-gestion-de-crisis.md), [23.15](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/15-escenario-de-tension-y-continuidad.md) |
| ¿Quién absorbe la pérdida? | Seguros, fondos de protección, resolución | [12.12](../modules/11-regulacion-cumplimiento-y-auditoria/classes/12-resolucion-bancaria-y-seguro-de-depositos.md), [23.16](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/classes/16-resolucion-ordenada-y-salida.md) |
| ¿Quién responde y cómo se audita? | Gobernanza, control interno, auditoría | [15.9](../modules/14-estrategia-y-direccion-bancaria/classes/09-gobierno-corporativo.md), [12.14](../modules/11-regulacion-cumplimiento-y-auditoria/classes/14-auditoria-interna.md), [12.15](../modules/11-regulacion-cumplimiento-y-auditoria/classes/15-auditoria-externa-y-control-interno.md) |

## Ruta progresiva de estudio

Se recomienda este orden, que **no sustituye** la ruta del programa: la
complementa una vez cursadas las partes que cada paso nombra.

1. **Después de la Parte 11 (riesgos):** secciones 1 a 3 de esta guía y los
   ejercicios 1 y 2.
2. **Después de la Parte 12 (regulación y cumplimiento):** secciones 4 y 5 y el
   ejercicio 4.
3. **Después de la Parte 20 (activos digitales):** sección 6 (el caso), el
   [caso Binance 2026](../case-studies/custody/binance-2026.md) y los
   ejercicios 3 y 5.
4. **Con la Parte 23 (banco digital):** el simulador bancario ampliado y la
   evaluación integradora de [ejercicios y evaluación](ejercicios-crisis-financiera-digital.md).

## 1. Primero la matemática: qué se mide y con qué unidad

Antes de cualquier simulación se fija el lenguaje. Cada fórmula se presenta con
sus variables, su unidad, el supuesto que la sostiene y su límite. Quien no
pueda decir el supuesto de una fórmula no debería usar su resultado.

### 1.1 Respaldo (backing ratio)

**Variables.** `A_liq`: activos líquidos a 24 h (MUSD). `A_nl`: activos no
líquidos o no disponibles a 24 h (MUSD). `P`: pasivos con clientes, es decir, lo
que la entidad debe restituir (MUSD). Todo medido a la misma hora de corte.

```text
respaldo bruto        R_b = (A_liq + A_nl) / P        [sin unidad; 1,00 = 100 %]
respaldo disponible   R_d = A_liq / P                 [sin unidad]
brecha                B   = P − (A_liq + A_nl)        [MUSD; > 0 = faltante]
```

**Supuesto.** Los activos se valoran a precio de mercado sin descuento y `P` se
mide en la misma unidad. **Límite.** Un respaldo de 100 % no prueba propiedad,
segregación ni que el activo pueda moverse hoy: dice solo que *la cifra* de
activos alcanza *la cifra* de obligaciones. Por eso existen `R_b` y `R_d`:
pueden diferir en veinte puntos y las dos son verdad a la vez.

### 1.2 Cuatro cifras que no son equivalentes

**Variables.** `S`: sustraído o transferido sin autorización. `F`: congelado por
terceros, con `F ≤ S`. `p`: probabilidad de que `F` sea restituido, `0 ≤ p ≤ 1`.

```text
sin congelar           U = S − F
restituible esperado   E[rec] = F · p
pérdida definitiva     D = S − F · p
```

**Supuesto.** `p` es único para todo `F`. **Límite.** En la práctica cada
emisor, red y monto tiene su propia probabilidad y su propio plazo; además `D`
es una *esperanza*: la pérdida realizada será un número, no una probabilidad.

> **Regla de lectura.** Un fondo *congelado* no está *recuperado*; un fondo
> *sustraído* no está *perdido* mientras haya `F` por restituir; una
> *transferencia sospechosa* puede resultar legítima; y una *pérdida definitiva*
> solo se conoce al cierre del proceso. Mezclar estas palabras produce titulares,
> no decisiones.

### 1.3 Efecto sobre el respaldo

El día del incidente el balance de la entidad cae en `S` (no en `S − F`), porque
el activo congelado no está bajo su control:

```text
A'_liq = A_liq − S_liq        S_liq = S · parte_líquida
R_b'   = (A_liq + A_nl − S) / P
R_b(t) = (A_liq + A_nl − S + Rest(t) + Rep(t)) / P
```

con `Rest(t)` (restituciones) y `Rep(t)` (reposiciones) acumuladas hasta el día
`t`. **Límite.** `parte_líquida` es un supuesto: un robo de hot wallets sale casi
todo de activos líquidos; otro tipo de pérdida puede salir de otras cuentas.

### 1.4 Riesgo de retiros masivos

**Variables.** `r0`: tasa diaria base de retiros. `k`: sensibilidad de los
retiros al deterioro del respaldo. `h`: descuento por vender un activo no
líquido en tensión.

```text
demanda del día    D_t = P_t · min(1, r0 + k · max(0, 1 − R_b,t))
tasa máx. atendible  r* = A_liq / P                (sin vender nada)
cobertura de retiros C  = A_liq / (r · P)          (C < 1: no se alcanza)
```

**Supuesto.** La respuesta lineal al deterioro es una hipótesis de trabajo.
**Límite.** La corrida real depende de qué se comunica, de si hay pausa y de
qué hacen los demás clientes; `k` debe re-estimarse con datos, no copiarse.

### 1.5 Reposición de reservas

```text
necesidad          N = max(0, objetivo · P − (A_liq + A_nl))
costo de compra    C = impacto · monto² / profundidad
costo del plan     Σ monto_i · costo_relativo_i      (fuentes en orden)
```

**Variables.** `objetivo`: respaldo buscado (1,00); `impacto`: deslizamiento por
fracción de la profundidad consumida; `profundidad`: monto que el mercado
absorbe con ese impacto. **Límite.** En tensión la profundidad se contrae y el
impacto deja de ser lineal: el modelo **subestima** el costo de comprar mucho en
poco tiempo.

### 1.6 Costo del incidente

```text
C_total = D + C_rep + C_for + C_op + C_comp
C_op    = ingreso_diario · días_de_pausa
C_comp  = tasa_comp · P_afectado
C_neto  = C_total − min(cobertura_seguro, pérdida_asegurable)
```

**Límite.** No incluye clientes perdidos a futuro ni daño reputacional: son
reales, pero ningún dato de este ejercicio permite estimarlos. Una cifra
omitida no es una cifra cero.

## 2. El incidente como cadena de decisiones

```text
 vector de ataque ─► transferencia no autorizada ─► detección ─► contención
        │                                                           │
        ▼                                                           ▼
 fondos sustraídos ─► congelamiento por terceros ─► conciliación ─► brecha firmada
        │                                                           │
        ▼                                                           ▼
 respaldo cae ─► riesgo de retiros ─► pausa / reapertura ─► reposición ─► verificación
```

Cada flecha es una decisión con un responsable. El plan de recuperación del
laboratorio (`apps/custody_crisis_lab/recovery.py`) fija siete fases, y de cada
una dice *acción*, *responsable*, *condición de entrada* y *condición de salida*.
Una fase termina cuando se cumple su condición de salida, no cuando pasa el
tiempo.

| Fase | Horizonte | Salida |
|---|---|---|
| 1. Contención | 0–4 h | Vector cerrado; sin movimientos adicionales no autorizados |
| 2. Cuantificación | 4–48 h | Brecha firmada y revisada por segunda línea |
| 3. Comunicación y reporte | 6–72 h | Informes enviados; canal único de actualización |
| 4. Reposición | 1–14 días | Respaldo bruto ≥ objetivo con activos propios |
| 5. Reapertura gradual | 2–10 días | Retiros normalizados dos días seguidos |
| 6. Verificación independiente | 7–30 días | Informe publicado con alcance y fecha de corte |
| 7. Aprendizaje | 30–90 días | Remediación cerrada y prueba de continuidad |

## 3. Controles que previenen o limitan: qué habría que preguntar

No hay un control único. La literatura de gestión de riesgo operacional coincide
en una idea: **las capas son independientes o no son capas**.

| Capa | Control | Pregunta de auditoría |
|---|---|---|
| Prevención | Segregación de funciones y de llaves; aprobación múltiple e independiente | ¿Puede una sola persona o estación mover fondos? |
| Prevención | Límites de saldo en billeteras calientes; listas blancas de destino | ¿Cuánto puede salir antes de que una persona lo vea? |
| Detección | Monitoreo transaccional en tiempo real y alertas de desvío | ¿Cuánto tarda en saltar la alerta y quién la recibe? |
| Contención | Interruptor de pausa; congelamiento coordinado con emisores | ¿Quién puede apretar el botón y a qué hora se probó? |
| Respaldo | Reservas propias, fondo de protección, seguros | ¿Cuánto cubre, qué excluye y quién es el beneficiario? |
| Evidencia | Conciliación diaria por activo; Proof of Reserves y de Liabilities | ¿Qué alcance, qué corte y quién lo emitió? |
| Gobierno | Comité de riesgos, auditoría interna y externa, plan de continuidad probado | ¿Cuándo fue la última prueba y qué falló? |

**Terceros.** Una cadena de proveedores puede tener una dependencia común que
ningún contrato muestra; véase el caso
[Veintidós entidades y un solo cable](../case-studies/cyber-incidents/proveedor-critico-comun.md).

## 4. Proof of Reserves y Proof of Liabilities: qué prueban y qué no

| Prueba | Responde | No reemplaza |
|---|---|---|
| Proof of Assets | Saldo observado en direcciones controladas | Pasivos, propiedad o disponibilidad |
| Proof of Reserves | Que ciertos activos están designados como respaldo | Auditoría financiera completa |
| Proof of Liabilities | El universo de obligaciones con clientes | Existencia de activos |
| Verificación independiente | Opinión bajo un alcance y marco definidos | Monitoreo continuo después del corte |

El **respaldo bruto de la sección 1.1 solo es creíble si ambas pruebas se emiten
con el mismo corte** y si los pasivos incluyen *todos* los productos (spot,
rendimiento, préstamos). Un Proof of Reserves publicado sin Proof of Liabilities
mide un numerador sin denominador.

## 5. Marco chileno e internacional aplicable

> Verificación local de este apartado: 2026-10-30. Las normas cambian: antes de
> citarlas en un trabajo, compruébalas en la fuente oficial. La
> [metodología de verificación](metodologia-verificacion-regulatoria.md) del
> programa describe el procedimiento.

| Materia | Chile (referencia a comprobar en fuente oficial) | Estándar internacional |
|---|---|---|
| Prestadores de servicios financieros con activos virtuales | Ley Fintec (Ley 21.521) y normas de la CMF | FSB, IOSCO, FATF |
| AML/CFT, KYC, reporte de operaciones sospechosas | Ley 19.913 (UAF) y normativa CMF | Recomendaciones del GAFI/FATF, incluida la regla del viaje |
| Ciberseguridad e incidentes | Ley 21.663 (marco de ciberseguridad); Ley 21.459 (delitos informáticos) | NIST CSF, ISO/IEC 27001 |
| Externalización y terceros | Normativa de la CMF sobre externalización de servicios | Principios de resiliencia operativa del BCBS |
| Continuidad y gestión de crisis | Normativa de gestión del riesgo operacional de la CMF | BCBS, FSB |
| Seguro de depósitos y resolución | Garantía estatal de depósitos y régimen de resolución bancaria | FSB Key Attributes, IADI |
| Protección del consumidor y fraudes | Ley del consumidor (19.496); régimen de fraudes con tarjetas | Principios G20/OCDE de protección financiera |

Mapas del programa: [regulatorio de Chile](mapa-regulatorio-chile.md),
[regulatorio internacional](mapa-regulatorio-internacional.md) y
[fichas normativas](../regulatory/README.md). Organismos de referencia:
[BCBS/BIS](https://www.bis.org/bcbs/), [GAFI/FATF](https://www.fatf-gafi.org/),
[CMF](https://www.cmfchile.cl/) y [Biblioteca del Congreso Nacional](https://www.bcn.cl/leychile/).
Un **fondo de protección** (como los fondos de emergencia que declaran algunas
plataformas) es una decisión privada de la entidad, **no** un seguro de depósitos
ni una garantía estatal.

## 6. El caso de octubre de 2026 en una página

Entre el 29 y el 30 de octubre de 2026 la prensa y la propia entidad informaron
de una sustracción de activos de clientes de la plataforma Binance del orden de
**6 300 millones de USD** (estimación de la entidad; otra firma de análisis
cifra 6 430), de los cuales unos **3 000 millones** habrían sido congelados por
terceros (un titular inicial hablaba de 2 540) y **6 340 millones** en recursos
propios estaban apartados para cubrir la diferencia. **Todas son cifras de
prensa, preliminares y sujetas a revisión.** El análisis completo, con fuentes,
discrepancias y preguntas, está en el
[caso Binance 2026](../case-studies/custody/binance-2026.md).

Lo que el caso enseña **no depende** de que las cifras finales sean estas: que
*sustraído*, *congelado* y *perdido* son tres números distintos; que un
respaldo se compone de un numerador y un denominador; y que reponer reservas
corta la brecha pero no sustituye la verificación independiente.

## 7. Simulaciones del laboratorio

```bash
python apps/custody_crisis_lab/cli.py caso --escenario crd_002
python apps/custody_crisis_lab/cli.py binance
python apps/openbank_simulator/cli.py crisis
```

| Simulación pedida | Dónde |
|---|---|
| Entidad custodio con activos y obligaciones | `entity.py` y `datasets/synthetic/custody_crisis_balance_synthetic.csv` |
| Pérdida extraordinaria de activos líquidos | `incident.aplicar_perdida` |
| Respaldo antes y después | `Custodio.respaldo_bruto` y `respaldo_disponible` |
| Congelamiento de fondos recuperables | `incident.clasificar_fondos` y `aplicar_restitucion` |
| Riesgo de retiros masivos | `runs.simular_corrida` |
| Reposición de reservas | `replenish.plan_de_reposicion` |
| Costos del incidente | `costs.Costos` |
| Plan de recuperación y continuidad | `recovery.PLAN` y `trayectoria_de_respaldo` |
| Escenario en el banco simulado (SQLite) | `apps/openbank_simulator/crisis_digital.py` |

Salida esperada del escenario `crd_002` (entidad de 100 000 MUSD; S = 6 300;
F = 3 000; p = 0,8): respaldo bruto de **100,00 % → 93,70 %**; restituible
esperado **2 400**; pérdida definitiva esperada **3 900**; costo total del
incidente **4 046 MUSD**. La cifra de costo (4 046) **no es** la cifra
sustraída (6 300): es otra pregunta con otra respuesta.

## Límites declarados

- Los parámetros de comportamiento (`r0`, `k`, `h`, `p`) son **hipótesis**; las
  conclusiones cambian con ellos y por eso viven en un CSV visible.
- El modelo no representa a ninguna entidad real: la entidad estilizada del caso
  de 2026 toma como pasivos los «activos bajo gestión» reportados, que es un
  supuesto del ejercicio.
- No modela contagio entre plataformas, efectos de precio en el mercado ni
  responsabilidad legal; para contagio véase la
  [clase 20.14](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/14-contagio-y-riesgo-sistemico.md).
- Es un laboratorio didáctico: no mueve fondos, no se conecta a ninguna red y no
  incluye herramientas para evadir controles.
