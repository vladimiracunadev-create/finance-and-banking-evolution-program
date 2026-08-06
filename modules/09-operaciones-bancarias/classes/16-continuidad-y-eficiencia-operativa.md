---
part: 10
class: 16
title: "Continuidad y eficiencia operativa"
level: profesional
duration_minutes: 90
status: complete
---

<!-- gen:header:start -->
# Clase 16 · Continuidad y eficiencia operativa

> [← 15 · Canales y experiencia del cliente](15-canales-y-experiencia-del-cliente.md) · [Índice de la parte](../README.md) · [Proyecto de la parte →](../project/README.md)

**Parte 10 — Operaciones bancarias** · **Nivel:** Profesional — perfil bancario · **Duración:** 90 minutos
<!-- gen:header:end -->

## 🎯 Propósito

Cerrar la parte integrando sus doce procesos en una sola pregunta de dirección: **¿puede el banco seguir
operando cuando algo falla, y a qué costo opera cuando todo funciona?** La continuidad y la eficiencia
son las dos medidas con las que se juzga una operación bancaria completa.

## 📚 Objetivos

Al finalizar podrás:

1. **Identificar** los procesos críticos de un banco y su tolerancia a la interrupción.
2. **Construir** un plan de continuidad con tiempos objetivo verificables.
3. **Calcular** e interpretar el índice de eficiencia operativa.
4. **Diagnosticar** una operación con indicadores de proceso, no de percepción.
5. **Integrar** los procesos de la Parte 10 en un mapa operativo coherente.

<!-- gen:agenda:start -->
## Agenda de 90 minutos

| Minutos | Bloque | Qué ocurre |
|---:|---|---|
| 0–10 | Activación | Pregunta diagnóstica y recuperación de la clase anterior. |
| 10–35 | Conceptos | Desarrollo guiado con la fuente oficial a la vista. |
| 35–55 | Ejemplo guiado | El docente resuelve el caso numérico paso a paso. |
| 55–80 | Práctica | El estudiante replica con datos propios o sintéticos. |
| 80–90 | Cierre | Preguntas de comprobación y registro en el portafolio. |
<!-- gen:agenda:end -->

## 🧩 Conceptos centrales

| Concepto | Comprensión verificable |
|---|---|
| `proceso crítico` | Aquel cuya interrupción impide cumplir obligaciones o daña gravemente al cliente. |
| `tiempo objetivo de recuperación` | Plazo máximo aceptable para restablecer un proceso. |
| `punto objetivo de recuperación` | Cantidad máxima de datos que se acepta perder, medida en tiempo. |
| `tolerancia a la interrupción` | Límite que el banco declara y el supervisor evalúa. |
| `índice de eficiencia` | Gastos operativos sobre ingresos operativos. Menor es mejor. |
| `resiliencia operacional` | Capacidad de seguir prestando servicios críticos ante disrupciones. |
| `dependencia de terceros` | Proveedor cuya falla interrumpe un proceso propio. |
| `prueba de continuidad` | Ejercicio real que verifica el plan; sin prueba, el plan es un documento. |

## 🧠 Modelo mental

```text
CONTINUIDAD responde:  ¿qué pasa si falla?
EFICIENCIA responde:   ¿cuánto cuesta que funcione?

y están conectadas por una sola variable: la REDUNDANCIA

  más redundancia → más continuidad → más costo → peor eficiencia
  menos redundancia → mejor eficiencia → hasta el día del incidente
```

**El punto de equilibrio no se elige por intuición: se calcula.** El costo de la redundancia se compara
con la pérdida esperada de la interrupción, y la decisión se documenta. Un banco sin ese cálculo está
apostando sin saber cuánto apostó.

## 📖 Desarrollo

### 1. Mapa de procesos de la Parte 10

```text
CAPTACIÓN ────► CUENTAS ────► MEDIOS DE PAGO ────► COMPENSACIÓN
   (cl. 2)      (cl. 4)          (cl. 9-10)          (cl. 7)
      │            │                  │                  │
      └────────────┴──────────────────┴──────────────────┘
                             │
                      CONCILIACIÓN (cl. 8)
                             │
COLOCACIÓN ────► CAJA Y SUCURSALES ────► TESORERÍA ────► INTERNACIONAL
   (cl. 3)          (cl. 11)              (cl. 12)        (cl. 13-14)
                             │
                      CANALES Y CLIENTE (cl. 15)
                             │
                    CONTINUIDAD Y EFICIENCIA (cl. 16)
```

