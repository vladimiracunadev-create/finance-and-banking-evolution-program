# Laboratorio 2: Emisión y ciclo de vida

## Propósito

Demostrar que **el bloqueo del importe es lo que hace informar al libro de órdenes**, y que un cupón sin verificar el aprovisionamiento no reparte: discrimina.

## Escenario

Una emisión de 30 000 000 recibe demanda por 112 400 000 de 6 800 inversionistas. Después hay que pagar dos cupones con incidencias, aplicar una inmovilización y llegar al vencimiento.

## Contexto

La clase 4 muestra que la sobredemanda es en su mayor parte artificial. La clase 5 muestra que el ciclo de vida es donde se rompen los proyectos, porque la emisión se prueba y el ciclo se improvisa.

## Datos

Libro sintético de 6 800 órdenes y un bono de 30 000 unidades con cupón semestral del 6,4 % anual.

## Supuestos del ejercicio

- Los inversionistas anticiparon un prorrateo del 35 % y multiplicaron su intención por 2,86.
- Coste de financiación del 4,2 % anual sobre 10 días.
- Tres titulares con cuenta bloqueada y uno no localizable.

## Requisitos

- Laboratorio 1 completado.
- Haber leído las clases 3, 4 y 5.

## Pasos

1. Resuelve la adjudicación con los tres mecanismos y anota la ventaja del primero en cada uno.
2. Calcula el coste de bloquear una orden grande durante el período.
3. Estima la demanda genuina declarando el factor de exageración.
4. Añade tramo mínimo y comprueba que redistribuye hacia el pequeño.
5. Ejecuta el escenario de emisión desierta con liberación automática.
6. Toma una instantánea a la fecha de corte y paga el cupón con un aprovisionamiento insuficiente; comprueba que **no paga a nadie**.
7. Repite con el aprovisionamiento completo y clasifica las incidencias.
8. Aplica una inmovilización con doble aprobación y comprueba que el derecho al cupón subsiste.
9. Vence el instrumento y verifica que solo se destruye lo pagado y confirmado.
10. Calcula el coste de un error de una hora en la fecha de corte.

## Arquitectura

```text
EMISION
  ordenar → adjudicar(mecanismo) → Resultado
  bloqueo_obligatorio → coste_del_bloqueo()
                     → la exageracion cuesta dinero

CICLO DE VIDA
  instantanea(corte) → cupon_total() → VERIFICAR
                    → pagar_cupon() → detalle por titular
  vencer(confirmados) → destruye solo lo confirmado
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El orden de llegada da ventaja 1,0 | Primer y último adjudicado |
| 2 | El prorrateo da ventaja 0,0 | Fracciones iguales |
| 3 | El bloqueo tiene coste | Cálculo sobre 500 000 y 10 días |
| 4 | Sin aprovisionamiento no paga a nadie | Excepción esperada |
| 5 | El inmovilizado conserva el derecho | Importe en pendiente |
| 6 | Solo se destruye lo confirmado | Quedan unidades vivas |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Sobredemanda artificial | El libro deja de informar | Bloqueo del importe al ordenar |
| Pago sin verificar fondos | Unos cobran y otros no, sin criterio | Verificación previa que aborta |
| Fecha de corte errónea | Cobra quien no debía | Instantánea verificable y publicada |
| Inmovilización sin doble aprobación | Un solo actor puede aplicarla | Dos aprobadores distintos |
| Destrucción anticipada | El tenedor pierde la prueba de su derecho | Destruir solo lo pagado y confirmado |

## Pruebas

```bash
python -m pytest tests/test_tokenization_platform.py -q -k "prorrateo or bloqueo_del_importe or desierta or cupon or vencer"
```

```bash
python apps/tokenization_platform/cli.py issuance
```

```bash
python apps/tokenization_platform/cli.py coupon
```

## Entregables

- La adjudicación con los tres mecanismos y su ventaja del primero.
- La demanda genuina estimada con su factor declarado.
- El pago de cupón con incidencias clasificadas.
- `solution.md` con la secuencia de vencimiento y su regla de destrucción.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Adjudicación con los tres mecanismos | 20 |
| Efecto del bloqueo del importe | 20 |
| Cupón con verificación previa | 25 |
| Inmovilización con doble aprobación | 20 |
| Vencimiento con destrucción selectiva | 15 |

## Solución de referencia

En [`solutions/lab-02.md`](../solutions/lab-02.md).
