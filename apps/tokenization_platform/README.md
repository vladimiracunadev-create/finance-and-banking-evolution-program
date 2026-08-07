# Tokenization Platform

Plataforma de tokenización didáctica de la **Parte 21**. Cinco módulos que
implementan el registro de referencia, la emisión, el ciclo de vida, la entrega
contra pago atómica y el colateral, **con la biblioteca estándar y sin red**.

> ## Aviso
>
> **Todo lo que hay aquí es didáctico y trabaja con datos sintéticos.** No emite
> ningún valor, no se conecta a ninguna red, no mueve fondos y **no recomienda
> ninguna inversión**. Las plataformas de producción exigen autorización,
> auditoría y controles que este material no reproduce.

## Qué demuestra ejecutando

Cinco afirmaciones que se repiten en el material comercial y se comprueban poco:

| Afirmación habitual | Lo que la plataforma demuestra | Clase |
|---|---|---|
| «Liquidación atómica con el registro oficial» | Un espejo lo impide por construcción | 2 |
| «Hubo 3,75 veces de demanda» | La mayor parte es artificial sin bloqueo | 4 |
| «El cupón es automático» | Falla si el emisor no aprovisiona | 5 |
| «Es atómico» | Se demuestra por la ausencia de estado intermedio | 8 |
| «El recorte es del 5 %, hay margen» | La cascada la produce vender entero | 14 |

## Estructura

```text
apps/tokenization_platform/
├── README.md
├── __init__.py
├── registry.py    espejo, bloqueo de origen, divergencia y conciliación
├── issuance.py    libro de órdenes, adjudicación y emisión desierta
├── lifecycle.py   cupón con verificación previa, inmovilización, vencimiento
├── settlement.py  entrega contra pago atómica y sus modos de fallo
├── collateral.py  recorte, llamada de margen y cascada
└── cli.py
```

## Uso

Comparar el espejo con el bloqueo de origen:

```bash
python apps/tokenization_platform/cli.py registry
```

Ver cuánta demanda es artificial y qué hace el bloqueo del importe:

```bash
python apps/tokenization_platform/cli.py issuance
```

Pagar un cupón con incidencias, inmovilización y vencimiento:

```bash
python apps/tokenization_platform/cli.py coupon
```

Comprobar que no existe estado intermedio observable:

```bash
python apps/tokenization_platform/cli.py settlement
```

Provocar una cascada de liquidaciones y apagarla:

```bash
python apps/tokenization_platform/cli.py collateral --drop 0.12
```

## Pruebas

```bash
python -m pytest tests/test_tokenization_platform.py -q
```

Tres de ellas **documentan defectos y deben pasar**:

- `test_el_espejo_no_permite_atomicidad_documenta_el_problema`
- `test_sin_aprovisionamiento_no_se_paga_a_nadie_documenta_el_problema`
- `test_liquidar_posiciones_enteras_produce_cascada_documenta_el_problema`

Sin ellas, el material afirmaría cosas que el código no sostiene.

## Decisiones de diseño que conviene mirar

**El liquidador rechaza antes de bloquear.** Una reversión implica que hubo un
estado intermedio, y en ese estado alguien pudo actuar. Rechazar no deja rastro.

**`observar()` existe para poder probar una ausencia.** La atomicidad no se
demuestra midiendo velocidad: se demuestra comprobando que ningún estado
observable tiene un tramo movido y el otro no.

**El liquidador se niega si el dinero está fuera del registro.** Lanza
`NoHayAtomicidad` en vez de ejecutar algo que se le parece. Es la condición de la
clase 8 hecha código.

**El pago de cupón verifica antes de empezar.** Un contrato que paga por orden
hasta quedarse sin fondos divide a los tenedores en dos grupos sin ningún
criterio. Si no alcanza, no paga a nadie.

**Al vencer solo se destruye lo confirmado.** Destruir todas las unidades a la
vez deja sin instrumento —y sin prueba de su derecho— a quien todavía no cobró.

**La inmovilización exige dos aprobadores distintos** y solo inmoviliza: no
transfiere ni altera saldos. Es el interruptor de la Parte 19, clase 8, aplicado
a un titular.

**`liquidacion_parcial` está en el sistema de colateral para poder compararlo.**
Es la corrección más eficaz de la clase 14 y no toca ningún parámetro de riesgo.

## Límites declarados

- La plataforma corre en un solo proceso: no modela concurrencia, latencias de
  red ni la mensajería real entre un depositario y una plataforma.
- Los costes de conciliación, resolución y financiación son **supuestos
  declarados** y están en constantes visibles: cambiarlos cambia la conclusión.
- El impacto de mercado en el módulo de colateral es proporcional al volumen
  frente a la profundidad al 1 %; en tensión el libro desaparece y no es lineal.
- El modelo de reintento de cupones se describe en la clase y **no se
  implementa**: exige un calendario y un sistema de notificación.
- Todos los instrumentos, libros de órdenes, carteras y posiciones son
  **sintéticos** y no representan a ningún emisor ni plataforma real.

## Referencias

- [Parte 21 — Tokenización, FX on-chain y mercados programables](../../modules/20-tokenizacion-fx-onchain-y-mercados-programables/README.md)
- [`apps/onchain_fx_lab/`](../onchain_fx_lab/README.md)
- [Etapa 5](../../docs/etapa-5-finanzas-digitales.md)
