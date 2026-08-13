# Parte 16: Proyecto Banco Virtual

Esta parte cierra la Etapa 4 y las 240 clases originales del programa
construyendo un banco completo. No introduce temas nuevos: obliga a que los
quince anteriores encajen entre sí, y ahí es donde aparecen las contradicciones
que ninguna parte por separado podía mostrar.

El Banco Austral es una entidad ficticia con parámetros fijos. Todo lo que se
afirme sobre él tiene que salir de un cálculo reproducible con datos sintéticos
declarados, y esa exigencia —más que el contenido— es lo que convierte el
ejercicio en formación profesional.

El eje es que **una decisión correcta por separado puede ser incorrecta en el
conjunto**. Las clases 16 y 17 lo demuestran haciendo operar el banco durante un
ciclo y durante una crisis, que es cuando las decisiones se estorban.

## Con qué hay que llegar

| Parte | Qué aporta |
|---|---|
| 9 – 12 | Crédito, operaciones, riesgos y regulación |
| 13 – 15 | Empresa, tecnología y dirección |

## Qué se aprende

1. **Acotar** el alcance de un banco con renuncias cuantificadas y un apetito de riesgo declarado.
2. **Diseñar** gobierno, atribuciones y arquitectura de datos antes de que existan las operaciones.
3. **Construir** precios desde la curva de transferencia y provisiones por el modelo de tres etapas.
4. **Someter** el banco a un escenario adverso diseñado contra sus vulnerabilidades específicas.
5. **Defender** cada decisión con su cálculo, su supuesto y la alternativa que se descartó.

## Cómo se encadenan las 18 clases

Las dieciocho clases construyen, operan y defienden.

Las **clases 1 a 4** fijan las reglas del proyecto y las decisiones fundacionales:
alcance, gobierno y arquitectura de datos. La 4 se toma antes de que existan los
datos, que es cuando cuesta poco y decide mucho.

Las **clases 5 a 8** definen qué se ofrece, a qué precio, cómo se decide y con qué
modelos, en un banco nuevo que no tiene historia con la que estimarlos.

Las **clases 9 a 11** montan la operación diaria, la contabilidad y la tesorería, y
la 11 encuentra que la restricción activa de un banco nuevo no es el capital.

Las **clases 12 a 14** ponen los límites: marco de riesgos con acciones
comprometidas, programa de cumplimiento proporcional al segmento y cuadro de
mando con contrapesos.

Las **clases 15 a 17** rompen el banco a propósito: prueba de estrés, un ciclo
completo con decisiones rezagadas y una crisis donde el efecto de señal domina.
La **clase 18** lo defiende ante un comité, y lo que más pesa no son las respuestas
sino los límites que se reconocen.

## Secuencia

1. [Alcance del proyecto](classes/01-alcance-del-proyecto.md)
2. [Modelo de negocio del banco](classes/02-modelo-de-negocio-del-banco.md)
3. [Constitución y gobierno](classes/03-constitucion-y-gobierno.md)
4. [Arquitectura de datos y sistemas](classes/04-arquitectura-de-datos-y-sistemas.md)
5. [Catálogo de productos](classes/05-catalogo-de-productos.md)
6. [Modelo de precios](classes/06-modelo-de-precios.md)
7. [Originación y decisión](classes/07-originacion-y-decision.md)
8. [Modelos de riesgo](classes/08-modelos-de-riesgo.md)
9. [Operaciones y pagos](classes/09-operaciones-y-pagos.md)
10. [Contabilidad y estados financieros](classes/10-contabilidad-y-estados-financieros.md)
11. [Tesorería y balance](classes/11-tesoreria-y-balance.md)
12. [Marco de riesgos](classes/12-marco-de-riesgos.md)
13. [Cumplimiento y prevención](classes/13-cumplimiento-y-prevencion.md)
14. [Cuadro de mando del banco](classes/14-cuadro-de-mando-del-banco.md)
15. [Prueba de estrés del banco](classes/15-prueba-de-estres-del-banco.md)
16. [Simulación de un ciclo](classes/16-simulacion-de-un-ciclo.md)
17. [Simulación de una crisis](classes/17-simulacion-de-una-crisis.md)
18. [Defensa y cierre](classes/18-defensa-y-cierre.md)

## Cómo se trabaja

Son **18 clases de 90 minutos** —27 horas de sesión— con **6 laboratorios**, **2 evaluaciones** y un proyecto integrador. Cada clase supone la anterior, así que el orden importa: saltarse una deja sin base a las que vienen después.

Los laboratorios se resuelven con datos propios o sintéticos y nunca con datos reales de terceros. Las evaluaciones son dos: una diagnóstica al empezar, que no se califica para aprobar sino para saber qué reforzar, y una final. El proyecto es el entregable que demuestra que la parte se entendió.

## Qué queda como evidencia

- El banco documentado en sus dieciocho entregables, con supuestos declarados.
- Los estados financieros proyectados y las provisiones por etapas.
- La prueba de estrés con la métrica que rompe primero.
- La bitácora del ciclo y de la crisis, con cada decisión y su razón.
- La defensa ante el comité con las preguntas difíciles anticipadas.

> **Sobre el Banco Austral.** Es una entidad ficticia y todos sus datos son
> sintéticos. El proyecto no se conecta con ninguna infraestructura real, no usa
> credenciales ni fondos, y ninguna de sus salidas constituye asesoría financiera,
> legal ni de inversión.

## Continúa en la Etapa 5

El banco de esta parte opera dentro de un país y con instrumentos tradicionales.
La Parte 23 construye el mismo banco con finanzas abiertas, pagos
transfronterizos, custodia de activos digitales y un mercado tokenizado, y lo
defiende ante un supervisor.

**Quince incidentes que la Etapa 5 añade a la simulación de crisis.** Se pueden
inyectar en el ejercicio de esta parte una vez estudiadas las Partes 17 a 22,
como ampliación del escenario:

```text
 1 · consentimiento revocado durante una
     operación en curso
 2 · interfaz de datos caída el día 1 de mes
 3 · mensaje de pago duplicado
 4 · pago transfronterizo retenido por
     coincidencia parcial de sanciones
 5 · falta de liquidez en la cuenta nostro
     antes del corte
 6 · instrumento estable que pierde su
     paridad durante nueve horas
 7 · pérdida de una parte del material
     criptográfico de custodia
 8 · oráculo que reporta un precio correcto
     de un mercado vacío
 9 · contrato inteligente que ejecuta lo que
     dice y no lo que se quiso decir
10 · manipulación del precio de referencia
     en la ventana de cálculo
11 · fallo de entrega contra pago en una
     emisión tokenizada
12 · fallo de pago contra pago en una
     operación de cambio
13 · proveedor tecnológico común a veinte
     entidades que deja de operar
14 · corrida digital sobre un pasivo
     reembolsable en horas
15 · incumplimiento de la regla del viaje
     detectado en inspección
```

Cada uno tiene su caso desarrollado en la
[biblioteca de casos](../../case-studies/README.md), con hechos, decisiones,
controles y preguntas.
