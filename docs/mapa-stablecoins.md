# Mapa de stablecoins

**Una ruta propia, que atraviesa cinco partes.** Las stablecoins no viven en un
solo módulo: aparecen como instrumento en la Parte 20, como riel de pago en la
18, como activo de liquidación en la 21, como exposición en la 11 y como sujeto
regulado en la 22. Este documento reúne esa ruta para quien quiere recorrerla
entera.

Hay una razón para separarla del [mapa de activos digitales](mapa-activos-digitales.md):
casi todo lo que se discute mal sobre stablecoins se discute mal por confundir la
promesa con el respaldo, y esa confusión solo se corrige recorriendo el ciclo
completo —diseño, emisión, reservas, circulación, custodia, redención, crisis,
resolución—, que ninguna parte contiene por sí sola.

---

## La distinción que ordena todo lo demás

```text
CINCO COSAS QUE NO SON LA MISMA COSA

  STABLECOIN
    activo digital que promete estabilidad
    frente a una referencia

  DINERO ELECTRÓNICO
    saldo emitido contra fondos recibidos,
    con régimen propio y anterior

  DEPÓSITO TOKENIZADO
    un depósito bancario cuya anotación
    cambia de soporte; sigue siendo depósito

  MONEDA DIGITAL DE BANCO CENTRAL
    pasivo del banco central

  FONDO MONETARIO TOKENIZADO
    participación en un fondo; su valor
    fluctúa y no promete la par

LA PREGUNTA QUE LAS SEPARA
  ¿quién es el deudor, y qué promete
  exactamente?
```

---

## La ruta, por orden de estudio

| Orden | Dónde | Qué aporta |
|---:|---|---|
| 1 | Parte 3, productos financieros | Qué es dinero y qué es un saldo |
| 2 | Parte 6, sistema financiero | Creación de dinero y política monetaria |
| 3 | [Parte 20, clase 1](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/01-taxonomia-de-los-activos-digitales.md) | Taxonomía: la clasificación por la promesa |
| 4 | [Parte 20, clase 3](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/03-stablecoins-tipologias-y-mecanica-de-la-paridad.md) | Tipologías y mecánica de la paridad |
| 5 | [Parte 20, clase 4](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/04-reservas-composicion-calidad-y-verificacion.md) | Reservas: composición, calidad y verificación |
| 6 | [Parte 20, clase 5](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/05-redencion-el-derecho-el-proceso-y-la-cola.md) | Redención: el derecho, el proceso y la cola |
| 7 | [Parte 20, clase 6](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/06-perdida-de-paridad-anatomia-de-una-corrida.md) | Pérdida de paridad: anatomía de una corrida |
| 8 | [Parte 20, clase 7](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/07-stablecoins-algoritmicas-y-su-modo-de-fallo.md) | Algorítmicas: el modo de fallo |
| 9 | [Parte 20, clases 8 y 9](../modules/19-activos-digitales-stablecoins-y-dinero-programable/classes/09-dinero-electronico-el-regimen-que-ya-existia.md) | Depósito tokenizado y dinero electrónico |
| 10 | [Parte 18, clase 14](../modules/17-pagos-transfronterizos-remesas-y-liquidacion/classes/14-stablecoins-y-pagos-internacionales.md) | Como riel de pago transfronterizo |
| 11 | [Parte 21, clase 11](../modules/20-tokenizacion-fx-onchain-y-mercados-programables/classes/11-fx-del-mercado-mayorista-al-registro.md) | Como activo de liquidación en FX |
| 12 | [Parte 22, clase 5](../modules/21-regulacion-de-mercados-financieros-digitales/classes/05-regimen-de-emisores.md) | Régimen del emisor |
| 13 | [Parte 22, clase 18](../modules/21-regulacion-de-mercados-financieros-digitales/classes/18-mica-obligaciones-reservas-y-supervision.md) | Reservas y reembolso en un régimen concreto |
| 14 | [Parte 22, clase 8](../modules/21-regulacion-de-mercados-financieros-digitales/classes/08-tratamiento-prudencial-de-las-exposiciones.md) | Qué capital consume tenerlas |

