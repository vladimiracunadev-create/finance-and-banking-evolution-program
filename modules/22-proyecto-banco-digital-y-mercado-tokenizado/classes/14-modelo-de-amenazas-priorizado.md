<!-- meta
part: 23
class: 14
title: "Modelo de amenazas priorizado"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [seguridad, riesgo-operativo, controles]
regulation_last_verified: 2026-08-19
regulatory_status: vigente
primary_authorities: [NIST, BCBS, FSB]
requires_legal_review: false
-->

<!-- gen:header:start -->
# Clase 14 · Modelo de amenazas priorizado

> [← 13 · Expediente regulatorio del sistema](13-expediente-regulatorio-del-sistema.md) · [Índice de la parte](../README.md) · [15 · Escenario de tensión y continuidad →](15-escenario-de-tension-y-continuidad.md)

**Parte 23 — Proyecto — banco digital y mercado tokenizado** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Enumerar las amenazas del sistema construido, **priorizarlas por efecto sobre el
cliente** y asociar a cada control una prueba que demuestre que funciona.

La clase 13 encontró lo que el sistema afirma y no puede sostener. Esta busca lo
que un atacante haría, que es un ejercicio distinto: no mira las
contradicciones, mira las oportunidades.

## 📚 Objetivos

Al finalizar podrás:

1. **Enumerar** las amenazas por componente y por actor.
2. **Priorizar** por probabilidad y efecto, no por sofisticación.
3. **Asociar** una prueba ejecutable a cada control.
4. **Identificar** las amenazas sin control y declararlas como riesgo residual.
5. **Diseñar** el escenario del atacante racional.

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

Los cuatro primeros términos son la amenaza y su control; los cuatro siguientes, el criterio de priorización y el riesgo que queda. El **atacante racional** es el criterio que reordena las prioridades: no se protege lo más sofisticado sino donde hay más valor detrás del control más débil.

| Concepto | Comprensión verificable |
|---|---|
| `amenaza` | Lo que alguien podría intentar |
| `vector` | Por dónde entraría |
| `control` | Lo que lo impide o lo detecta |
| `prueba de control` | Ejecución que demuestra que funciona |
| `riesgo residual` | Amenaza sin control, declarada |
| `atacante racional` | El que compara coste y beneficio |
| `amenaza interna` | La que viene de dentro |
| `efecto sobre el cliente` | Qué pierde él, no la entidad |

## 🧠 Modelo mental

Un modelo de amenazas se llena de escenarios sofisticados y se olvida de los
tres que ocurren de verdad: una sesión comprometida, un empleado con demasiados
permisos y un proveedor que falla. La priorización corrige eso.

```text
EL ATACANTE RACIONAL

  compara lo que gana con lo que le cuesta

  · valor acumulado en el objetivo
  · coste de comprometer el control
  · probabilidad de ser detectado

Y ELIGE EL PUNTO MÁS BARATO,
que casi nunca es el más sofisticado

POR ESO LA PREGUNTA ÚTIL ES
  «¿dónde está el mayor valor detrás
   del control más débil?»
```

## 📖 Desarrollo

### 1. Amenazas por componente

El inventario se hace por componente y por actor, y se cruza. Un componente sin
amenazas identificadas suele significar que nadie lo miró, no que sea seguro.

```text
POR COMPONENTE
  registro · claves · interfaces · pagos
  · colateral · liquidación

POR ACTOR
  externo · cliente · empleado · proveedor
  · autoridad

Y EL CRUCE PRODUCE LA MATRIZ
  cada celda con al menos una amenaza
  o con la razón de por qué no la hay
```

### 2. Una prueba por control

Un control descrito y no probado es una intención. La prueba no tiene que ser
compleja: tiene que ejecutarse y fallar cuando el control falla.

```text
EJEMPLOS

  lista blanca con espera
    → prueba: intentar retirar a destino
      nuevo y comprobar el rechazo

  verificación de aprovisionamiento
    → prueba: pagar con fondos insuficientes
      y comprobar que no paga a nadie

  congelación simultánea
    → prueba: congelar y comprobar que
      ambos registros rechazan
```

