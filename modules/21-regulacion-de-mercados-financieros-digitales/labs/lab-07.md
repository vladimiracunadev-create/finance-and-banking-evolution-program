# Laboratorio 7: Resiliencia y terceros críticos

## Propósito

Descubrir que **contar proveedores da una diversificación aparente** y medir la concentración real por infraestructura.

Hasta aquí los laboratorios han mirado a una entidad. Este mira al sector, y encuentra un riesgo que no está en el perímetro de nadie: veintidós entidades cumplen su norma de externalización, cada contrato bilateral es correcto, y el conjunto tiene un punto único de fallo del 86,4 %.

## Escenario

Un supervisor recibe la declaración de 41 proveedores entre 22 entidades. Al pedir la subcontratación descubre que se apoyan en tres infraestructuras.

## Contexto

La clase 14 distingue continuidad, resiliencia y ciberseguridad, y sostiene que la única respuesta proporcionada al riesgo de concentración es supervisar directamente al proveedor. La clase 10 añade la estrategia de transición.

## Datos

Mapa sintético de dependencias con proveedores, infraestructuras y entidades.

## Supuestos del ejercicio

- Umbral de designación del 40 %.
- Coste de migrar una entidad: 240 000 y 9 meses.
- Tolerancia de liquidación de 2 horas.

## Requisitos

- Laboratorio 6 completado.
- Haber leído las clases 10 y 14.

## Pasos

1. Construye el mapa registrando cada proveedor con su infraestructura.
2. Calcula la concentración por proveedor y comprueba que ninguno parece crítico.
3. Calcula la concentración por infraestructura y compárala.
4. Aplica el umbral de designación y anota qué infraestructuras lo superan.
5. Calcula cuántas entidades incumplirían su tolerancia ante un fallo.
6. Compara diversificación forzosa con designación, con sus costes.
7. Diseña la prueba sectorial y declara su nivel en el gradiente.
8. Redacta la estrategia de transición con sus seis elementos.

## Arquitectura

```text
MapaDeTerceros
  registrar(proveedor, INFRAESTRUCTURA)
  depende(entidad, proveedor)

  concentracion_por_proveedor()
     → diversificacion APARENTE
  concentracion_por_infraestructura()
     → la real

  criticos(umbral)  las que hay que designar
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Ningún proveedor supera el 50 % | Diversificación aparente |
| 2 | Una infraestructura llega al 86,4 % | Concentración real |
| 3 | El umbral se aplica sobre infraestructuras | No sobre proveedores |
| 4 | Un proveedor desconocido falla | Excepción esperada |
| 5 | La comparación de costes se hace | Migración frente a designación |
| 6 | La prueba declara su nivel | Del gradiente de cinco |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Contar proveedores | Es el dato declarado | Contar infraestructuras |
| Tolerancia por sistema | La fija el área técnica | Se fija por función y en el consejo |
| Confiar en el contrato | Está bien redactado | No escala al riesgo colectivo |
| Salida sin probar | Migrar es caro | Migrar un subconjunto |
| Reportar pruebas de escritorio | Cumplen el requisito | Declarar el nivel de la prueba |

## Pruebas

```bash
python -m pytest tests/test_regulatory_perimeter_engine.py -q -k "proveedores or umbral_de_designacion or desconocido"
```

```bash
python apps/regulatory_perimeter_engine/cli.py compliance
```

## Entregables

- El mapa de dependencias con subcontratación.
- La concentración por proveedor y por infraestructura.
- La comparación entre migración y designación.
- `solution.md` con la prueba sectorial y su nivel.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Mapa construido | 20 |
| Contraste de las dos concentraciones | 30 |
| Umbral aplicado correctamente | 20 |
| Comparación de respuestas | 15 |
| Prueba sectorial con nivel | 15 |

## Solución de referencia

En [`solutions/lab-07.md`](../solutions/lab-07.md).
