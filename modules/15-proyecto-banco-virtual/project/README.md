# Proyecto integrador: Banco Virtual — Banco Austral

## De qué se trata

Este es el proyecto que cierra las cuatro primeras etapas y las 240 clases
originales del programa. Construye un banco completo, lo hace operar durante un
ciclo y una crisis, y lo defiende ante un comité.

No introduce temas nuevos. Su dificultad es otra: las quince partes anteriores se
estudiaron por separado y aquí tienen que encajar entre sí. La decisión de precio
de la Parte 15 compite con el apetito de riesgo de la Parte 11; el modelo
operativo de la Parte 10 tiene que soportar la propuesta de valor de la Parte 15.
Esas contradicciones son el contenido del proyecto.

Todo dato es sintético y todo cálculo tiene que ser reproducible. Esa exigencia
—más que el contenido— es lo que convierte el ejercicio en formación
profesional.

## Contexto

Un grupo con licencia bancaria en trámite quiere operar en dieciocho meses con un
presupuesto que no cubre todo lo que el equipo comercial ha prometido. Tú diriges
el diseño y responderás ante un comité que va a buscar dónde el plan se
contradice.

## Alcance

| Incluido | Excluido |
|---|---|
| Alcance, gobierno y arquitectura de datos | Conexiones bancarias reales |
| Productos, precios y motor de originación | Credenciales, claves o fondos reales |
| Contabilidad, tesorería y marco de riesgos | Datos personales de cualquier tipo |
| Cumplimiento proporcional y cuadro de mando | Asesoría legal, financiera o de inversión |
| Estrés, ciclo, crisis y defensa | Interlocución con ninguna autoridad |

## Entregables

| # | Entregable | Qué debe contener |
|---:|---|---|
| 1 | Alcance y modelo de negocio | Cuatro preguntas, exclusiones cuantificadas y apetito preliminar |
| 2 | Gobierno y atribuciones | Órganos, matriz de atribuciones sin huecos y políticas obligatorias |
| 3 | Arquitectura de datos | Capas, dato maestro, identificador único y capa semántica |
| 4 | Catálogo y precios | Productos justificados y precio con sus cuatro componentes |
| 5 | Originación y modelos | Tres zonas de decisión y parámetros con su dominio declarado |
| 6 | Contabilidad y tesorería | Estados proyectados, provisiones por etapas y restricción activa |
| 7 | Marco de riesgos y cumplimiento | Límites con acciones comprometidas y programa proporcional |
| 8 | Cuadro de mando | Con contrapesos y fichas completas |
| 9 | Estrés, ciclo y crisis | Escenario que rompe, bitácora del ciclo y de la crisis |
| 10 | Defensa y límites | Ocho límites y siete preguntas anticipadas con su respuesta |

## Rúbrica

| Criterio | Puntos | Qué se valora |
|---|---:|---|
| Coherencia del conjunto | 25 | Que las quince partes encajen entre sí |
| Reproducibilidad | 20 | Cada cifra desde sus supuestos declarados |
| Escenario que rompe | 15 | Contra las vulnerabilidades propias del banco |
| Bitácora de decisiones | 15 | Con la información disponible en cada momento |
| Límites declarados | 15 | Ocho, cada uno con su razón |
| Defensa | 10 | Preguntas anticipadas y respondidas con dato |

**Total:** 100 puntos. **Aprobación:** 70.

## Restricciones

- **No** se usan claves, credenciales, tokens ni fondos reales de ningún tipo.
- **No** se usan datos personales de ninguna persona, ni siquiera propios.
- **No** se conecta con ninguna infraestructura de producción.
- **No** se presenta como asesoría legal, financiera ni de inversión.
- Todo dato es sintético y está declarado como tal en cada entregable.
- Cada cifra del proyecto remite a un cálculo que otra persona puede reproducir.

## Cómo se comprueba

```bash
python -m pytest -q
```

## Aviso

Material **docente**. El Banco Austral es una entidad ficticia con datos
sintéticos y **no es un banco**. Ninguna de sus salidas constituye asesoría
financiera, legal ni de inversión, y ninguna de sus cifras debe usarse para
decidir sobre una entidad real.
