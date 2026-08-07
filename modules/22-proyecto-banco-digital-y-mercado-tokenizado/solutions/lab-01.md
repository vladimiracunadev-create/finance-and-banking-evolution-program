# Solución de referencia — Laboratorio 1: alcance y decisiones de arquitectura

> Material docente.

## Once funciones, cuatro incluidas y el mismo ingreso

Reducir el alcance no fue una decisión de prudencia sino de aritmética: siete de las once funciones no tenían quien las necesitara en el segmento, y por eso excluirlas no bajó el ingreso ni un peso.

## La prueba que lo demuestra

```python
def test_reducir_el_alcance_no_baja_el_ingreso_documenta_el_problema():
    ingreso_con_todas = a.ingreso
    excluidas = a.excluir_las_que_no_aportan()

    assert excluidas == 3
    assert a.ingreso == ingreso_con_todas   # <- NO BAJA
```

**Esta prueba debe pasar.** El ingreso es idéntico antes y después porque las funciones excluidas tenían ingreso cero: nadie del segmento las pedía. Lo que cambió fue el coste y el número de regímenes.

## Las cuatro preguntas

```text
1 ¿QUIÉN LA NECESITA?   un segmento concreto
2 ¿QUÉ PAGA POR ELLA?   una cifra
3 ¿QUÉ CUESTA SERVIRLA? otra cifra
4 ¿QUÉ DECISIÓN OBLIGA? y si condiciona otras

SI LA 1 ES «TODOS» O LA 2 ES «NADA»,
LA FUNCIÓN SE EXCLUYE
```

La primera es la que más elimina. «Todos» no es un segmento: es la señal de que nadie se preguntó a quién se sirve.

## La exclusión exige su razón

```python
with pytest.raises(ValueError):
    a.excluir("custodia digital", razon="")
```

Es una decisión de diseño deliberada. Una exclusión sin razón escrita reaparece en la reunión siguiente, y el equipo vuelve a discutirla desde cero.

## La cifra que decide si el proyecto existe

```text
carga regulatoria anual        404 000
facturación necesaria        1 836 364

  antes de ganar nada
```

Si el mercado objetivo no soporta esa facturación, el proyecto no es viable por mucho que la tecnología funcione. Saberlo en la clase 1 ahorra las diecisiete siguientes.

## La salida manda sobre el coste

```python
def test_la_salida_manda_sobre_el_coste_documenta_el_problema():
    componente = _sin_salida()
    assert componente.coste_integrar(5) < componente.coste_construir(5)

    decision, motivo = componente.decidir()
    assert decision is DecisionBuild.CONSTRUIR
    assert "dependencia estructural" in motivo
```

**Esta prueba también debe pasar.** Integrar el registro de colateral es más barato y aun así se construye: sin proveedor alternativo, el coste de abandonarlo no es la migración sino rehacerlo entero.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Incluir todo lo aprendido | Muchas cosas mal en vez de pocas bien |
| Exclusión sin razón | Reaparece en la reunión siguiente |
| Segmento «todos» | Es la señal de que no hay segmento |
| Carga regulatoria al final | Decide si el proyecto existe |
| Comparar solo el coste inicial | La salida es lo que decide |

## Límites

- Los ingresos y costes por función son **supuestos declarados**; con otro segmento las conclusiones cambian.
- El modelo no incluye el efecto de red entre funciones: en algunos negocios una función sin ingreso propio sostiene a otra.
- La carga regulatoria por régimen es una media: en la práctica varía mucho según la actividad.