**Todo proceso operativo termina en una conciliación y empieza en un registro.** Esa es la columna
vertebral: si el registro es incompleto o la conciliación no se hace, ningún otro control funciona.

### 2. Criticidad y tolerancia

| Proceso | Criticidad | Tiempo objetivo de recuperación | Punto objetivo |
|---|---|---:|---:|
| Sistema de pagos de alto valor | Máxima | 2 horas | 0 |
| Medios de pago con tarjeta | Máxima | 4 horas | 0 |
| Banca en línea y móvil | Alta | 4 horas | 15 min |
| Cajeros automáticos | Alta | 8 horas | 15 min |
| Contabilidad y cierre diario | Alta | 24 horas | 0 |
| Originación de créditos | Media | 48 horas | 4 horas |
| Reportes de gestión | Baja | 5 días | 24 horas |

*(Valores ilustrativos. Cada institución los define y su supervisor los evalúa; verifica los tuyos.)*

```text
CÓMO SE DETERMINA
  1. análisis de impacto: ¿qué se pierde por cada hora de interrupción?
     · pérdida financiera directa
     · incumplimiento de obligación (multas, sanciones)
     · daño al cliente
     · daño reputacional
  2. la curva de impacto casi nunca es lineal:
     saltos en el corte de compensación, en el cierre contable,
     en el vencimiento de una obligación
  3. el tiempo objetivo se fija ANTES del salto
```

### 3. Componentes de un plan de continuidad

```text
1. ANÁLISIS DE IMPACTO          procesos, dependencias, tiempos objetivo
2. ESCENARIOS                   falla técnica, ciberincidente, indisponibilidad
                                de sede, falla de proveedor, evento natural
3. ESTRATEGIA DE RECUPERACIÓN   redundancia, sitio alterno, proveedor alterno,
                                procedimiento manual de contingencia
4. PLAN DE ACCIÓN               quién hace qué, en qué orden, con qué autoridad
5. COMUNICACIÓN                 clientes, supervisor, personal, medios
6. PRUEBAS                      calendario, alcance, criterios de éxito
7. LECCIONES                    hallazgos incorporados al plan
```

**La dependencia de terceros es hoy el punto más frágil.** Un banco puede tener su continuidad
resuelta y depender de un único proveedor de nube, de un único procesador de tarjetas o de un único
proveedor de conectividad. Los marcos de resiliencia operacional del Comité de Basilea y de la
autoridad europea insisten en el mismo punto: **la responsabilidad no se terceriza**.

```text
PREGUNTAS SOBRE UN PROVEEDOR CRÍTICO
  · ¿existe alternativa y cuánto tarda activarla?
  · ¿los datos son portables o quedan cautivos?
  · ¿el contrato incluye derecho de auditoría y de salida ordenada?
  · ¿el proveedor tiene concentración sistémica (lo usan todos)?
  · ¿se ha probado la salida, o solo está escrita?
```

### 4. Prueba: el plan que no se prueba no existe

| Tipo de prueba | Qué verifica | Frecuencia típica |
|---|---|---|
| Revisión documental | Coherencia y actualización | Anual |
| Simulación de escritorio | Comprensión de roles | Semestral |
| Prueba técnica parcial | Recuperación de un componente | Trimestral |
| Conmutación a sitio alterno | Recuperación real | Anual |
| Ejercicio con proveedores | Dependencias externas | Anual |
| Prueba sorpresa | Comportamiento sin preparación | Ocasional |

**Criterio de éxito verificable:** «se restableció el servicio X en menos de N horas con pérdida de datos
menor a M minutos, sin intervención del personal que diseñó el plan». Sin ese último requisito, la
prueba mide el conocimiento de dos personas, no la capacidad de la organización.

### 5. Eficiencia operativa

```text
                    gastos operativos
ÍNDICE DE EFICIENCIA = ─────────────────────
                    ingresos operativos

interpretación:
  < 45 %   muy eficiente
  45–55 %  eficiente
  55–65 %  promedio
  > 65 %   presión sobre la rentabilidad
```

