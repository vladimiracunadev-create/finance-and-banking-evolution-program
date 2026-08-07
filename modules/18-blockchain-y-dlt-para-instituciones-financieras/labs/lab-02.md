# Laboratorio 2: Firma de transacciones

## Propósito

Firmar, verificar y **romper**. El laboratorio no termina cuando la firma
funciona: termina cuando se ha demostrado qué ataques corta y cuáles no.

## Escenario

El consorcio va a aceptar transacciones firmadas por sus participantes. Antes de
habilitarlo, tienes que demostrar qué pasa con una firma capturada, con un
mensaje alterado y con una clave perdida.

## Contexto

Una firma prueba **quién**, no **qué es verdad** ni **cuándo**. El laboratorio
construye las pruebas que lo demuestran.

## Datos

Claves generadas en el laboratorio, de juguete y en memoria.

## Supuestos del ejercicio

- Se usa la biblioteca estándar; en producción se usan bibliotecas auditadas.
- El esquema de firma es **simplificado y didáctico**: no ofrece las garantías
  de un esquema real y no debe usarse fuera del laboratorio.
- No hay red: la captura de mensajes se simula.

## Requisitos

- Laboratorio 1 completado.
- Haber leído las clases 2 y 3.

## Pasos

1. Genera un par de claves y deriva la dirección con verificación de errores.
2. Firma una transacción y verifícala.
3. **Altera un byte del mensaje** y comprueba que la verificación falla.
4. **Captura una firma válida y reenvíala**: comprueba que se acepta si no hay
   número de orden, y que se rechaza si lo hay.
5. Implementa un esquema de firma múltiple m-de-n y prueba el umbral.
6. Demuestra que con m−1 firmas no se puede disponer.
7. Analiza la correlación de un conjunto de guardianes dado.
8. Escribe el procedimiento de recuperación con las siete preguntas de la
   clase 3.

## Arquitectura

```text
clave privada ──► clave pública ──► dirección (con verificación)
      │
   firma(resumen del mensaje)
      │
verificación con clave pública ──► válida / inválida

firma múltiple m-de-n
  guardián 1 ─┐
  guardián 2 ─┼─► m firmas ──► disposición autorizada
  guardián n ─┘
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Un mensaje alterado falla | Prueba negativa por byte |
| 2 | Una dirección mal tecleada se detecta | Prueba con carácter cambiado |
| 3 | La repetición se corta con número de orden | Dos pruebas: con y sin |
| 4 | Con m−1 firmas no se dispone | Prueba de umbral |
| 5 | La correlación se analiza | Informe por guardián |
| 6 | El procedimiento responde las siete preguntas | Revisión del documento |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Repetición de una firma | La operación se ejecuta dos veces | Número de orden por cuenta |
| Dirección mal tecleada | Fondos irrecuperables | Codificación con verificación |
| Guardianes correlacionados | El umbral es menor del nominal | Diversidad efectiva |
| Clave perdida | Pérdida definitiva | Procedimiento de recuperación |
| Firma a ciegas | Se firma algo que no se vio | Mostrar siempre el contenido |
| Entropía insuficiente | La clave se reconstruye | Generador criptográfico |

## Pruebas

```bash
python -m pytest tests/test_dlt_financial_lab.py -q -k firma
```

## Entregables

- Firma y verificación funcionales.
- Las cuatro pruebas negativas.
- El esquema m-de-n con su análisis de correlación.
- El procedimiento de recuperación con las siete preguntas.
- `solution.md` con qué demuestra y qué no demuestra una firma.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Firma y verificación | 20 |
| Pruebas negativas completas | 30 |
| Firma múltiple y umbral | 20 |
| Análisis de correlación | 15 |
| Procedimiento de recuperación | 15 |

## Solución de referencia

En [`solutions/lab-02.md`](../solutions/lab-02.md).
