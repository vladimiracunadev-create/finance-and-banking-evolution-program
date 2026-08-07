# Laboratorio 1: Alcance y decisiones de arquitectura

## Propósito

Reducir un alcance de once funciones a cuatro y **comprobar que el ingreso no baja**, porque las excluidas no lo generaban.

Es el primer laboratorio del capstone y el que fija el método. Todo lo que viene después se construye sobre las funciones que sobrevivan a este filtro, de modo que un error aquí se paga en las nueve semanas siguientes.

## Escenario

Un equipo propone once funciones para un banco digital dirigido a 2 400 pymes exportadoras. Hay que aplicar las cuatro preguntas, excluir lo que nadie necesita y tomar las tres decisiones de arquitectura.

## Contexto

La clase 1 sostiene que los capstones fracasan por exceso de alcance. Las clases 2 y 4 añaden que la decisión de construir o integrar la manda la salida, y que solo una de las seis preguntas justifica un registro distribuido.

## Datos

Once funciones sintéticas con su segmento, su ingreso y su coste.

## Supuestos del ejercicio

- Coste unitario de 20 al año por cliente.
- Margen del 22 % sobre ingresos.
- Coste del capital del 8 %.

## Requisitos

- Haber leído las clases 1, 2 y 4.
- Python 3.11 o superior.

## Pasos

1. Propón las once funciones con su segmento, ingreso y coste.
2. Aplica las cuatro preguntas y comprueba cuáles no aportan.
3. Excluye las que fallan y verifica que una exclusión sin razón se rechaza.
4. Comprueba que el ingreso no baja tras excluir.
5. Calcula la carga regulatoria con los regímenes restantes.
6. Halla la facturación necesaria y el saldo mínimo por cliente.
7. Decide construir o integrar cada componente con el criterio de la salida.
8. Aplica las seis preguntas del registro distribuido y compara arquitecturas.

## Arquitectura

```text
Alcance
  proponer(funcion)
  excluir(nombre, RAZON)  ← sin razon se rechaza
  excluir_las_que_no_aportan()

Componente.decidir()
  la SALIDA manda sobre el coste:
  sin salida real, integrar es una
  dependencia estructural
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Tres funciones no aportan | Ninguna las necesita |
| 2 | El ingreso no baja al excluir | Comparación antes y después |
| 3 | Una exclusión sin razón se rechaza | Excepción esperada |
| 4 | La carga cae con menos regímenes | 350 000 menos |
| 5 | La salida decide dos componentes | Se construyen aunque integrar sea más barato |
| 6 | Ninguna de las seis preguntas justifica el registro | Con su fundamento |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Incluir todo lo aprendido | Muchas cosas mal en vez de pocas bien | Cuatro preguntas por función |
| Exclusión sin razón | Reaparece en la reunión siguiente | Razón escrita |
| Comparar solo el coste inicial | Se ignora la salida | Coste total con salida |
| Integrar sin alternativa | Dependencia estructural | Construir aunque cueste más |
| Justificar el registro | Ya se decidió usarlo | Las seis preguntas deciden |

## Pruebas

```bash
python -m pytest tests/test_digital_bank_capstone.py -q -k "alcance or exclusion or salida or carga or facturacion"
```

```bash
python apps/digital_bank_capstone/cli.py scope
```

```bash
python apps/digital_bank_capstone/cli.py build
```

## Entregables

- Las cuatro preguntas aplicadas a las once funciones.
- Las exclusiones con su razón escrita.
- La carga regulatoria y la facturación necesaria.
- `solution.md` con las tres decisiones de arquitectura.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Cuatro preguntas aplicadas | 25 |
| Exclusiones con razón | 20 |
| Carga y facturación | 20 |
| Decisión construir o integrar | 20 |
| Seis preguntas del registro | 15 |

## Solución de referencia

En [`solutions/lab-01.md`](../solutions/lab-01.md).
