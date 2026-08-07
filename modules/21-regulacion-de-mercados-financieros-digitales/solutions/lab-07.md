# Solución de referencia — Laboratorio 7: resiliencia y terceros críticos

> Material docente.

## 41 proveedores, 3 infraestructuras, 86,4 % de concentración

Las veintidós entidades cumplían individualmente la norma de externalización. El riesgo del conjunto no lo veía ninguna, porque ninguna tenía por qué mirarlo: estaba fuera de todos los perímetros a la vez.

## La diversificación aparente

```python
def test_contar_proveedores_oculta_la_concentracion_documenta_el_problema():
    por_proveedor = mapa.concentracion_por_proveedor()
    por_infraestructura = mapa.concentracion_por_infraestructura()

    assert max(por_proveedor.values()) < 0.50   # ninguno parece crítico
    assert por_infraestructura["C"] == pytest.approx(0.864, abs=0.005)
```

**Esta prueba debe pasar.** Ningún proveedor llega al 50 % y una infraestructura llega al 86,4 %. La declaración inicial de 41 proveedores era cierta y describía un sector diversificado que no existe.

## Por qué los contratos no bastan

```text
19 entidades con derecho de auditoría sobre C
  si las 19 lo ejercen a la vez, C dedica
  su año a atender auditorías

19 estrategias de salida hacia los mismos
  dos alternativos
  si las 19 salen a la vez, no hay capacidad
```

Los derechos individuales están bien redactados y no escalan al riesgo colectivo. Es la razón por la que la norma de externalización clásica, pensada para relaciones bilaterales, se queda corta aquí.

## La comparación de respuestas

```text
MIGRACIÓN FORZOSA
  10 entidades × 240 000 = 2 400 000
  y la concentración quedaría en el 40 %

DESIGNACIÓN Y VIGILANCIA DIRECTA
  supervisor 135 000 + proveedor 280 000
  = 415 000 al año
```

La migración cuesta seis veces más y deja el riesgo en un nivel que sigue siendo alto, porque solo hay tres proveedores con capacidad real. La designación ataca el problema donde está.

## El gradiente de pruebas

```text
1 revisión documental      no demuestra nada
2 simulación de escritorio  se conoce el plan
3 entorno aislado           el procedimiento funciona
4 conmutación planificada   la arquitectura aguanta
5 conmutación no anunciada  la organización aguanta
```

La mayoría se queda en el nivel 2 y reporta haber probado la continuidad. Declarar el nivel en el informe es lo que convierte esa afirmación en información.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Contar proveedores | Contar infraestructuras |
| Tolerancia por sistema | Se fija por función y en el consejo |
| Confiar en el contrato | No escala al riesgo colectivo |
| Salida sin probar | Migrar un subconjunto |
| Reportar pruebas de escritorio | Declarar el nivel de la prueba |

## Límites

- El mapa depende de que las entidades declaren la subcontratación; lo que no se declara no aparece, y esa es su principal limitación.
- El umbral de designación del 40 % es un **supuesto**: cada jurisdicción fija el suyo y algunas no lo tienen.
- El coste de migración es una estimación media; en la práctica varía mucho según la función.