### 3. El riesgo residual se declara

Hay amenazas sin control razonable. Declararlas es lo que distingue un modelo
honesto de uno tranquilizador, y es lo que un supervisor busca primero.

```text
CÓMO SE DECLARA

  · la amenaza y su efecto
  · por qué no hay control proporcionado
  · qué la detectaría a posteriori
  · qué se haría si ocurriera
  · y quién aceptó el riesgo, con fecha

LA ÚLTIMA LÍNEA ES LA QUE CONVIERTE
UN RIESGO EN UNA DECISIÓN
```

## 🧮 Ejemplo guiado

El ejemplo prioriza las amenazas del sistema con el criterio racional. El orden que sale no es el que sugiere la sofisticación técnica.

**Situación.** El equipo construye la matriz y encuentra que el punto más barato
para un atacante no es el más protegido.

```text
VALOR ACUMULADO POR COMPONENTE
  colateral custodiado         24 000 000
  saldo de liquidación            144 000
  saldos de clientes           91 200 000
  claves del registro          controla todo
```

**Paso 1 — cruza componentes y actores.**

```text
AMENAZAS DESTACADAS

  externo   × interfaces   sesión comprometida
  cliente   × colateral    valoración manipulada
  empleado  × claves       exceso de permisos
  proveedor × custodio     disposición indebida
  externo   × pagos        destino sustituido

  CINCO CON VALOR ALTO DETRÁS
```

**Paso 2 — aplica el criterio del atacante racional.**

```text
¿DÓNDE ESTÁ EL MAYOR VALOR DETRÁS
DEL CONTROL MÁS DÉBIL?

  claves del registro
    valor: controla todo
    control: 3-de-5 con independencia 4
    → caro de comprometer

  saldos de clientes
    valor: 91 200 000
    control: autenticación del cliente
    → el más barato por unidad de valor

  → EL PUNTO ES LA AUTENTICACIÓN,
    no la criptografía del registro
```

**Paso 3 — asocia pruebas a los controles.**

```text
autenticación reforzada
  prueba: intento con credencial válida y
  segundo factor ausente → rechazo

lista blanca con espera
  prueba: alta de destino y retirada
  inmediata → rechazo y 48 h de margen

verificación de aprovisionamiento
  prueba: pago con fondos insuficientes
  → no paga a nadie

congelación simultánea
  prueba: congelar y operar en ambos
  registros → rechazo en los dos

CUATRO PRUEBAS EJECUTABLES
```

**Paso 4 — declara el riesgo residual.**

```text
AMENAZA SIN CONTROL PROPORCIONADO

  coacción sobre un guardián que además
  conoce la composición del esquema

  · no hay control que lo impida
  · la señal de coacción lo detecta si se
    usa, y depende de una persona bajo
    presión
  · se detectaría a posteriori por el
    registro inmutable
  · si ocurriera: congelación inmediata y
    denuncia

  ACEPTADO POR la dirección, con fecha

Y SE MITIGA PARCIALMENTE
  no publicando la composición y rotándola
```

**Interpreta:** El punto más barato para un atacante no era la criptografía del registro sino
**la autenticación del cliente**, que protege un valor cuatro veces mayor con un
control mucho más débil. Priorizar por sofisticación habría llevado a reforzar lo
que ya estaba bien.

## 🧭 Perspectivas

Las amenazas afectan a cada actor de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Una autenticación más estricta | Si la acepta |
| Equipo | Cinco amenazas destacadas | Qué controla primero |
| Seguridad | El punto más barato | Dónde invierte |
| Empleado | Permisos revisados | — |
| Proveedor | Controles sobre su acceso | Qué acepta |
| Dirección | Un riesgo residual | Si lo acepta con fecha |
| Supervisor | Una prueba por control | Qué verifica |
| Auditor | Riesgo residual declarado | Qué observa |

## 🏦 Del cliente al banco

