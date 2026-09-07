# Solución de referencia — Laboratorio 9: conciliación de custodia

> Material docente. No constituye una opinión contable, legal ni de auditoría.

## Resultado ejecutivo

El mayor cuadra en USD 7 000 000, pero solo hay USD 6 450 000 disponibles. La
institución muestra activos brutos por 102,14 % de sus pasivos de clientes y,
al mismo tiempo, tiene cobertura disponible de 92,14 %: faltan USD 550 000.

| Medida | Resultado |
|---|---:|
| Activos propios | 1 800 000 |
| Pasivos propios | 1 350 000 |
| Patrimonio | 450 000 |
| Pasivos de clientes | 7 000 000 |
| Activos custodiados brutos | 7 150 000 |
| Activos custodiados disponibles | 6 450 000 |
| Diferencia disponible | **−550 000** |

Los USD 6 450 000 no se suman a los USD 1 800 000 de activos propios. Hacerlo
presentaría fondos de clientes como recursos de la compañía.

## Roll-forward

```text
6 800 000 + 1 000 000 − 600 000 − 150 000 − 50 000 = 7 000 000
```

Diferencia del mayor: cero. La inferencia permitida es «las partidas provistas
reconstruyen el cierre»; no es «hay activos suficientes».

## Conciliación por activo

| Activo | Bruta | Disponible | Diferencia disponible |
|---|---:|---:|---:|
| BTC | 100,00 % | 91,67 % | −200 000 |
| ETH | 103,13 % | 96,88 % | −50 000 |
| USDC | 103,33 % | 90,00 % | −300 000 |
| **Total** | **102,14 %** | **92,14 %** | **−550 000** |

No se compensa BTC con USDC: hacerlo supone vender, encontrar mercado, asumir
precio, plazo y autorización. La diferencia se gestiona por activo.

## Trading

| Libro | Nocional | P/L | Pasivo creado | Colateral inmovilizado |
|---|---:|---:|---:|---:|
| Clientes | 2 000 000 | −150 000 | 150 000 | 400 000 |
| Propio | 1 600 000 | −150 000 | 350 000 | 350 000 |
| **Total** | **3 600 000** | **−300 000** | **500 000** | **750 000** |

La pérdida de clientes sin mandato no deja de ser pérdida porque el ledger la
registre: crea una obligación de restitución, riesgo de fraude y posible
insuficiencia patrimonial.

## Liquidez y decisión

```text
CLIENTES:  6 800 000 − 6 450 000 = 350 000 de brecha 24 h
COMPAÑÍA:  1 400 000 − 1 200 000 = 200 000 de brecha 24 h
```

Decisión de referencia: detener uso y trading de activos de clientes, restringir
nuevas posiciones apalancadas, preservar una regla justa de retiros hasta el
saldo inequívocamente disponible, reponer por activo con fondos propios libres,
confirmar propiedad y gravámenes, y escalar el posible fraude. No usar activos
segregados para cubrir los USD 200 000 de la compañía.

## Separación de funciones

Ana/Bruno/Carla/Diego/Elena/Fátima ocupan, respectivamente, Maker, Checker,
Approver, Executor, Reconciler y Auditor. Ninguna persona prepara, aprueba,
ejecuta y concilia la misma operación.

## Qué no concluye la solución

- No emite una opinión de auditoría.
- No determina el tratamiento jurídico de la segregación.
- No afirma que la valoración USD pueda realizarse sin pérdida.
- No sustituye confirmaciones externas ni evidencia de control de claves.
