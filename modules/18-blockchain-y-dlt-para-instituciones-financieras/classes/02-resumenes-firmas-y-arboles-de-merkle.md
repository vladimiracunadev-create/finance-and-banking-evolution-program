---
part: 19
class: 2
title: "Resúmenes, firmas y árboles de Merkle"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [global]
regulatory_topics: [dlt, criptografia, integridad]
regulation_last_verified: 2026-08-06
regulatory_status: estandar-vigente
primary_authorities: [NIST]
requires_legal_review: false
---

<!-- gen:header:start -->
# Clase 02 · Resúmenes, firmas y árboles de Merkle

> [← 01 · Sistemas distribuidos aplicados a finanzas](01-sistemas-distribuidos-aplicados-a-finanzas.md) · [Índice de la parte](../README.md) · [03 · Claves, direcciones y gestión criptográfica →](03-claves-direcciones-y-gestion-criptografica.md)

**Parte 19 — Blockchain y DLT para instituciones financieras** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Entender las tres piezas criptográficas sobre las que se apoya todo lo demás, y
—sobre todo— **qué garantiza cada una y qué no**. La mayoría de los errores de
diseño en esta materia vienen de atribuirle a una pieza una propiedad de otra.

## 📚 Objetivos

Al finalizar podrás:

1. **Distinguir** integridad, autenticidad y no repudio, y decir qué pieza
   aporta cada una.
2. **Explicar** qué propiedades tiene una función de resumen y qué ocurre cuando
   una se rompe.
3. **Construir** y verificar una firma digital, y describir el ataque que corta.
4. **Implementar** un árbol de Merkle y su prueba de inclusión.
5. **Determinar** qué se puede y qué no se puede demostrar con estas piezas.

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

| Concepto | Comprensión verificable |
|---|---|
| `función de resumen` | Transforma cualquier entrada en una salida de tamaño fijo |
| `resistencia a preimagen` | Dado el resumen, no se puede reconstruir la entrada |
| `resistencia a colisión` | No se pueden encontrar dos entradas con el mismo resumen |
| `firma digital` | Prueba de que quien posee una clave privada aprobó un contenido |
| `no repudio` | El firmante no puede negar haber firmado |
| `árbol de Merkle` | Estructura que resume un conjunto en un solo valor |
| `raíz de Merkle` | Resumen del conjunto completo |
| `prueba de inclusión` | Demostración de que un elemento está, sin mostrar el resto |

## 🧠 Modelo mental

```text
TRES PIEZAS, TRES PROPIEDADES DISTINTAS

  RESUMEN        integridad
                 «este contenido no cambió»
                 NO dice quién lo produjo

  FIRMA          autenticidad y no repudio
                 «quien tiene esta clave aprobó esto»
                 NO dice cuándo, ni que sea verdad

  ÁRBOL          integridad de un CONJUNTO, con prueba parcial
                 «este elemento está en el conjunto»
                 NO dice que el conjunto sea el correcto

EL ERROR CLÁSICO
  «está firmado, luego es cierto»

  una firma prueba QUIÉN, no QUÉ es verdad.
  Un banco puede firmar un dato falso perfectamente.
```

## 📖 Desarrollo

### 1. Qué garantiza una función de resumen

```text
PROPIEDADES QUE SE EXIGEN

  DETERMINISTA     la misma entrada da siempre la misma salida
  RÁPIDA           calcularla es barato
  PREIMAGEN        dado h, no se puede hallar m tal que H(m) = h
  SEGUNDA PREIMAGEN dado m, no se puede hallar m' ≠ m con igual resumen
  COLISIÓN         no se pueden hallar dos mensajes cualesquiera
                   con el mismo resumen
  EFECTO AVALANCHA cambiar un bit cambia media salida

QUÉ PASA CUANDO SE ROMPE LA RESISTENCIA A COLISIÓN
  se pueden construir DOS documentos con el mismo resumen:
  uno inocuo, que se firma, y otro malicioso, que hereda
  la firma

  → por eso las funciones con colisiones demostradas
    se retiran del uso, aunque «sigan funcionando»
```

### 2. Firma digital, paso a paso

