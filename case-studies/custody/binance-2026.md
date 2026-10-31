# Caso · Binance, octubre de 2026: sustraído, congelado y perdido

**Tema:** incidente de custodia, respaldo y recuperación · **Partes relacionadas:**
11, 12, 15, 20, 22 y 23 · **Naturaleza:** caso real documentado, **en desarrollo y
con cifras preliminares** · **Fecha de verificación:** 2026-10-30

El 29 y 30 de octubre de 2026 la prensa y la propia plataforma informaron del que
se describe como el mayor robo de criptoactivos registrado. Este caso se escribió
**el mismo día en que las noticias salieron**: las cifras cambian de una fuente a
otra y seguirán cambiando. Por eso el valor del caso no está en memorizar números
sino en **aprender a leerlos**: qué mide cada uno, quién lo dice y qué no permite
concluir.

> ⚖️ **Aviso.** Se trata de cifras públicas **preliminares**, atribuidas a su
> fuente. No hay sentencia, informe forense final ni balance auditado. Alegación,
> atribución de autoría y hallazgo no son equivalentes. Este material no valora la
> solvencia de ninguna entidad ni constituye asesoría.

## Hechos

```text
HECHOS INFORMADOS (atribuidos; todos preliminares)

  Monto afectado
    · ~6 300 MUSD    Binance, via CNBC, CoinDesk y Al Jazeera
    · ~6 360 MUSD    TRM Labs, "monto movido", via CNBC
    · ~6 400-6 430   Chainalysis, via CNBC y prensa
  Fondos congelados
    · "alrededor de" 3 000 MUSD   Binance, via CNBC, CoinDesk, Al Jazeera
    · 2 540 MUSD     cifra de un titular inicial, luego superada
  Reservas anunciadas
    · >6 340 MUSD de recursos propios apartados (CoinDesk);
      5 000 MUSD ya mantenidos en los mismos activos afectados
    · Fondo de emergencia SAFU: ~1 000 MUSD (CoinDesk) o ~1 200 (CNBC)
  Operación
    · el robo se ejecutó en unos 20 minutos, en 10 redes (CNBC, CoinDesk)
    · retiros pausados; depósitos "abiertos" (CoinDesk) o también
      suspendidos (CNBC, Al Jazeera): las fuentes no coinciden
  Causa y autoría (alegaciones, no hallazgos)
    · la entidad apunta al ordenador de un ingeniero comprometido; luego
      habló de puntos de explotación adicionales sin detallarlos
    · TRM Labs: autoría atribuida "con alta confianza" a TraderTraitor;
      Chainalysis: "probablemente"

SUPUESTO DEL EJERCICIO
  · pasivos con clientes = "activos bajo gestión" reportados (~155 000 MUSD)
  · respaldo antes del incidente = 100 %, 85 % líquido a 24 h
```

Una cifra de la lista **no** se utiliza como si estuviera confirmada: algunos
resúmenes atribuyen a Tether «más de 1 570 millones» y a Circle «más de 800
millones» congelados, pero esas cifras **no pudieron contrastarse** en la lectura
directa de la fuente al escribir este caso; suman 2 370, por debajo de los ~3 000
declarados por la entidad. Ese hueco es, en sí mismo, una pregunta del caso.

## Actores

| Actor | Qué persigue | Qué información tiene |
|---|---|---|
| Plataforma custodia | Restituir a clientes y reabrir operaciones | Su balance, sus pasivos, su incidente |
| Clientes | Acceder a sus fondos | Un comunicado y un estado de retiros |
| Emisores de stablecoins | Cumplir sus políticas y órdenes legales | Direcciones señaladas y su capacidad de congelar |
| Firmas de analítica on-chain | Rastrear y atribuir | Flujos públicos; no las intenciones |
| Autoridades y fuerzas de seguridad | Investigar y recuperar | Información reservada |
| Atacante | Mover y convertir fondos antes del congelamiento | Rutas, puentes y mezcladores disponibles |
| Mercado | Reaccionar | Cifras preliminares (el bitcoin cayó cerca de 5 %, según Al Jazeera) |

## Decisiones

```text
DE LA PLATAFORMA (según lo informado)
  pausar retiros mientras se verifica
  RAZÓN: contener, cuantificar, evitar una corrida
  COSTO: ingresos perdidos y confianza

  apartar recursos propios para cubrir la brecha
  RAZÓN: demostrar que el respaldo se repone
  LÍMITE: el monto apartado (6 340) supera la estimación
  del daño (6 300) por un margen de ~40 MUSD

  coordinar congelamientos con terceros
  RAZÓN: inmovilizar lo que sea congelable
  LÍMITE: solo se congela lo que alguien tiene
  capacidad de congelar (stablecoins; no bitcoin ni ether)

  prometer verificación mediante Proof of Reserves
  RAZÓN: reemplazar la afirmación por una prueba
  LÍMITE: sin Proof of Liabilities del mismo corte,
  mide un numerador sin denominador
```

## Riesgos

| Riesgo | Presente | Cómo se manifiesta |
|---|---|---|
| Operacional / tecnológico | Sí | Compromiso de una estación de trabajo con acceso a firmas |
| Tercero | Posible | Dependencia de emisores para congelar |
| Custodia | Sí | Activos de clientes fuera del control de la plataforma |
| Liquidez | Latente | Retiros pausados; riesgo de corrida al reabrir |
| Solvencia | En evaluación | Depende de reposición y de pasivos totales no publicados |
| Mercado | Sí | Ventas de reposición y movimiento de precios |
| AML / sanciones | Sí | Fondos movidos por rutas de ocultamiento y atribución a un actor estatal |
| Reputacional | Sí | No cuantificable con estos datos |

