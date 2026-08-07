<!-- meta
part: 23
class: 9
title: "Custodia y gestión de claves"
level: profesional
duration_minutes: 90
status: complete
jurisdictions: [internacional]
regulatory_topics: [custodia, claves, segregacion]
regulation_last_verified: 2026-08-06
regulatory_status: vigente
primary_authorities: [IOSCO, NIST, CMF]
requires_legal_review: true
-->

<!-- gen:header:start -->
# Clase 09 · Custodia y gestión de claves

> [← 08 · Interfaces, consentimiento y terceros](08-interfaces-consentimiento-y-terceros.md) · [Índice de la parte](../README.md) · [10 · Liquidación y sus modos de fallo →](10-liquidacion-y-sus-modos-de-fallo.md)

**Parte 23 — Proyecto — banco digital y mercado tokenizado** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Diseñar la custodia del colateral y de las claves del sistema, con la
**independencia efectiva medida** en vez de supuesta.

La clase 3 delegó la custodia del colateral en un tercero autorizado, y aun así el
sistema tiene claves propias: las que operan el registro y las que firman las
liquidaciones. Esta clase las diseña con el método de la Parte 20, clase 12.

## 📚 Objetivos

Al finalizar podrás:

1. **Medir** la independencia efectiva del esquema de claves del sistema.
2. **Diseñar** el procedimiento de recuperación sin crear una puerta trasera.
3. **Especificar** la cadena de controles de una operación con clave.
4. **Verificar** la segregación del colateral con el custodio delegado.
5. **Probar** la sustitución del custodio antes de necesitarla.

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

Los cuatro primeros términos son el esquema de claves y su recuperación; los cuatro siguientes, la custodia delegada y su protección jurídica. La **no pignoración** es la cláusula que decide en un concurso, y su ausencia es el hallazgo más caro de todo el capstone.

| Concepto | Comprensión verificable |
|---|---|
| `independencia efectiva` | Guardianes que un evento no tumba a la vez |
| `esquema de umbral` | m de n firmas para operar |
| `recuperación con retardo` | Camino alternativo que se puede cancelar |
| `lista blanca` | Destinos aprobados con espera previa |
| `señal de coacción` | Firma que valida en apariencia y alerta |
| `segregación jurídica` | El activo no integra la masa del custodio |
| `no pignoración` | Compromiso de no usar el activo como garantía propia |
| `plan de sustitución` | Traslado a otro custodio, probado |

## 🧠 Modelo mental

Un esquema «3 de 5» no dice nada por sí solo. Lo que decide es qué eventos dejan
inoperativos a cuántos guardianes a la vez, y esa medición cambia el resultado
sin tocar el umbral.

```text
LA MEDICIÓN

  para cada factor —ubicación, dispositivo,
  jurisdicción, proveedor— se cuenta el
  mayor grupo que lo comparte

  independencia efectiva = n − peor grupo + 1

Y LA CONDICIÓN
  peor grupo < umbral

Si no se cumple, un solo evento alcanza
el umbral, y el esquema no tolera nada.
```

## 📖 Desarrollo

### 1. Los dos fallos simétricos

Perder la clave y filtrarla son fallos opuestos, y casi toda medida que reduce
uno aumenta el otro. El diseño consiste en elegir dónde ponerse, no en eliminar
ambos.

```text
PERDER   nadie puede mover
FILTRAR  cualquiera puede mover

  más copias    → menos pérdida, más filtración
  umbral alto   → menos filtración, más bloqueo
  recuperación  → menos pérdida, y un segundo
                  camino de ataque

Y POR ESO LA RECUPERACIÓN LLEVA RETARDO
Y CANCELACIÓN
```

### 2. La cadena de una retirada

El control que detiene el ataque más común no es criptográfico: es una espera de
48 horas antes de poder retirar a una dirección nueva.

```text
1 origen autorizado
2 destino en lista blanca
3 ALTA DE DESTINO CON ESPERA DE 48 h
4 límite por importe
5 segunda aprobación fuera de banda
6 verificación de la dirección completa
7 registro inmutable

EL 3 CONVIERTE MINUTOS EN DOS DÍAS
de margen para detectar
```

