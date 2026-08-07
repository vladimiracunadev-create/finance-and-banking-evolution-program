---
part: 17
class: 12
title: "Privacidad, finalidad, minimización y portabilidad"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global, chile, union-europea]
regulatory_topics: [open-finance, proteccion-de-datos, etica]
regulation_last_verified: 2026-08-06
regulatory_status: en-implantacion
primary_authorities: [CMF]
requires_legal_review: true
---

<!-- gen:header:start -->
# Clase 12 · Privacidad, finalidad, minimización y portabilidad

> [← 11 · Autenticación reforzada, fraude y responsabilidad](11-autenticacion-reforzada-fraude-y-responsabilidad.md) · [Índice de la parte](../README.md) · [13 · Disponibilidad, SLA, observabilidad e incidentes →](13-disponibilidad-sla-y-observabilidad.md)

**Parte 17 — Finanzas abiertas, APIs y economía de datos** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Separar dos regímenes que conviven sobre el mismo dato: el de finanzas abiertas
—que autoriza a compartir— y el de protección de datos personales —que limita a
tratar—. Cumplir uno no exime del otro, y la mayoría de los problemas nacen de
haber leído solo uno.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** base de licitud, finalidad y consentimiento, que no son lo mismo.
2. **Aplicar** minimización y limitación de la finalidad a un caso concreto.
3. **Diseñar** una política de retención por finalidad, no por comodidad.
4. **Evaluar** el derecho de portabilidad y sus límites reales.
5. **Detectar** un tratamiento que es técnicamente posible, jurídicamente dudoso y
   éticamente indefendible, y argumentar la diferencia.

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

Los cuatro primeros términos son la base del tratamiento y sus límites; los cuatro siguientes, la retención y los derechos. La **limitación de finalidad** es la restricción que más se incumple sin querer: un dato obtenido para una finalidad no se puede usar para otra sin una base nueva.

| Concepto | Comprensión verificable |
|---|---|
| `base de licitud` | Fundamento jurídico que habilita un tratamiento |
| `finalidad` | Para qué se trata el dato; debe ser determinada y previa |
| `minimización` | Solo el dato necesario para esa finalidad |
| `limitación de finalidad` | No usarlo para otra cosa sin nueva base |
| `retención` | Cuánto tiempo se conserva y por qué |
| `portabilidad` | Derecho a recibir o trasladar los datos propios |
| `tratamiento ulterior` | Uso posterior distinto del original |
| `evaluación de impacto` | Análisis previo cuando el tratamiento es de alto riesgo |

## 🧠 Modelo mental

El modelo mental es un dato con una etiqueta pegada: la finalidad para la que se obtuvo. Esa etiqueta viaja con el dato y limita todo lo que se puede hacer con él después, incluido el entrenamiento de modelos.

```text
DOS PERMISOS DISTINTOS SOBRE EL MISMO DATO

  RÉGIMEN DE FINANZAS ABIERTAS
    responde: ¿puedo ACCEDER a este dato?
    lo habilita: el consentimiento del cliente
                 y la obligación de la institución

  RÉGIMEN DE PROTECCIÓN DE DATOS
    responde: ¿puedo TRATAR este dato, para qué,
              cuánto tiempo y con qué garantías?
    lo habilita: una base de licitud

TENER ACCESO NO ES TENER PERMISO DE USO
  la pregunta «¿puedo bajarlo?» y la pregunta
  «¿puedo entrenarlo, cederlo, cruzarlo o conservarlo?»
  se responden en cuerpos normativos distintos
```

## 📖 Desarrollo

### 1. Base de licitud, finalidad y consentimiento

```text
NO SON SINÓNIMOS

  BASE DE LICITUD    por qué está permitido tratar
                     (consentimiento, contrato, obligación legal,
                      interés legítimo, según la norma aplicable)

  FINALIDAD          para qué se trata
                     («categorizar gastos», no «mejorar el servicio»)

  CONSENTIMIENTO     UNA de las bases posibles

CONSECUENCIA PRÁCTICA
  · un tratamiento necesario para ejecutar el contrato
    no siempre necesita consentimiento
  · un consentimiento no convierte en lícita
    una finalidad indeterminada
  · «mejorar el servicio» no es una finalidad:
    no permite saber qué queda dentro y qué fuera
```