El cliente confía en el sistema y el sistema se defiende donde el atacante atacaría. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Usan criptografía fuerte» | Y el punto débil es la autenticación | 23, clase 14 |
| «Está todo controlado» | Hay un riesgo residual declarado | 23, clase 14 |
| «Nunca ha pasado» | La prueba demuestra que el control funciona | 23, clase 14 |

## ⚖️ Riesgos y controles

Los riesgos son de priorización equivocada y de controles sin prueba. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Priorizar por sofisticación | Los escenarios complejos atraen | Prioriza por valor sobre control |
| Control sin prueba | Está descrito | Es una intención |
| Componente sin amenazas | Parece seguro | Suele significar que nadie lo miró |
| Riesgo residual no declarado | Incomoda | Es lo que da credibilidad |
| Olvidar la amenaza interna | Se piensa en el atacante externo | El empleado tiene acceso |
| Aceptar el riesgo sin firma | Queda en el aire | Con nombre y fecha |

## 🧪 Práctica

El laboratorio pide construir la matriz de amenazas y asociar una prueba a cada control. Los controles sin prueba son lo que se busca.

En [`labs/lab-07.md`](../labs/lab-07.md):

1. Construye la matriz de componentes por actores.
2. Aplica el criterio del atacante racional y ordena.
3. Asocia una prueba ejecutable a cada control.
4. Declara el riesgo residual con sus cinco elementos.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen sistemas atacados por el punto más barato. La causa es haber priorizado por sofisticación.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Empezar por los escenarios complejos | Son los interesantes | Los tres habituales ocurren más |
| Describir controles | Es lo rápido | Sin prueba no está |
| Dejar celdas vacías | No se encontró nada | Escribe por qué no la hay |
| Ocultar el residual | Da mala imagen | Es lo que se busca primero |
| Solo amenazas externas | Es el modelo mental | La interna tiene acceso |
| Aceptación sin firma | Se asume | Con nombre y fecha |

## ❓ Preguntas de comprobación

1. ¿Qué compara un atacante racional y qué pregunta se deriva?
2. ¿Cómo se construye la matriz de amenazas?
3. ¿Qué convierte a un control descrito en un control real?
4. ¿Qué cinco elementos tiene un riesgo residual declarado?
5. En el ejemplo, ¿por qué el punto más barato no era el registro?

## 📥 Entregable

Guarda en `portfolio/parte-23/clase-14/`:

- la matriz de componentes por actores;
- la priorización por valor sobre control;
- una prueba ejecutable por cada control;
- el riesgo residual declarado y aceptado.

## 🔗 Referencias cruzadas

- **Viene de:** clases 9 y 13; Parte 19, clase 8.
- **Continúa en:** clase 15 de esta parte.
- **Se aplica en:** clases 16 y 18 de esta parte.

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

- NIST (2016). *SP 800-57 Part 1: Recommendation for Key Management*. NIST. Amenazas sobre la clave y controles de su ciclo de vida. <https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final>
- NIST (2020). *SP 800-207: Zero Trust Architecture*. NIST. Segmentación y verificación continua como control transversal. <https://csrc.nist.gov/pubs/sp/800/207/final>
- Basel Committee on Banking Supervision (2021). *Principles for Operational Resilience*. BIS. Priorización de amenazas por efecto sobre el servicio crítico. <https://www.bis.org/bcbs/publ/d516.htm>
- Financial Stability Board (2020). *Effective Practices for Cyber Incident Response and Recovery*. FSB. Preparación de la respuesta a la amenaza materializada. <https://www.fsb.org/2020/10/effective-practices-for-cyber-incident-response-and-recovery-final-report/>
- Verificación local: comprueba en la fuente oficial vigente qué exige tu jurisdicción sobre este punto. **Fecha de verificación de esta clase: 2026-08-19.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 13 · Expediente regulatorio del sistema](13-expediente-regulatorio-del-sistema.md) | [Parte 23](../README.md) · [Programa](../../../SYLLABUS.md) | [15 · Escenario de tensión y continuidad →](15-escenario-de-tension-y-continuidad.md) |
<!-- gen:footer:end -->
