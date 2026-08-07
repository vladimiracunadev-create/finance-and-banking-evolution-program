# Cross-Border Payments Lab

Laboratorio de pagos transfronterizos de la **Parte 18**. Modela los cuatro
flujos de un pago, el motor de rutas, la mensajería ISO 20022, el screening, la
liquidación con pago contra pago y las arquitecturas alternativas —enlace de
pagos inmediatos y ruta con stablecoin—, **sin red, sin dependencias y sin mover
un solo fondo**.

> No es un sistema de pagos. Es material formativo: no se conecta con ninguna
> red real, no liquida nada y no sustituye la normativa de cambios
> internacionales aplicable.

## Qué demuestra ejecutando

| Componente | Decisión de diseño que demuestra | Clase |
|---|---|---|
| `flows` | El mensaje tarda segundos y el dinero, horas o días | 2, 5 |
| `routing_engine` | Un filtro de cumplimiento **no** se compensa con precio | 12, 16 |
| `iso20022` | La referencia se genera una vez y sobrevive al reintento | 6 |
| `screening` | Descartar por falta de dato es el falso negativo a evitar | 12 |
| `remittances` | El diferencial cruzado se **compone**, no se suma | 1, 9, 10 |
| `settlement` | La exposición es el máximo simultáneo, no la operación mayor | 7, 8, 15 |
| `fast_payment_link` | El alias inexistente responde igual que el sin cuenta | 13 |
| `stablecoin_route` | El 97 % del ahorro viene de la topología, no del registro | 14 |

## Estructura

```text
apps/cross_border_payments_lab/
├── README.md
├── __init__.py               # build(): monta el laboratorio completo
├── flows/                    # mensaje, fondos, contable, cumplimiento
├── routing_engine/           # tres filtros y tres factores
├── iso20022/                 # pacs.008, pacs.002 y máquina de estados
├── screening/                # métricas y prueba retrospectiva
├── remittances/              # comparador con el denominador honesto
├── settlement/               # exposición, PvP, netting y liquidez
├── fast_payment_link/        # alias, subasta y cobertura real
├── stablecoin_route/         # comparación y descomposición del ahorro
├── data/                     # plazas, corredores, rutas, mensajes, operaciones
└── cli.py
```

## Uso

Trazar los cuatro flujos y ver dónde está realmente el tiempo:

```bash
python apps/cross_border_payments_lab/cli.py trace --corridor CL-VN --amount 10000
```

Elegir la ruta de un pago y ver el motivo y las descartadas:

```bash
python apps/cross_border_payments_lab/cli.py route --corridor C --amount 20000
```

Comparar la ruta clásica con la de stablecoin y descomponer el ahorro:

```bash
python apps/cross_border_payments_lab/cli.py compare-routes --amount 20000
```

Ejecutar el escenario de fallo del coordinador en un pago contra pago:

```bash
python apps/cross_border_payments_lab/cli.py pvp --scenario coordinator-failure
```

Validar los mensajes ISO 20022 y ejecutar las pruebas:

```bash
python tools/validate_iso20022.py && python -m pytest tests/test_cross_border_payments_lab.py -q
```

## Los seis corredores

Cada uno fuerza una decisión distinta del motor de rutas:

| Corredor | Característica | Ruta que debe elegir |
|---|---|---|
| A | Enlace de pagos inmediatos disponible | `A-enlace` |
| B | Cadena clásica de un intermediario | `B-clasica` |
| C | Cadena clásica de tres intermediarios | `C-stablecoin` |
| D | La ruta alternativa no soporta la regla del viaje | `D-clasica` |
| E | Diferencia horaria grande | Depende de los pesos |
| F | Receptor sin cuenta | `F-efectivo` |

El corredor D es el importante: la ruta con stablecoin es más barata y **queda
descartada por el filtro de cumplimiento**. Ese es el comportamiento que la
Parte 18 exige y que una implementación que pondere el cumplimiento no tendría.

## Datos

Todos sintéticos y generados con semilla fija:

- 6 plazas con huso, horario y calendario de festivos;
- 12 rutas repartidas en 6 corredores;
- 180 operaciones de cambio para el cálculo de exposición;
- 3 mensajes `pacs.008` completos;
- 4 alias para el directorio del enlace.

Además, en `datasets/synthetic/`: 36 rutas de remesas por 9 corredores y 12 000
alertas de screening con su resolución etiquetada.

**Ninguna lista, nombre, entidad ni identificador corresponde a algo real.**
`tools/detect_pii.py` lo comprueba en cada ejecución de CI.

## Límites declarados

- **No hay liquidación real.** Los estados y las ventanas se simulan.
- **La validación ISO 20022 cubre un subconjunto de campos**, no el esquema
  oficial ni las guías de uso vigentes.
- **Las listas de screening son sintéticas** y no reproducen la distribución de
  ninguna lista oficial. El módulo no sirve para calibrar un sistema real.
- **Los costes y plazos son ilustrativos**: los valores reales cambian por
  corredor y por mes.
- **La stablecoin es sintética**: su diseño, reservas y regulación son materia
  de la Parte 20 y aquí no se modelan.
- **No se prueba carga sostenida** ni comportamiento bajo partición de red.
- Los proyectos institucionales citados en la Parte 18 son pilotos o pruebas de
  concepto; este laboratorio **no reproduce ninguno de ellos**.

## Referencias

- [Parte 18 — Pagos transfronterizos, remesas y liquidación](../../modules/17-pagos-transfronterizos-remesas-y-liquidacion/README.md)
- [Mapa de pagos transfronterizos](../../docs/mapa-pagos-transfronterizos.md)
