# Guía docente de la Etapa 5

**Cómo se enseña la etapa de finanzas digitales, infraestructura y mercados
tokenizados.** Complementa a la [guía docente general](guia-docente.md), que
sigue siendo válida para el formato de sesión, la evaluación y las rúbricas. Este
documento trata lo que cambia en las Partes 17 a 23 y solo eso.

Lo que cambia se resume en una frase: **en las cuatro primeras etapas el error
típico del estudiante es de cálculo; en la quinta es de categoría.** Confundir una
stablecoin con dinero electrónico, una billetera con una moneda, o SWIFT con
liquidación no se corrige repitiendo el ejercicio: se corrige con una distinción
explícita, y por eso cada parte de la etapa abre con una tabla de separación
terminológica.

---

## Las siete partes y su carácter

| Parte | Carácter | Qué exige del docente |
|---|---|---|
| 17 · Finanzas abiertas | Técnica y de consentimiento | Manejar OAuth y consentimiento sin perderse en el protocolo |
| 18 · Pagos transfronterizos | Operativa y de flujo | Distinguir mensaje, fondos, contabilidad y cumplimiento |
| 19 · Blockchain y DLT | Conceptual y comparativa | Neutralidad tecnológica sostenida, sin entusiasmo ni desdén |
| 20 · Activos digitales | De taxonomía y de riesgo | Precisión terminológica en cada frase |
| 21 · Tokenización y FX | De mercado y de derecho | Separar el token del derecho que representa |
| 22 · Regulación | De método | No dar respuestas: enseñar a determinar |
| 23 · Proyecto | Integradora | Sostener el cruce entre piezas sin resolverlo |

---

## Las seis distinciones que hay que sostener en toda la etapa

```text
SI EL GRUPO SALE DE LA ETAPA SIN ESTAS
SEIS, LA ETAPA NO SE DIO

  1 · activo digital ≠ criptoactivo ≠ token
  2 · stablecoin ≠ dinero electrónico ≠
      depósito tokenizado ≠ moneda digital
      de banco central
  3 · mensajería ≠ compensación ≠ liquidación
  4 · pago transfronterizo ≠ remesa ≠
      operación de cambio
  5 · banca abierta ≠ finanzas abiertas ≠
      datos abiertos
  6 · técnicamente posible ≠ económicamente
      viable ≠ jurídicamente válido ≠
      prudencialmente aceptable ≠
      operacionalmente resiliente ≠
      éticamente defendible
```

---

## Los cinco errores docentes propios de esta etapa

**1. Convertir la Parte 19 en un curso de programación.** El objetivo no es
escribir contratos: es saber cuándo un registro distribuido resuelve un problema y
cuándo no. Si la sesión se va en sintaxis, se perdió la clase.

**2. Presentar la tecnología como solución.** Cada caso debe comparar la
alternativa sin registro distribuido. Si nunca gana la base de datos centralizada,
la comparación no se está haciendo.

**3. Dar respuestas regulatorias.** La Parte 22 enseña a determinar, no qué norma
aplica al proyecto del estudiante. La respuesta correcta a «¿esto necesita
licencia?» es «¿qué está haciendo exactamente, y con qué hechos lo acreditas?».

**4. Tratar un proyecto piloto como producción.** Los proyectos institucionales que
la Parte 18 estudia demostraron cosas concretas y no demostraron otras. Conviene
decir siempre las dos.

**5. Dejar que el precio entre en la conversación.** Ni como argumento a favor ni
en contra. Ninguna clase de esta etapa se apoya en la cotización de nada, y el
programa no da recomendaciones de inversión.

---

## Cómo se corrige una respuesta de esta etapa

```text
SE VALORA

  · que distinga hecho verificado,
    supuesto e interpretación
  · que cite fuente y fecha
  · que declare qué NO se puede afirmar
    con los datos disponibles
  · que compare con la alternativa
    tradicional
  · que identifique quién asume el riesgo
    y quién soporta el coste

NO SE VALORA

  · coincidir con la respuesta del docente
  · usar el vocabulario correcto sin el
    concepto
  · citar una norma sin decir su fecha
  · concluir «depende» sin decir de qué
```

