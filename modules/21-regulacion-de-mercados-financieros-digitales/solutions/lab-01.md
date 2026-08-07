# Solución de referencia — Laboratorio 1: determinación de perímetro

> Material docente.

## Siete regímenes ejercidos y ninguno declarado

La plataforma no mentía a propósito. Nadie había hecho las seis preguntas, y el método no exige conocer todas las normas del mundo: exige mirar qué hace la entidad y contrastarlo con seis conductas que casi todas las jurisdicciones regulan.

## El código exige la fuente, no la declaración

```python
def test_un_hecho_sin_fuente_no_es_observable_documenta_el_problema():
    entidad = Entidad("x")
    with pytest.raises(ValueError):
        entidad.observar("tiene_las_claves", "las tiene", fuente="")
```

Es una decisión de diseño deliberada. Un hecho sin fuente es una declaración disfrazada, y aceptarla convierte el análisis en una transcripción de lo que dice la entidad.

## Las seis preguntas sobre los nueve hechos

```text
1 ¿recibe fondos con obligación de devolver?  CAPTACIÓN
2 ¿custodia por cuenta de terceros?           CUSTODIA
3 ¿casa oferta y demanda?                     MERCADO
4 ¿ejecuta por cuenta ajena?                  INTERMEDIACIÓN
5 ¿asesora o recomienda?                      ASESORÍA
6 ¿presta servicios de pago?                  CAMBIO

Y DOS QUE APARECEN AL MIRAR LO ACCESORIO
  crédito contra el saldo                     CRÉDITO

  SIETE REGÍMENES · CERO DECLARADOS
```

El orden importa: se llega a los siete recorriendo hechos, no leyendo la descripción del servicio. Los dos últimos son los que más se olvidan, porque el crédito y el cambio se ven como funcionalidades accesorias y cada uno activa su propio régimen.

## La custodia se activa aunque se niegue

```python
entidad.declarar(Regimen.MERCADO)   # declara mercado y niega custodia
assert Regimen.CUSTODIA in entidad.efectivos()
assert Regimen.CUSTODIA in entidad.no_declarados()
```

Quien tiene la clave tiene el activo, y eso ya lo había establecido la Parte 20, clase 12. La declaración no cambia el hecho: lo único que cambia es que ahora hay una discrepancia documentada entre lo declarado y lo efectivo.

## La asesoría exige dos hechos juntos

```text
destacar instrumentos            → por sí solo, discutible
destacar Y cobrar por destacar   → asesoría con conflicto
```

Este es el caso más discutido de la clase y el código lo refleja: destacar puede ser una selección editorial legítima; destacar cobrando por ello es otra cosa. La respuesta honesta es que depende, y que hay que preguntarlo.

## Lo que aplica aunque no se active nada

```text
protección al consumidor
publicidad no engañosa
protección de datos personales
prevención de lavado, si hay umbral
responsabilidad civil y penal general
```

«No estamos regulados» casi siempre significa «no necesitamos autorización financiera», y quien lo dice omite estas cinco. Es la frase que más se repite y la que menos se sostiene.

## Errores que se penalizan

| Error | Por qué |
|---|---|
| «¿Qué licencia pido?» | Se empieza por el final |
| Aceptar «somos tecnología» | Mira los hechos observables |
| Ignorar la actividad accesoria | Cada una activa su régimen |
| «No estamos regulados» | Enumera lo que sí aplica |
| Determinarlo una vez | El modelo cambia y hay que revisarlo |

## Límites

- El motor cubre ocho regímenes habituales; una jurisdicción concreta puede tener más, y su lista es la que manda.
- Los activadores son una simplificación: en la práctica, algunos regímenes exigen umbrales de importe o de habitualidad que aquí no se modelan.
- La determinación del perímetro **no sustituye a un informe jurídico**: lo prepara y lo hace discutible.
