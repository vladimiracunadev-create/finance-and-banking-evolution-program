---
part: 11
class: 16
title: "Comité de riesgos e integración"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 16 · Comité de riesgos e integración

> [← 15 · Riesgos climáticos y emergentes](15-riesgos-climaticos-y-emergentes.md) · [Índice de la parte](../README.md) · [Proyecto de la parte →](../project/README.md)

**Parte 11 — Gestión integral de riesgos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Cerrar la parte convirtiendo quince mediciones separadas en una sola decisión de dirección. Un banco no
tiene un riesgo de crédito y un riesgo de liquidez y un riesgo operacional: tiene **un balance** que los
sufre todos a la vez. Esta clase construye el proceso que integra la medición y produce decisiones.

Esta clase cierra la parte reuniendo los quince riesgos anteriores en un solo gobierno. Y su aportación es la que ninguna clase individual podía dar: los riesgos interactúan, y las crisis reales no son un riesgo grande sino varios medianos que se activan juntos por la misma causa.

## 📚 Objetivos

Al finalizar podrás:

1. **Diseñar** la estructura de gobierno de riesgos de un banco.
2. **Construir** un tablero integrado de riesgos con límites y alertas.
3. **Preparar** y conducir un comité de riesgos efectivo.
4. **Integrar** los riesgos en un escenario único y evaluar sus interacciones.
5. **Vincular** la gestión de riesgos con la remuneración y la cultura.

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

Los tres primeros términos son los órganos de gobierno; los cinco siguientes, sus instrumentos y su cultura. La **interacción de riesgos** es el concepto que justifica la clase: es lo que ninguna medición individual captura y lo que produce las crisis.

| Concepto | Comprensión verificable |
|---|---|
| `comité de riesgos del directorio` | Órgano de gobierno que aprueba el marco y vigila su aplicación. |
| `comité de activos y pasivos` | Gestiona el balance estructural: liquidez, tasas, monedas. |
| `director de riesgos` | Responsable de la segunda línea, con acceso directo al directorio. |
| `tablero de riesgos` | Panel único con métricas, límites, alertas y tendencia. |
| `escalamiento` | Ruta y plazo por los que un exceso llega a quien decide. |
| `interacción de riesgos` | Efecto conjunto mayor que la suma de los efectos separados. |
| `remuneración ajustada por riesgo` | Incentivo que considera cómo se obtuvo el resultado. |
| `declaración de apetito` | Documento que declara y limita el riesgo asumible. |

## 🧠 Modelo mental

El modelo mental es un tablero único: cada riesgo tiene su métrica y su límite, y lo que decide es mirarlos a la vez bajo un mismo escenario. Un banco puede estar dentro de todos sus límites por separado y no sobrevivir al escenario que los activa todos.

```text
UN COMITÉ DE RIESGOS EFECTIVO SE RECONOCE POR UNA SOLA COSA:
LAS DECISIONES QUE TOMA

  comité que revisa informes         → no es un comité, es una audiencia
  comité que aprueba lo propuesto    → no decide, ratifica
  comité que discute y cambia cosas  → gobierna

PRUEBA VERIFICABLE
  ¿cuántas veces en los últimos 12 meses el comité
  rechazó una propuesta o modificó un límite?
  si la respuesta es cero, el comité no está funcionando
```

## 📖 Desarrollo

### 1. Estructura de gobierno

El gobierno del riesgo se reparte entre órganos con composiciones e independencias distintas. La tabla los recoge.

```text
DIRECTORIO
  aprueba el marco, el apetito y la estrategia
  designa al director de riesgos
      │
      ├── COMITÉ DE RIESGOS (del directorio)
      │     revisa el perfil de riesgo, la coherencia con el apetito,
      │     los excesos y las decisiones de límites
      │     mayoría de miembros independientes
      │
      ├── COMITÉ DE AUDITORÍA
      │     eficacia del control interno; recibe a la tercera línea
      │
      └── GERENCIA GENERAL
            ├── COMITÉ DE ACTIVOS Y PASIVOS   balance estructural
            ├── COMITÉ DE CRÉDITO             exposiciones individuales
            ├── COMITÉ DE RIESGO OPERACIONAL  eventos y controles
            └── DIRECTOR DE RIESGOS
                  acceso DIRECTO al comité de riesgos del directorio
                  sin filtro de la gerencia general
```