---

## Duración y recorte

| Situación | Qué se recorta | Qué no se recorta nunca |
|---|---|---|
| Sesión de 90 min completa | Nada | — |
| Sesión de 60 min | La práctica, que pasa a laboratorio | El ejemplo guiado |
| Curso de 8 semanas | Partes 19 y 21 se comprimen | Las tablas de separación terminológica |
| Público no técnico | Detalle criptográfico de la Parte 19 | La comparación con la alternativa |
| Público técnico | Repaso de productos de la Parte 3 | El bloque regulatorio |

---

## Los laboratorios de la etapa

Cómo son, cómo se ejecutan y cómo se corrigen está en
**[guia-laboratorios-digitales.md](guia-laboratorios-digitales.md)**. Tres reglas
que conviene anunciar el primer día:

```text
  1 · se ejecutan en local, sin red externa
  2 · con datos sintéticos, nunca reales
      de terceros
  3 · ninguna aplicación del repositorio
      es un banco, un mercado ni un
      custodio: son simuladores
```

---

## Los casos

La [biblioteca de casos](../case-studies/README.md) da veintiséis escenarios con
la misma estructura. El uso recomendado en esta etapa:

```text
  · reparte solo HECHOS y ACTORES
  · pide una decisión razonada, por escrito,
    en quince minutos
  · entrega después el bloque DECISIONES
  · la distancia entre lo que decidió el
    grupo y lo que se decidió en el caso
    ES LA CLASE

Y UNA ADVERTENCIA QUE CONVIENE HACER
  los casos son sintéticos y compuestos;
  no describen a ninguna entidad real
```

---

## Verificación regulatoria en el aula

La Parte 22 y buena parte de la 20 y la 21 citan normas. El método está en
**[metodologia-verificacion-regulatoria.md](metodologia-verificacion-regulatoria.md)**
y se resume en tres reglas para la sesión:

1. **Ninguna afirmación normativa sin fecha.** Si no se sabe la fecha, se dice que
   no se sabe.
2. **La fuente es la autoridad, no el resumen.** Un resumen sirve para orientar y
   no para decidir.
3. **Si la norma cambió después de escribirse la clase, gana la norma.** El
   material lo dice de forma expresa en cada bloque de fuentes.

---

## Material de apoyo

| Documento | Para qué |
|---|---|
| [Etapa 5 — finanzas digitales](etapa-5-finanzas-digitales.md) | Qué es y qué no es la etapa |
| [Glosario de finanzas digitales](glosario-finanzas-digitales.md) | Cada término con su «qué NO significa» |
| [Mapa de stablecoins](mapa-stablecoins.md) | Ruta transversal completa |
| [Mapa de FX on-chain](mapa-fx-onchain.md) | Ruta transversal completa |
| [Arquitectura de un mercado tokenizado](arquitectura-mercado-tokenizado.md) | El plano del proyecto final |
| [Matriz normativa de Chile](mapa-regulatorio-chile.md) | A qué puerta llamar |
| [Mapa regulatorio internacional](mapa-regulatorio-internacional.md) | Cómo comparar sin equivocarse |
| [Referencias oficiales](referencias-oficiales-digitales.md) | Dónde verificar cada cosa |

---

## Limitaciones

- Esta guía **no sustituye** a la guía docente general ni al criterio de quien
  enseña.
- El material es formativo y **no constituye asesoría financiera, tributaria ni
  legal**; conviene repetirlo al inicio de cada parte de esta etapa.
- La etapa cita regímenes que **cambian**: el docente debe verificar antes de cada
  edición del curso qué sigue vigente.

---

[🏠 Inicio](../README.md) · [📚 Documentación](README.md) · [📖 Programa](../SYLLABUS.md)