---

## El ciclo completo, y dónde se estudia cada tramo

```text
DISEÑO          Parte 20, clases 1 y 3
  qué promete y contra qué

EMISIÓN         Parte 20, clase 3
  quién emite y con qué autorización

RESERVAS        Parte 20, clase 4
  composición, custodia, segregación
                Parte 22, clase 18
  las cuatro reglas en derecho positivo

DISTRIBUCIÓN    Parte 20, clase 13
  quién la pone en circulación

CIRCULACIÓN     Parte 18, clase 14
  como riel de pago

NEGOCIACIÓN     Parte 20, clase 13
  formación de precio y profundidad

CUSTODIA        Parte 20, clase 12
  llaves, esquemas y segregación

REDENCIÓN       Parte 20, clase 5
  el derecho, y quién lo tiene de verdad

CRISIS          Parte 20, clase 6
                caso: perdida-de-paridad
                caso: corrida-de-reembolsos

RESOLUCIÓN      Parte 22, clase 18
  plan de recuperación y plan de reembolso
```

---

## Las seis afirmaciones que esta ruta desmonta

| Afirmación frecuente | Qué falta | Dónde se corrige |
|---|---|---|
| «Está respaldada al 100 %, es segura» | La cobertura no dice nada sobre composición ni segregación | Parte 20, clase 4 |
| «Es dinero digital» | El emisor no es un banco central y la promesa no es la misma | Parte 20, clases 8 y 9 |
| «Hay auditoría de reservas» | Existencia no es suficiencia | Parte 22, clase 18 |
| «Puedo reembolsar cuando quiera» | Depende del mínimo y de la liquidez de la reserva | Caso `stablecoins/perdida-de-paridad` |
| «Las algorítmicas ya se corrigieron» | El mecanismo que falla es el incentivo, no el código | Parte 20, clase 7 |
| «Sirve para pagos internacionales sin más» | Falta el tramo de entrada y salida a moneda local | Parte 18, clase 14 |

---

## Qué se puede ejecutar

| Aplicación | Qué hace |
|---|---|
| [`apps/digital_assets_risk_lab/`](../apps/digital_assets_risk_lab/README.md) | Motor de emisor, reservas, redención y escenarios de pérdida de paridad |
| [`apps/cross_border_payments_lab/`](../apps/cross_border_payments_lab/README.md) | Ruta de pago con stablecoin, comparada con la corresponsal |
| [`apps/onchain_fx_lab/`](../apps/onchain_fx_lab/README.md) | Liquidación con activos tokenizados y pago contra pago |

---

## Casos asociados

- [`case-studies/stablecoins/perdida-de-paridad.md`](../case-studies/stablecoins/perdida-de-paridad.md)
- [`case-studies/stablecoins/corrida-de-reembolsos.md`](../case-studies/stablecoins/corrida-de-reembolsos.md)
- [`case-studies/european-union/mica-transicion.md`](../case-studies/european-union/mica-transicion.md)

---

## Fichas normativas relacionadas

- [`regulatory/union-europea/mica-reglamento-2023-1114.yml`](../regulatory/union-europea/mica-reglamento-2023-1114.yml)
- [`regulatory/internacional/fsb-stablecoins-globales.yml`](../regulatory/internacional/fsb-stablecoins-globales.yml)
- [`regulatory/internacional/bcbs-sco60-criptoactivos.yml`](../regulatory/internacional/bcbs-sco60-criptoactivos.yml)

---

## Limitaciones

- Ninguna clase de esta ruta constituye asesoría de inversión ni recomendación
  sobre instrumento alguno.
- El régimen aplicable a las stablecoins **cambia con rapidez** y de forma
  desigual entre jurisdicciones: la ruta enseña el método de análisis, no un
  catálogo estable.
- Los emisores concretos que se citen en clase se citan por sus documentos
  públicos y con fecha de consulta; el programa no evalúa a ninguno.

---

[🏠 Inicio](../README.md) · [📚 Documentación](README.md) · [📖 Programa](../SYLLABUS.md)
