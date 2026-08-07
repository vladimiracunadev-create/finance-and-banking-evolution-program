# Laboratorio 7: Modelo de amenazas

## Propósito

Priorizar las amenazas por **valor detrás del control más débil** y asociar a cada control una prueba ejecutable.

El laboratorio 6 encontró las contradicciones internas. Este busca lo que alguien haría a propósito, y descubre que el punto más barato para un atacante no es el que más se protege.

## Escenario

El sistema completo se somete a la matriz de componentes por actores, y se identifica dónde está el mayor valor detrás del control más débil.

## Contexto

La clase 14 introduce el atacante racional, que compara lo que gana con lo que le cuesta y elige el punto más barato, que casi nunca es el más sofisticado.

## Datos

Los valores acumulados por componente del sistema construido.

## Supuestos del ejercicio

- Saldos de clientes de 91 200 000 y colateral de 24 000 000.
- Las claves del registro controlan todo el sistema.
- La autenticación del cliente es el control de los saldos.

## Requisitos

- Laboratorio 6 completado.
- Haber leído la clase 14.

## Pasos

1. Construye la matriz de componentes por actores.
2. Anota al menos una amenaza por celda, o la razón de por qué no la hay.
3. Calcula el valor acumulado detrás de cada control.
4. Aplica el criterio del atacante racional y ordena.
5. Asocia una prueba ejecutable a cada control.
6. Ejecuta las pruebas y comprueba que fallan cuando el control falla.
7. Declara el riesgo residual con sus cinco elementos.
8. Obtén la aceptación con nombre y fecha.

## Arquitectura

```text
EL ATACANTE RACIONAL

  valor acumulado en el objetivo
  coste de comprometer el control
  probabilidad de deteccion

Y LA PREGUNTA
  ¿donde esta el mayor valor detras
   del control mas debil?
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | La matriz no deja celdas vacías | Amenaza o razón |
| 2 | El valor por control se calcula | Por componente |
| 3 | El orden sale del criterio racional | No de la sofisticación |
| 4 | Cada control tiene una prueba | Ejecutable |
| 5 | Las pruebas fallan si el control falla | Comprobación |
| 6 | El riesgo residual se declara | Cinco elementos y firma |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Priorizar por sofisticación | Los escenarios complejos atraen | Valor sobre control |
| Control sin prueba | Está descrito | Es una intención |
| Componente sin amenazas | Parece seguro | Nadie lo miró |
| Riesgo residual oculto | Incomoda | Da credibilidad |
| Solo amenazas externas | Es el modelo mental | La interna tiene acceso |

## Pruebas

```bash
python -m pytest tests/test_digital_bank_capstone.py -q -k "fuente or correlaciona"
```

```bash
python apps/digital_bank_capstone/cli.py stress
```

## Entregables

- La matriz de componentes por actores completa.
- La priorización por valor sobre control.
- Una prueba ejecutable por control.
- `solution.md` con el riesgo residual declarado y aceptado.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Matriz completa | 20 |
| Priorización racional | 25 |
| Prueba por control | 25 |
| Riesgo residual declarado | 20 |
| Aceptación con firma | 10 |

## Solución de referencia

En [`solutions/lab-07.md`](../solutions/lab-07.md).
