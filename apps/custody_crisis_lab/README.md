# Custody Crisis Lab

Laboratorio de **crisis de custodia digital**: qué le ocurre a una entidad que
custodia activos de clientes cuando pierde una parte de ellos, y qué tiene que
medir, reponer y comunicar. Siete módulos con la biblioteca estándar y sin red.

> ## Aviso
>
> **Todo lo que hay aquí es didáctico.** Trabaja con datos sintéticos y, en el
> módulo `cases`, con estimaciones públicas del caso de octubre de 2026
> declaradas como **preliminares y sujetas a revisión**. No se conecta a ninguna
> red, no mueve fondos, no recomienda ninguna inversión y no contiene
> herramientas para ocultar fondos ni evadir controles.

## Estructura

```text
apps/custody_crisis_lab/
├── README.md
├── __init__.py
├── entity.py      entidad custodio: activos, pasivos, respaldo bruto y disponible
├── incident.py    sustraído, congelado, restituible, pérdida definitiva
├── runs.py        riesgo de retiros masivos y simulación diaria
├── replenish.py   necesidad de reposición, fuentes y costo de compra
├── costs.py       costo total del incidente y recuperación de seguro
├── recovery.py    trayectoria del respaldo y plan de siete fases
├── cases.py       cifras públicas del caso Binance 2026 y entidad estilizada
├── datos.py       carga de los CSV sintéticos
├── scenario.py    orquestación de un escenario completo
└── cli.py
```

## Uso

```bash
python apps/custody_crisis_lab/cli.py caso --escenario crd_002
```

```bash
python apps/custody_crisis_lab/cli.py fondos --sustraido 6300 --congelado 3000 --p 0.8
```

```bash
python apps/custody_crisis_lab/cli.py plan
```

```bash
python apps/custody_crisis_lab/cli.py binance
```

Datos: [`custody_crisis_balance_synthetic.csv`](../../datasets/schemas/custody_crisis_balance_synthetic.md)
y [`custody_crisis_scenarios_synthetic.csv`](../../datasets/schemas/custody_crisis_scenarios_synthetic.md).

## Pruebas

```bash
python -m pytest tests/test_custody_crisis_lab.py tests/test_openbank_crisis.py -q
```

Tres de ellas **documentan trampas conceptuales y deben pasar**:

- `test_congelado_no_es_recuperado_documenta_el_problema`
- `test_el_costo_no_es_el_monto_sustraido_documenta_el_problema`
- `test_las_fuentes_discrepan_documenta_el_problema`

## Decisiones de diseño que conviene mirar

**Las fórmulas viven en la cabecera de cada módulo.** Variables, unidad,
supuesto y límite están antes del código: quien no pueda decir el supuesto de una
fórmula no debería fiarse de su resultado.

**Los parámetros de comportamiento viven en un CSV.** `r0`, `k`, `p` y el
descuento son hipótesis; verlos en una tabla evita que se escondan en una
fórmula.

**La pérdida mayor que los activos lanza `ValueError`.** Más allá de ese punto la
entidad no tiene activos que contar y el modelo deja de aplicar.

**La entidad del caso de 2026 es estilizada.** Toma como pasivos los «activos
bajo gestión» reportados; es un supuesto del ejercicio y no un dato de la
entidad.

## Límites declarados

- La respuesta lineal de los retiros al deterioro del respaldo es una hipótesis.
- El impacto de mercado lineal subestima el costo en tensión.
- Un único `p` para todo lo congelado simplifica plazos y emisores distintos.
- No modela contagio, litigio, daño reputacional ni clientes futuros.

## Referencias

- [Guía de crisis financiera digital](../../docs/crisis-financiera-digital.md)
- [Ejercicios y evaluación](../../docs/ejercicios-crisis-financiera-digital.md)
- [Caso Binance 2026](../../case-studies/custody/binance-2026.md)
- [Laboratorio de activos digitales](../digital_assets_risk_lab/README.md)
- [Simulador OpenBank y su escenario de crisis](../openbank_simulator/README.md)
