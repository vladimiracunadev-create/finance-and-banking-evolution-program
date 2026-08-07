<!-- meta
part: 3
class: 14
title: "Proyecto: comparador de productos"
level: intermedio
duration_minutes: 90
status: complete
-->

<!-- gen:header:start -->
# Clase 14 · Proyecto: comparador de productos

> [← 13 · Comisiones, CAE y costo total](13-comisiones-cae-y-costo-total.md) · [Índice de la parte](../README.md) · [Proyecto de la parte →](../project/README.md)

**Parte 03 — Productos y servicios financieros** · **Nivel:** Intermedio — requiere las partes anteriores · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Construir una herramienta que compare ofertas reales de crédito, depósito y cuenta sobre una base
homogénea, y que documente sus supuestos y límites. Es el primer producto del programa destinado a ser
usado por otra persona, lo que agrega una exigencia nueva: **que no induzca a error**.

Esta clase cierra la parte construyendo la herramienta que las trece anteriores hacían falta. No introduce productos nuevos: introduce la exigencia de comparar sin inducir a error, que es más difícil que calcular bien y es lo que separa un comparador útil de uno que vende.

## 📚 Objetivos

Al finalizar podrás:

1. **Especificar** los requisitos de un comparador financiero honesto.
2. **Implementar** el cálculo de CAE y de costo total para al menos tres tipos de producto.
3. **Diseñar** una salida que muestre supuestos y límites junto al resultado.
4. **Validar** la herramienta contra casos verificados a mano.
5. **Defender** las decisiones de diseño y las exclusiones declaradas.

<!-- gen:agenda:start -->
## Agenda de 90 minutos

La clase dura noventa minutos y se recorre en cinco tramos. No es un horario
rígido: es el orden en que los bloques de esta página se sostienen unos a otros, y
por eso conviene respetarlo aunque cambien los tiempos.

Los **diez primeros minutos** se dedican a recuperar la clase anterior, porque casi
todo lo que aquí se explica supone algo que ya se vio. Los **veinticinco
siguientes** desarrollan los conceptos con la fuente oficial a la vista: las
referencias del final de la página no son un adorno bibliográfico, se consultan
mientras se estudia. Del **minuto 35 al 55** se resuelve el ejemplo guiado paso a
paso, sin saltarse ninguno, porque el error típico vive precisamente en el paso que
parece obvio. Los **veinticinco minutos siguientes** son de práctica con datos
propios o sintéticos —nunca reales de terceros—, que es cuando se comprueba si se
entendió. Los **diez últimos** cierran con las preguntas de comprobación y el
registro del entregable.

Si el tiempo aprieta, lo que se recorta es la práctica y se traslada al
laboratorio de la parte; lo que no se recorta nunca es el ejemplo guiado.
<!-- gen:agenda:end -->

## 🧩 Conceptos centrales

Los cinco términos son de diseño de la herramienta. **No inducir a error** es el que gobierna a los demás: un comparador puede tener todos los cálculos correctos y aun así llevar a una decisión equivocada por cómo presenta el resultado, y evitarlo es una decisión de diseño, no de cálculo.

| Concepto | Comprensión verificable |
|---|---|
| `base homogénea` | Todas las ofertas se reducen a las mismas métricas: CAE, costo total, cuota y desembolso inicial. |
| `supuesto explícito` | Todo dato no informado por la oferta que la herramienta debe asumir, y que se muestra al usuario. |
| `límite declarado` | Lo que la herramienta **no** calcula. Su omisión convierte una ayuda en una fuente de error. |
| `caso de validación` | Oferta con resultado conocido, calculado de forma independiente. |
| `no inducir a error` | La salida no debe sugerir precisión ni recomendación que los datos no respaldan. |

## 🧠 Modelo mental

Un comparador tiene **tres responsabilidades, en orden**:

```text
1. calcular bien              → si falla, todo lo demás es irrelevante
2. mostrar los supuestos      → sin esto, el número es una opinión
3. declarar lo que no cubre   → sin esto, la herramienta engaña por omisión
```

La tercera es la que separa una herramienta profesional de una calculadora bonita. Un comparador que
no dice "no incluyo notaría ni tasación" está afirmando implícitamente que sí.

