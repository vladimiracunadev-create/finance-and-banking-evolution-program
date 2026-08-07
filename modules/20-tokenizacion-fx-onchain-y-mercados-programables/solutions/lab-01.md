# Solución de referencia — Laboratorio 1: registro de referencia y divergencia

> Material docente.

## Un espejo nunca permite atomicidad

Es el hallazgo del laboratorio y de la clase 2.

```python
def test_el_espejo_no_permite_atomicidad_documenta_el_problema():
    espejo  = Emisor(Configuracion.ESPEJO)
    bloqueo = Emisor(Configuracion.BLOQUEO_DE_ORIGEN)

    assert not espejo.permite_atomicidad
    assert bloqueo.permite_atomicidad
```

**Esta prueba debe pasar.** No es una limitación de la implementación: con un
espejo, la transferencia del token no es válida hasta que la confirma el
registro oficial, y ese intervalo es un estado intermedio observable. Un
proyecto que promete entrega contra pago atómica y mantiene el registro oficial
como referencia promete algo que su propia arquitectura impide.

**Cómo detectarlo en una propuesta:** busca la frase «se refleja en el
depositario central». Si está, no hay atomicidad.

## El bloqueo de origen no deja dos versiones activas

```python
emisor.emitir("inv", 1_000)
emisor.bloquear_y_representar("inv", 400)

assert emisor.oficial.saldo("inv") == 600
assert emisor.token.saldo("inv")   == 400
assert emisor.oficial.saldo("inv") + emisor.bloqueado["inv"] == 1_000
```

En cada momento, para cada unidad, **solo un registro está operativo**. No hay
divergencia estructural posible porque no hay dos versiones que puedan diferir.

## Las seis causas, y cuáles vienen de fuera

```text
FALLO DE PROPAGACIÓN    dentro   automatizable
ORDEN DISTINTO          dentro   automatizable
ERROR OPERATIVO         dentro   automatizable
ATAQUE                  dentro   automatizable
EVENTO CORPORATIVO      FUERA    ninguna automatización lo cubre
DECISIÓN JUDICIAL       FUERA    ninguna automatización lo cubre
```

Las dos últimas son la razón por la que hay que designar una autoridad de
resolución **antes** de emitir: vienen de fuera del sistema y no tienen una
condición verificable en el registro.

## La congelación alcanza a los dos registros

```python
emisor.congelar("a")

with pytest.raises(SaldoCongelado):
    emisor.oficial.transferir("a", "b", 100)
with pytest.raises(SaldoCongelado):
    emisor.token.transferir("a", "b", 100)
```

Congelar solo uno agrava el problema: el saldo sigue moviéndose en el otro y la
diferencia crece mientras se investiga.

## Resolver exige una autoridad designada

```python
with pytest.raises(SinAutoridadDeResolucion):
    emisor.resolver("a", 1_000)
```

Es una decisión de diseño deliberada: el código se niega a resolver si nadie
declaró quién decide. Si esa decisión no está tomada antes del conflicto, la
tomará un tribunal, tarde y caro.

## La ventana

```text
OPERACIONES MENSUALES        2 770 sobre 6 400 partícipes
DISTRIBUCIÓN                 el 5 % activo hace el 60 %
  320 partícipes con 1 662 operaciones
  → 5,2 operaciones por partícipe y mes
  → una cada 5,8 días = 139 horas

CONCILIACIÓN SEMANAL (168 h)  NO protege
CONCILIACIÓN DIARIA  (24 h)   protege al medio
CONCILIACIÓN HORARIA (1 h)    protege también al activo
```

Si la ventana no es menor que el intervalo entre dos operaciones del mismo
saldo, **la conciliación no protege: solo documenta el daño**.

## El coste anual

```text
CONFIGURACIÓN ESPEJO
  conciliación completa diaria     8 360 al mes → 100 320
  incremental horaria             10 032 al mes → 120 384
  divergencias   40 × 4 200                     → 168 000
  eventos corporativos 2,8 × 4 200              →  11 760
  TOTAL                                            400 464

BLOQUEO DE ORIGEN
  entradas y salidas  620 × 45                  →  27 900
  eventos corporativos 14 × 900                 →  12 600
  TOTAL                                             40 500

DIFERENCIA: 359 964 al año
```

Y el beneficio del token en ese caso era de 133 200 al año: **la configuración
espejo perdía 267 264 antes de contar nada más.**

## Configuración elegida y autoridad de resolución

```text
CONFIGURACIÓN: bloqueo de origen

AUTORIDAD DE RESOLUCIÓN
  el administrador del fondo, con obligación de comunicar
  al operador del registro en un plazo máximo de 2 horas
  hábiles

PROCEDIMIENTO
  1 el administrador congela el saldo bloqueado
  2 comunica al operador del registro
  3 el operador congela el token
  4 se resuelve en el registro oficial
  5 se destruye o reemite el token según el resultado
  6 se compensa a quien haya sufrido daño

Y ESTO SE ESCRIBE ANTES DE EMITIR,
no cuando llega el primer embargo.
```

## Errores que se penalizan

| Error | Por qué |
|---|---|
| No decidir quién manda | Es la decisión que define el proyecto |
| Prometer atomicidad con espejo | La arquitectura lo impide |
| Conciliar por muestreo | Una divergencia no vista es una pérdida |
| Congelar solo el token | Es el registro que se controla, no el que basta |
| Olvidar los eventos corporativos | Son la causa que ninguna automatización cubre |
| Revertir el registro correcto | Se compensa al perjudicado, no se altera lo válido |

## Límites

- El modelo de divergencia es didáctico: no reproduce la mensajería real entre
  un depositario y una plataforma, ni sus latencias.
- Los costes de conciliación y de resolución son **supuestos declarados** y
  cambian la conclusión: con una conciliación diez veces más barata, el espejo
  seguiría perdiendo, pero por menos.
- El bloqueo de origen reduce la divergencia estructural y **no la elimina**:
  una orden judicial sobre un saldo bloqueado sigue exigiendo el procedimiento
  de cuatro tiempos.