### 2. Minimización con criterio operativo

```text
LA PRUEBA DE LA MINIMIZACIÓN

  para cada campo, responde:
    «si elimino este campo, ¿qué función deja de funcionar?»

  si la respuesta es
    «ninguna, pero podríamos usarlo después»  → sobra
    «el modelo pierde 0,3 puntos de precisión» → argumentable,
      hay que comparar el beneficio con el riesgo
    «el producto no funciona»                  → necesario

MINIMIZACIÓN NO ES SOLO «MENOS CAMPOS»
  también es:
    · menor granularidad   (mes en vez de día, si basta)
    · menor precisión      (rango en vez de importe exacto)
    · agregación           (total en vez de movimientos)
    · seudonimización      (identificador en vez de nombre)
```

### 3. Limitación de la finalidad y tratamiento ulterior

```text
EL CASO TÍPICO
  se obtuvieron los movimientos para categorizar gastos.
  Un año después, el equipo de riesgo quiere usarlos
  para entrenar un modelo de scoring.

  ¿ES EL MISMO TRATAMIENTO? NO.
  ¿ES COMPATIBLE? Hay que analizarlo, no asumirlo.

CRITERIOS DE COMPATIBILIDAD
  1. relación entre la finalidad original y la nueva
  2. contexto en que se obtuvo el dato y expectativa
     razonable del cliente
  3. naturaleza del dato (¿hay categorías protegidas?)
  4. consecuencias posibles para la persona
  5. garantías aplicadas (seudonimización, agregación)

EL CRITERIO 4 ES EL DECISIVO EN FINANZAS
  un modelo de scoring produce una DECISIÓN sobre la persona:
  la consecuencia es material, no estadística
```

### 4. Retención por finalidad

```text
UNA POLÍTICA DE RETENCIÓN TIENE UNA FILA POR FINALIDAD,
NO UNA CIFRA GLOBAL

  finalidad                  dato              plazo   fundamento
  ─────────────────────────────────────────────────────────────────
  categorizar gastos         movimientos       13 m    función del producto
  detectar fraude            metadatos         24 m    interés legítimo
  atender reclamos           evidencia         según norma  obligación legal
  cumplimiento LA/FT         registros         según norma  obligación legal
  mejorar el modelo          agregados         indefinido  sin dato personal

REGLAS
  · el plazo más largo no se aplica a todo el conjunto:
    se aplica al dato que lo requiere
  · vencido el plazo: eliminación o anonimización efectiva
  · «anonimizado» significa NO REVERSIBLE.
    Si se puede reidentificar, sigue siendo dato personal.
```

### 5. Portabilidad y sus límites

```text
QUÉ PERMITE
  recibir los datos propios en formato estructurado
  y de uso común, y en algunos regímenes,
  que se transmitan directamente a otro proveedor

QUÉ NO PERMITE
  · llevarse datos inferidos o derivados que sean
    propiedad intelectual del proveedor
  · llevarse datos de terceros contenidos en los propios
  · exigir un formato concreto si la norma solo exige
    «estructurado y de uso común»

LA TENSIÓN REAL
  el histórico de movimientos contiene datos de contrapartes.
  Portarlo entero porta datos de personas que no lo pidieron.
  → se porta con los campos de tercero enmascarados
```

### 6. Los tres planos que no hay que confundir

```text
TÉCNICAMENTE POSIBLE      ¿se puede construir?
JURÍDICAMENTE VÁLIDO      ¿la norma lo permite?
ÉTICAMENTE DEFENDIBLE     ¿lo defenderías ante quien lo sufre?

LOS TRES SON INDEPENDIENTES
  posible + válido + indefendible   → existe y es frecuente
  posible + inválido + defendible   → hay que cambiar la norma
                                       o no hacerlo
  imposible                          → la discusión no llega

LA PREGUNTA QUE ORDENA EL TERCER PLANO
  «si el cliente supiera exactamente esto,
   ¿seguiría usando el producto?»
  si la respuesta honesta es no,
  el problema no es de comunicación
```

