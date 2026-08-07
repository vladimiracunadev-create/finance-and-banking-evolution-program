# Solución de referencia — Laboratorio 8: grafo de contagio

> Material docente.

## Exposición cero y 117 millones de necesidad de liquidez

Es el hallazgo del laboratorio y de la clase 14.

```python
def test_exposicion_cero_con_38_millones_en_riesgo_documenta_el_problema():
    grafo = _grafo()
    assert grafo.exposicion_directa("banco") == 0
    assert grafo.exposicion_economica("banco") == pytest.approx(38_050_000, rel=0.001)
```

**Esta prueba debe pasar.** La cifra de «cero» era cierta y completamente
inútil: el indicador que se vigilaba era el único irrelevante.

## Exposición de segundo grado

```text
VÍA F   38 000 000 / 120 000 000 = 31,7 %
        42 000 000 × 31,7 % = 13 300 000

VÍA D  105 000 000 / 340 000 000 = 30,9 %
        68 000 000 × 30,9 % = 21 000 000

VÍA P   12 000 000 /  80 000 000 = 15,0 %
        25 000 000 × 15,0 % =  3 750 000

TOTAL                          38 050 000
```

El método supone **traslado lineal** de la pérdida al capital. En una quiebra no
lo es: sirve para **ordenar** contrapartes, no para predecir el importe exacto, y
así hay que escribirlo en el informe.

## El custodio: cero indirecta, todo el riesgo de liquidez

```python
def test_el_custodio_sin_posicion_propia_no_aporta_exposicion_indirecta():
    assert "C" not in _grafo().exposicion_indirecta("banco")

def test_el_custodio_si_aporta_riesgo_de_liquidez():
    cascada = _grafo().cascada("banco", 0.60, 0.40, 0.35)
    assert cascada["depositos_retirados"] == 63_000_000
```

C no tiene posición propia, pero custodia 900 000 000 por cuenta de clientes. Si
el instrumento se desploma, sus clientes retiran, C tiene un problema de ingresos
y **retira sus depósitos del banco**. C no es una contraparte de crédito del
banco: es su **acreedor mayorista**.

Ninguna fórmula de segundo grado captura este canal.

## La cascada

```text
RONDA 1 · deterioro de contrapartes
  F pierde 19,0 % de su capital
  D pierde 18,5 %
  P pierde  9,0 %
  ninguno cae, pero los tres se deterioran

RONDA 2 · reacción
  disponen el 40 % de sus líneas
  (42 + 68 + 25) × 40 % = 54 000 000

RONDA 3 · custodio
  retira el 35 % de sus depósitos
  180 000 000 × 35 % = 63 000 000

NECESIDAD DE LIQUIDEZ         117 000 000
EXPOSICIÓN DECLARADA                    0
```

## El nodo crítico

```python
def test_el_nodo_critico_no_aparece_en_ningun_balance():
    clave, afectadas = _grafo().nodo_critico()
    assert clave == "proveedor_de_precios:P1"
    assert afectadas == ["D", "F", "P"]
```

F, D y P usan el mismo proveedor de precios. Si ese proveedor falla o publica un
precio erróneo:

```text
  los tres valoran mal a la vez
  los tres liquidan garantías a la vez
  el banco recibe las tres llamadas de liquidez
  el mismo día

→ EL MISMO EFECTO QUE UNA CAÍDA DEL 60 %,
  SIN QUE EL INSTRUMENTO SE MUEVA
```

Y este nodo no está en ningún balance ni en ningún límite. Se descubre leyendo
condiciones de servicio y cuestionarios de contraparte.

## Los cuatro límites propuestos

| Límite | Valor | Método | Frecuencia | Disparador |
|---|---|---|---|---|
| Exposición indirecta de 2.º grado | 5 % del capital | Suma ponderada por fracción en riesgo | Mensual | 80 % informa · 100 % detiene nuevas líneas |
| Concentración por proveedor común | 3 contrapartes relevantes | Mapa de dependencias | Trimestral | Superarlo eleva al comité |
| Depósitos de un custodio de activos digitales | 8 % de los depósitos mayoristas | Saldo medio de 30 días | Mensual | 100 % activa plan de diversificación |
| Líneas a entidades con exposición > 15 % de su capital | Revisión obligatoria | Cuestionario de contraparte | Trimestral | Sin respuesta, se reduce la línea |

## Página de supuestos

```text
· caída del instrumento del 60 %
· traslado lineal de la pérdida al capital
· disposición del 40 % de las líneas comprometidas
· retirada del 35 % de los depósitos del custodio
· que F, D y P usan el mismo proveedor de precios

SI ALGUNO CAMBIA, LA CONCLUSIÓN CAMBIA.
Por eso van en la primera página, no en un anexo.
```

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Reportar «exposición cero» | Es cierto y no informa de nada |
| Ignorar al custodio | Es tu depositante mayorista |
| Olvidar el proveedor de precios | Su fallo equivale a una caída del activo |
| Tratar el lineal como predicción | Falsa precisión |
| Escenarios de un solo nodo | El daño viene de la simultaneidad |
| Supuestos en un anexo | El lector decide sin verlos |

## Límites

- El grafo se construye con la información disponible: estados financieros,
  condiciones de servicio y cuestionarios. Lo que no se declara no aparece, y esa
  es su principal limitación.
- El traslado lineal de pérdidas es una aproximación gruesa; en un concurso la
  recuperación depende de la prelación y del tiempo.
- El modelo no incluye la reacción del banco central ni la de otros acreedores,
  que en la práctica cambian el desenlace.
- Las cinco entidades son sintéticas y no representan a ninguna organización
  real.
