# Caso · La cuenta nostro que se quedó seca

**Tema:** pagos transfronterizos · **Parte relacionada:** 18 · **Naturaleza:**
caso sintético compuesto · **Fecha de verificación:** 2026-08-12

Un banco mediano deja de poder pagar en una divisa a las 11:40 de un jueves. No
es insolvente: tiene el dinero, en otra cuenta y en otro huso horario. Este es el
caso que enseña por qué prefinanciar es caro y no prefinanciar es peor.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · el banco liquida esa divisa a través de
    una cuenta nostro en un corresponsal
  · saldo de apertura        14 200 000
  · pagos presentados ese día 19 800 000
  · cobros esperados          21 400 000
    de los cuales, con valor del mismo día
                              6 100 000
    y el resto, valor D+1

SUPUESTO DEL EJERCICIO
  · corte del corresponsal       16:00 local
  · diferencia horaria            −6 h
  · descubierto intradía autorizado
                              3 000 000
  · coste del descubierto no autorizado
                                    0,45 %
    sobre el importe, mínimo 2 500
```

La aritmética del día es sencilla y descorazonadora: 14,2 disponibles más 6,1 que
entran el mismo día son 20,3 frente a 19,8 de pagos. Cabe. Pero los 6,1 entran a
las 15:20 hora del corresponsal, y el 63 % de los pagos hay que presentarlos antes
de las 12:00 para que el beneficiario cobre ese día.

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Tesorería del banco | No pagar descubierto | Saldo de apertura y previsión |
| Mesa de pagos | Que todo salga en plazo | La cola de pagos |
| Banco corresponsal | Cobrar por el descubierto | El saldo, en tiempo real |
| Clientes corporativos | Que su proveedor cobre hoy | Nada |
| Contrapartes que pagan al banco | Cumplir en su horario | Su propio calendario |
| Riesgo de liquidez | Un límite que se cruzó | El informe, al día siguiente |

## Decisiones

```text
08:00  tesorería ve el saldo y decide no
       prefinanciar
       RAZÓN: el coste de mantener saldo
       ocioso es 0,9 % anual
       CÁLCULO CORRECTO EN PROMEDIO

11:40  se agota el disponible
       DECISIÓN: usar el descubierto
       autorizado de 3 000 000

12:30  se agota también
       DECISIÓN: encolar los pagos
       restantes para el día siguiente
       ALTERNATIVA DESCARTADA: descubierto
       no autorizado

15:20  entran los 6 100 000
       demasiado tarde para el corte de
       presentación

16:00  corte
       PAGOS NO EJECUTADOS      4 900 000
       OPERACIONES AFECTADAS          212
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Desajuste horario de cobros y pagos | Estructural | Sí |
| Previsión de tesorería por saldo, no por hora | Desde el diseño | Sí |
| Liquidez atrapada en otras divisas | Estructural | Sí |
| Concentración en un solo corresponsal | Estructural | Sí |
| Riesgo reputacional con clientes | Desde las 12:30 | Sí |
| Riesgo de crédito intradía del corresponsal | Estructural | No |

## Regulación

```text
QUÉ ALCANZA

  GESTIÓN DE LIQUIDEZ INTRADÍA
    los estándares prudenciales exigen
    medir y gestionar la liquidez dentro
    del día, no solo al cierre

  RIESGO DE CONCENTRACIÓN
    la dependencia de un único corresponsal
    por divisa es una exposición que debe
    identificarse y limitarse

  PROTECCIÓN DEL CLIENTE
    el plazo prometido al ordenante y su
    incumplimiento tienen consecuencias
    contractuales y, según el régimen,
    regulatorias

LÍMITE
  los indicadores exigidos y sus umbrales
  dependen del marco prudencial aplicable
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Previsión diaria de tesorería | Sí | Sí, y era insuficiente | Perfil horario, no saldo diario |
| Límite de descubierto autorizado | Sí | Sí | Escalado cuando se consume el 70 % |
| Segundo corresponsal | No | — | Alternativa activada y probada |
| Prioridad de pagos | Parcial | No | Regla escrita de qué se paga primero |
| Alerta de consumo intradía | No | — | Umbral con aviso a las 10:00 |
| Acuerdos de neteo con contrapartes | No | — | Reduce el bruto que hay que financiar |

El cuarto control es el que más discusión genera: cuando no se puede pagar todo,
alguien decide el orden, y si no hay regla escrita esa decisión la toma quien
atienda el teléfono. Una política de prioridades —importe, cliente, consecuencia
del retraso, riesgo de liquidación— convierte una improvisación en una decisión
defendible.

## Resultado

```text
COSTE DEL DÍA (supuestos)

  descubierto autorizado usado
    3 000 000 × 0,12 % =         3 600
  212 operaciones retrasadas
    reclamaciones 38 × 45 =      1 710
    penalizaciones comerciales
    estimadas                   11 400
  revisión posterior y proyecto
    de mejora                   26 000

  TOTAL                         42 710

COMPARACIÓN CON PREFINANCIAR
  saldo adicional necesario   5 000 000
  coste anual 0,9 %              45 000
  coste diario equivalente          178

  178 AL DÍA FRENTE A 42 710 UNA VEZ
  → el prefinanciamiento se paga solo
    si este día ocurre más de una vez
    cada 240 días hábiles
```

## Lecciones

1. **La liquidez se gestiona por hora, no por día.** Un saldo suficiente al cierre
   puede ser insuficiente a las once y cuarenta.
2. **No prefinanciar es una apuesta con frecuencia asociada**, y hay que
   calcularla explícitamente: 178 al día contra 42 710 por episodio define cuántos
   episodios se toleran.
3. **Sin política de prioridades, el orden de pago lo decide el azar** y el banco
   pierde la capacidad de defender su decisión.
4. **Un solo corresponsal por divisa es una decisión de riesgo**, no una decisión
   operativa, y debe aprobarse en ese nivel.

## Preguntas

1. ¿Cómo construirías una previsión de tesorería con perfil horario? ¿Qué datos
   necesitas que hoy no tienes?
2. ¿Qué criterio usarías para priorizar 19,8 millones de pagos con 17,2 de
   liquidez? Justifícalo ante un cliente que quedó fuera.
3. ¿Es razonable el cálculo de 178 al día? ¿Qué falta en él?
4. ¿Qué cambiaría si existiera un acuerdo de neteo con las tres contrapartes
   principales?
5. ¿En qué punto este incidente deja de ser operativo y pasa a ser un asunto de
   riesgo de liquidez que el comité debe conocer?

## Fuentes

- Comité de Supervisión Bancaria de Basilea (2013). *Monitoring tools for intraday liquidity management*. BIS. <https://www.bis.org/publ/bcbs248.htm>
- CPMI (2020). *Enhancing cross-border payments: building blocks of a global roadmap*. BIS. <https://www.bis.org/cpmi/publ/d193.htm>
- Financial Stability Board. *G20 Roadmap for Enhancing Cross-border Payments*. <https://www.fsb.org/work-of-the-fsb/financial-innovation-and-structural-change/cross-border-payments/>
- Banco Central de Chile. *Compendio de Normas Financieras y sistemas de pago*. <https://www.bcentral.cl/>
- Verificación local: caso sintético; cifras supuestas. Los indicadores de liquidez intradía exigibles dependen del marco prudencial aplicable. **Fecha de verificación: 2026-08-12.** No constituye asesoría legal.