```text
DESCOMPOSICIÓN ÚTIL
  gastos operativos = personal + tecnología + inmuebles + terceros + otros
  ingresos operativos = margen financiero + comisiones + otros ingresos

MEJORAR EL ÍNDICE tiene dos caminos:
  bajar el numerador   → riesgo de degradar control y servicio
  subir el denominador → sostenible, pero más lento

el banco que solo recorta gastos mejora el índice
y empeora su riesgo operativo: la Parte 11, clase 10 lo mide
```

## 🧮 Ejemplo guiado

**Situación.** El banco sufre una interrupción y luego evalúa su inversión en continuidad.

```text
INCIDENTE
  falla del procesador de tarjetas, proveedor único
  hora de inicio: 14:20 de un viernes
  duración: 6 h 40 min
  transacciones afectadas: 214 000
  monto no procesado: 3 840 millones

TIEMPO OBJETIVO DECLARADO PARA MEDIOS DE PAGO: 4 horas
```

**Paso 1 — cuantifica la pérdida directa.**

```text
comisiones de intercambio no percibidas
  214 000 × 0,9 % × monto medio (17 950) = 34,6 millones
compensaciones a clientes comprometidas       12,0
sobrecosto de atención (llamadas, refuerzo)     8,4
penalidad contractual de red de tarjetas        6,0
PÉRDIDA DIRECTA                                61,0 millones
```

**Paso 2 — cuantifica lo que no aparece en la factura.**

```text
fuga de clientes atribuible (0,6 % de 128 000 tarjetahabientes activos)
  = 768 clientes × margen anual 96 000 = 73,7 millones anuales
  valor presente a 5 años al 9 %: 73,7 × 3,890 = 286,7 millones

sanción del supervisor por exceder el tiempo objetivo declarado
  estimada: 45 millones

PÉRDIDA TOTAL ESTIMADA: 61,0 + 286,7 + 45,0 = 392,7 millones
```

**Paso 3 — evalúa la alternativa que no se había aprobado.**

```text
PROPUESTA RECHAZADA HACE 18 MESES
  procesador secundario con conmutación automática
  inversión inicial          180 millones
  costo anual de operación    62 millones
  tiempo de conmutación       25 minutos
```

**Paso 4 — calcula la pérdida esperada anual sin redundancia.**

```text
probabilidad histórica de interrupción > 4 h: 1 cada 3 años → 0,333 al año
pérdida por evento: 392,7

PÉRDIDA ESPERADA ANUAL SIN REDUNDANCIA: 0,333 × 392,7 = 130,8
```

**Paso 5 — calcula la pérdida esperada con redundancia.**

```text
con conmutación en 25 min, la pérdida por evento se reduce a:
  comisiones no percibidas (25 min de 400)  = 2,2
  sin compensaciones, sin penalidad, sin sanción
  fuga despreciable
  pérdida por evento ≈ 3,5

PÉRDIDA ESPERADA ANUAL CON REDUNDANCIA: 0,333 × 3,5 = 1,2
BENEFICIO ANUAL: 130,8 − 1,2 = 129,6
COSTO ANUAL: 62,0
BENEFICIO NETO ANUAL: 67,6 millones
```

**Paso 6 — valor presente de la decisión.**

```text
VPN a 7 años al 9 %:
  −180 + 67,6 × 5,033 = −180 + 340,2 = +160,2 millones

la propuesta rechazada tenía VPN positivo de 160 millones
se rechazó porque se comparó su COSTO (62 anuales)
contra un beneficio que nadie había cuantificado
```

**Paso 7 — efecto sobre el índice de eficiencia.**

```text
                        sin redundancia   con redundancia
gastos operativos            48 200            48 262
ingresos operativos          82 400            82 400
índice de eficiencia         58,5 %            58,6 %

el efecto en el índice es de 0,1 puntos
la exposición evitada es de 393 millones por evento
```

**Interpreta:** la decisión se había tomado mirando el indicador equivocado. **Un deterioro de 0,1
puntos en el índice de eficiencia bloqueó una inversión con valor presente de 160 millones.** Ese es el
patrón que esta clase busca instalar: la eficiencia sin continuidad es una eficiencia contable, y se
paga entera el día del incidente. La Parte 11, clase 10 formaliza esta misma pérdida como riesgo
operacional y le asigna capital.