## 🧮 Ejemplo guiado

El ejemplo evalúa si un tratamiento ulterior está cubierto por la finalidad original. Conviene aplicar el criterio de compatibilidad: en dos de los tres casos no lo está.

**Situación.** El equipo de datos propone tres usos nuevos de los movimientos ya
obtenidos para categorizar gastos.

```text
USO 1 · entrenar un modelo de scoring crediticio propio
USO 2 · vender informes agregados de gasto por comuna
        a cadenas de retail
USO 3 · detectar embarazo por patrón de compras
        y ofrecer un crédito de consumo
```

**Paso 1 — evalúa el USO 1 con los cinco criterios.**

```text
1. RELACIÓN CON LA FINALIDAD ORIGINAL
   categorizar gastos → scoring: ambas son «entender
   las finanzas del cliente», pero una informa y la otra decide
   → relación débil

2. EXPECTATIVA RAZONABLE
   ¿el cliente esperaba que su categorización
   alimentara una decisión de crédito? No.
   → expectativa no cumplida

3. NATURALEZA DEL DATO
   movimientos: pueden contener inferencias sensibles (clase 4)
   → riesgo alto

4. CONSECUENCIAS
   una decisión de crédito adversa es material
   → consecuencia alta

5. GARANTÍAS
   ¿se puede hacer con datos agregados? No: el scoring
   necesita el individuo
   → sin garantía mitigadora

CONCLUSIÓN: no es tratamiento compatible.
Requiere base propia y, si es consentimiento,
uno nuevo, específico e informado.
```

**Paso 2 — evalúa el USO 2.**

```text
INFORMES AGREGADOS POR COMUNA

  ¿HAY DATO PERSONAL EN EL RESULTADO? Depende de la agregación.

  PRUEBA DE REIDENTIFICACIÓN
    comuna con 340 clientes en la muestra
    corte por comuna + rango etario + categoría de gasto
    → celdas de 2 y 3 personas

    con celdas de 2, quien conozca a una persona
    de la celda deduce el gasto de la otra

  CORRECCIÓN
    · umbral mínimo de celda: 50 clientes
    · supresión de celdas por debajo del umbral
    · ruido calibrado si se publica repetidamente
      (dos publicaciones sin ruido permiten diferencias)

  CON ESAS TRES CORRECCIONES
    el resultado deja de ser dato personal
    → el tratamiento pasa a ser viable
```

**Paso 3 — cuantifica el USO 2 corregido.**

```text
INGRESO ESTIMADO           68 000 000 al año
COSTE DE IMPLEMENTAR
  umbral y supresión         6 000 000
  ruido calibrado            9 000 000
  revisión y auditoría       7 000 000 al año
  RESULTADO                 46 000 000 el primer año

RIESGO RESIDUAL
  si el umbral se relaja «solo para un cliente grande»,
  la reidentificación vuelve
  → la decisión debe fijar el umbral en el sistema,
    no en el procedimiento
```

**Paso 4 — evalúa el USO 3 en el plano técnico.**

```text
¿ES POSIBLE? Sí, y es conocido:
cambios de patrón de compra permiten inferir embarazo
con precisión útil.

¿ES PRECISO? El ejercicio supone 78 % de precisión.
  de 10 000 detecciones: 7 800 aciertos, 2 200 errores
```

**Paso 5 — evalúa el USO 3 en el plano jurídico.**

```text
EL DATO INFERIDO ES UN DATO DE SALUD

  · categoría especialmente protegida en la mayoría
    de los regímenes
  · la base de licitud es mucho más estrecha
  · un consentimiento «para categorizar gastos»
    no lo cubre en ningún caso
  · exigiría, como mínimo, consentimiento explícito
    y específico para inferir y usar esa condición

CONCLUSIÓN JURÍDICA: no con la base actual.
Y con base propia, sigue siendo un tratamiento
de alto riesgo que exige evaluación de impacto previa.
```

