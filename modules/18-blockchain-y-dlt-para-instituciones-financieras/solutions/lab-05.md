# Solución de referencia — Laboratorio 5: contrato de depósito en garantía

> Material docente. El «contrato» es una simulación en Python.

## El ataque de reentrada, paso a paso

```python
# CODIGO DEFECTUOSO
def retirar(self, quien):
    importe = self.saldos[quien]
    if importe == 0:
        raise SinFondos()
    self.transferir(quien, importe)   # ← llamada externa
    self.saldos[quien] = 0            # ← el saldo aun no es cero
```

```python
class BeneficiarioMalicioso:
    def recibir(self, importe):
        # Vuelve a entrar mientras el saldo sigue sin actualizar.
        if self.contrato.saldo_del_contrato() >= importe:
            self.contrato.retirar(self.direccion)
```

```text
EJECUCIÓN
  saldo del contrato: 28 000 000
  saldo del atacante:    180 000

  retirar() → transferir 180 000 → recibir() → retirar()
           → transferir 180 000 → recibir() → retirar()
           ...

  RESULTADO: el contrato queda a cero
```

## La corrección

```python
# CODIGO CORRECTO
def retirar(self, quien):
    importe = self.saldos[quien]
    if importe == 0:
        raise SinFondos()
    self.saldos[quien] = 0            # ← primero el estado
    self.transferir(quien, importe)   # ← despues la llamada
```

Dos líneas intercambiadas. Es todo. Y es la causa de una parte
desproporcionada de las pérdidas conocidas del sector.

## La prueba que debe pasar y la que debe fallar

```python
def test_el_ataque_vacia_el_contrato_defectuoso():
    contrato = Escrow(orden_correcto=False)
    contrato.depositar("importador", 28_000_000)
    atacante = BeneficiarioMalicioso(contrato)
    contrato.saldos[atacante.direccion] = 180_000

    atacante.atacar()
    assert contrato.saldo_del_contrato() == 0        # DEBE pasar


def test_tras_la_correccion_el_ataque_falla():
    contrato = Escrow(orden_correcto=True)
    contrato.depositar("importador", 28_000_000)
    atacante = BeneficiarioMalicioso(contrato)
    contrato.saldos[atacante.direccion] = 180_000

    atacante.atacar()
    assert contrato.saldo_del_contrato() == 28_000_000 - 180_000
```

## Los invariantes

```python
def comprobar_invariantes(self) -> None:
    assert self.saldo_del_contrato() == sum(
        d.importe for d in self.depositos if d.estado == "fondeado"
    ), "el saldo no cuadra con los depositos activos"

    for deposito in self.depositos:
        assert not (deposito.liberado and deposito.devuelto), (
            "un deposito no puede estar liberado y devuelto"
        )
```

Se comprueban **tras cada transición**, no al final. Un invariante que solo se
verifica en las pruebas no protege en ejecución.

## El interruptor de emergencia

```text
QUÉ HACE     detiene todas las funciones que mueven fondos
QUÉ NO HACE  no altera saldos, no transfiere, no revierte
QUIÉN        firma 2-de-3 del equipo de operaciones
OBJETIVO     menos de 10 minutos desde la detección

SIMULACRO TRIMESTRAL
  se activa en preproducción con tráfico simulado
  se mide el tiempo y se registra
  si supera 10 minutos, se revisa el procedimiento
```

Que el interruptor **solo pare** es la decisión importante: da capacidad de
contener sin dar a nadie capacidad de mover fondos (clase 8).

## Qué queda fuera del código

```text
FUERA
  · si la mercancía es conforme (juicio)
  · si el verificador actuó correctamente
  · qué ocurre si el verificador se equivoca
  · la identidad de las partes
  · la interpretación del contrato

DENTRO
  · custodia condicionada
  · transiciones objetivas
  · plazos y límites
  · registro de lo ocurrido

REGLA
  si para decidir hace falta una persona,
  el código ESPERA y ejecuta su decisión
```

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Corregir sin demostrar el ataque | No se aprende el mecanismo |
| Invariantes solo en las pruebas | No protegen en ejecución |
| Interruptor que también mueve fondos | Da poder en vez de contención |
| Meter juicio en el código | El código no interpreta |
| Simulacro sin medir | No se sabe si funciona |

## Límites

- El «contrato» es una clase de Python: no reproduce el modelo de ejecución ni
  el coste de gas de ninguna plataforma real.
- No se modela el orden de las transacciones ni el valor extraíble (clase 12).
- El oráculo del paso 8 usa cinco fuentes simuladas; la manipulación real de un
  mercado poco profundo no se reproduce.
