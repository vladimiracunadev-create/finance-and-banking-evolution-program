# Laboratorio 1: Registro de referencia y divergencia

## Propósito

Comprobar ejecutando que **un espejo nunca permite liquidación atómica**, y que el bloqueo de origen elimina la divergencia
estructural por una fracción del coste.

## Escenario

Una plataforma tokeniza participaciones de un fondo cuyo registro oficial es el del administrador. Hay que dimensionar la conciliación, provocar las seis causas de divergencia y decidir la configuración.

## Contexto

La clase 1 sostiene que la pregunta de quién manda decide si el proyecto existe. La clase 2 la responde: con un espejo, la atomicidad es imposible porque no se puede entregar de forma atómica algo cuya titularidad decide otro registro.

## Datos

Dos libros sintéticos con 6 400 partícipes y 2 770 operaciones mensuales.

## Supuestos del ejercicio

- El 5 % más activo hace el 60 % de las operaciones.
- Coste de una conciliación completa: 380.
- Coste de resolver una divergencia: 4 200.

## Requisitos

- Haber leído las clases 1 y 2.
- Python 3.11 o superior.

## Pasos

1. Construye un `Emisor` en configuración espejo y otro en bloqueo de origen, y comprueba `permite_atomicidad` en cada uno.
2. Emite posiciones y ejecuta `bloquear_y_representar`; verifica que el saldo oficial más el bloqueado es constante.
3. Provoca las seis causas de divergencia y comprueba que dos vienen de fuera del sistema.
4. Concilia sobre **todos** los saldos y detecta la diferencia.
5. Congela en ambos registros y demuestra que ninguno admite movimientos.
6. Intenta resolver sin autoridad designada y comprueba que falla.
7. Calcula la ventana de divergencia y compárala con el intervalo entre operaciones del partícipe activo.
8. Compara el coste anual de las dos configuraciones.

## Arquitectura

```text
Emisor(configuracion)
   ESPEJO             oficial y token con saldo simultaneo
                      → conciliacion permanente
                      → atomicidad IMPOSIBLE

   BLOQUEO_DE_ORIGEN  un solo registro operativo por saldo
                      → sin divergencia estructural
                      → atomicidad alcanzable
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | El espejo no permite atomicidad | `permite_atomicidad` es falso |
| 2 | El bloqueo conserva el total | Oficial más bloqueado constante |
| 3 | Dos causas vienen de fuera | `viene_de_fuera` verdadero |
| 4 | La conciliación cubre todos los saldos | Revisión del código |
| 5 | La congelación alcanza a ambos | Excepción en los dos libros |
| 6 | Sin autoridad no se resuelve | Excepción esperada |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Configuración sin decidir | Lo decide un tribunal, tarde y caro | Respuesta por escrito antes de emitir |
| Ventana larga | Se transfiere un saldo inexistente | Frecuencia menor que el intervalo real |
| Congelar un solo registro | Se agrava la divergencia | Congelación simultánea |
| Evento corporativo desalineado | Cupón pagado dos veces o ninguna | Aplicación única sobre el saldo bloqueado |
| Revertir el registro correcto | Se altera lo que estaba bien | Compensar al perjudicado |

## Pruebas

```bash
python -m pytest tests/test_tokenization_platform.py -q -k "espejo or bloqueo or divergencia or congelacion or ventana"
```

```bash
python apps/tokenization_platform/cli.py registry
```

## Entregables

- La comparación de configuraciones con su propiedad de atomicidad.
- Las seis causas provocadas, con la marca de cuáles vienen de fuera.
- El cálculo de ventana frente al intervalo real.
- `solution.md` con la configuración elegida y su autoridad de resolución.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Comparación de configuraciones | 20 |
| Divergencias provocadas y clasificadas | 20 |
| Detección, congelación y resolución | 25 |
| Cálculo de ventana y coste anual | 20 |
| Autoridad de resolución designada | 15 |

## Solución de referencia

En [`solutions/lab-01.md`](../solutions/lab-01.md).
