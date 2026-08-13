# Mapa regulatorio internacional

**Qué comparar, cómo compararlo y qué no se puede afirmar sin verificar.** Este
documento no contiene una tabla de trece países con sus regímenes: contiene el
método para construirla y mantenerla, más el mapa de qué organismo produce qué.

La razón de esa decisión es la que la Parte 22, clase 16 desarrolla: **una tabla
comparada sin nivel, referencia y fecha por celda no sirve para decidir**, y una
tabla publicada en un repositorio se desactualiza más rápido de lo que se
actualiza. Lo que sí se puede fijar por escrito es el método y las fuentes.

---

## Los tres niveles que no se mezclan

```text
REQUISITO NORMATIVO
  obliga; su incumplimiento se sanciona

GUÍA SUPERVISORA
  orienta; apartarse exige justificar

PRÁCTICA DE MERCADO
  no obliga; describe lo que se hace

EL ERROR QUE ARRUINA LA MAYOR PARTE DE
LAS COMPARACIONES
  poner los tres en la misma celda
```

---

## Las diez obligaciones que más discriminan

Comparar «regímenes» enteros no lleva a ninguna parte. Se comparan obligaciones
concretas, y estas son las que más separan a unas jurisdicciones de otras.

```text
  1 · qué actividades exigen autorización
  2 · qué instrumentos se califican como valor
  3 · qué se exige a un emisor de fichas
      referenciadas
  4 · si el reembolso a la par admite mínimos
      o condiciones
  5 · qué régimen de custodia aplica y si se
      admite la reutilización
  6 · qué exige la regla del viaje y desde qué
      umbral
  7 · qué tratamiento prudencial consume la
      exposición
  8 · si existe régimen piloto o exención
      temporal
  9 · qué se exige a un proveedor extranjero
      que se dirige a residentes
 10 · si existe una figura de proveedor
      tecnológico crítico
```

---

## Organismos internacionales: quién produce qué

| Organismo | Qué produce | Naturaleza | Sitio |
|---|---|---|---|
| **FSB** | Recomendaciones sobre criptoactivos y stablecoins globales | Estándar, no obliga | <https://www.fsb.org/> |
| **BIS — CPMI** | Principios y trabajos sobre pagos e infraestructuras | Estándar | <https://www.bis.org/cpmi/> |
| **IOSCO** | Recomendaciones sobre mercados de activos digitales y finanzas descentralizadas | Estándar | <https://www.iosco.org/> |
| **Comité de Basilea** | Tratamiento prudencial de exposiciones a criptoactivos | Estándar | <https://www.bis.org/bcbs/> |
| **GAFI** | Recomendaciones sobre activos virtuales y regla del viaje | Estándar con evaluación mutua | <https://www.fatf-gafi.org/> |
| **FMI** | Análisis de estabilidad y asesoramiento de política | Análisis | <https://www.imf.org/> |
| **Banco Mundial** | Inclusión financiera, remesas y pagos | Análisis y datos | <https://www.worldbank.org/> |
| **OCDE** | Tokenización, política y datos | Análisis | <https://www.oecd.org/> |
| **Comisión Europea, EBA, ESMA** | Derecho de la Unión y normas técnicas | Obliga en la Unión | <https://finance.ec.europa.eu/> |
| **OpenID Foundation, IETF, NIST** | Estándares técnicos de seguridad y autorización | Técnico | <https://openid.net/> |

**La distinción que hay que retener:** todo lo de la columna «estándar» orienta y
se incorpora por cada jurisdicción a su propio ritmo. Lo único que obliga es la
norma nacional —o, en la Unión Europea, el reglamento— que lo recoge.

---

## Cuándo se activa el régimen de otra jurisdicción

Esta es la pregunta operativa, y la respuesta no depende de dónde esté la entidad.

```text
INDICIOS DE COMERCIALIZACIÓN ACTIVA

  · sitio en el idioma de esa jurisdicción
  · precios en su moneda
  · publicidad dirigida a sus residentes
  · atención al cliente en su horario
  · métodos de pago locales
  · registro de dominio local

UNO SOLO SUELE NO BASTAR.
VARIOS JUNTOS SUELEN BASTAR.

CONSECUENCIA
  si el régimen se activa, hace falta
  autorización allí o cesar la actividad
  dirigida a esos residentes
```

---

## Por qué el arbitraje regulatorio funciona menos de lo que se cree

```text
DONDE NO FUNCIONA
  · el régimen del cliente se aplica igual
    si hay comercialización activa
  · los bancos corresponsales exigen
    estándares propios
  · los proveedores de infraestructura
    también
  · las listas de sanciones son globales

DONDE SÍ FUNCIONA
  · coste de la autorización inicial
  · plazos
  · carga de reporte

Y ESO SUELE SER UN AHORRO DE UNA VEZ
frente a un coste permanente de acceso
a servicios financieros
```

---

## Cómo mantener una tabla comparada

```text
REGLAS DE MANTENIMIENTO

  · una fila por obligación concreta
  · una columna por jurisdicción
  · en cada celda: nivel, referencia y fecha
  · una casilla de «no aplica» explícita
  · revisión semestral, con calendario
  · alerta cuando una autoridad publica
    consulta o proyecto
  · y una persona responsable, con nombre

SIN MANTENIMIENTO, LA TABLA SE CONVIERTE
EN UNA FUENTE DE ERRORES CON APARIENCIA
DE RIGOR: peor que no tenerla.
```

---

## Regímenes que el programa estudia con nombre propio

| Jurisdicción | Dónde se estudia | Ficha normativa |
|---|---|---|
| Chile | Parte 17, clase 3; Parte 22, clases 4 y 16; [matriz](mapa-regulatorio-chile.md) | [`ley-21521`](../regulatory/chile/ley-21521.yml) · [`ncg-502`](../regulatory/chile/ncg-502-prestadores-fintec.yml) |
| Unión Europea | Parte 22, clases 17, 18 y 19 | [`mica`](../regulatory/union-europea/mica-reglamento-2023-1114.yml) · [`dora`](../regulatory/union-europea/dora-reglamento-2022-2554.yml) · [`piloto DLT`](../regulatory/union-europea/dlt-pilot-reglamento-2022-858.yml) · [`transferencias`](../regulatory/union-europea/transferencias-fondos-reglamento-2023-1113.yml) |
| El Salvador | Parte 22, clase 20 | [`ley bitcoin`](../regulatory/el-salvador/ley-bitcoin-decreto-57-2021.yml) · [`activos digitales`](../regulatory/el-salvador/ley-emision-activos-digitales-2023.yml) |

Para el resto de jurisdicciones, el programa enseña el **método** de la clase 16 y
no publica una tabla: construirla es el ejercicio del laboratorio 8 de la Parte 22.

---

## Limitaciones

- **Este documento no es asesoría legal** y no afirma el contenido del régimen de
  ninguna jurisdicción concreta salvo las tres que el programa estudia con ficha.
- Los estándares internacionales **no obligan por sí mismos**: obliga la norma
  nacional que los incorpora, con su calendario propio.
- Cualquier comparación caduca. La fecha de verificación de cada celda es parte
  del dato, no un adorno.

**Fecha de verificación de este documento: 2026-08-12.**

---

[🏠 Inicio](../README.md) · [📚 Documentación](README.md) · [📖 Programa](../SYLLABUS.md)