## 📖 Desarrollo

### 1. Requisitos funcionales

Los requisitos se escriben antes de programar y se convierten en casos de prueba. La lista siguiente es el mínimo que el comparador debe resolver.

| # | Requisito | Entrada | Salida |
|---:|---|---|---|
| 1 | Comparar créditos de cuota fija | Monto, plazo, tasa, comisiones, seguros | CAE, cuota, costo total |
| 2 | Comparar depósitos | Monto, plazo, tasa, impuesto, inflación | Rendimiento nominal, neto y real |
| 3 | Comparar cuentas | Saldo promedio, comisiones, tasa | Costo anual total |
| 4 | Ordenar ofertas | Conjunto de ofertas | Ranking por métrica elegida |
| 5 | Mostrar supuestos | — | Lista de supuestos aplicados |
| 6 | Declarar exclusiones | — | Lista de conceptos no considerados |
| 7 | Advertir empates | Diferencias menores al umbral | "Diferencia no significativa" |

El requisito 7 merece atención: dos ofertas que difieren en 0,05 puntos de CAE **no** son distinguibles
en la práctica, porque los supuestos tienen más incertidumbre que esa diferencia. Presentarlas como
"ganadora y perdedora" es falsa precisión.

### 2. Arquitectura

La separación entre cálculo y presentación es la que permite probar el primero sin ejecutar la segunda. El esquema siguiente la recoge.

```text
apps/product_comparator/
  comparator.py     lógica de cálculo (funciones puras)
  models.py         estructuras: Oferta, ResultadoComparacion
  cli.py            interfaz de línea de comandos
  README.md         uso, supuestos y límites
tests/
  test_comparator.py
portfolio/parte-03/clase-14/
  ofertas.csv       ofertas reales recolectadas, con fecha y fuente
  validacion.md     casos verificados a mano
```

### 3. Implementación de referencia

Las funciones necesarias existen parcialmente en el repositorio y hay que ampliarlas. La lista indica cuáles y con qué comportamiento.

```python
from dataclasses import dataclass, field

@dataclass
class OfertaCredito:
    """Oferta de crédito de cuota fija.

    Todos los montos en la misma moneda. `seguros_mensuales` agrupa los
    seguros exigidos por el acreedor; los opcionales se excluyen y se
    declaran en `excluidos`.
    """

    nombre: str
    monto_recibido: float
    plazo_meses: int
    tasa_mensual: float
    comision_apertura: float = 0.0
    seguros_mensuales: float = 0.0
    gastos_excluidos: float = 0.0
    excluidos: list[str] = field(default_factory=list)

    def cuota_total(self) -> float:
        capital = self.monto_recibido + self.comision_apertura
        i = self.tasa_mensual
        if i == 0:
            base = capital / self.plazo_meses
        else:
            factor = (1 + i) ** self.plazo_meses
            base = capital * i * factor / (factor - 1)
        return base + self.seguros_mensuales

    def cae(self) -> float:
        """Tasa anual que iguala el monto recibido con el flujo de cuotas."""
        pago = self.cuota_total()
        bajo, alto = 0.0, 1.0
        for _ in range(200):
            medio = (bajo + alto) / 2
            factor = (1 + medio) ** self.plazo_meses
            vp = pago * (factor - 1) / (medio * factor) if medio else pago * self.plazo_meses
            if abs(vp - self.monto_recibido) < 0.01:
                break
            if vp > self.monto_recibido:
                bajo = medio
            else:
                alto = medio
        return (1 + medio) ** 12 - 1

    def desembolso_total(self) -> float:
        return self.cuota_total() * self.plazo_meses + self.gastos_excluidos
```

### 4. La salida honesta

La misma comparación se puede presentar de forma que ayude a decidir o de forma que empuje hacia un producto. El contraste siguiente muestra las dos.