## Regulación

La plataforma opera en múltiples jurisdicciones y su perímetro regulatorio no se
analiza aquí. Para un lector chileno, la estructura de preguntas es la de
[la guía de crisis financiera digital](../../docs/crisis-financiera-digital.md#5-marco-chileno-e-internacional-aplicable):
prestadores de servicios con activos virtuales, AML/CFT, ciberseguridad,
externalización y continuidad. **Un fondo de emergencia privado (como el SAFU)
no es un seguro de depósitos ni una garantía estatal.**

## Controles

```text
LOS QUE LA INFORMACIÓN PÚBLICA SUGIERE QUE EXISTÍAN
  · congelamiento coordinado con emisores (funcionó parcialmente)
  · reservas propias y fondo de emergencia
  · monitoreo on-chain por terceros

LOS QUE FALLARON O NO CONSTAN
  · ningún control impidió que una estación comprometida
    iniciara movimientos a gran escala
  · no consta un límite de salida por ventana de tiempo
  · no consta segregación efectiva de funciones y de llaves

LOS QUE HABRÍA QUE PREGUNTAR (sin presumir su ausencia)
  · límites de saldo en billeteras calientes
  · aprobación múltiple e independiente por dispositivo y persona
  · tiempo entre la primera transferencia y la pausa
  · prueba reciente del plan de continuidad
```

## Resultado

Al cierre de la verificación, el resultado **no está determinado**. Lo que sí se
puede decir con las propias cifras informadas:

```text
S (sustraído)             ~6 300
F (congelado)             ~3 000     ->  F/S ~ 47,6 %
S − F (sin congelar)      ~3 300     (CNBC cita a un analista: ~3 300)
reserva anunciada          6 340     ->  cubre S en ~100,6 %
respaldo estilizado        100 % -> 95,94 %  (1 − 6 300/155 000)
```

La reserva anunciada *cubre en cifra* la sustracción estimada, y el
congelamiento *podría* devolver parte del activo si el proceso legal lo
permite; pero **ni lo uno ni lo otro es todavía un hecho cumplido**. Un
analista citado por CNBC evaluó que, con los datos disponibles, el caso «no
parece crear un riesgo de solvencia significativo», y señaló que la señal clave
sería *cuán rápido se reanudan los retiros y si las salidas se mantienen
ordenadas*. Otro experto citado indicó que no hay un plazo estándar de
recuperación y que puede llevar meses o años.

## Lecciones

1. **Tres números, tres significados.** Sustraído, congelado y perdido no se
   restan entre sí sin supuestos: la pérdida definitiva depende de `p`.
2. **Una reserva anunciada no es un respaldo demostrado.** Se demuestra con
   activos observables, pasivos completos, mismo corte y alcance declarado.
3. **Un congelamiento depende de quién puede congelar.** Lo que no tiene emisor
   no se congela; la tecnología del activo decide la recuperabilidad.
4. **La liquidez manda en la semana uno; la solvencia, en el mes tres.** El
   orden de las preguntas importa.
5. **Las fuentes discrepan, y eso es información.** Una cifra sin fuente ni fecha
   no se usa; dos cifras que discrepan se muestran las dos.

## Preguntas

1. ¿Qué diferencia hay entre «fondos congelados», «fondos recuperados» y
   «pérdida definitiva»? Construye un ejemplo con `S = 100`, `F = 50`, `p = 0,6`.
2. La reserva anunciada supera la pérdida estimada en ~40 MUSD. ¿Qué cifras
   adicionales necesitarías para afirmar que el respaldo es del 100 %?
3. Los emisores señalados suman 2 370 MUSD y la entidad declara ~3 000. Enumera
   tres explicaciones posibles y qué evidencia distinguiría entre ellas.
4. ¿Reabrirías los retiros de golpe, por tramos o con un tope diario? Justifica
   con la cobertura de retiros `C = A_liq / (r · P)`.
5. Diseña un Proof of Reserves y un Proof of Liabilities que, juntos, hubieran
   permitido a un cliente comprobar el respaldo antes del incidente.

## Fuentes

Consultadas el 2026-10-30. Cifras de prensa, preliminares.

- CNBC (29 y 30 de octubre de 2026): [Binance hack: $6.3 billion stolen, $3 billion frozen](https://www.cnbc.com/2026/10/30/billions-in-crypto-frozen-in-binance-hack-heres-what-happens-next-.html) — lectura directa.
- CoinDesk (30 de octubre de 2026): [Binance arranges $6.34 billion to cover losses from record crypto hack](https://www.coindesk.com/business/2026/10/30/binance-arranges-usd6-34-billion-to-cover-losses-from-record-crypto-hack) — lectura directa.
- Al Jazeera (30 de octubre de 2026): [Binance says $6.3bn stolen in biggest crypto heist in history](https://www.aljazeera.com/economy/2026/10/30/binance-says-2-54bn-in-crypto-funds-frozen-amid-potential-security-issue) — lectura directa.
- The Hacker News (octubre de 2026): [Binance Suffers Security Breach](https://thehackernews.com/2026/10/binance-suffers-security-breach.html) — solo resultado de búsqueda; no usada para cifras.
- Material del programa: [guía de crisis financiera digital](../../docs/crisis-financiera-digital.md), [custodia y conciliación](../../docs/custodia-conciliacion-y-gobernanza.md), [caso FTX/Alameda](ftx-alameda.md), [caso de un puente atacado](../blockchain/ataque-a-un-puente.md) y [pérdida de claves](../blockchain/perdida-de-claves.md).
