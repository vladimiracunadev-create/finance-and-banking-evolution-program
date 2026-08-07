# Solución de referencia — Laboratorio 4: salvaguarda y segregación

> Material docente.

## Dos documentos separan el 18 % del 99,5 %

La entidad tenía cuenta segregada, contrato específico y una declaración correcta en su web. Lo que decidía si el cliente recuperaba el 44,8 % o el 97,3 % eran dos documentos que no existían, y ninguna inspección de conducta los habría echado en falta.

## La tercera pregunta es la que falla

```python
def test_la_salvaguarda_falla_en_la_renuncia_a_compensar_documenta_el_problema():
    salvaguarda = _salvaguarda()
    assert not salvaguarda.acreditada
    assert "renuncia_a_compensar" in salvaguarda.fallos()

    exposicion = salvaguarda.exposicion()
    assert exposicion["por_compensacion"] == 4_200_000
```

**Esta prueba debe pasar.** Cuenta a nombre de clientes y contrato específico son las dos primeras y casi siempre están; la renuncia del banco a compensar es la tercera y casi nunca.

## La exposición se cuantifica

```text
saldo de clientes                68 000 000
por compensación                 −4 200 000
por conciliación semanal           −900 000
RECUPERABLE                      62 900 000  (92,5 %)

con las cuatro resueltas          68 000 000  (100 %)
```

El coste de las dos correcciones es una carta y una modificación contractual. El efecto son 5,1 millones sobre 42 000 clientes, algo más de cien por cliente de media y mucho más para quien tenga saldo mayor.

## La pregunta previa de la custodia

```text
¿ESTÁ CALIFICADO COMO VALOR?  NO

  → el régimen protector de custodia
    de valores no aplica
  → todo depende del contrato
  → y el contrato no prohíbe disponer
```

Esta pregunta va antes que las tres segregaciones, y remite al laboratorio 2. Si el instrumento no es un valor, la protección que muchos dan por supuesta simplemente no está.

## La segregada era asequible

```text
1 840 posiciones × 0,4 × 12 = 8 832 al año
sobre 280 000 000 custodiados = 0,0032 %
```

La decisión de usar cuenta ómnibus no se sostiene por coste. Con un registro programable, una posición por titular no cuesta significativamente más que una global, y esa es una de las ventajas reales y poco citadas de la tokenización.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Auditar solo la conducta | Pregunta qué recupera el cliente |
| Confiar en «cuenta segregada» | Falta la renuncia a compensar |
| Conciliar semanalmente | La diferencia la pagan los clientes |
| Suponer el régimen de valores | Depende de la calificación |
| Ómnibus por coste | 0,0032 % del custodiado |

## Límites

- La recuperación ordinaria del 18 % es un **supuesto**: depende de la masa, de la prelación y del tiempo del concurso.
- El modelo no incluye el seguro de custodia, que en algunos mercados cambia sustancialmente el resultado.
- La verificación documental **no sustituye** una opinión jurídica sobre la oponibilidad de las cláusulas en el concurso.