**El acceso directo del director de riesgos al directorio es estructural, no ceremonial.** Sin él, la
información sobre el riesgo llega al órgano de gobierno filtrada por quienes lo toman.

### 2. Tablero integrado

El tablero reúne las métricas de todos los riesgos con sus límites y su tendencia. La tabla muestra su forma.

| Dimensión | Métrica | Límite | Alerta | Actual | Tendencia |
|---|---|---:|---:|---:|:---:|
| Solvencia | Capital nivel 1 ordinario | 12,0 % | 12,8 % | 13,0 % | ↓ |
| Crédito | Mora > 90 días | 3,5 % | 2,9 % | 2,6 % | ↑ |
| Crédito | Costo de riesgo | 1,8 % | 1,5 % | 1,3 % | ↑ |
| Concentración | Mayor sector correlacionado | 25 % | 22 % | 24,1 % | ↑ |
| Liquidez | Cobertura de liquidez | 110 % | 125 % | 131 % | → |
| Liquidez | Financiamiento estable neto | 105 % | 115 % | 118 % | → |
| Tasa | Caída del valor económico | 15 % cap. | 12 % | 13,4 % | ↑ |
| Mercado | Déficit esperado diario | 0,4 % PE | 0,32 % | 0,29 % | → |
| Moneda | Posición global bruta | 12 % PE | 9 % | 4,2 % | → |
| Operacional | Pérdida anual / ingresos | 0,9 % | 0,7 % | 0,5 % | → |
| Tecnológico | Incidentes críticos | 2/año | 1 | 1 | → |
| Modelo | Modelos fuera de revalidación | 0 | 0 | 2 | ↑ |
| Conducta | Reclamos fundados por 1 000 | 1,2 | 1,0 | 0,8 | ↓ |

```text
REGLAS DE LECTURA
  · el color no lo da el nivel: lo da la TENDENCIA + la distancia a la alerta
  · una métrica dentro de límite con tendencia adversa sostenida
    es más grave que una en alerta con tendencia favorable
  · toda métrica en alerta debe traer su ACCIÓN COMPROMETIDA
  · toda métrica sobre el límite debe traer su PLAN Y PLAZO
```

### 3. Escalamiento

Cuando una métrica se acerca a su límite hay un procedimiento de escalamiento con plazos. La tabla lo recoge.

```text
NIVEL 1  dentro de límites, sin alerta
         → reporte periódico

NIVEL 2  alerta alcanzada
         → notificación al director de riesgos en 2 días
         → acción comprometida en el siguiente comité

NIVEL 3  límite excedido
         → notificación inmediata al director de riesgos y al gerente general
         → informe al comité de riesgos en la sesión más próxima
         → plan de retorno con plazo

NIVEL 4  exceso material o repetido
         → sesión extraordinaria del comité de riesgos
         → informe al directorio y, cuando corresponda, al supervisor
```

**El plazo es parte del control.** Un escalamiento sin plazo definido se convierte en una notificación
que llega cuando ya no puede cambiar nada.

### 4. Integración en un escenario único

Someter todos los riesgos al mismo escenario es lo que revela las interacciones. El procedimiento siguiente lo hace.