```text
FIRMAR
  1. se calcula el resumen del mensaje
  2. se opera ese resumen con la clave PRIVADA
  3. el resultado es la firma

VERIFICAR
  1. se calcula el resumen del mensaje recibido
  2. se opera la firma con la clave PÚBLICA
  3. si coinciden, la firma es válida

POR QUÉ SE FIRMA EL RESUMEN Y NO EL MENSAJE
  · el mensaje puede ser enorme; el resumen es fijo
  · la operación criptográfica es cara

Y AQUÍ ESTÁ LA DEPENDENCIA QUE HAY QUE VER
  la seguridad de la FIRMA depende de la del RESUMEN.
  Si se puede fabricar una colisión, la firma de un
  documento vale para el otro.
```

### 3. Lo que una firma no dice

```text
UNA FIRMA VÁLIDA DEMUESTRA
  que quien poseía la clave privada aprobó ESE contenido

NO DEMUESTRA
  · CUÁNDO se firmó
      → hace falta un sello de tiempo de un tercero
  · que el firmante sea quien dice
      → hace falta ligar la clave a una identidad
  · que el contenido sea VERDADERO
      → una firma no valida hechos
  · que el firmante quisiera firmar ESO
      → si firma a ciegas un resumen, no sabe qué firmó
  · que la clave no estuviera comprometida
      → hace falta revocación

CONSECUENCIA PRÁCTICA
  «lo firmó el banco» y «es cierto» son afirmaciones
  distintas. Un registro distribuido garantiza la primera.
```

### 4. Árbol de Merkle

```text
CONSTRUCCIÓN
  hojas:  H(d1) H(d2) H(d3) H(d4)
  nivel 1: H(H(d1)+H(d2))   H(H(d3)+H(d4))
  raíz:    H( nivel1_izq + nivel1_der )

PARA QUÉ SIRVE
  · resumir un conjunto grande en un valor
  · demostrar que un elemento pertenece,
    revelando solo log₂(n) resúmenes

PRUEBA DE INCLUSIÓN DE d3 EN UN ÁRBOL DE 4
  se entregan H(d4) y H(H(d1)+H(d2))
  el verificador recalcula la raíz
  → con 2 valores prueba pertenencia a un conjunto de 4
  → con 20 valores, a uno de un millón
```

```text
LA PROPIEDAD QUE LO HACE ÚTIL EN FINANZAS
  un participante puede demostrar que su operación
  está en el bloque SIN revelar las demás operaciones

  → confidencialidad entre participantes
    con verificabilidad del conjunto
```

### 5. Prueba de exclusión: lo que cuesta más

```text
DEMOSTRAR QUE ALGO ESTÁ ES BARATO.
DEMOSTRAR QUE ALGO NO ESTÁ, NO.

  con un árbol de Merkle simple: imposible sin
  recorrer todo el conjunto

  CON EL CONJUNTO ORDENADO
    se demuestra que dos elementos consecutivos
    «rodean» al buscado y que no hay nada entre ellos
    → prueba de exclusión con el mismo coste logarítmico

POR QUÉ IMPORTA EN FINANZAS
  «esta garantía NO está pignorada» es una prueba
  de exclusión, y es la que un banco necesita antes
  de prestar (clase 1, ejemplo guiado)
```

## 🧮 Ejemplo guiado

**Situación.** Un consorcio publica cada día la raíz de Merkle de sus reservas
para que cualquiera pueda comprobar que su saldo está incluido. Un auditor debe
evaluar si esa publicación demuestra lo que el consorcio afirma.

```text
LO QUE EL CONSORCIO PUBLICA
  · raíz de Merkle diaria de los saldos de clientes
  · cada cliente puede pedir su prueba de inclusión
  · el total declarado de pasivos: 4 820 000 000

LO QUE EL CONSORCIO AFIRMA
  «cualquiera puede verificar que sus fondos están
   respaldados»
```

**Paso 1 — comprueba qué demuestra la prueba de inclusión.**

```text
UN CLIENTE CON SALDO DE 12 000 RECIBE SU PRUEBA
Y RECALCULA LA RAÍZ. COINCIDE.

  QUÉ HA DEMOSTRADO
    que su saldo de 12 000 está en el conjunto
    que produjo esa raíz

  QUÉ NO HA DEMOSTRADO
    · que el conjunto contenga a TODOS los clientes
    · que la suma del conjunto sea 4 820 000 000
    · que existan activos que respalden ese pasivo
```