```text
COMPARACIÓN DE 3 OFERTAS DE CRÉDITO — monto recibido 4 000 000

  #  Oferta        CAE      Cuota    Desembolso total
  1  Banco C     18,87 %  223 273        5 358 552
  2  Banco A     20,44 %  223 170        5 356 080
  3  Banco B     19,97 %  221 585        5 318 040

  ⚠ Las ofertas 2 y 3 difieren en 0,47 pp de CAE: diferencia significativa.
  ⚠ El desembolso total ordena distinto que la CAE porque los plazos difieren.

SUPUESTOS APLICADOS
  · seguros considerados: solo los declarados como exigibles
  · sin prepagos ni mora
  · impuestos no incluidos en la CAE

NO INCLUIDO EN ESTE CÁLCULO
  · notaría, tasación e inscripción
  · costo de oportunidad del pie
  · comisión de prepago (eventual)
  · gastos de cobranza (eventual)

Este resultado es educativo y no constituye asesoría ni oferta.
```

Nótese que la salida **advierte cuando el orden por CAE difiere del orden por desembolso total**. Ese
aviso es el que evita la conclusión equivocada más común de cualquier comparador.

### 5. Validación

La validación compara la salida del comparador con casos resueltos a mano en las clases anteriores. Es el control que impide que un error se propague sin que nadie lo note.

```text
Caso 1 — CAE verificada a mano (clase 13)
  entrada   recibido 3 000 000 · 24 cuotas de 152 400
  esperado  21,84 % (±0,05)
  obtenido  21,83 %   ✔

Caso 2 — tasa cero
  entrada   recibido 1 200 000 · 12 cuotas · tasa 0 · sin seguros
  esperado  CAE 0,00 % · cuota 100 000
  obtenido  0,00 % · 100 000   ✔

Caso 3 — orden invertido entre métricas
  entrada   tres ofertas de la clase 13
  esperado  la advertencia de orden divergente se activa
  obtenido  advertencia mostrada   ✔

Caso 4 — diferencia no significativa
  entrada   dos ofertas con CAE 19,98 % y 20,01 %
  esperado  "diferencia no significativa"
  obtenido  mensaje mostrado   ✔
```

## 🧮 Ejemplo guiado

El ejemplo recorre la construcción completa, de los requisitos a la validación. Conviene respetar ese orden: escribir los casos de prueba antes que el código es lo que evita probar el código contra sí mismo.

**Situación de defensa.** Presentas el comparador y el revisor pregunta: *"Tu herramienta ordena por
CAE. ¿Por qué no por costo total, que es lo que la persona efectivamente paga?"*

**Respuesta defendible.**

1. **Porque el costo total no es comparable entre plazos distintos.** Un crédito a 12 meses y otro a
   48 tienen costos totales que difieren por el plazo, no por lo caros que sean. La CAE normaliza esa
   diferencia; el costo total no.
2. **Porque la herramienta muestra ambos.** El orden principal es por CAE y la tabla incluye el
   desembolso total, con una advertencia explícita cuando los dos criterios ordenan distinto. La
   decisión final queda en el usuario, que es quien conoce su restricción de flujo.
3. **Porque el criterio está declarado.** La salida dice qué métrica ordena. Un comparador que ordena
   sin decir por qué es el que induce a error, con cualquier métrica que use.

**Contra-pregunta esperable:** *"¿Y si alguien elige solo mirando el primer lugar?"* Respuesta: por eso
existe el requisito 7 y la advertencia de orden divergente. La herramienta no puede impedir una mala
lectura, pero sí debe hacerla difícil. Esa es la diferencia entre informar y aconsejar, y esta
herramienta hace lo primero.

**Lo que este intercambio enseña:** una herramienta financiera se defiende explicando **qué decisión
deja al usuario y qué decisión toma por él**. Toda métrica de orden es una decisión tomada por la
herramienta, y por eso debe ser visible.

## 🏦 Del cliente al banco

El cliente quiere elegir bien y el banco quiere que se elija su producto. La tabla enfrenta las dos lecturas de la misma comparación, y explica por qué el diseño de la salida es una decisión ética además de técnica.

| Tu comparador | Equivalente en la industria |
|---|---|
| Cálculo de CAE | Motor de cumplimiento normativo del área legal |
| Advertencia de orden divergente | Deber de información y no inducción a error |
| Supuestos declarados | Documentación de modelo (Parte 12, clase 13) |
| Exclusiones explícitas | Limitaciones declaradas en materiales comerciales |
| Casos de validación | Suite de pruebas regulatorias antes de publicar |