```text
LA PRÁCTICA HABITUAL: cada riesgo con su prueba de estrés
LA PRÁCTICA CORRECTA: un escenario, todos los riesgos

  ejemplo de escenario integrado
    recesión + alza de tasas + depreciación + ciberincidente

    crédito       ↑ mora en todos los segmentos
    tasa          ↓ valor económico
    moneda        ↑ riesgo de crédito inducido
    liquidez      ↓ depósitos, ↑ costo de financiamiento
    operacional   ↑ pérdidas por el incidente
    reputacional  ↑ fuga por la conjunción de eventos
    capital       ↓ por resultado y ↑ activos ponderados

  y las INTERACCIONES:
    la mora reduce el margen que absorbería la pérdida
    la fuga de depósitos obliga a vender activos
    la venta materializa la pérdida de valor por tasas
    el ciberincidente ocurre cuando menos capacidad de respuesta hay
```

### 5. Remuneración y cultura

Los incentivos determinan el riesgo que se asume más que cualquier política escrita. La tabla recoge los mecanismos de ajuste.

```text
PRINCIPIOS DE REMUNERACIÓN COHERENTES CON EL RIESGO
  · una porción variable significativa DIFERIDA en el tiempo
  · ajuste ex post: la porción diferida se reduce si el riesgo
    asumido se materializa (malus)
  · recuperación de lo ya pagado en casos graves (clawback)
  · el personal de control NO se remunera por el resultado
    de las áreas que controla
  · métricas de riesgo y de conducta en la evaluación, con peso real
```

```text
LA PRUEBA DE LA CULTURA
  ¿alguna vez se redujo la remuneración variable de alguien
  por CÓMO obtuvo un resultado positivo?

  si nunca ocurrió, el ajuste por riesgo es nominal
```

## 🧮 Ejemplo guiado

El ejemplo somete todos los riesgos de un banco a un escenario único. Conviene mirar qué métricas se activan a la vez: eso es lo que ninguna medición individual mostraba.

**Situación.** El comité de riesgos recibe el tablero del trimestre y debe decidir.

```text
SITUACIÓN DEL TABLERO (ver tabla anterior)

ALERTAS Y EXCESOS
  · concentración sectorial 24,1 % — alerta en 22 %, límite 25 %, tendencia ↑
  · valor económico 13,4 % del capital — alerta en 12 %, límite 15 %, ↑
  · 2 modelos fuera de revalidación — límite 0
  · capital 13,0 %, tendencia ↓ desde 13,8 % hace 4 trimestres

PROPUESTA DE LA GERENCIA COMERCIAL
  crecer 18 % la cartera hipotecaria el próximo año
  argumento: mejor margen que el consumo, menor mora, garantía real
```

**Paso 1 — evalúa la propuesta contra cada límite.**

```text
CONCENTRACIÓN
  la cartera hipotecaria está ligada al sector inmobiliario
  crecimiento de 18 % → concentración sectorial de 24,1 % a 27,3 %
  → EXCEDE el límite de 25 %

VALOR ECONÓMICO
  el hipotecario es el activo de mayor duración (6,4 años)
  crecer 18 % aumenta la brecha de duración
  efecto estimado: caída del valor económico de 13,4 % a 15,8 %
  → EXCEDE el límite de 15 %

CAPITAL
  crecimiento de activos ponderados por el hipotecario:
  890 000 × 18 % × ponderación 45 % = 72 090 de activos ponderados
  capital: 296 400 / (2 280 000 + 72 090) = 12,60 %
  → dentro del límite de 12,0 %, pero rompe la alerta de 12,8 %

LIQUIDEZ
  crédito a 20 años financiado con la estructura actual
  financiamiento estable requerido: +72 090 × 65 % = +46 859
  NSFR: de 118 % a 113 % → rompe la alerta de 115 %
```

**Paso 2 — resume: la propuesta rompe cuatro límites o alertas.**

```text
concentración sectorial   EXCEDE límite
valor económico           EXCEDE límite
capital                   rompe alerta
financiamiento estable    rompe alerta

y ninguna de estas cuatro consecuencias
estaba en la presentación de la gerencia comercial,
que mostraba margen, mora y garantía
```

**Paso 3 — evalúa las interacciones, no solo los límites.**