### 3. La segregación del colateral delegado

Delegar la custodia no delega la responsabilidad. Hay tres cláusulas que decidir
en el contrato y una verificación que hacer todos los meses.

```text
LAS TRES CLÁUSULAS
  · de quién es el activo
  · prohibición de disponer y de pignorar
  · verificación independiente del saldo

Y LA VERIFICACIÓN MENSUAL
  saldo total del custodio contra la suma
  de posiciones de clientes, por un tercero

SIN ELLA, LA SEGREGACIÓN ES UNA
EXPECTATIVA
```

## 🧮 Ejemplo guiado

El ejemplo mide la independencia efectiva de un esquema y revisa las tres cláusulas del custodio. El hallazgo mayor no está en la criptografía sino en el contrato.

**Situación.** El equipo diseña el esquema de claves del registro y verifica la
custodia delegada del colateral.

```text
PROPUESTA INICIAL
  esquema 3-de-5
  G1, G2, G3  oficina central
  G4          filial
  G5          proveedor externo
  todos con el mismo modelo de dispositivo

COLATERAL DELEGADO       24 000 000
clientes con colateral          180
```

**Paso 1 — mide la independencia efectiva.**

```text
mayor grupo por ubicación     3
mayor grupo por dispositivo   5
mayor grupo por jurisdicción  5
mayor grupo por proveedor     5

  peor grupo 5 ≥ umbral 3
  → UN SOLO EVENTO ALCANZA EL UMBRAL
  independencia efectiva = 1
```

**Paso 2 — redistribuye sin cambiar el umbral.**

```text
G1 central   · tipo X · cl · interno_1
G2 filial    · tipo Y · cl · interno_2
G3 remota    · tipo X · uy · interno_3
G4 proveedor · tipo Z · pe · externo_1
G5 despacho  · tipo Y · es · externo_2

mayor grupo por cualquier factor: 2
  2 < 3 → tolera un evento correlacionado
  independencia efectiva = 4

EL UMBRAL NO CAMBIÓ.
```

**Paso 3 — diseña la recuperación.**

```text
4-DE-7
  los 5 guardianes + notario + caja en
  otra jurisdicción

  retardo 7 días
  notificación a los 7 por dos canales
  cualquiera puede CANCELAR

¿POR QUÉ 4-DE-7 Y NO 3-DE-5?
  la recuperación evita el esquema normal:
  tiene que ser más difícil, no igual
```

**Paso 4 — verifica la custodia delegada.**

```text
LAS TRES CLÁUSULAS
  propiedad del cliente        sí
  prohibición de disponer      NO CONSTA
  verificación independiente   NO

DOS HALLAZGOS BLOQUEANTES

  sin prohibición de disponer, en un
  concurso del custodio los 180 clientes
  son acreedores ordinarios

  supuesto de recuperación 18 %
  pérdida = 24 000 000 × 82 % = 19 680 000

  COSTE DE CORREGIRLO
  una cláusula y 34 000 al año de
  verificación mensual
```

**Interpreta:** El esquema «3 de 5» tenía una independencia efectiva de **1**, y redistribuir las
partes la llevó a 4 sin tocar el umbral. Y el hallazgo mayor no estaba en las
claves: estaba en una cláusula ausente del contrato de custodia que valía
19,7 millones.

## 🧭 Perspectivas

La custodia afecta a cada actor de forma distinta. La tabla lo recoge.

| Actor | Qué ve | Qué decide |
|---|---|---|
| Cliente | Su colateral custodiado | Si confía |
| Equipo | Un esquema que parecía robusto | Cómo lo redistribuye |
| Custodio | Tres cláusulas que firmar | Si las acepta |
| Auditor | Verificación mensual | Qué certifica |
| Supervisor | Independencia medida | Qué exige |
| Aseguradora | Cobertura de pérdida | Qué excluye |
| Administrador concursal | Cláusulas del contrato | Cómo reparte |
| Sociedad | Fondos protegidos | — |

## 🏦 Del cliente al banco

