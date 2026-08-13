# Caso · Un pago retenido once días

**Tema:** pagos transfronterizos · **Parte relacionada:** 18 · **Naturaleza:**
caso sintético compuesto · **Fecha de verificación:** 2026-08-12

Una transferencia de 47 500 unidades hacia un proveedor industrial queda retenida
en un banco intermediario. Nadie la rechaza y nadie la devuelve: simplemente no
avanza. Once días después el ordenante todavía no sabe dónde está su dinero, y esa
es la parte del caso que hay que explicar.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · importe            47 500
  · cadena: banco ordenante → intermediario A
    → intermediario B → banco beneficiario
  · retención en el intermediario B
  · motivo: coincidencia parcial del nombre
    del beneficiario con una lista de
    sanciones
  · el nombre coincidente correspondía a
    otra persona, en otro país

SUPUESTO DEL EJERCICIO
  · días hasta la resolución            11
  · consultas del ordenante              9
  · coste de investigación por tramo     35
  · penalización contractual del
    ordenante por retraso de entrega  2 800
```

El dato que ordena el caso es de estructura: **el ordenante no tiene relación
contractual con el banco que retuvo el pago**. Solo puede preguntar a su banco,
que a su vez pregunta al siguiente, y así hasta el punto de retención. Cada salto
añade horas y pierde contexto.

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Ordenante | Que llegue y que le digan cuándo | Un identificador y silencio |
| Banco ordenante | Responder a su cliente | Que envió correctamente |
| Intermediario A | Pasar el mensaje | Que lo pasó |
| Intermediario B | No incumplir sanciones | Una coincidencia parcial |
| Banco beneficiario | Abonar cuando llegue | Que no ha llegado |
| Beneficiario | Cobrar y despachar la mercancía | Que no ha cobrado |

## Decisiones

```text
DÍA 0   B retiene por coincidencia parcial
        DECISIÓN CORRECTA: ante duda,
        se retiene

DÍA 0   B no comunica la retención aguas
        arriba
        DECISIÓN HABITUAL Y COSTOSA

DÍA 2   el ordenante pregunta a su banco
        su banco abre una investigación
        formal y espera

DÍA 5   A responde que lo envió a B

DÍA 7   B pide documentación adicional
        del beneficiario

DÍA 9   el beneficiario aporta documentos
        a su banco, que los envía aguas
        arriba

DÍA 11  B libera el pago

NINGUNA DE LAS DECISIONES ES INCORRECTA
POR SEPARADO. El resultado agregado sí.
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Falso positivo de cribado | Estructural | Sí |
| Datos del beneficiario incompletos | Desde el origen | Sí |
| Falta de trazabilidad extremo a extremo | Estructural | Sí |
| Comunicación asíncrona por saltos | Estructural | Sí |
| Riesgo comercial del ordenante | Desde el día 5 | Sí |
| De-risking del corredor | A medio plazo | No en este caso |

## Regulación

```text
QUÉ ALCANZA

  SANCIONES
    la obligación de cribar es propia de
    cada entidad y no se delega; ante duda
    razonable, la retención es la conducta
    debida

  REGLA DEL VIAJE
    la información del ordenante y del
    beneficiario debe acompañar a la
    operación; su calidad determina la
    tasa de falsos positivos

  TRANSPARENCIA AL CLIENTE
    varios regímenes exigen informar del
    coste y del plazo estimado; el deber
    de informar del estado durante una
    retención por sanciones es más limitado

LÍMITE
  qué se puede comunicar durante una
  retención por sanciones depende de la
  jurisdicción; hay supuestos en que
  informar está restringido
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Cribado de sanciones | Sí | Sí | Calibración de coincidencia parcial |
| Datos estructurados del beneficiario | Parcial | No | Identificador y país en campo propio |
| Estado del pago para el ordenante | No | — | Confirmación de posición en la cadena |
| Investigación con plazo | No | — | Escalado automático a las 48 h |
| Lista de excepciones verificadas | No | — | Memoria de falsos positivos resueltos |
| Aviso al beneficiario | No | — | Que sepa que le van a pedir papeles |

El quinto control es el más barato y el que más ahorra. Un falso positivo
resuelto en enero vuelve a producirse en marzo si nadie guarda el resultado de la
verificación; y la segunda retención cuesta lo mismo que la primera.

## Resultado

```text
COSTE DEL EPISODIO (supuestos)

  investigación, 3 tramos × 35 =     105
  penalización comercial          2 800
  9 gestiones del ordenante
    a 45 por gestión                 405
  coste de oportunidad del importe
    11 días                        ~ 65

  TOTAL                            3 375
  SOBRE UN PAGO DE 47 500 = 7,1 %

Y NINGUNA COMISIÓN EXPLÍCITA
SUBIÓ UN CÉNTIMO.
```

## Lecciones

1. **La transparencia de un pago transfronterizo no es la comisión: es el
   estado.** El ordenante toleró el coste; lo que no toleró fue no saber.
2. **La calidad del dato de origen determina el coste del cumplimiento aguas
   abajo.** Un identificador y un país estructurados habrían reducido la
   coincidencia parcial a cero.
3. **Los falsos positivos deben tener memoria.** Sin registro de verificaciones,
   el mismo beneficiario se retiene cada vez.
4. **Una investigación sin plazo no es una investigación**, es una cola.

## Preguntas

1. ¿Quién debía haber comunicado la retención, y por qué no lo hizo?
2. ¿Qué parte del coste corresponde al cumplimiento y qué parte a la mala calidad
   del dato? ¿Se pueden separar?
3. ¿Cómo se calibra un motor de cribado sin aumentar el riesgo de falso negativo?
   ¿Quién aprueba ese umbral?
4. Si eres el banco ordenante, ¿qué prometes a tu cliente sobre plazos?
5. ¿Cambia algo si el pago se hubiera enrutado por menos intermediarios? ¿Y qué
   se pierde al reducir la cadena?

## Fuentes

- Comité de Pagos e Infraestructuras del Mercado (2020). *Enhancing cross-border payments: building blocks of a global roadmap*. BIS-CPMI. <https://www.bis.org/cpmi/publ/d193.htm>
- Financial Stability Board. *G20 Roadmap for Enhancing Cross-border Payments*. FSB. <https://www.fsb.org/work-of-the-fsb/financial-innovation-and-structural-change/cross-border-payments/>
- GAFI. *Recomendación 16 e información del ordenante y del beneficiario*. FATF. <https://www.fatf-gafi.org/>
- ISO 20022. *Message definitions for payments*. <https://www.iso20022.org/>
- Verificación local: caso sintético; cifras supuestas. Lo que puede comunicarse durante una retención por sanciones depende de la jurisdicción. **Fecha de verificación: 2026-08-12.** No constituye asesoría legal.
