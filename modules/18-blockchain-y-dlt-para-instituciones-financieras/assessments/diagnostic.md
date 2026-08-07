# Evaluación diagnóstica: Blockchain y DLT para instituciones financieras

## Instrucciones

Responde antes de empezar la parte. No se califica para aprobar: sirve para
saber qué necesitas reforzar. Marca con `NO SÉ` lo que no sepas.

**Puntaje total:** 40 puntos. **Tiempo sugerido:** 45 minutos.

## Sección A — Conceptos (12 puntos)

**1.** (3 pts) Explica en una frase qué problema resuelve un registro distribuido,
**sin usar la palabra «blockchain»**.

**2.** (3 pts) ¿Qué garantiza una función de resumen y qué garantiza una firma
digital? ¿Cuál de las dos dice que algo es verdad?

**3.** (3 pts) ¿Qué relación hay entre clave privada, clave pública y dirección, y
qué operación es irreversible?

**4.** (3 pts) ¿Qué significa que un mecanismo de consenso decida «el orden»?

## Sección B — Técnica (12 puntos)

**5.** (4 pts) Si manipulas una transacción de un bloque antiguo y recalculas todos
los bloques posteriores, ¿lo detecta la validación de la cadena? Explica.

**6.** (4 pts) ¿Qué diferencia hay entre tolerar fallos por caída y tolerar fallos
bizantinos, y cuántos nodos exige cada uno?

**7.** (4 pts) ¿Por qué un contrato no puede consultar por sí mismo una fuente de
datos externa?

## Sección C — Riesgo (10 puntos)

**8.** (4 pts) Un esquema de firma 4-de-7 con los siete guardianes usando el mismo
proveedor de módulos, ¿cuántos fallos independientes tolera realmente?

**9.** (3 pts) ¿Qué diferencia hay entre finalidad técnica y finalidad jurídica?

**10.** (3 pts) Nombra dos cosas que un registro distribuido **no** arregla.

## Sección D — Criterio (6 puntos)

**11.** (6 pts) Un proveedor propone sustituir una base de datos compartida por una
red con registro distribuido. Escribe las tres preguntas que harías antes de
evaluar la propuesta.

## Escala

- 0–15: la parte te va a exigir apoyo en las clases 1 a 5.
- 16–25: base suficiente; refuerza la sección donde perdiste más puntos.
- 26–33: buena base; enfócate en las clases 8 a 13.
- 34–40: puedes ir al proyecto y usar las clases como referencia.

## Guía de corrección

| Pregunta | Idea que debe aparecer |
|---:|---|
| 1 | Partes que no confían mantienen un registro que ninguna controla |
| 2 | Resumen: integridad. Firma: autenticidad. Ninguna dice que sea verdad |
| 3 | La privada genera la pública, y esta la dirección; no se puede volver |
| 4 | Con el orden se decide cuál de dos gastos del mismo saldo vale |
| 5 | No: vuelve a encajar. La inmutabilidad la da el consenso y el coste |
| 6 | 2f+1 frente a 3f+1; el bizantino responde mal, no calla |
| 7 | Los nodos recibirían respuestas distintas y el estado divergiría |
| 8 | Cero fallos del proveedor: los siete caen juntos |
| 9 | La técnica la da el protocolo; la jurídica, la norma |
| 10 | Dato malo, proceso malo, obligación regulatoria, identidad |
| 11 | «¿Hay tercero neutral?», «¿cuánto cuesta la alternativa?», «¿cómo salimos?» |
