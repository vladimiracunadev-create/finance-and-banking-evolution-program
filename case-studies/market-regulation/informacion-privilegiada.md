# Caso · La lista de admisión y el mensaje de las 18:40

**Tema:** regulación de mercados · **Parte relacionada:** 22 · **Naturaleza:**
caso sintético compuesto · **Fecha de verificación:** 2026-08-12

Una plataforma decide admitir a negociación un instrumento. La decisión se toma a
las 17:10 y se publica a las 09:00 del día siguiente. Entre esas dos horas, el
precio del instrumento en otros mercados sube un 14 % con un volumen anómalo. El
caso trata de una información que casi nadie clasifica como privilegiada y lo es.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · decisión de admisión           17:10
  · anuncio público                09:00 D+1
  · personas que conocían la decisión:
      comité de admisión                 6
      equipo técnico de integración      9
      equipo de comunicación             3
      proveedor externo de integración   4
      TOTAL                             22
  · no existía lista de iniciados
  · el precio sube 14 % entre 18:40 y 23:00
  · volumen 6,3 veces el habitual

SUPUESTO DEL EJERCICIO
  · capitalización del instrumento 310 000 000
  · beneficio potencial del movimiento
    para quien comprara                 ~ 4 %
    del volumen anómalo   →      1 740 000
```

Que la información sea privilegiada no depende de que sea sobre el emisor: **la
decisión de un tercero que afectará al precio también lo es.** Una admisión a
negociación es exactamente eso, y por eso la ausencia de lista de iniciados es el
hallazgo central.

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Comité de admisión | Decidir bien | La decisión |
| Equipo técnico | Integrar a tiempo | La decisión, para trabajar |
| Proveedor externo | Cumplir su encargo | La decisión, sin acuerdo específico |
| Inversores del mercado | Precio justo | Nada, hasta las 09:00 |
| Emisor del instrumento | Ser admitido | La decisión |
| Supervisor | Integridad | El patrón, después |

## Decisiones

```text
17:10  se decide admitir
       NO SE ABRE LISTA DE INICIADOS
       RAZÓN: «no somos el emisor»
       ERROR DE CALIFICACIÓN

17:30  se informa al equipo técnico
       para preparar la integración
       DECISIÓN OPERATIVA NECESARIA
       Y NO CONTROLADA

18:00  se contrata al proveedor externo
       sin cláusula específica de
       confidencialidad sobre la operación

18:40  empieza el movimiento de precio

09:00  se publica
       el precio ya había recogido el 14 %
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Información no calificada como privilegiada | Desde el diseño | Sí |
| Círculo de conocedores sin registro | Desde las 17:10 | Sí |
| Tercero sin obligación específica | Desde las 18:00 | Sí |
| Ventana larga entre decisión y anuncio | Desde el procedimiento | Sí |
| Ausencia de vigilancia previa al anuncio | Estructural | Sí |
| Riesgo reputacional de la plataforma | Latente | Sí |

## Regulación

```text
QUÉ ALCANZA

  INFORMACIÓN PRIVILEGIADA
    los regímenes suelen definirla como
    información concreta, no pública, que
    de hacerse pública podría influir de
    manera apreciable en el precio; no
    exige que se refiera al emisor

  LISTA DE INICIADOS
    varios regímenes la exigen de forma
    expresa, con identidad, motivo y fecha
    y hora de acceso

  COMUNICACIÓN ILÍCITA
    revelar la información fuera del
    ejercicio normal del trabajo es
    conducta autónoma, aunque quien la
    reciba no opere

LÍMITE
  la exigencia concreta y su alcance a
  estos instrumentos dependen de la
  jurisdicción
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Política de información privilegiada | Sí | No aplicada a este supuesto | Incluir decisiones propias |
| Lista de iniciados | No | — | Con hora de acceso y motivo |
| Acuerdo específico con terceros | No | — | Por operación, no genérico |
| Reducción de la ventana | No | — | Decidir y anunciar el mismo día |
| Vigilancia previa al anuncio | No | — | Observar el instrumento desde la decisión |
| Formación del personal técnico | Parcial | No | Saber que lo que manejan es sensible |

El cuarto control es el más eficaz y el menos usado: **cuanto más corta es la
ventana entre la decisión y el anuncio, menos vale la información.** Dieciséis
horas es una eternidad; cuarenta minutos, no.

## Resultado

```text
CONSECUENCIAS

  · el precio recogió el 14 % antes del
    anuncio: quien compró en el mercado a
    las 09:05 pagó de más
  · investigación abierta
  · sin lista de iniciados, determinar
    quién tuvo acceso exige reconstruirlo
    a partir de registros técnicos
  · el proveedor externo queda fuera del
    alcance de las políticas internas

COSTE DIRECTO PARA LA PLATAFORMA
  (supuestos)
  investigación y asesoría   240 000
  implantación de controles  180 000
  daño reputacional            no cuantificado

Y LA CIFRA IMPORTANTE
  1 740 000 que se llevó alguien a quien
  quizá no se pueda identificar
```

## Lecciones

1. **La información privilegiada no es solo la del emisor.** Cualquier decisión
   propia que moverá el precio lo es, y se gestiona igual.
2. **Sin lista de iniciados no hay investigación posible**, solo reconstrucción
   parcial a partir de registros técnicos.
3. **Los terceros necesitan acuerdo específico por operación.** Un acuerdo marco
   genérico no acredita que supieran qué manejaban.
4. **La ventana entre decisión y anuncio es el principal control**, y depende solo
   de la organización.

## Preguntas

1. ¿Qué decisiones internas de tu organización serían información privilegiada
   bajo esta definición? Enumera cinco.
2. ¿Cómo se abre y se mantiene una lista de iniciados sin frenar el trabajo?
3. ¿Puede reducirse la ventana a cero? ¿Qué se pierde al anunciar antes de estar
   técnicamente listo?
4. ¿Qué responsabilidad tiene el proveedor externo si no se le advirtió?
5. ¿Qué vigilancia previa al anuncio es proporcionada, y quién la ejecuta?

## Fuentes

- IOSCO. *Investigating and Prosecuting Market Manipulation*. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD103.pdf>
- Diario Oficial de la Unión Europea (2023). *Reglamento (UE) 2023/1114*, título sobre abuso de mercado. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32023R1114>
- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- CMF. *Normativa sobre información privilegiada y deberes de reserva*. <https://www.cmfchile.cl/>
- Verificación local: caso sintético; cifras supuestas. La definición de información privilegiada y la exigencia de lista de iniciados dependen de la jurisdicción. **Fecha de verificación: 2026-08-12.** No constituye asesoría legal.