```text
las cuatro consecuencias NO son independientes:

  más hipotecario → más concentración inmobiliaria
                  → más duración → peor valor económico
                  → más financiamiento estable requerido
                  → más capital

y en un escenario adverso se refuerzan:
  caída de precios inmobiliarios
    → sube la LGD del segmento concentrado
    → sube el costo de riesgo
    → cae el resultado, cae el capital
    → y el valor económico ya estaba deteriorado por tasas
```

**Paso 4 — construye la alternativa.**

```text
¿cuánto puede crecer el hipotecario sin romper nada?

restricción activa: concentración sectorial (límite 25 %)
  actual 24,1 % sobre cartera total de 2 940 000 → 708 540
  máximo al 25 %: 735 000
  espacio: 26 460 → crecimiento máximo de 3,0 % en hipotecario

verificación de las otras restricciones con ese crecimiento:
  valor económico: 13,4 % → 13,8 %  ✓ (alerta 12 %, ya superada)
  capital: 12,60 % → 12,93 %  ✓
  NSFR: 118 % → 117 %  ✓

CRECIMIENTO VIABLE: 3,0 %, no 18 %
```

**Paso 5 — busca la alternativa que sí permite crecer.**

```text
si el objetivo es crecer con buen margen y baja mora,
¿qué otro camino existe?

OPCIÓN A — hipotecario con venta de cartera
  originar 18 % y vender el 15 % a un tercero
  · el banco conserva la relación con el cliente y la comisión
  · no consume concentración, capital ni financiamiento estable
  · margen menor, pero retorno sobre capital mayor

OPCIÓN B — hipotecario a tasa variable o con repactación
  reduce la duración de 6,4 a 2,1 años
  · efecto en valor económico: 13,4 % → 13,6 % con 18 % de crecimiento
  · no resuelve la concentración sectorial

OPCIÓN C — crecer en servicios y pagos
  RAROC 33,9 % (clase 14), consumo de capital mínimo
  · no consume ninguno de los límites en tensión
  · la restricción es capacidad operativa
```

**Paso 6 — decide y documenta.**

```text
DECISIÓN DEL COMITÉ

1. Rechazar la propuesta de crecimiento de 18 % en hipotecario.

2. Autorizar crecimiento de 3,0 % en hipotecario propio,
   más originación con venta de cartera hasta 15 % adicional,
   sujeta a acuerdo firmado con el comprador ANTES de originar.

3. Exigir que toda propuesta de crecimiento incluya
   su efecto sobre las trece métricas del tablero.
   Ninguna propuesta se presenta sin esa sección.

4. Modelos fuera de revalidación: plazo de 60 días.
   Si al vencimiento siguen fuera, suspensión de su uso.

5. Valor económico en 13,4 % con tendencia al alza:
   instruir al comité de activos y pasivos ejecutar
   la cobertura con swaps evaluada en la clase 5.

6. Capital con tendencia descendente cuatro trimestres seguidos:
   solicitar al gerente general el plan de capital a tres años
   para la próxima sesión, con la prueba de estrés actualizada.

7. Redirigir el objetivo de crecimiento a servicios y pagos:
   solicitar a la gerencia comercial el plan de capacidad
   operativa de esa unidad.
```

**Paso 7 — evalúa el propio comité.**

```text
INDICADORES DE FUNCIONAMIENTO DEL COMITÉ
  · propuestas rechazadas o modificadas en 12 meses: 4 de 19  ✓
  · tiempo medio entre exceso y decisión: 11 días  ✓
  · asistencia de miembros independientes: 94 %  ✓
  · sesiones con el director de riesgos sin la gerencia: 2 de 12  ✗
    → debería ser al menos 4 (una por trimestre)
  · hallazgos de auditoría sobre el marco sin cerrar: 3
    → antigüedad media 8 meses  ✗
```

