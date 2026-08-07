# Solución de referencia — Laboratorio 8: colateral con llamada de margen

> Material docente.

## Liquidar posiciones enteras produce la cascada

Es el hallazgo del laboratorio y de la clase 14.

```python
def test_liquidar_posiciones_enteras_produce_cascada_documenta_el_problema():
    entera = _sistema(parcial=False)
    entera.cascada(0.12)

    assert len(entera.vueltas) >= 5
    assert entera.vueltas[0].impacto > 0.05
```

**Esta prueba debe pasar.** Y la comparación es lo que enseña:

```text
CAÍDA INICIAL DEL 12 %

  LIQUIDACIÓN ENTERA
    vuelta 1: 62 liquidadas · vendido 24 200 556 · impacto 10,08 %
    vuelta 2: 43 liquidadas · vendido 17 298 387 · impacto  7,21 %
    vuelta 3: 34 liquidadas · vendido 13 879 198 · impacto  5,78 %
    ... continúa hasta agotar el límite de vueltas

  LIQUIDACIÓN PARCIAL
    vuelta 1: 62 liquidadas · vendido  5 748 638 · impacto  2,40 %
    vuelta 2:  9 liquidadas · vendido    664 579 · impacto  0,28 %
    vuelta 3:  1 liquidada  · vendido     71 088 · impacto  0,03 %
    vuelta 4:  0 → SE APAGA
```

**La corrección más eficaz no toca ningún parámetro de riesgo.** El recorte, los
umbrales y el ratio exigido son idénticos: lo único que cambia es vender lo
justo en vez de la posición entera.

## El recorte estaba bien calculado y era irrelevante

```python
r = recorte(0.018, 2.33, 0.0015, 0.0005)
c = colchon_implicito(1.50, 1.20)

assert r == pytest.approx(0.0439, abs=0.0005)
assert c == pytest.approx(0.20, abs=0.001)
```

```text
RECORTE = 4,39 %
  volatilidad × confianza   1,8 % × 2,33 = 4,19 %
  impacto de mercado                       0,15 %
  coste de operación                       0,05 %

  cubre lo que pasa DESPUÉS de decidir liquidar

COLCHÓN IMPLÍCITO = 20,00 %
  del ratio exigido (150 %) al umbral (120 %)

  cubre lo que pasa ANTES de decidir liquidar

SON DOS COSAS DISTINTAS Y SE CONFUNDEN
CON FRECUENCIA.
```

Quien las confunde concluye que hay sobrecobertura del 33 % y que el sistema es
holgado. No lo era.

## La distribución de umbrales es lo que decide

```text
340 POSICIONES · RATIOS ENTRE 115 % Y 233 %

CAÍDA DEL 12 % → todos los ratios × 0,88

  las posiciones con ratio inicial < 136 %
  cruzan el umbral de liquidación

  → 62 posiciones a liquidar en la primera vuelta
```

Sin esta medición no se puede saber si una caída dispara una cascada o se apaga
sola. Y el dato no está publicado en ninguna parte: hay que construirlo.

## El volumen frente a la profundidad

```text
LIQUIDACIÓN ENTERA · VUELTA 1
  62 posiciones × 390 331 de colateral medio
  = 24 200 556 a vender

  profundidad al 1 %        2 400 000
  → 10,08 veces la profundidad
  → impacto del 10,08 %

LIQUIDACIÓN PARCIAL · VUELTA 1
  se vende solo lo necesario para volver al 150 %
  = 5 748 638
  → 2,40 veces la profundidad
  → impacto del 2,40 %

EL VOLUMEN SE REDUCE A UNA CUARTA PARTE
Y EL IMPACTO CON ÉL.
```

## La pausa

```python
sistema.pausa_si_cae_mas_de = 0.08
sistema.cascada(0.12)

assert sistema.pausado
assert sistema.vueltas[0].liquidadas == 0
```

La pausa es el control más eficaz y el más criticado, porque deja posiciones
infragarantizadas mientras dura. El intercambio es real:

```text
CON PAUSA      protege de la cascada
               expone al movimiento genuino

SIN PAUSA      la cascada no encuentra freno

MITIGACIÓN
  pausa con límite de tiempo, ampliación del plazo
  de aportación y notificación inmediata al deudor
```

## El punto de amplificación

```text
PROBANDO DISTINTAS CAÍDAS INICIALES

  · 6 %  →  9 liquidaciones → impacto 2,0 % → se apaga
  · 9 %  → 16 liquidaciones → impacto 3,5 % → se apaga
  · 12 % → 62 liquidaciones → impacto 10,1 % → CRECE

  PUNTO DE AMPLIFICACIÓN ≈ 10,5 % DE CAÍDA

CON UNA VOLATILIDAD DIARIA DEL 1,8 %
  una caída del 10,5 % está a 5,8 desviaciones en un día
  ... o a 2,3 en una semana
```

Y con las cuatro correcciones aplicadas, el punto sube a un supuesto 21 %.

## La llamada de margen

| Parámetro | Valor | Justificación |
|---|---|---|
| **Umbral** | 135 % | Deja un 12,5 % de margen antes de liquidar |
| **Plazo** | 4 horas | Permite vender ordenadamente y aportar |
| **Importe** | Lo necesario para volver al 150 % | No la posición entera |
| **Consecuencia** | Liquidación **parcial** escalonada | Máximo el 20 % de la profundidad por ventana |

### Vía de excepción

```text
1 QUIÉN
    el responsable de riesgos, con suplente designado

2 JUSTIFICACIÓN
    fallo verificado del sistema de notificación,
    caída del mercado superior al 8 % en una hora,
    o causa acreditada del deudor con doble aprobación

3 REGISTRO
    quién, cuándo, por qué, quién aprobó, en un
    registro inalterable

4 REVISIÓN POSTERIOR
    muestreo mensual del 10 % de las prórrogas
    y reporte trimestral al comité
```

Un plazo de cuatro horas es razonable; uno de cuatro minutos no permite nada, y
**liquidar es siempre peor que dejar aportar**.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Recorte por analogía | Se copia de un activo cien veces más profundo |
| Confundir recorte y colchón | Cubren momentos distintos |
| Liquidar posiciones enteras | Es lo simple de programar y lo que rompe |
| Ignorar la distribución de umbrales | Es lo que decide la cascada |
| Plazo de minutos | Nadie puede aportar |
| Sin pausa por caída | La cascada no encuentra freno |

## Límites

- El impacto de mercado es proporcional al volumen frente a la profundidad al
  1 %: es una aproximación lineal, y en tensión el libro desaparece.
- El modelo no repone el libro entre vueltas de la misma cascada, lo que es
  conservador para el caso enteras y realista en un episodio rápido.
- La distribución de ratios es sintética y uniforme; una cartera real suele estar
  concentrada cerca del umbral, lo que empeora el resultado.
- El punto de amplificación se halla por prueba y error sobre este conjunto de
  posiciones: cambia con cada cartera y hay que recalcularlo.
