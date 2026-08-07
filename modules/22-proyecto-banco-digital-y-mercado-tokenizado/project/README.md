# Proyecto capstone: banco digital con mercado tokenizado

## De qué se trata

Este es el proyecto final del programa y no se parece a los veintidós anteriores.
Los otros pedían aplicar un método a un problema acotado. Este pide **construir un
sistema completo, hacerlo funcionar durante un día simulado y defenderlo ante un
comité que va a buscar dónde se contradice**.

La diferencia no es de tamaño. Un proyecto grande sigue siendo un proyecto: cada
pieza se diseña, se prueba y se da por buena. Un capstone es otra cosa. Aquí las
piezas se diseñan por separado —y cada una queda correcta— y luego se integran,
y en la integración aparecen contradicciones que ninguna revisión individual podía
detectar. **Esas contradicciones son el contenido del proyecto.** Un capstone que
no encuentra ninguna no ha integrado nada: ha yuxtapuesto.

El proyecto **puede concluir que el sistema propuesto no debe construirse**, y esa
conclusión vale lo mismo que la contraria si está sostenida por el expediente
completo. Lo que no vale es un sistema que funciona porque nunca se le hicieron
las preguntas difíciles.

## Contexto

Un grupo con licencia bancaria en trámite quiere ofrecer a 2 400 pymes exportadoras
un banco digital que combine cuentas locales, pagos transfronterizos, cambio de
divisas y crédito con colateral tokenizado. Dispone de dieciocho meses y de un
presupuesto que no cubre todo lo que el equipo comercial ha prometido. Tú diriges
el diseño.

## Alcance

| Incluido | Excluido |
|---|---|
| Alcance funcional y su carga regulatoria | Conexiones bancarias reales |
| Decisiones de construir, integrar o comprar | Credenciales, claves o fondos reales |
| Arquitectura del registro y del dinero | Creación de una criptomoneda de uso real |
| Custodia, liquidación, pagos y ciclo de vida | Datos personales de cualquier tipo |
| Expediente regulatorio y modelo de amenazas | Asesoría legal, financiera o de inversión |
| Escenario de tensión y plan de resolución | Interlocución real con una autoridad |

Todos los datos del proyecto son **sintéticos y declarados como tales**. El sistema
que se construye es un simulador con fines docentes y no es un banco.

## Las tres fases

El proyecto sigue los tres bloques de la parte, y cada fase produce un entregable
que la siguiente consume.

### Fase 1 — Qué construir (clases 1 a 6)

Se decide el alcance y se toman las tres decisiones de arquitectura. La fase
termina cuando las cuatro preguntas se han aplicado a todas las funciones
propuestas, las excluidas tienen su razón escrita y la cadena de decisiones
—registro, dinero, producto— está cerrada sin dependencias abiertas.

**Criterio de cierre:** la carga regulatoria del alcance y la facturación necesaria
están calculadas, y el equipo ha decidido conscientemente si el proyecto es viable
con esas cifras.

### Fase 2 — Construirlo y encontrar las contradicciones (clases 7 a 12)

Se construyen los componentes: registro, interfaces, custodia, liquidación, pagos
y ciclo de vida. Y luego se hacen funcionar juntos un día completo con seis
incidencias, que es cuando aparecen las tensiones.

**Criterio de cierre:** cada tensión está declarada entre las dos decisiones que la
producen, resuelta, y con el sacrificio cuantificado. Una tensión sin resolver
bloquea el sistema, y eso está implementado en el código: no es una recomendación.

### Fase 3 — Probarlo y defenderlo (clases 13 a 18)

Se ensambla el expediente, se cruza por parejas, se modelan las amenazas, se
diseña el escenario que rompe el sistema, se prueba el plan de resolución, se
escribe lo que el sistema no puede hacer y se defiende ante el comité.

**Criterio de cierre:** las siete preguntas del comité tienen respuesta con
evidencia, y la sección de límites tiene al menos ocho puntos con su razón.

## Entregables

| # | Entregable | Fase | Qué debe contener |
|---:|---|:---:|---|
| 1 | Alcance justificado | 1 | Cuatro preguntas por función y exclusiones con razón |
| 2 | Análisis de construir o integrar | 1 | Coste total con salida y decisión por componente |
| 3 | Perímetro del propio sistema | 1 | Hechos de diseño con su fuente y regímenes activados |
| 4 | Las tres decisiones de arquitectura | 1 | Registro, dinero y producto, con su cadena cerrada |
| 5 | Sistema construido | 2 | Código que corre, con sus pruebas |
| 6 | Bitácora del día simulado | 2 | Las seis incidencias y su resultado |
| 7 | Tensiones resueltas | 2 | Cada una con su sacrificio cuantificado |
| 8 | Expediente de doce piezas | 3 | Cada afirmación con su evidencia |
| 9 | Modelo de amenazas | 3 | Priorizado y con una prueba por control |
| 10 | Escenario de tensión | 3 | Con punto de rotura y nivel de prueba declarado |
| 11 | Plan de resolución probado | 3 | Con el plazo medido, no el declarado |
| 12 | Sección de límites y defensa | 3 | Ocho límites y siete respuestas |

## Rúbrica

| Criterio | Puntos | Qué se valora |
|---|---:|---|
| Alcance y su justificación | 12 | Las exclusiones, no las inclusiones |
| Decisiones de arquitectura encadenadas | 13 | Que ninguna se tome antes de la que la condiciona |
| Sistema que corre y se prueba | 15 | Las cinco pruebas de modos de fallo |
| Tensiones encontradas y resueltas | 20 | Es el núcleo del capstone |
| Expediente con evidencia | 12 | Afirmación sin evidencia se retira |
| Escenario que rompe el sistema | 13 | Con fuente de correlación identificada |
| Límites y defensa | 15 | La sección de lo que no se puede hacer |

**Total:** 100 puntos. **Aprobación:** 70.

## Restricciones de seguridad

Estas restricciones no son recomendaciones y su incumplimiento invalida el
proyecto:

- **No** se usan claves, semillas, credenciales bancarias, tokens ni secretos
  reales. Solo `.env.example` con valores de ejemplo.
- **No** se usan datos personales de ninguna persona, ni siquiera propios.
- **No** se despliegan fondos reales ni se conecta con ninguna infraestructura de
  producción.
- **No** se crea una criptomoneda ni un instrumento destinado a uso real.
- **No** se construyen herramientas para ocultar fondos, eludir controles ni
  manipular mercados.
- Todo dato es sintético y está declarado como tal en el entregable.

## Cómo se entrega

```bash
python -m pytest tests/test_digital_bank_capstone.py -q
```

```bash
python apps/digital_bank_capstone/cli.py scope
```

```bash
python apps/digital_bank_capstone/cli.py tensions
```

El repositorio entregado debe pasar sus propias pruebas y las del programa. Un
capstone con pruebas en rojo no se defiende: se corrige primero.

## Aviso

Material **docente**. El sistema construido es un simulador con datos sintéticos y
**no es un banco**. Ninguna de sus salidas constituye asesoría legal, financiera ni
de inversión. Toda referencia normativa debe verificarse en su fuente oficial antes
de cualquier uso profesional.