**Interpreta:** la propuesta comercial no era mala: **estaba incompleta**. Mostraba tres variables
favorables y omitía cuatro restricciones que ella misma activaba. La decisión del comité no fue decir
que no, sino **cambiar el formato de toda propuesta futura** para que llegue con su efecto sobre el
tablero completo. Esa es la función de un comité de riesgos: no vigilar los números, sino **cambiar la
forma en que la organización decide**.

## 🏦 Del cliente al banco

El cliente ve un banco y el directorio ve un tablero con quince riesgos que interactúan. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «El banco dejó de dar hipotecarios» | Límite de concentración alcanzado | 11, clase 16 |
| «Me ofrecen el crédito y otro banco lo compra» | Originación con venta de cartera | 10, clase 3 |
| «Mi banco es prudente y crece poco» | Apetito de riesgo explícito | 11, clase 1 |
| «Cambiaron las condiciones a mitad de año» | Decisión de comité por tendencia adversa | 11, clase 16 |
| «Al ejecutivo le importaba solo vender» | Remuneración no ajustada por riesgo | 12, clase 8 |

## 🧪 Práctica

El laboratorio pide construir el tablero integrado y someterlo a un escenario. El banco cumple todos los límites por separado y falla en el escenario conjunto.

En `labs/lab-06.md`, sección de integración:

1. Construye el tablero integrado de un banco sintético con límites y alertas.
2. Define la matriz de escalamiento con niveles, destinatarios y plazos.
3. Evalúa una propuesta de crecimiento contra todas las métricas del tablero.
4. Diseña un escenario integrado y traza las interacciones entre riesgos.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen crisis en bancos que cumplían sus límites. La causa es la interacción de riesgos no evaluada.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El comité nunca rechaza nada | Es una audiencia | Mide propuestas modificadas o rechazadas. |
| Las propuestas muestran solo lo favorable | Formato incompleto | Exige efecto sobre todo el tablero. |
| Cada riesgo se estresa por separado | Sin integración | Un escenario, todos los riesgos. |
| El director de riesgos reporta al negocio | Sin independencia | Acceso directo al directorio. |
| Escalamiento sin plazo | Llega tarde | El plazo es parte del control. |
| La remuneración variable nunca se ajustó | Cultura nominal | Aplica malus cuando corresponda. |

## ❓ Preguntas de comprobación

1. ¿Cuál es la prueba verificable de que un comité de riesgos funciona?
2. ¿Por qué el acceso directo del director de riesgos al directorio es estructural?
3. ¿Por qué una métrica dentro de límite puede ser más grave que una en alerta?
4. ¿Qué se pierde al estresar cada riesgo por separado?
5. ¿Cómo se comprueba que el ajuste por riesgo de la remuneración es real?

## 📥 Entregable

Guarda en `portfolio/parte-11/clase-16/`:

- el tablero integrado con métricas, límites, alertas y tendencia;
- la matriz de escalamiento con destinatarios y plazos;
- la evaluación de una propuesta contra todo el tablero, con la decisión y su fundamento;
- el escenario integrado con las interacciones entre riesgos trazadas.

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

- Basel Committee on Banking Supervision (2015). *Corporate governance principles for banks*. BIS. <https://www.bis.org/bcbs/publ/d328.htm>
- Financial Stability Board (2013). *Principles for an Effective Risk Appetite Framework*. FSB. <https://www.fsb.org/2013/11/r_131118/>
- Financial Stability Board (2009). *Principles for Sound Compensation Practices* y sus estándares de implementación. FSB.
- Financial Stability Board (2014). *Guidance on Supervisory Interaction with Financial Institutions on Risk Culture*. FSB.
- Institute of Internal Auditors (2020). *The IIA's Three Lines Model*. IIA.
- Verificación local: revisa las exigencias de composición del comité de riesgos, independencia del director de riesgos y política de remuneraciones de tu supervisor.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 15 · Riesgos climáticos y emergentes](15-riesgos-climaticos-y-emergentes.md) | [Parte 11](../README.md) · [Programa](../../../SYLLABUS.md) | [Proyecto de la parte →](../project/README.md) |
<!-- gen:footer:end -->
