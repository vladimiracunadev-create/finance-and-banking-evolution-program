# Solución de referencia — Laboratorio 6: custodia y segregación

> Material docente.

## Un 3-de-5 puede tener independencia efectiva 1

Es el hallazgo del laboratorio y de la clase 12.

```python
def test_un_3_de_5_puede_tener_independencia_efectiva_1_documenta_el_problema():
    esquema = Esquema(umbral=3, guardianes=[
        Guardian(f"G{i}", "oficina_A", "tipo_X", "cl") for i in range(1, 6)
    ])
    assert esquema.independencia_efectiva() == 1
    assert not esquema.tolera_evento_correlacionado()
```

**Esta prueba debe pasar.** El número «3 de 5» suena prudente y no dice nada: lo
que importa es qué eventos dejan inoperativos a cuántos a la vez.

## La medición

```text
ESQUEMA INICIAL · 3-de-5

  mayor grupo por ubicación        3   ← alcanza el umbral
  mayor grupo por dispositivo      5   ← los tumba a todos
  mayor grupo por jurisdicción     5
  mayor grupo por proveedor        5

  independencia efectiva:          1
  tolera evento correlacionado: False

ESQUEMA CORREGIDO · 3-de-5

  mayor grupo por ubicación        1
  mayor grupo por dispositivo      2
  mayor grupo por jurisdicción     2
  mayor grupo por proveedor        1

  independencia efectiva:          4
  tolera evento correlacionado: True
```

**El umbral no cambió.** Cambió dónde y con qué están las partes.

## Por qué la probabilidad de bloqueo es idéntica

```python
assert esquema.probabilidad_de_bloqueo(0.04) == pytest.approx(0.0006, abs=0.0002)
```

La fórmula binomial solo depende de `n`, `m` y `p`, y **supone independencia**.
Ese supuesto era falso en el esquema inicial y es defendible en el corregido. La
cifra es la misma; su validez, no.

Es el error habitual: calcular una probabilidad antes de comprobar que su
supuesto se sostiene.

## La recuperación

```python
mala  = Recuperacion(umbral=3, tenedores=7, retardo_dias=0, umbral_de_firma=3)
buena = Recuperacion(umbral=4, tenedores=7, retardo_dias=7, umbral_de_firma=3)

assert len(mala.defectos) == 2
assert buena.defectos == []
```

```text
DEFECTOS DE LA MALA
  1 el umbral no supera al de firma:
    es un segundo camino igual de fácil
  2 sin retardo no hay ventana para cancelar

DISEÑO CORRECTO · 4-DE-7
  · 5 guardianes de firma + 2 depositarios que NO firman
  · retardo de 7 días
  · notificación a los 7 por dos canales
  · cualquiera puede CANCELAR durante el retardo

EL RETARDO ES LA PIEZA CLAVE
  un atacante que consigue 4 partes necesita además
  que nadie cancele durante 7 días
```

## El control que detiene el ataque real

```python
def test_la_lista_blanca_con_espera_detiene_la_sesion_comprometida():
    permitida, motivo, horas = politica.evaluar(ataque, "destino_nuevo")
    assert not permitida
    assert horas == 48
```

```text
ESCENARIO: sesión de un operador comprometida

  control 2 lista blanca         → la dirección no está
  control 3 espera de 48 h       → el alta queda pendiente
  control 5 segunda aprobación   → por otro canal

  TIEMPO PARA DETECTAR: 48 horas
  frente a los minutos que habría sin el control 3
```

No es criptográfico. Es una espera, y es el control que más ataques detiene.

## Pago programable frente a dinero programable

| Condición | Tipo | Por qué |
|---|---|---|
| Pagar contra entrega verificada | Pago | La condición se agota al ejecutar |
| Liberar por tramos según hitos | Pago | El destinatario recibe dinero libre |
| Solo gastable en comercios de una lista | **Dinero** | La restricción viaja con la unidad |
| Caducidad a 90 días | **Dinero** | Es una quita encubierta |
| Doble firma sobre un importe | Pago | Actúa sobre la operación |

La prueba: **cuando el dinero llega al destinatario, ¿sigue llevando la
restricción?**

## Vía de excepción

```text
1 QUIÉN
    el responsable de operaciones, con nombre
    y suplente designado. Nunca «el sistema».

2 JUSTIFICACIÓN
    causas previstas (error de dato verificado,
    urgencia médica documentada, fallecimiento)
    más una cláusula abierta con doble aprobación.

3 REGISTRO
    quién, cuándo, por qué, quién aprobó,
    en un registro inalterable.

4 REVISIÓN POSTERIOR
    muestreo mensual del 10 % de las excepciones
    y reporte trimestral al comité.
```

Sin vía de excepción, la automatización convierte cada error en un daño
permanente.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Elegir el umbral por intuición | «3 de 5 suena bien» no es un análisis |
| Todos con el mismo dispositivo | Una vulnerabilidad afecta a los cinco |
| Calcular la probabilidad primero | Su supuesto puede ser falso |
| Recuperación igual de fácil que firmar | Es un segundo camino de ataque |
| Sin espera para destinos nuevos | Es el control que detiene el ataque típico |
| Confiar en la segregación operativa | La jurídica es la que decide en la quiebra |

## Límites

- El modelo de independencia usa cuatro factores; en la práctica hay más
  (proveedor de correo, cadena de suministro, mismo administrador de sistemas).
- La probabilidad de indisponibilidad del 4 % es un supuesto y debe estimarse con
  el histórico de la propia organización.
- La señal de coacción se describe pero no se implementa: exige un simulacro con
  personas, y sin ese simulacro no existe.
- Ningún control criptográfico sustituye a las tres cláusulas contractuales de
  propiedad, no pignoración y verificación independiente.
