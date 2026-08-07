# Solución de referencia — Laboratorio 6: interconexión de pagos inmediatos

> Material docente.

## Los seis problemas y cuál es técnico

| # | Problema | ¿Técnico? | Cómo se resuelve |
|---:|---|:---:|---|
| 1 | Identificar al beneficiario | Sí | Resolución de alias con confirmación de nombre |
| 2 | Quién aporta la divisa | No | Acuerdo con proveedores de liquidez |
| 3 | A qué tipo y quién asume el riesgo | No | Diseño de cambio y contrato |
| 4 | Cumplimiento de los dos países | No | Reglas comunes y responsabilidades |
| 5 | Quién responde si falla | No | Acuerdo de responsabilidad y foro |
| 6 | Quién decide las reglas | No | Gobernanza del enlace |

**Uno de seis.** Un proyecto que solo resuelve el primero no tiene un enlace:
tiene una integración.

## Confirmación de nombre: el control que evita la pérdida irreversible

```python
def resolver(alias: str, solicitante: str) -> Resolucion:
    if consultas_recientes(solicitante) > LIMITE_POR_HORA:
        raise LimiteExcedido("posible enumeracion")

    cuenta = directorio.buscar(alias)
    if cuenta is None:
        # Respuesta uniforme: no revela si el alias existe.
        raise NoResuelto("alias no disponible")

    registrar_consulta(solicitante, alias)
    # Se devuelve el nombre PARCIALMENTE enmascarado para
    # confirmar sin exponer el nombre completo a quien consulta.
    return Resolucion(banco=cuenta.banco, nombre_mascara=enmascarar(cuenta.nombre))
```

Dos decisiones que la corrección busca:

- **respuesta uniforme** cuando el alias no existe: si difiere, se puede
  enumerar qué números tienen cuenta;
- **nombre enmascarado**: basta para que el ordenante confirme y no expone el
  nombre completo a quien solo tiene un número de teléfono.

## Subasta de liquidez y su sensibilidad

```text
CUATRO PROVEEDORES
  cotizaciones: 42, 45, 51, 58 pb
  gana: 42 pb

DOS PROVEEDORES
  cotizaciones: 45, 58 pb
  gana: 45 pb  →  observado en la práctica: ~110 pb
                  cuando ambos saben que solo compiten entre sí

UNO
  no hay subasta: el precio lo pone el proveedor
  supuesto del ejercicio: 250 pb
```

El resultado del corredor es **robusto**: incluso a 250 pb, el coste total es
1,79 % frente al 7,9 % actual. La decisión de construir el enlace no depende del
número de proveedores; la de cómo gobernarlo, sí.

## Cobertura real

```text
OPERACIONES DEL CORREDOR              2 900 000
  bajo el límite de 2 000 USD           96 %  → 2 784 000
  con cuenta o billetera en destino     74 %  → 2 060 160

COBERTURA REAL: 71 % del corredor
```

Y el dato que el proyecto debe publicar junto al titular:

```text
EL 29 % QUEDA FUERA
  26 % por no tener cuenta ni billetera
   3 % por superar el límite

Y SU COSTE PROBABLEMENTE SUBE: los operadores actuales
pierden el 71 % del volumen y reparten sus costes fijos
entre menos operaciones (estimado: de 7,9 % a ~9,5 %)
```

## La mitigación no es opcional

Sin la entrega en efectivo desde el enlace o la apertura simplificada de
billetera, **el enlace aumenta la desigualdad dentro del corredor**. Un proyecto
que las deja «para la fase 2» está eligiendo, sin decirlo, que el segmento más
vulnerable pague más.

## Las cinco reglas mínimas

```text
1. LEY APLICABLE
   qué ordenamiento rige la operación y en qué momento cambia

2. RESPONSABILIDAD POR PAGO NO AUTORIZADO
   quién responde ante el cliente y quién repite contra quién

3. PLAZO Y PROCEDIMIENTO DE DEVOLUCIÓN
   en cuánto tiempo, con qué mensaje y con qué consentimiento

4. ARBITRAJE DE DISPUTAS
   qué foro resuelve y con qué reglas

5. CONTINGENCIA
   qué pasa si un sistema cae con pagos a medias,
   quién declara la contingencia y cómo se reconcilia
```

Ninguna es técnica. Las cinco tienen que estar escritas **antes** del primer
pago, no después del primer incidente.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Resolver alias sin confirmación de nombre | Pago irreversible al destinatario equivocado |
| Respuesta distinta si el alias no existe | Permite enumerar |
| Publicar «pagos internacionales instantáneos» | Cubre el 71 %, no el 100 % |
| Dejar la mitigación para la fase 2 | Aumenta la brecha desde el día 1 |
| Reglas escritas después de operar | El primer incidente no tiene procedimiento |

## Límites

- La liquidación se simula: no hay conexión con ningún sistema real.
- Los proyectos institucionales citados en la clase 13 son pilotos o pruebas de
  concepto; este laboratorio no reproduce ninguno de ellos.
- El modelo de subasta es simplificado: no incorpora tamaño, horario ni límite
  de exposición del proveedor.
