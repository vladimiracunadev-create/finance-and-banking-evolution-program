# Evaluación diagnóstica: Finanzas abiertas, APIs y economía de datos

## Instrucciones

Responde antes de empezar la parte. No se califica para aprobar: sirve para
saber qué necesitas reforzar. Marca con `NO SÉ` lo que no sepas; es información
útil y no resta.

**Puntaje total:** 40 puntos. **Tiempo sugerido:** 45 minutos.

## Sección A — Conceptos (12 puntos)

**1.** (3 pts) Explica la diferencia entre **banca abierta**, **finanzas abiertas** y
**datos abiertos**.

**2.** (3 pts) ¿Qué es un proveedor de servicios de información de cuentas y en qué
se diferencia de un proveedor de iniciación de pagos?

**3.** (3 pts) ¿Por qué compartir la contraseña del banco con una aplicación es un
modelo peor que la delegación por token, incluso si funciona?

**4.** (3 pts) ¿Qué significa que un consentimiento sea *granular*?

## Sección B — Técnica (12 puntos)

**5.** (4 pts) En un flujo de autorización con código, ¿qué problema resuelve PKCE?

**6.** (4 pts) ¿Qué es una operación idempotente y por qué importa en un pago?

**7.** (4 pts) ¿Por qué una API no debe representar importes con números en coma
flotante?

## Sección C — Riesgo y regulación (10 puntos)

**8.** (4 pts) Si una aplicación autorizada por el cliente ejecuta un pago que el
cliente niega haber ordenado, ¿quién responde y de qué depende?

**9.** (3 pts) Nombra dos riesgos **sistémicos** —no individuales— del modelo de
finanzas abiertas.

**10.** (3 pts) ¿Qué autoridad regula las finanzas abiertas en tu país y qué norma
las establece? Si no lo sabes, escribe cómo lo averiguarías.

## Sección D — Criterio (6 puntos)

**11.** (6 pts) Un producto pide acceso a 24 meses de movimientos para «mejorar la
experiencia». No sabe todavía qué hará con ellos. Argumenta en contra en
cinco líneas, usando un criterio y no una opinión.

## Escala

- 0–15: la parte te va a exigir apoyo en las clases 1 a 6.
- 16–25: base suficiente; refuerza la sección donde perdiste más puntos.
- 26–33: buena base; enfócate en las clases 7 a 13.
- 34–40: puedes ir directo al proyecto y usar las clases como referencia.

## Guía de corrección

| Pregunta | Idea que debe aparecer |
|---:|---|
| 1 | Ampliación del alcance: cuentas → todos los productos → datos no financieros |
| 2 | Lectura frente a orden de movimiento de fondos |
| 3 | Credencial no acotada, no revocable y no auditable |
| 4 | Alcance por finalidad, no un permiso único |
| 5 | Evita el uso de un código interceptado por un cliente público |
| 6 | Repetir la petición no repite el efecto |
| 7 | Error de representación binaria en decimales |
| 8 | Depende de si hubo autenticación reforzada y de la norma aplicable |
| 9 | Concentración de agregadores y proveedores tecnológicos críticos |
| 10 | Se acepta el procedimiento de búsqueda como respuesta válida |
| 11 | Minimización y finalidad determinada previa |