**Paso 2 — identifica el hueco.**

```text
EL CONSORCIO PODRÍA OMITIR CLIENTES DEL ÁRBOL

  si omite a los que no piden su prueba,
  la raíz publicada corresponde a un conjunto
  MENOR que el pasivo real

  cada cliente que comprueba ve su saldo
  y ninguno detecta la omisión

  → la prueba de inclusión NO impide la subdeclaración
```

**Paso 3 — introduce la corrección.**

```text
ÁRBOL DE SUMAS (Merkle sum tree)

  cada nodo guarda, además del resumen,
  la SUMA de los saldos de su subárbol

  la raíz contiene el TOTAL

  QUÉ CAMBIA
    el cliente verifica su saldo Y comprueba que el total
    de la raíz es el que el consorcio declara

    omitir un cliente ahora exige reducir el total,
    y eso es visible
```

**Paso 4 — busca el hueco de la corrección.**

```text
EL ÁRBOL DE SUMAS IMPIDE OMITIR.
¿IMPIDE TODO?

  NO. El consorcio puede incluir saldos NEGATIVOS
  en ramas que nadie va a verificar, reduciendo el total
  sin omitir a nadie

  CORRECCIÓN
    exigir que cada hoja demuestre saldo no negativo
    → una prueba criptográfica de rango por hoja

  y ahí es donde entra la clase 10
```

**Paso 5 — evalúa el otro lado del balance.**

```text
TODO LO ANTERIOR DEMUESTRA EL PASIVO.
NO DICE NADA DEL ACTIVO.

  «tus fondos están respaldados» exige demostrar
  que existen activos ≥ pasivos

  eso NO se demuestra con un árbol de Merkle:
  exige verificar la titularidad de activos que
  viven fuera del registro

  → prueba de reservas y prueba de pasivos
    son dos cosas distintas, y la segunda es la fácil
```

**Paso 6 — cuantifica lo que sí aporta.**

```text
ANTES DE LA PUBLICACIÓN
  el cliente confiaba en el estado de cuenta del consorcio,
  sin verificación posible

DESPUÉS, CON ÁRBOL DE SUMAS Y PRUEBA DE RANGO
  el cliente verifica:
    · que su saldo está incluido
    · que el total declarado es la suma real de los saldos
    · que ninguna hoja es negativa

  eso es MUCHO más de lo que había, y sigue sin ser
  «tus fondos están respaldados»
```

**Paso 7 — escribe el dictamen.**

```text
DICTAMEN DEL AUDITOR

  LA AFIRMACIÓN «cualquiera puede verificar que sus
  fondos están respaldados» ES INCORRECTA.

  LO QUE LA PUBLICACIÓN DEMUESTRA, CON LAS CORRECCIONES:
    que el pasivo declarado es consistente con
    los saldos individuales

  LO QUE NO DEMUESTRA:
    que existan activos suficientes

  REDACCIÓN CORRECTA PROPUESTA
    «cualquiera puede verificar que su saldo está incluido
     en el total de pasivos que publicamos. La existencia
     de activos suficientes la verifica [x] y su informe
     está en [y], con fecha [z].»

  Y UNA OBSERVACIÓN DE MÉTODO
    la publicación es un avance real. El problema no es
    la técnica: es la frase que la describe.
```

**Interpreta:** el árbol de Merkle hacía exactamente lo que sabe hacer —demostrar
pertenencia a un conjunto— y la afirmación comercial le atribuía una propiedad
que ninguna pieza criptográfica puede dar. **Atribuir a una pieza la propiedad de
otra es el error que esta clase enseña a detectar.**

## 🧭 Perspectivas

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | «Puedo verificar mis fondos» | Si confía |
| Consorcio | Una publicación que da confianza | Cómo la describe |
| Auditor | Una prueba de pasivos | Qué dictamina |
| Supervisor | Una afirmación de respaldo | Si exige verificación del activo |
| Tecnología | Un árbol con o sin sumas | Qué implementa |
| Competidor | Una práctica de transparencia | Si la adopta |
| Sociedad | «Verificable» como sello | Riesgo de falsa seguridad |

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Puedo comprobar mi saldo» | Prueba de inclusión, no de respaldo | 19, clase 2 |
| «Está firmado por el banco» | La firma dice quién, no qué es cierto | 19, clase 2 |
| «Publican la raíz cada día» | Sin árbol de sumas, se puede omitir | 19, clase 2 |

