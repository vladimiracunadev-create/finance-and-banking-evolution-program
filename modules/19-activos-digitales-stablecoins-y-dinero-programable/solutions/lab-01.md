# Solución de referencia — Laboratorio 1: clasificador de activos digitales

> Material docente.

## La ficha no tiene ni una pregunta técnica

Es el hallazgo del laboratorio y de la clase 1. Las cinco preguntas —quién
promete, qué promete, con qué respaldo, exigible cuándo y ante quién— clasifican
las cuatro propuestas sin mirar la red, el estándar de contrato ni la billetera.

```text
                     A            B            C            D
quién promete      emisor       emisor       banco        nadie
                   autorizado   no financ.
qué promete        la par       la par       depósito     canje
respaldo           fondos       cartera      balance      otro token
                   salvaguard.  declarada    del banco    del sistema
exigible           a la vista   con umbral   como         solo canje
                   cualquiera   100 000      depósito
ante quién         supervisor   tribunal     supervisor   nadie
                   y tribunal   civil        y tribunal

CLASIFICACIÓN      dinero       referenciado depósito     no
                   electrónico               tokenizado   respaldado
```

## El umbral convierte la paridad en un privilegio de tamaño

```python
def test_el_minimo_de_redencion_convierte_la_paridad_en_privilegio_de_tamano():
    ficha = Ficha(..., umbral_redencion=100_000)

    apta_grande, _ = ficha.apta_para_tesoreria(500_000)
    apta_pequena, motivo = ficha.apta_para_tesoreria(40_000)

    assert apta_grande
    assert not apta_pequena
```

**La misma ficha, dos resultados.** Para el tenedor de 40 000 la paridad no es un
derecho: es un precio de mercado, y en tensión ese precio puede caer mientras la
redención mayorista sigue a la par.

## El rastreo del respaldo

```text
INSTRUMENTO S
  S ──► letras del Tesoro (externo)
  rastreo termina en un activo fuera del sistema  ✓

INSTRUMENTO D
  E ──► V ──► E
  el rastreo vuelve sobre sus pasos             ✗ CIRCULAR
```

La función `llega_a_activo_externo` devuelve **falso** para D, y no porque el
token V valga poco: porque V pierde valor exactamente cuando E lo necesita. Ese
respaldo no absorbe, amplifica (clase 7).

## Los tres elementos, aplicados a la variante 2

```python
def test_los_tres_incumplimientos_de_la_variante_2():
    fallos = incumplimientos_dinero_electronico(ficha)
    assert len(fallos) == 3
```

1. **Remunera el saldo**, y el régimen lo prohíbe: pagar interés obliga a
   invertir con más plazo o más riesgo, y eso es hacer de banco sin serlo.
2. **La redención tiene mínimo**, incompatible con la redención a la par en
   cualquier momento.
3. **La redención no es a la vista.**

El producto no era «otra cosa que necesita un régimen nuevo»: era dinero
electrónico con tres incumplimientos, y cada uno corresponde a una fragilidad
que las clases 3 a 6 miden.

## El depósito tokenizado y la CBDC

```text
DEPÓSITO TOKENIZADO   obligado: banco
                      → régimen bancario, garantía de depósitos
                      → el registro cambia CÓMO se transfiere,
                        no QUÉ es

CBDC                  obligado: banco central
                      → no hay reserva: ES la reserva
                      → pasivo soberano
```

La misma función `clasificar` los separa, y sigue sin mirar la tecnología.

## Decisión de tesorería

```text
CRITERIO: disponer del importe nominal cuando haga falta

  A  derecho de redención universal ......... apta
  C  depósito con garantía .................. apta
  B  sin derecho para el tamaño de esta caja  no apta
  D  sin obligado ........................... no apta

Y LA DECISIÓN SE JUSTIFICA CON LA FICHA,
no con el rendimiento ofrecido.
```

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Clasificar por el nombre comercial | «Estable» no es una propiedad |
| Usar «token» como tipo | Es un contenedor: di qué contiene |
| Detener el rastreo en el primer eslabón | El respaldo circular no se ve |
| Ignorar el umbral de redención | Define quién tiene derecho |
| Elegir el régimen más cómodo | Los tres elementos deciden |
| Suponer garantía de depósitos por parecido | Cubre depósitos, no parecidos |

## Límites

- La ficha clasifica por la promesa **declarada**; verificar que esa declaración
  se cumple es el objeto de los laboratorios 2 y 4.
- La calificación regulatoria definitiva depende de la jurisdicción y exige
  revisión legal, que este laboratorio no sustituye.
- Los cuatro instrumentos son sintéticos y no representan a ningún emisor real.