## 🏦 Del cliente al banco

| Vista del cliente | Vista del banco | Parte |
|---|---|---|
| «Mi tarjeta no funcionó todo el viernes» | Falla de proveedor único y tiempo objetivo excedido | 10, clase 16 |
| «El banco compensó el inconveniente» | Costo directo del incidente | 12, clase 9 |
| «Este banco cobra menos comisiones» | Índice de eficiencia y su traslado al precio | 15, clase 7 |
| «Cerraron cajas y hay más fila» | Recorte de gasto sin rediseño de proceso | 10, clase 11 |
| «Perdí confianza y me cambié» | Fuga como componente mayor de la pérdida | 10, clase 15 |

## 🧪 Práctica

En `labs/lab-06.md`, sección de continuidad:

1. Clasifica diez procesos por criticidad y asígnales tiempo y punto objetivo de recuperación.
2. Construye el análisis de impacto de una interrupción de 8 horas en dos procesos.
3. Calcula el índice de eficiencia de un banco sintético y descomponlo por componente.
4. Evalúa una inversión en redundancia comparando su costo con la pérdida esperada evitada.

## ⚠️ Errores frecuentes

| Síntoma | Causa probable | Corrección |
|---|---|---|
| El plan existe pero nunca se probó | Sin calendario de pruebas | Prueba real, sin quien lo diseñó. |
| Se depende de un proveedor único | Concentración no evaluada | Exige alternativa probada y salida ordenada. |
| Se rechaza redundancia por su costo | Pérdida esperada no cuantificada | Compara costo contra pérdida esperada. |
| Se mejora la eficiencia recortando control | Numerador como única palanca | Mide también el riesgo operacional resultante. |
| Tiempos objetivo sin fundamento | Sin análisis de impacto | Deriva los tiempos de la curva de impacto. |
| Se terceriza el proceso y la responsabilidad | Interpretación errónea del contrato | La responsabilidad no se terceriza. |

## ❓ Preguntas de comprobación

1. ¿Qué distingue el tiempo objetivo de recuperación del punto objetivo de recuperación?
2. ¿Por qué la curva de impacto de una interrupción no es lineal?
3. ¿Qué debe cumplir una prueba de continuidad para ser válida?
4. ¿Por qué mejorar el índice de eficiencia puede aumentar el riesgo operacional?
5. ¿Cómo se decide cuánta redundancia comprar?

## 📥 Entregable

Guarda en `portfolio/parte-10/clase-16/`:

- la clasificación de procesos con tiempos y puntos objetivo justificados;
- el análisis de impacto de la interrupción con su curva de pérdida;
- el índice de eficiencia calculado y descompuesto;
- la evaluación de la inversión en redundancia con su valor presente.

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

- Basel Committee on Banking Supervision (2021). *Principles for Operational Resilience*. BIS. <https://www.bis.org/bcbs/publ/d516.htm>
- Basel Committee on Banking Supervision (2021). *Revisions to the Principles for the Sound Management of Operational Risk*. BIS.
- Financial Stability Board (2020). *Effective Practices for Cyber Incident Response and Recovery*. FSB. <https://www.fsb.org/2020/10/effective-practices-for-cyber-incident-response-and-recovery-final-report/>
- ISO (2019). *ISO 22301: Security and resilience — Business continuity management systems*. ISO.
- Rose, P. y Hudgins, S. (2013). *Bank Management and Financial Services* (9.ª ed.). McGraw-Hill. Capítulo 6: análisis de eficiencia y desempeño.
- Verificación local: revisa los requisitos de continuidad operacional, notificación de incidentes y gestión de proveedores críticos que exige tu supervisor.

<!-- gen:footer:start -->
---

| Anterior | Índice | Siguiente |
|---|---|---|
| [← 15 · Canales y experiencia del cliente](15-canales-y-experiencia-del-cliente.md) | [Parte 10](../README.md) · [Programa](../../../SYLLABUS.md) | [Proyecto de la parte →](../project/README.md) |
<!-- gen:footer:end -->