## ⚖️ Riesgos y controles

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Atribuir a una pieza otra propiedad | «Firmado, luego cierto» | Separar integridad, autenticidad y verdad |
| Subdeclaración del conjunto | Se omiten hojas del árbol | Árbol con sumas |
| Hojas negativas | Se reduce el total sin omitir | Prueba de rango por hoja |
| Función de resumen obsoleta | Colisión demostrada | Política de retirada de algoritmos |
| Firma a ciegas | Se firma un resumen sin ver el contenido | Mostrar siempre lo que se firma |
| Confundir pasivo con respaldo | Se demuestra lo fácil | Verificación independiente del activo |

## 🧪 Práctica

En [`labs/lab-02.md`](../labs/lab-02.md) y [`labs/lab-03.md`](../labs/lab-03.md):

1. Implementa firma y verificación, y demuestra que un mensaje alterado falla.
2. Construye un árbol de Merkle y su prueba de inclusión sobre 10 000 hojas.
3. Añade sumas al árbol y demuestra que omitir una hoja se detecta.
4. Escribe qué demuestra y qué no demuestra tu construcción.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| «Firmado, luego verdadero» | Se confundió autenticidad con verdad | La firma dice quién |
| Prueba de inclusión como prueba de reservas | Se demostró el pasivo | El activo se verifica aparte |
| Árbol sin sumas | Se copió la construcción básica | Con sumas, omitir es visible |
| Implementar la criptografía a mano en producción | Se copió el laboratorio | Bibliotecas auditadas |
| Firma sin sello de tiempo | Se asumió el momento | La firma no dice cuándo |
| Clave sin revocación | No se previó el compromiso | Mecanismo de revocación |

## ❓ Preguntas de comprobación

1. ¿Qué propiedad aporta cada una de las tres piezas y cuál falta siempre?
2. ¿Por qué la seguridad de una firma depende de la de la función de resumen?
3. ¿Qué cinco cosas **no** demuestra una firma válida?
4. ¿Por qué una prueba de exclusión exige un conjunto ordenado?
5. En el ejemplo guiado, ¿por qué la afirmación del consorcio era incorrecta aun
   siendo la técnica correcta?

## 📥 Entregable

Guarda en `portfolio/parte-19/clase-02/`:

- la implementación de firma y verificación, con su prueba de alteración;
- el árbol de Merkle con prueba de inclusión sobre 10 000 hojas;
- la versión con sumas y la demostración de que detecta una omisión;
- la lista escrita de qué demuestra y qué no demuestra tu construcción.

## 🔗 Referencias cruzadas

- **Viene de:** clase 1; Parte 17, clase 7 (firma de mensajes).
- **Continúa en:** clase 3 (claves), clase 4 (bloques), clase 10 (pruebas
  criptográficas).
- **Se aplica en:** Parte 20, clase 7 (prueba de reservas); Parte 21, clase 10.

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

- NIST (2015). *FIPS 180-4: Secure Hash Standard*. National Institute of Standards and Technology. <https://csrc.nist.gov/pubs/fips/180-4/upd1/final>
- NIST (2023). *FIPS 186-5: Digital Signature Standard*. NIST. <https://csrc.nist.gov/pubs/fips/186-5/final>
- Merkle, R. (1988). *A Digital Signature Based on a Conventional Encryption Function*. CRYPTO '87.
- NIST (2018). *NISTIR 8202: Blockchain Technology Overview*. NIST. <https://csrc.nist.gov/pubs/ir/8202/final>
- NIST (2020). *SP 800-57 Part 1 Rev. 5: Recommendation for Key Management*. NIST. <https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final>
- Verificación local: comprueba qué algoritmos admite tu jurisdicción para firma electrónica con efectos jurídicos y cuáles están en retirada. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 01 · Sistemas distribuidos aplicados a finanzas](01-sistemas-distribuidos-aplicados-a-finanzas.md) | [Parte 19](../README.md) · [Programa](../../../SYLLABUS.md) | [03 · Claves, direcciones y gestión criptográfica →](03-claves-direcciones-y-gestion-criptografica.md) |
<!-- gen:footer:end -->