**Paso 6 — evalúa el USO 3 en el plano ético.**

```text
SUPÓN QUE SE OBTIENE LA BASE JURÍDICA PERFECTA.
¿HAY QUE HACERLO?

  QUIÉN GANA        la empresa, por conversión
  QUIÉN PIERDE      · las 2 200 personas mal clasificadas
                    · quien no ha comunicado su embarazo
                    · quien tuvo una pérdida gestacional
                      y recibe publicidad de bebé

  LA PRUEBA
    «si el cliente supiera que deducimos su embarazo
     de sus compras y por eso le ofrecemos crédito,
     ¿seguiría usando el producto?»

  y una segunda, más dura
    «¿defenderías esto ante la persona que perdió
     un embarazo y siguió recibiendo la oferta?»

CONCLUSIÓN: no.
Y la razón NO es que sea ilegal. Es que sigue siendo
indefendible aunque se legalice.
```

**Paso 7 — formula las tres decisiones.**

```text
USO 1 · RECHAZADO con la base actual.
        Si el negocio lo quiere: consentimiento nuevo,
        específico, con explicación de la consecuencia,
        y evaluación de impacto previa.

USO 2 · APROBADO con umbral de celda 50, supresión
        automática y ruido calibrado, fijados en el sistema.
        Revisión anual de reidentificación.

USO 3 · RECHAZADO en los tres planos.
        Se documenta el rechazo y su motivo, para que
        la próxima propuesta no repita el análisis.

Y UNA REGLA GENERAL QUE SALE DEL EJERCICIO
  todo uso nuevo de un dato ya obtenido pasa por
  los cinco criterios de compatibilidad ANTES de
  entrar en el plan de producto, no después.
```

**Interpreta:** los tres usos eran técnicamente viables. Uno se aprobó cambiando
el diseño, otro exige empezar de nuevo el permiso, y el tercero se rechazó por un
motivo que no está en ninguna norma. Los tres planos dieron respuestas distintas
sobre el mismo dato.

## 🧭 Perspectivas

La privacidad afecta a cada actor con obligaciones distintas. La tabla las recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Una oferta que le inquieta | Si sigue usando el producto |
| Fintech | Un dato ya disponible | Si lo usa para algo nuevo |
| Banco | Riesgo reputacional | Qué autoriza a sus áreas |
| Supervisor | Tratamiento de alto riesgo | Si exige evaluación de impacto |
| Autoridad de datos | Base de licitud del uso ulterior | Si sanciona |
| Auditor | Política de retención | Si se ejecuta o solo existe |
| Sociedad | Inferencia sobre la vida privada | Presión normativa |

## 🏦 Del cliente al banco

El cliente comparte para una cosa y el dato puede usarse para otra. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «¿Cómo saben eso de mí?» | Dato inferido, no declarado | 17, clase 12 |
| «Autoricé ver, no analizar» | Acceso ≠ base de tratamiento | 17, clase 12 |
| «Quiero llevarme mis datos» | Portabilidad con terceros enmascarados | 17, clase 12 |
| «Borren todo lo mío» | Retención por finalidad, con obligaciones legales | 17, clase 12 |

## ⚖️ Riesgos y controles

Los riesgos son de finalidad y de retención. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Uso ulterior incompatible | Datos de un producto usados en otro | Cinco criterios antes del plan |
| Finalidad indeterminada | «Mejorar el servicio» | Finalidad verificable y previa |
| Reidentificación | Celdas pequeñas en agregados | Umbral en el sistema, no en el proceso |
| Retención indefinida | Un plazo único para todo | Una fila por finalidad |
| Inferencia sensible | Se deduce salud del gasto | Prohibición explícita y control técnico |
| Portabilidad con datos ajenos | Histórico con contrapartes | Enmascarar antes de exportar |