El cliente cree que su colateral es suyo y eso depende de una cláusula. La tabla enfrenta las dos lecturas.

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Es 3 de 5, es seguro» | La independencia efectiva era 1 | 23, clase 9 |
| «Lo custodia un tercero» | Sin prohibición de disponer | 23, clase 9 |
| «Está todo verificado» | No había verificación independiente | 23, clase 9 |

## ⚖️ Riesgos y controles

Los riesgos son de concentración de claves y de segregación no pactada. La tabla los recoge con su control.

| Riesgo | Cómo se materializa | Control |
|---|---|---|
| Umbral elegido por intuición | «3 de 5 suena bien» | Medir la independencia efectiva |
| Mismo dispositivo para todos | Compra centralizada | Diversificar fabricante |
| Recuperación igual de fácil | Se busca comodidad | Umbral mayor y retardo |
| Sin espera para destinos nuevos | Molesta a operaciones | Es el control que detiene el ataque |
| Delegar y creerse cubierto | El custodio está autorizado | Las tres cláusulas |
| Sin verificación independiente | La hace quien custodia | Un tercero, mensual |

## 🧪 Práctica

El laboratorio pide medir la independencia efectiva y verificar las tres cláusulas. La cuantificación de la exposición es lo que convierte el hallazgo en decisión.

En [`labs/lab-04.md`](../labs/lab-04.md):

1. Mide la independencia efectiva del esquema propuesto.
2. Redistribuye las partes sin cambiar el umbral y vuelve a medir.
3. Diseña la recuperación con su umbral, retardo y cancelación.
4. Verifica las tres cláusulas del contrato de custodia.

## ⚠️ Errores frecuentes

Los síntomas de la tabla describen pérdidas de activos custodiados. Las causas son independencia efectiva de uno y cláusulas ausentes.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| Elegir el umbral y parar | Parece la decisión | Falta medir la independencia |
| Un solo tipo de dispositivo | Es más fácil de gestionar | Una vulnerabilidad los tumba |
| Recuperación sin retardo | Agiliza | Es un segundo camino de ataque |
| Confiar en el custodio autorizado | Lo está | Las cláusulas deciden en el concurso |
| Verificar internamente | Es más barato | Lo hace quien podría tener la diferencia |
| Plan de sustitución sin probar | Está escrito | Pruébalo una vez al año |

## ❓ Preguntas de comprobación

1. ¿Cómo se calcula la independencia efectiva y qué condición debe cumplir?
2. ¿Cuáles son los dos fallos simétricos de la custodia por clave?
3. ¿Qué control detiene el ataque más común y por qué?
4. ¿Por qué el umbral de recuperación debe superar al de firma?
5. ¿Qué tres cláusulas protegen ante el concurso del custodio?

## 📥 Entregable

Guarda en `portfolio/parte-23/clase-09/`:

- la medición de independencia antes y después;
- el esquema redistribuido con su justificación;
- el diseño de recuperación con retardo y cancelación;
- la verificación de las tres cláusulas del custodio.

## 🔗 Referencias cruzadas

- **Viene de:** clases 3 y 7; Parte 20, clase 12; Parte 21, clase 9.
- **Continúa en:** clases 10 y 14 de esta parte.
- **Se aplica en:** clases 15 y 16 de esta parte.

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

- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. IOSCO. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- NIST (2016). *SP 800-57 Part 1: Recommendation for Key Management*. NIST. <https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final>
- NIST (2020). *SP 800-207: Zero Trust Architecture*. NIST. <https://csrc.nist.gov/pubs/sp/800/207/final>
- Comisión para el Mercado Financiero. *Normativa aplicable a entidades financieras*. CMF. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Verificación local: comprueba en la fuente oficial vigente qué exige tu jurisdicción sobre este punto. Esta clase no constituye asesoría legal. **Fecha de verificación de esta clase: 2026-08-06.**

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 08 · Interfaces, consentimiento y terceros](08-interfaces-consentimiento-y-terceros.md) | [Parte 23](../README.md) · [Programa](../../../SYLLABUS.md) | [10 · Liquidación y sus modos de fallo →](10-liquidacion-y-sus-modos-de-fallo.md) |
<!-- gen:footer:end -->
