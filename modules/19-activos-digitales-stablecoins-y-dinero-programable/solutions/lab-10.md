# Solución de referencia — Laboratorio 10: GAMECO

> Resultado pedagógico bajo supuestos declarados. No es asiento normativo ni
> calificación jurídica universal.

## Clasificación

- Nivel A: unidad interna de acceso; no transferible ni convertible.
- Nivel B: valor transferible de plataforma; existe P2P, pero no cash-out.
- Nivel C: valor convertible; añade payout, liquidez e intermediación potencial.

## Stock y flujo

```text
960.000 + 100.000 sources − 60.000 sinks = 1.000.000 GEM
sinks/sources = 60 %
stock medio = 980.000
velocity = 240.000 / 980.000 = 0,2449
```

La emisión neta de 40.000 aumenta el stock. Si la oferta crece persistentemente
por encima de demanda y sinks, puede caer el poder de compra interno; eso no
convierte GEM en moneda de curso legal.

## Unit economics

```text
pagadores = 10.000 × 5 % = 500
gross bookings = 500 × CLP 12.000 = CLP 6.000.000
```

Con impuesto de 19 % incluido, fee de plataforma de 15 % sobre base sin impuesto,
processing fee de 2 % sobre esa base, refunds de 3 % y chargebacks de 0,5 %, la
recepción neta aproximada es CLP 3,97 millones. Cambiar contrato o base de cada
fee cambia el resultado.

## Cobro, cumplimiento y breakage

Para CLP 5.990 asignados al derecho de 1.000 GEM, con 600 consumidas:

```text
ingreso ilustrativo por ejercicio = CLP 3.594
breakage proporcional ilustrativo = CLP 539,10
ingreso pedagógico total          = CLP 4.133,10
saldo pendiente                   = CLP 1.856,90
```

El 15 % no se reconoce entero al vender: el ejemplo lo reconoce en proporción al
patrón ejercido y sólo bajo el supuesto de que GAMECO espera tener derecho a ese
breakage. Contrato, datos, reembolso, principal/agente y jurisdicción pueden
cambiar el tratamiento.

## Conciliación

`PAID / SETTLED / NOT_CREDITED / EMPTY / NOT_DELIVERED` produce
`cobrado_no_acreditado`. El dueño operativo debe resolver crédito o refund dentro
del plazo definido; Finanzas concilia settlement, ledger e impuesto; Riesgo mide
chargeback y recurrencia. No se cierra el caso porque la interfaz diga «error».

## Perímetro

La fase A requiere revisar contrato, consumidor, datos e impuestos. B añade
transferencia, custodia y fraude. C añade marketplace e intermediación. D exige
revisar payout, pagos, liquidez y AML/KYC potencial. E añade custodia de claves,
mercado externo, activos virtuales y posible calificación financiera según
derechos y promoción. Ningún paso entrega por sí solo una conclusión jurídica.
