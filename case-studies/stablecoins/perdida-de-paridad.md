# Caso · Ochenta y siete céntimos durante nueve horas

**Tema:** stablecoins · **Parte relacionada:** 20 · **Naturaleza:** caso sintético
compuesto · **Fecha de verificación:** 2026-08-12

Una ficha que promete un valor por unidad cotiza a 0,87 durante nueve horas y
recupera la paridad al día siguiente. La reserva estaba completa, el emisor era
solvente y el reembolso funcionaba. Aun así, hubo pérdidas reales de 34 millones,
y este caso explica de dónde salieron.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · fichas en circulación      1 200 000 000
  · reserva                    1 206 000 000
    · 21 % depósitos en un banco
    · 68 % deuda pública corta
    · 11 % repos a un día
  · el banco donde estaba el 21 % anuncia
    un problema de liquidez un viernes
  · el emisor no puede confirmar el estado
    de esos 252 000 000 hasta el lunes
  · el precio en mercado secundario cae a
    0,87 y se mantiene 9 horas
  · reembolso directo del emisor: operativo
    todo el tiempo, con mínimo de 100 000

SUPUESTO DEL EJERCICIO
  · volumen negociado bajo la par 391 000 000
  · pérdida realizada por vendedores 34 000 000
```

El dato que ordena el caso es el mínimo de reembolso. **Quien tenía más de 100 000
podía reembolsar a la par y no perdió nada; quien tenía menos solo podía vender en
mercado, y vendió a 0,87.** La reserva protegió a los grandes y no a los pequeños,
y eso no estaba escrito en ninguna parte visible.

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Tenedor minorista | No perder | El precio en pantalla |
| Tenedor institucional | Reembolsar a la par | El canal directo |
| Emisor | Sostener la paridad | Todo, salvo el estado de los 252 M |
| Banco depositario | Su propia liquidez | Lo suyo |
| Creadores de mercado | Margen | Un riesgo que no podían cubrir |
| Supervisor | Que no haya contagio | Informes con retraso |

## Decisiones

```text
VIERNES 14:00
  el emisor decide no comunicar hasta
  tener certeza
  RAZÓN: evitar alarma
  EFECTO: el mercado supone lo peor

VIERNES 15:20
  creadores de mercado retiran cotizaciones
  DECISIÓN RACIONAL: no pueden valorar
  el riesgo

VIERNES 16:00
  el precio cae a 0,87

VIERNES 18:30
  el emisor publica la composición de la
  reserva y confirma que el reembolso
  sigue abierto
  NO MENCIONA EL MÍNIMO DE 100 000

SÁBADO 01:00
  el precio recupera 0,96

LUNES
  paridad restablecida
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Concentración en un depositario | Desde siempre | Sí |
| Mínimo de reembolso excluyente | Desde el diseño | Sí |
| Opacidad en el momento crítico | Desde la política | Sí |
| Retirada de creadores de mercado | Estructural | Sí |
| Contagio a protocolos que la usaban | Estructural | Parcialmente |
| Riesgo de reputación del emisor | Estructural | Sí |

## Regulación

```text
QUÉ ALCANZA

  RESERVA Y REDENCIÓN
    los regímenes que regulan estas fichas
    exigen composición de reserva con
    límites de concentración y un derecho
    de reembolso; algunos limitan de forma
    expresa las condiciones que pueden
    imponerse a ese derecho

  INFORMACIÓN AL TENEDOR
    la composición de la reserva y las
    condiciones de reembolso son
    información material y deben ser
    accesibles antes del episodio, no
    durante

  ESTABILIDAD FINANCIERA
    una ficha grande deja de ser un
    producto y pasa a ser infraestructura;
    de ahí los umbrales de significatividad

LÍMITE
  el régimen concreto depende de la
  jurisdicción y de la fecha
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Reserva sobrecolateralizada | Sí | Sí, e irrelevante | No era un problema de suficiencia |
| Límite de concentración | No | — | Máximo por depositario |
| Reembolso sin mínimo | No | — | O canal minorista alternativo |
| Publicación diaria de la reserva | No | — | Composición, no solo importe |
| Protocolo de comunicación de crisis | No | — | Publicar en 60 min, aunque sea parcial |
| Prueba de estrés con depositario | No | — | Escenario de banco bloqueado |

## Resultado

```text
QUIÉN PERDIÓ Y QUIÉN NO

  tenedores con ≥ 100 000
    reembolsaron a la par
    pérdida: 0

  tenedores con < 100 000
    solo mercado
    pérdida realizada     34 000 000

  creadores de mercado
    ganancia por diferencial estimada
                           9 000 000

  emisor
    pérdida contable            0
    pérdida de circulante  180 000 000
      en las dos semanas siguientes

LA RESERVA NUNCA ESTUVO EN DUDA.
LO QUE FALLÓ FUE EL ACCESO A ELLA.
```

## Lecciones

1. **Una paridad se sostiene por el acceso al reembolso, no por el tamaño de la
   reserva.** Un mínimo de reembolso convierte una promesa universal en una
   promesa mayorista.
2. **La concentración en un depositario es riesgo de la ficha**, aunque el
   depositario sea solvente: basta con no poder confirmar.
3. **En una crisis de confianza, no comunicar es comunicar.** El silencio se
   interpreta siempre en la peor dirección disponible.
4. **La composición de la reserva debe publicarse antes del episodio**, porque
   durante el episodio nadie cree lo que se publica.

## Preguntas

1. ¿Es legítimo un mínimo de reembolso? ¿Qué justificación operativa tiene y qué
   consecuencia distributiva?
2. ¿Qué límite de concentración por depositario fijarías, y cómo lo defiendes
   frente al coste de fragmentar la reserva?
3. ¿Qué habrías publicado el viernes a las 14:30 con la información incompleta que
   había?
4. ¿Debe un supervisor exigir un canal minorista de reembolso? ¿Quién lo paga?
5. ¿Por qué el emisor pierde 180 millones de circulante si no perdió dinero?

## Fuentes

- Financial Stability Board (2023). *High-level Recommendations for the Regulation, Supervision and Oversight of Global Stablecoin Arrangements*. <https://www.fsb.org/2023/07/high-level-recommendations-for-the-regulation-supervision-and-oversight-of-global-stablecoin-arrangements-final-report/>
- CPMI-IOSCO (2022). *Application of the Principles for Financial Market Infrastructures to stablecoin arrangements*. <https://www.bis.org/cpmi/publ/d206.htm>
- Diario Oficial de la Unión Europea (2023). *Reglamento (UE) 2023/1114*. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32023R1114>
- BIS (2023). *Annual Economic Report*, capítulo sobre el sistema monetario futuro. <https://www.bis.org/publ/arpdf/ar2023e3.htm>
- Verificación local: caso sintético; cifras supuestas. Las exigencias sobre reserva y reembolso dependen de la jurisdicción. **Fecha de verificación: 2026-08-12.** No constituye asesoría de inversión.