## 🧪 Práctica

Este proyecto es la práctica. Trabaja en `project/README.md` de esta parte.

1. Recolecta al menos seis ofertas reales con fecha y fuente, en `ofertas.csv`.
2. Implementa los siete requisitos y ejecuta `pytest -q` hasta verlo en verde.
3. Redacta la salida honesta con supuestos y exclusiones.
4. Prepara una defensa de tres minutos con dos decisiones de diseño justificadas.

## ⚠️ Errores frecuentes

Los síntomas de la tabla aparecen cuando otra persona usa el comparador. Casi todos se evitan declarando los supuestos y los límites en la propia salida, y no en una nota aparte.

| Síntoma | Causa probable | Corrección |
|---|---|---|
| La herramienta recomienda sin advertir | No hay declaración de límites | Muestra siempre supuestos y exclusiones. |
| Se declara ganadora una oferta por 0,03 pp | Falsa precisión | Implementa el umbral de significancia. |
| El orden confunde al usuario | Se ordena por una métrica sin decirlo | Declara la métrica de orden en la salida. |
| Las pruebas validan el propio código | Esperados calculados con la misma función | Usa valores verificados de forma independiente. |
| Las ofertas no tienen fecha | Los datos caducan | Registra fecha y fuente de cada oferta. |
| Se comparan productos distintos | Base no homogénea | Compara solo productos de la misma naturaleza. |

## ❓ Preguntas de comprobación

1. ¿Cuáles son las tres responsabilidades de un comparador y en qué orden?
2. ¿Por qué el costo total no es comparable entre plazos distintos?
3. ¿Qué debe ocurrir cuando dos ofertas difieren en 0,03 puntos de CAE?
4. ¿Qué conceptos debes declarar como excluidos y por qué?
5. Defiende en tres frases la métrica de orden que elegiste.

## 📥 Entregable

Guarda en `portfolio/parte-03/clase-14/` y en `apps/product_comparator/`:

- el código con los siete requisitos y sus pruebas en verde;
- `ofertas.csv` con al menos seis ofertas reales fechadas y con fuente;
- `validacion.md` con cuatro casos verificados de forma independiente;
- la salida de ejemplo con supuestos y exclusiones, y tus notas de defensa.

<!-- gen:etica:start -->
## 🔐 Seguridad, ética y límites

Trabaja siempre con datos sintéticos o propios: nunca uses datos reales de terceros,
números de cuenta, documentos de identidad ni antecedentes crediticios ajenos. Este
material es formativo y **no constituye asesoría financiera, tributaria ni legal**; las
tasas, comisiones, límites y normas citados cambian y deben verificarse en la fuente
oficial vigente del país donde se aplique. Cuando un cálculo alimente una decisión que
afecte a otra persona, registra los supuestos y quién los aprobó.
<!-- gen:etica:end -->

## 📗 Fuentes y verificación

- Benninga, S. (2014). *Financial Modeling* (4.ª ed.). MIT Press. Diseño y validación de modelos comparativos.
- Ross, S., Westerfield, R. y Jordan, B. (2022). *Fundamentos de finanzas corporativas* (12.ª ed.). McGraw-Hill. Capítulo 6: base de cálculo de la tasa efectiva.
- World Bank (2017). *Good Practices for Financial Consumer Protection*. Banco Mundial. Requisitos de comparabilidad y no inducción a error.
- European Union (2008). *Directive 2008/48/EC on credit agreements for consumers*. Anexo I: fórmula normativa de la tasa anual equivalente.
- Federal Reserve / OCC (2011). *Supervisory Guidance on Model Risk Management* (SR 11-7). Documentación y validación de herramientas de cálculo.
- Verificación local: si publicas el comparador, revisa las normas de tu país sobre publicidad financiera y sobre la obligación de advertir que no constituye asesoría.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 13 · Comisiones, CAE y costo total](13-comisiones-cae-y-costo-total.md) | [Parte 03](../README.md) · [Programa](../../../SYLLABUS.md) | [Proyecto de la parte →](../project/README.md) |
<!-- gen:footer:end -->
