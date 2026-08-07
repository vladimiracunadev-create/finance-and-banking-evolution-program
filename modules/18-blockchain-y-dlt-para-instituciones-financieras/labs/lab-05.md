# Laboratorio 5: Contrato de depósito en garantía

## Propósito

Escribir un contrato con máquina de estados, **introducir el defecto de
reentrada a propósito**, demostrar que vacía el contrato y corregirlo.

## Escenario

Es el contrato de la clase 8: el importador deposita, un verificador confirma y
el contrato libera al exportador. Tu tarea es construirlo, romperlo y arreglarlo.

## Contexto

Un contrato inteligente es código irreversible con dinero dentro. El laboratorio
existe para que veas la diferencia entre «funciona» y «no se puede vaciar».

## Datos

Estado en memoria; sin red ni registro real.

## Supuestos del ejercicio

- El «contrato» es una clase de Python que simula la ejecución sobre un
  registro. No es código de ninguna plataforma real.
- Las llamadas externas se simulan con un objeto que puede reentrar.
- Los importes son enteros.

## Requisitos

- Laboratorio 1 completado.
- Haber leído las clases 8, 9 y 13.

## Pasos

1. Implementa la máquina de estados: `creado`, `fondeado`, `en_disputa`,
   `liberado`, `devuelto`.
2. Implementa los invariantes: el saldo del contrato es la suma de los depósitos
   activos, y ningún depósito se libera y se devuelve.
3. Añade control de acceso por función y prueba que `confirmar` solo la puede
   llamar el verificador.
4. Implementa `retirar` **con el orden incorrecto**: transferir antes de poner
   el saldo a cero.
5. Escribe un beneficiario malicioso que reentre y demuestra que **vacía el
   contrato**.
6. Corrige el orden y demuestra que el ataque ahora falla.
7. Implementa el interruptor de emergencia con firma 2-de-3 y su simulacro.
8. Añade un oráculo de precio con mediana de cinco fuentes y mínimo de fuentes
   vivas.

## Arquitectura

```text
creado ──depositar──► fondeado ──confirmar──► liberado
                          │
                          ├──disputar──► en_disputa ──resolver──► liberado
                          │                                    └─► devuelto
                          └──vencer────► devuelto

invariantes comprobados en cada transición:
  saldo == suma(depósitos activos)
  ningún depósito en dos estados finales
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Transiciones ilegales rechazadas | Prueba por transición |
| 2 | Invariantes se cumplen siempre | Comprobación tras cada operación |
| 3 | `confirmar` solo del verificador | Prueba de acceso |
| 4 | El ataque de reentrada vacía el contrato | Prueba que **debe** pasar |
| 5 | Tras la corrección, el ataque falla | Prueba negativa |
| 6 | El interruptor detiene y no altera | Prueba de estado tras parar |
| 7 | Con menos fuentes vivas, no se publica | Prueba de pausa |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Reentrada | El contrato se vacía | Estado antes de la llamada |
| Función sin control de acceso | Cualquiera libera | Comprobación por función |
| Oráculo manipulado | Liquidación a precio falso | Mediana y mínimo de fuentes |
| Sin interruptor | El daño continúa | Parada con firma múltiple |
| Clave de actualización única | Es la clave de los fondos | Firma múltiple y retardo |
| Transición no prevista | Estado inconsistente | Máquina cerrada |

## Pruebas

```bash
python -m pytest tests/test_dlt_financial_lab.py -q -k contrato
```

```bash
python apps/dlt_financial_lab/cli.py escrow --attack reentrancy
```

## Entregables

- El contrato con máquina de estados e invariantes.
- La demostración del ataque de reentrada, ejecutada.
- La corrección y su prueba negativa.
- El interruptor de emergencia y el resultado del simulacro.
- `solution.md` con la lista de lo que queda fuera del código y por qué.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Máquina de estados e invariantes | 25 |
| Demostración del ataque | 25 |
| Corrección probada | 20 |
| Interruptor y simulacro | 20 |
| Qué queda fuera del código | 10 |

## Solución de referencia

En [`solutions/lab-05.md`](../solutions/lab-05.md).
