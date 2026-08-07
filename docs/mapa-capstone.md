<!-- portada:inicio -->
<div align="center">

# 🏗️ Mapa del capstone

**La cadena de decisiones de la Parte 23, de dónde viene cada una y las cinco afirmaciones que desmonta.**

[![parte](https://img.shields.io/badge/parte-23%20%C2%B7%20capstone-7c5cff?style=flat-square)](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/README.md)
[![lab](https://img.shields.io/badge/lab-digital__bank__capstone-3776AB?style=flat-square)](../apps/digital_bank_capstone/)

[⬅️ Mapa anterior](mapa-regulatorio.md) ·
[🏠 Inicio](../README.md) ·
[📘 Parte 23](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/README.md) ·
[📚 Documentación](README.md)

</div>
<!-- portada:fin -->

---

Guía de navegación de la Parte 23: dónde está cada decisión, de qué parte del
programa viene y qué se puede ejecutar para comprobarla.

## ⭐ Qué hace distinta a esta parte

Las veintidós partes anteriores enseñan. Esta construye. No introduce ningún
concepto nuevo, y esa es exactamente su dificultad: **todo lo que hace falta ya se
explicó, y aun así el sistema no sale bien a la primera**.

La razón es que un programa enseña por temas y un sistema no funciona por temas.
Cada clase pudo diseñar su componente en aislamiento, con sus propios supuestos y
sin nadie que le llevara la contraria. Al integrarlos, esos supuestos chocan.

```text
UN PROYECTO       yuxtapone piezas correctas
UN CAPSTONE       las hace funcionar juntas
                  y encuentra donde se estorban

SI NO ENCUENTRA NINGUNA CONTRADICCION,
NO HA INTEGRADO: HA APILADO.
```

## 🧱 Los tres bloques

La parte se organiza en tres bloques de seis clases, y el orden importa porque
cada bloque solo puede empezar cuando el anterior ha cerrado sus decisiones.

| Bloque | Clases | Qué se resuelve |
|---|:---:|---|
| Qué construir | 1-6 | Alcance, perímetro propio y tres decisiones de arquitectura |
| Construirlo | 7-12 | Registro, interfaces, custodia, liquidación, pagos y ciclo de vida |
| Probarlo y defenderlo | 13-18 | Expediente, amenazas, tensión, resolución, límites y defensa |

## 🔗 La cadena de decisiones

Es lo que distingue este capstone de una lista de tareas. Cuatro decisiones
dependen unas de otras, y tomarlas en otro orden produce un sistema que se
justifica hacia atrás.

```text
1  ¿QUE ENTRA EN EL ALCANCE?
      cuatro preguntas por funcion
             ↓
2  ¿HACE FALTA UN REGISTRO COMPARTIDO?
      seis preguntas · pendiente de 3
             ↓
3  ¿DONDE ESTA EL DINERO?
      cuatro opciones · resuelve 2
             ↓
4  ¿QUE SE OFRECE Y A QUE IMPORTE?
      calificacion y punto de equilibrio
```

La clase 4 deja su conclusión **explícitamente pendiente** de la 5, en vez de
resolverla por adelantado para que salga como se quería. Cerrar la cadena al
revés es el error más frecuente de los capstones y el más difícil de detectar,
porque el resultado parece coherente.

## 🗺️ Dónde está cada cosa

| Concepto | Clase | Laboratorio | Código |
|---|:---:|:---:|---|
| Las cuatro preguntas del alcance | 1 | 1 | `scope.py` |
| Construir, integrar o comprar | 2 | 1 | `build.py` |
| Perímetro del propio sistema | 3 | 2 | — |
| ¿Hace falta un registro? | 4 | 1 | — |
| Dónde está el dinero | 5 | 3 | — |
| Calificación del catálogo | 6 | 2 | — |
| Registro de referencia | 7 | 3 | — |
| Interfaces y consentimiento | 8 | 4 | — |
| Custodia y claves | 9 | 4 | — |
| Liquidación y modos de fallo | 10 | 5 | — |
| Pagos y exterior | 11 | 5 | — |
| Ciclo de vida y tensiones | 12 | 6 | `tensions.py` |
| Expediente regulatorio | 13 | 9 | — |
| Modelo de amenazas | 14 | 7 | — |
| Escenario de tensión | 15 | 8 | `stress.py` |
| Resolución ordenada | 16 | 9 | — |
| Lo que el sistema no puede hacer | 17 | 9 | — |
| Defensa ante el comité | 18 | 9 | — |

## 🚫 Las cinco afirmaciones que la parte desmonta

Cada una es una intuición razonable que el sistema construido contradice con una
prueba ejecutable.

| Afirmación | Lo que se comprueba | Dónde |
|---|---|---|
| «Reducir el alcance baja el ingreso» | El ingreso no cambia: las excluidas no lo generaban | 23.1 |
| «Se integra lo que es más barato integrar» | Sin salida real, integrar es una dependencia estructural | 23.2 |
| «Si cada componente está bien, el sistema está bien» | Una tensión sin resolver bloquea la operación | 23.12 |
| «Tres fallos simultáneos son improbables» | Un proveedor con tres papeles los produce con uno | 23.15 |
| «Un expediente debe mostrar fortalezas» | La sección de límites es la que da credibilidad | 23.17 |

## 🧪 Qué se puede ejecutar

```bash
python apps/digital_bank_capstone/cli.py scope
```

```bash
python apps/digital_bank_capstone/cli.py build
```

```bash
python apps/digital_bank_capstone/cli.py tensions
```

```bash
python apps/digital_bank_capstone/cli.py stress
```

```bash
python -m pytest tests/test_digital_bank_capstone.py -q
```

## 🧭 De dónde viene cada método

El capstone no inventa herramientas: reutiliza las de las seis partes anteriores
de la Etapa 5 y las de las cuatro etapas previas.

| Método | Viene de |
|---|---|
| Determinación del perímetro por hechos | Parte 22, clase 1 |
| Calificación por cuatro criterios | Parte 22, clase 3 |
| Independencia efectiva de las claves | Parte 20, clase 12 |
| Atomicidad y sus modos de fallo | Parte 21, clases 5 y 10 |
| Los cuatro flujos de un pago | Parte 18, clase 4 |
| Consentimiento con alcance por finalidad | Parte 17, clase 6 |
| Tolerancia al impacto por función | Parte 22, clase 14 |
| Gradiente de niveles de prueba | Parte 22, clase 15 |

## ⚠️ Aviso

Material **docente**. El sistema del capstone es un simulador con datos sintéticos
y **no es un banco**. No usa credenciales, claves ni fondos reales, no se conecta
con ninguna infraestructura de producción y ninguna de sus salidas constituye
asesoría legal, financiera ni de inversión.

---

**Ver también:** [Etapa 5](etapa-5-finanzas-digitales.md) ·
[Glosario de finanzas digitales](glosario-finanzas-digitales.md) ·
[Mapa regulatorio](mapa-regulatorio.md) ·
[Mapa de tokenización](mapa-tokenizacion.md)

<!-- pie:inicio -->
---

<div align="center">

[⬅️ Mapa anterior](mapa-regulatorio.md) · [🏠 Inicio](../README.md) · [📘 Parte 23](../modules/22-proyecto-banco-digital-y-mercado-tokenizado/README.md) · [📚 Documentación](README.md)

</div>
<!-- pie:fin -->
