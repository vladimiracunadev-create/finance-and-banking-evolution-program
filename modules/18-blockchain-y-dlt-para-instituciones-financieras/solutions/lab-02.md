# Solución de referencia — Laboratorio 2: firma de transacciones

> Material docente. El esquema de firma es simplificado y didáctico.

## Qué demuestra y qué no demuestra una firma

```text
DEMUESTRA
  que quien poseía la clave privada aprobó ESE contenido

NO DEMUESTRA
  cuándo          → hace falta un sello de tiempo de un tercero
  quién es        → hace falta ligar la clave a una identidad
  que sea verdad  → una firma no valida hechos
  qué se firmó    → si se firma un resumen a ciegas
  que la clave no estuviera comprometida → hace falta revocación
```

Las cinco filas de la derecha son la respuesta a la pregunta del laboratorio.

## Las cuatro pruebas negativas

```python
def test_un_byte_alterado_invalida_la_firma(par):
    mensaje = b"transferir 1000 a acc_02"
    firma = firmar(par.privada, mensaje)
    alterado = b"transferir 9000 a acc_02"
    assert not verificar(par.publica, alterado, firma)


def test_una_direccion_mal_tecleada_se_detecta():
    direccion = derivar_direccion(par.publica)
    con_error = direccion[:-3] + "XYZ"
    assert not direccion_valida(con_error)


def test_sin_numero_de_orden_la_firma_se_reutiliza(cadena_sin_orden):
    tx = firmar_transaccion(par, destino="acc_02", importe=1000)
    cadena_sin_orden.aplicar(tx)
    cadena_sin_orden.aplicar(tx)          # se acepta: DEFECTO
    assert cadena_sin_orden.saldo("acc_02") == 2000


def test_con_numero_de_orden_la_repeticion_se_rechaza(cadena):
    tx = firmar_transaccion(par, destino="acc_02", importe=1000, orden=0)
    cadena.aplicar(tx)
    with pytest.raises(TransaccionInvalida):
        cadena.aplicar(tx)
```

La tercera es la que más cuesta escribir porque **debe pasar**: documenta el
defecto que la cuarta corrige.

## El umbral y su análisis

```text
ESQUEMA 3-DE-5 DEL EJERCICIO

  guardián  ubicación   proveedor de módulo
  ────────────────────────────────────────
  G1        Madrid      Proveedor A
  G2        Madrid      Proveedor A
  G3        Santiago    Proveedor A
  G4        Santiago    Proveedor B
  G5        Lisboa      Proveedor B

ANÁLISIS
  fallo del Proveedor A → se pierden G1, G2, G3 = 3
  quedan 2 < umbral 3   → NO se puede firmar

  incendio en Madrid    → se pierden G1, G2 = 2
  quedan 3 = umbral 3   → se puede firmar, sin margen

CONCLUSIÓN
  el esquema tolera una pérdida de ubicación
  y CERO fallos del proveedor mayoritario
```

Es el mismo hallazgo de la clase 3: contar claves no es contar independencias.

## El procedimiento de recuperación

Las siete preguntas, respondidas:

```text
1. QUÉ SE RECUPERA   la capacidad de firmar, no la clave
2. QUIÉN AUTORIZA    2 del comité + auditoría interna
3. DÓNDE ESTÁN       5 fragmentos, 4 ubicaciones, 2 países
4. INTEGRIDAD        resumen por copia, verificado en cada ensayo
5. ENSAYO            trimestral, con firma real de importe simbólico
6. GUARDIÁN QUE SE VA  rotación de su fragmento en 5 días hábiles
7. TRAS RECUPERAR    rotación completa del esquema
```

El punto 5 con **firma real** es lo que distingue un procedimiento de un
documento.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Solo la prueba positiva | No demuestra nada |
| Omitir la prueba que debe pasar | No se documenta el defecto |
| Contar guardianes | El umbral efectivo es menor |
| Ensayo sin firma real | No prueba que las copias sirvan |
| Implementar criptografía propia en producción | Se usa lo auditado |

## Límites

- El esquema de firma es **simplificado**: no ofrece las garantías de uno real y
  no debe salir del laboratorio.
- No se modela la revocación de claves ni la infraestructura de certificados.
- La entropía del generador es la de la biblioteca estándar; en producción se
  usa un módulo de seguridad.
