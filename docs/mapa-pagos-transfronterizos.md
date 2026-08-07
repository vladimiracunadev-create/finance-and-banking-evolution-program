<!-- portada:inicio -->
<div align="center">

# 🌍 Mapa de pagos transfronterizos

**Dónde está cada concepto de la Parte 18, con qué se conecta y los siete errores que persigue.**

[![parte](https://img.shields.io/badge/parte-18%20%C2%B7%20pagos%20transfronterizos-7c5cff?style=flat-square)](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/README.md)
[![lab](https://img.shields.io/badge/lab-cross__border__payments__lab-3776AB?style=flat-square)](../apps/cross_border_payments_lab/)

[⬅️ Mapa anterior](mapa-finanzas-abiertas.md) ·
[🏠 Inicio](../README.md) ·
[📘 Parte 18](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/README.md) ·
[➡️ Mapa siguiente](mapa-blockchain-dlt.md)

</div>
<!-- portada:fin -->

---

Guía de navegación de la Parte 18: dónde está cada concepto, con qué se conecta
y qué se puede ejecutar para comprobarlo.

## 🎯 El eje de la parte

```text
UN MENSAJE NO ES UN MOVIMIENTO DE FONDOS

  la red de mensajería transporta INSTRUCCIONES
  los fondos se mueven en CUENTAS
  la liquidación ocurre en un SISTEMA DE PAGOS
  y la FINALIDAD la da la norma, no el software

  confundir esas cuatro cosas es el origen
  de la mitad de los errores de esta materia
```

Si un diagnóstico o una propuesta no distingue las cuatro capas, no ha
diagnosticado nada.

## 🤝 La pregunta que ordena cualquier propuesta

```text
«¿EN QUÉ CAPA ACTÚA?»

  capa de MENSAJERÍA    formatos más ricos, validación en origen
                        → menos reparaciones, NO menos tiempo
  capa de LIQUIDACIÓN   ventanas más largas, libro común, prefinanciación
                        → menos tiempo real
  ambas                 interconexión de sistemas de pagos inmediatos

SI PROMETE VELOCIDAD Y SOLO TOCA LA CAPA 1,
NO VA A ENTREGARLA
```

## 🎯 Los cuatro problemas del G20 y dónde se atacan

| Problema | Causa dominante | Clases |
|---|---|---|
| **Coste** | Cadena de intermediarios y diferencial de cambio | 1, 3, 9, 10 |
| **Velocidad** | Husos, ventanas, días inhábiles, controles | 5, 7, 8, 13 |
| **Acceso** | Retirada de corresponsalías y última milla | 3, 10, 13 |
| **Transparencia** | Comisiones deducidas en tránsito y diferencial oculto | 1, 6, 9 |

## 🧭 Recorrido de la parte

```text
FUNDAMENTO      1 · qué es     2 · quién participa
                       │
INFRAESTRUCTURA 3 · corresponsalía   4 · nostro y vostro
                       │
LA DISTINCIÓN   5 · MENSAJE ≠ FONDOS  ◄── el eje
                       │
MENSAJERÍA      6 · ISO 20022
                       │
LIQUIDACIÓN     7 · finalidad   8 · liquidez y netting
                       │
PRECIO          9 · el cambio de divisa
                       │
SEGMENTOS      10 · remesas    11 · comercio exterior
                       │
CONTROL        12 · AML, sanciones y regla del viaje
                       │
ALTERNATIVAS   13 · pagos inmediatos  14 · stablecoins  15 · PvP
                       │
INTEGRACIÓN    16 · red de pagos y defensa
```

## 🗺️ Dónde está cada concepto

| Concepto | Clase | Laboratorio | Código |
|---|:---:|:---:|---|
| Pago transfronterizo vs. remesa vs. FX | 1 | 1, 5 | — |
| Coste total y su descomposición | 1, 9 | 5 | `remittances` |
| Los cuatro flujos | 2 | 1 | `flows` |
| Pago en serie y con cobertura | 2 | 1 | — |
| Corresponsalía y banca anidada | 3 | 2, 4 | — |
| Retirada de relaciones | 3 | 2 | — |
| Nostro, vostro y conciliación | 4 | 1 | `flows` (asientos) |
| Mensaje frente a fondos | 5 | 1 | `flows` |
| Ventanas, husos y días inhábiles | 5, 8 | 1, 6 | `flows.Plaza` |
| `pacs.008` y su validación | 6 | 3 | `iso20022` |
| Deudor último y acreedor último | 6 | 3 | `iso20022` |
| Referencia estable en reintentos | 6 | 3 | `iso20022.Orden` |
| Cancelación frente a devolución | 6 | 3 | `iso20022.transitar` |
| Compensación, liquidación, finalidad | 7 | 1, 7 | `settlement` |
| Riesgo Herstatt | 7, 15 | 7 | — |
| Saldo objetivo y netting | 8 | 2, 6 | `settlement` |
| Diferencial en puntos básicos | 9 | 5 | `remittances.Tramo` |
| Diferencial cruzado compuesto | 9 | 5 | `remittances` |
| Corredores y última milla | 10 | 5 | — |
| Instrumentos de comercio exterior | 11 | 3 | — |
| Precisión y exhaustividad | 12 | 4 | `screening` |
| Prueba retrospectiva | 12 | 4 | `screening` |
| Regla del viaje | 12 | 3, 4 | — |
| Enlace, alias y subasta de liquidez | 13 | 6 | `fast_payment_link` |
| Cobertura real y segmento excluido | 13 | 6 | `fast_payment_link.Enlace` |
| Ruta con stablecoin y sus cinco tramos | 14 | 8 | `stablecoin_route` |
| Atribución del ahorro por fuente | 14, 16 | 8 | `stablecoin_route` |
| Exposición máxima simultánea | 15 | 7 | `settlement` |
| Atomicidad y fallo del coordinador | 15 | 7 | `settlement.liquidar_pvp` |
| Motor de rutas con seis criterios | 16 | 2 | `routing_engine` |
| Las quince métricas | 16 | todos | — |

## ⚠️ Los siete errores que la parte persigue

1. **«SWIFT mueve dinero.»** Transporta instrucciones; el dinero se mueve en
   cuentas.
2. **Comparar solo comisiones.** El diferencial suele ser la mitad del coste y
   no aparece en el comprobante.
3. **Medir el diferencial sobre la base equivocada.** Se mide sobre lo que el
   cliente recibe, no sobre lo que el banco cotiza.
4. **Sumar diferenciales cruzados.** Se componen.
5. **Subir el umbral de screening porque la cola crece.** Antes va la prueba
   retrospectiva.
6. **Exposición = la operación mayor.** Es el máximo simultáneo.
7. **Atribuir el ahorro a la tecnología.** Hay seis fuentes posibles y ninguna
   se llama así.

Los siete tienen una prueba asociada en
[`tests/test_cross_border_payments_lab.py`](../tests/test_cross_border_payments_lab.py).

## 🧪 Qué se puede ejecutar

```bash
python apps/cross_border_payments_lab/cli.py trace --corridor CL-VN --amount 10000
```

```bash
python apps/cross_border_payments_lab/cli.py compare-routes --amount 20000
```

```bash
python apps/cross_border_payments_lab/cli.py pvp --scenario b-failure
```

```bash
python tools/validate_iso20022.py
```

```bash
python -m pytest tests/test_cross_border_payments_lab.py -q
```

## 📎 Cómo citar los proyectos institucionales

Nexus, mBridge, Jura, Dunbar, Mariana, Agorá, Meridian FX y Rialto aparecen en
la clase 13. La regla del programa para citarlos:

```text
POR CADA PROYECTO SE DECLARA
  problema · arquitectura · participantes · activo de liquidación
  estado · qué demostró · qué NO demostró

NINGUNO ES INFRAESTRUCTURA OPERATIVA A ESCALA GLOBAL.
Presentar una prueba de concepto como producción
es el error más común al citarlos.
```

## ➡️ Hacia dónde sigue

| De esta parte | A | Qué se profundiza |
|---|---|---|
| Stablecoins como medio de pago (14) | Parte 20 | Diseño, reservas, redención y regulación |
| Registro distribuido (14) | Parte 19 | Qué es y cuándo compensa |
| PvP y atomicidad (15) | Parte 21 | DvP y liquidación en mercados tokenizados |
| Normativa de cambios (9, 11) | Parte 22 | Perímetro y regulación comparada |
| Todo | Parte 23 | Capa transfronteriza del banco digital |

---

**Ver también:** [Parte 18](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/README.md) ·
[Etapa 5](etapa-5-finanzas-digitales.md) ·
[Cross-Border Payments Lab](../apps/cross_border_payments_lab/README.md) ·
[Glosario de finanzas digitales](glosario-finanzas-digitales.md)

<!-- pie:inicio -->
---

<div align="center">

[⬅️ Mapa anterior](mapa-finanzas-abiertas.md) · [🏠 Inicio](../README.md) · [📘 Parte 18](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/README.md) · [➡️ Mapa siguiente](mapa-blockchain-dlt.md)

</div>
<!-- pie:fin -->