## 🧪 Práctica

El laboratorio pide evaluar tratamientos ulteriores contra la finalidad declarada. El criterio de compatibilidad es lo que se evalúa.

En [`labs/lab-01.md`](../labs/lab-01.md) y el [proyecto](../project/README.md):

1. Escribe la base de licitud y la finalidad de cada alcance de tu producto.
2. Aplica la prueba de minimización a quince campos.
3. Construye la política de retención con una fila por finalidad.
4. Evalúa un uso ulterior con los cinco criterios y con los tres planos.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen tratamientos indebidos. Las causas son finalidades demasiado amplias y retención sin plazo.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| «Tengo acceso, puedo usarlo» | Se leyó un solo régimen | Acceso y tratamiento son distintos |
| Finalidad genérica | Se redactó para no limitar | Determinada, explícita y previa |
| Un plazo de retención único | Se simplificó | Una fila por finalidad |
| «Anonimizado» reversible | Se seudonimizó y se llamó anónimo | Anónimo es no reversible |
| Umbral de agregación en el proceso | Se dejó al criterio del analista | Fíjalo en el sistema |
| Confundir legal con defendible | Se detuvo el análisis en la norma | Evalúa los tres planos |

## ❓ Preguntas de comprobación

1. ¿Por qué tener acceso a un dato no habilita a tratarlo, y qué régimen responde
   cada pregunta?
2. ¿Cuáles son los cinco criterios de compatibilidad y cuál pesa más en finanzas?
3. ¿Qué distingue seudonimizar de anonimizar y por qué importa?
4. ¿Qué límite tiene la portabilidad cuando el histórico contiene datos de
   terceros?
5. En el ejemplo guiado, ¿por qué se rechazó el USO 3 aunque pudiera legalizarse?

## 📥 Entregable

Guarda en `portfolio/parte-17/clase-12/`:

- base de licitud y finalidad de cada alcance de tu producto;
- la prueba de minimización aplicada a quince campos;
- la política de retención con una fila por finalidad y su fundamento;
- la evaluación de un uso ulterior con los cinco criterios y los tres planos.

## 🔗 Referencias cruzadas

- **Viene de:** clase 4 (clasificación e inferencia), clase 5 (consentimiento),
  clase 9 (familias de producto); Parte 14, clase 11 (ética algorítmica).
- **Continúa en:** clase 13 (incidentes), clase 14 (proyecto).
- **Se aplica en:** Parte 22, clase 12; Parte 23, clases 6 y 16.

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

- Parlamento Europeo y Consejo. *Reglamento (UE) 2016/679 (RGPD)*. <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
- European Data Protection Board (2021). *Guidelines 06/2020 on the interplay of PSD2 and the GDPR*. EDPB. <https://www.edpb.europa.eu/>
- Biblioteca del Congreso Nacional de Chile. *Ley N.º 19.628 sobre protección de la vida privada y su normativa sucesora sobre datos personales*. <https://www.bcn.cl/leychile>
- OECD (2013). *OECD Privacy Framework*. OECD. <https://www.oecd.org/digital/ieconomy/privacy-guidelines.htm>
- NIST (2020). *NIST Privacy Framework 1.0*. NIST. <https://www.nist.gov/privacy-framework>
- Verificación local: comprueba qué norma de protección de datos está vigente en tu jurisdicción, qué autoridad la aplica, en qué fase de implantación se encuentra y qué categorías reciben tratamiento reforzado. **Fecha de verificación de esta clase: 2026-08-06.** Esta clase no constituye asesoría legal.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 11 · Autenticación reforzada, fraude y responsabilidad](11-autenticacion-reforzada-fraude-y-responsabilidad.md) | [Parte 17](../README.md) · [Programa](../../../SYLLABUS.md) | [13 · Disponibilidad, SLA, observabilidad e incidentes →](13-disponibilidad-sla-y-observabilidad.md) |
<!-- gen:footer:end -->
