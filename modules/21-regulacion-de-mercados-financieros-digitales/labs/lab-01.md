# Laboratorio 1: Determinación de perímetro

## Propósito

Determinar qué actividades ejerce una entidad **a partir de hechos observables**, y comprobar que la declaración no coincide con la realidad.

Este es el primer laboratorio de la parte y el que fija el método que usarán los demás. Todo lo que viene después —calificar, autorizar, cumplir— depende de haber respondido bien qué hace la entidad, porque un perímetro mal determinado invalida el resto del expediente por más cuidado que se ponga en cada pieza.

## Escenario

Una plataforma se presenta como «tecnología, no finanzas». Hay que recoger sus hechos observables, aplicar las seis preguntas y contar cuántos regímenes activa sin haberlos declarado.

## Contexto

La clase 1 sostiene que la pregunta no es si el token está regulado sino qué está haciendo la entidad. La clase 2 añade que el principio de misma actividad tiene tres límites, y este laboratorio prepara el terreno para verlos.

## Datos

Nueve hechos observables de una plataforma sintética, cada uno con su fuente de verificación.

## Supuestos del ejercicio

- Las condiciones de servicio publicadas reflejan la práctica real.
- La captura de la aplicación tiene fecha y es contrastable.
- El tarifario vigente es el publicado.

## Requisitos

- Haber leído las clases 1 y 2.
- Python 3.11 o superior.

## Pasos

1. Registra los nueve hechos observables con su fuente; comprueba que un hecho sin fuente se rechaza.
2. Aplica las seis preguntas del perímetro y anota qué régimen activa cada una.
3. Comprueba que tener las claves activa la custodia aunque la entidad la niegue.
4. Verifica que la asesoría exige dos hechos juntos y no basta con destacar instrumentos.
5. Cuenta los regímenes ejercidos sin declarar y enumera la evidencia de cada uno.
6. Comprueba qué sigue aplicando aunque no se active ningún régimen financiero.
7. Compara una actividad tradicional con su equivalente digital y determina si el riesgo es el mismo, mayor en grado o distinto en naturaleza.
8. Compara las tres opciones de la clase 2 —norma existente, norma nueva y guía técnica— con su coste y su plazo.

## Arquitectura

```text
Entidad
  observar(clave, descripcion, FUENTE)
     → un hecho sin fuente se rechaza

  efectivos()        regimenes que activan los hechos
  no_declarados()    lo que se ejerce sin decirlo
  evidencia(reg)     los hechos que lo sostienen

SIEMPRE_APLICAN  cinco normas que no dependen
                 de ningun regimen financiero
```

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Un hecho sin fuente se rechaza | Excepción esperada |
| 2 | Se activan siete regímenes | Cálculo sobre los nueve hechos |
| 3 | La custodia se activa por las claves | Aunque se declare lo contrario |
| 4 | La asesoría exige dos hechos | Uno solo no basta |
| 5 | Cada régimen tiene evidencia | Fuente por hecho |
| 6 | Las cinco normas generales aparecen | Con la entidad vacía |

## Amenazas a considerar

| Amenaza | Efecto | Mitigación esperada |
|---|---|---|
| Aceptar la declaración | Se clasifica por lo que dice la entidad | Verificar hechos observables |
| Empezar por la autorización | Se pide la licencia equivocada | Primero qué haces, luego qué permiso |
| Actividad accesoria ignorada | El crédito «es solo un extra» | Cada una activa su régimen |
| «No estamos regulados» | Se refiere solo a lo financiero | Enumerar lo que sí aplica |
| Determinarlo una vez | El modelo de negocio cambia | Revisión periódica documentada |

## Pruebas

```bash
python -m pytest tests/test_regulatory_perimeter_engine.py -q -k "regimenes or custodia or asesoria or evidencia or fuente"
```

```bash
python apps/regulatory_perimeter_engine/cli.py perimeter
```

## Entregables

- La lista de hechos observables con su fuente de verificación.
- Las seis preguntas respondidas, con el régimen que activa cada una.
- Las actividades ejercidas y no declaradas, con su evidencia.
- `solution.md` con la comparación de las tres opciones normativas.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Hechos recogidos con fuente | 20 |
| Seis preguntas aplicadas | 25 |
| Actividades no declaradas identificadas | 25 |
| Normas que siempre aplican | 15 |
| Comparación de opciones normativas | 15 |

## Solución de referencia

En [`solutions/lab-01.md`](../solutions/lab-01.md).
