# Caso · Un agregador con demasiadas llaves

**Tema:** finanzas abiertas · **Parte relacionada:** 17 · **Naturaleza:** caso
sintético compuesto · **Fecha de verificación:** 2026-08-12

Un mercado abre sus interfaces para que compitan muchos proveedores y, tres años
después, uno solo concentra el acceso a los datos del 61 % de los clientes
conectados. Nadie infringió nada. La concentración es un resultado del diseño, no
una desviación.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · 14 bancos con interfaces reguladas
  · 47 proveedores terceros registrados
  · de esos 47, 39 no acceden directamente
    a los bancos: acceden a través de un
    intermediario técnico
  · ese intermediario es el mismo para los 39

SUPUESTO DEL EJERCICIO
  · clientes con al menos un consentimiento
    activo                       2 400 000
  · cuyos datos pasan por el intermediario
                                 1 464 000  (61 %)
  · el intermediario NO es entidad regulada
    en este mercado: es un proveedor de
    tecnología

INTERPRETACIÓN
  el registro cuenta 47 participantes; el
  riesgo operativo tiene 9 puntos de fallo,
  no 47
```

La distinción entre el mapa contractual y el mapa técnico es el núcleo del caso.
El supervisor ve cuarenta y siete relaciones; la infraestructura tiene nueve
caminos, y uno de ellos lleva el sesenta y uno por ciento del tráfico.

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Proveedor tercero pequeño | Llegar al mercado sin construir 14 conexiones | Su contrato, no el mapa completo |
| Intermediario técnico | Escala y márgenes | El mapa completo, y solo él |
| Bancos | Cumplir su obligación de dar acceso | Contratos con 47, tráfico de 9 |
| Clientes | Un servicio que funcione | Nada de esto |
| Supervisor | Competencia e inclusión | El registro de 47 |
| Competidor del intermediario | Entrar en un mercado ya repartido | El coste de replicar la integración |

## Decisiones

```text
AÑO 1  se publica la norma y las interfaces
       DECISIÓN: exigir interfaz a los
       bancos, no exigir nada a quien la
       consume

AÑO 1  aparecen tres intermediarios técnicos
       DECISIÓN DE LOS PEQUEÑOS: usar uno
       en lugar de integrar 14 veces
       RACIONAL Y CORRECTA

AÑO 2  dos intermediarios se retiran o son
       adquiridos
       NADIE LO REGISTRA COMO EVENTO
       DE MERCADO

AÑO 3  el superviviente concentra el 61 %
       DECISIÓN PENDIENTE: ¿es un problema
       de competencia, de resiliencia,
       o de ambos?
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Punto único de fallo no supervisado | Desde el año 2 | No todavía |
| Concentración de datos de 1,46 M | Desde el año 2 | Sí, como hecho |
| Dependencia comercial del pequeño | Desde el año 1 | Sí |
| Opacidad del mapa real | Desde el inicio | Sí |
| Barrera de entrada a nuevos entrantes | Desde el año 3 | Sí |
| Arbitraje de perímetro | Estructural | Sí |

El último merece explicación. El intermediario hace algo funcionalmente idéntico
a lo que hace un proveedor registrado —mover datos financieros de clientes— pero
como contractualmente es un subcontratista técnico, queda fuera del registro. No
hay engaño: hay una definición de perímetro que se dibujó por relación jurídica y
no por función.

## Regulación

```text
QUÉ ALCANZA Y QUÉ NO

  AL PROVEEDOR REGISTRADO
    sí: obligaciones de seguridad,
    consentimiento, reporte

  AL BANCO
    sí: obligación de dar acceso y de
    controlar su tercería

  AL INTERMEDIARIO TÉCNICO
    indirectamente, a través de los
    contratos de sus clientes

  LA PREGUNTA ABIERTA
    ¿debe existir una figura de proveedor
    tecnológico crítico también aquí?
    Algunos regímenes la han creado para
    el sector financiero; otros no la
    tienen para finanzas abiertas

LÍMITE DE ESTE BLOQUE
  depende de la jurisdicción y de la fecha
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Registro de proveedores | Sí | Sí, y no bastó | Mapa técnico, no solo contractual |
| Declaración de subcontratación | Parcial | No | Obligación de declarar el camino real |
| Métrica de concentración | No | — | Publicar cuota por infraestructura |
| Plan de salida del intermediario | No | — | Exigible a cada proveedor |
| Prueba de conmutación | No | — | Ejercicio periódico, no documental |
| Vigilancia del proveedor común | No | — | Figura de tercero crítico |

## Resultado

```text
NO HAY INCIDENTE. HAY UNA MEDICIÓN.

  si el intermediario deja de operar
    proveedores afectados            39
    clientes sin servicio     1 464 000
    tiempo estimado de reintegración
      por proveedor           4 a 9 meses
      (construir 14 conexiones)

  COSTE ESTIMADO DE LA RECONSTRUCCIÓN
    39 × 210 000 =           8 190 000

Y LA CIFRA QUE IMPORTA
  ninguna de las 39 entidades tiene ese
  importe presupuestado, porque cada una
  ve su propio contrato y ninguna ve el 61 %
```

## Lecciones

1. **Contar participantes no mide resiliencia.** Un registro de cuarenta y siete
   entidades puede describir una infraestructura de nueve caminos.
2. **La concentración aparece por eficiencia, no por abuso.** Cada decisión
   individual fue racional; el resultado agregado no lo eligió nadie.
3. **El perímetro dibujado por relación jurídica deja fuera funciones idénticas.**
   Es el mismo problema que este programa estudia en la clase de terceros
   críticos, aquí en versión de datos.
4. **Un plan de salida solo es real si se ha probado**, y ninguna de las treinta y
   nueve entidades lo había probado.

## Preguntas

1. ¿La concentración de este caso es un problema de competencia, de resiliencia o
   de ambos? ¿Cambia la respuesta según quién la mire?
2. ¿Debería el registro exigir declarar el camino técnico además del contractual?
   ¿Qué coste tendría?
3. ¿Qué haría un supervisor con la cifra del 61 % si la tuviera? ¿Y qué podría
   hacer sin una figura de proveedor crítico?
4. Si eres uno de los treinta y nueve, ¿qué haces el lunes por la mañana?
5. ¿Existe una versión de este mercado con muchos proveedores y sin
   intermediarios? ¿Qué haría falta para que existiera?

## Fuentes

- Financial Stability Board (2020). *Regulatory and Supervisory Issues Relating to Outsourcing and Third-Party Relationships*. FSB. <https://www.fsb.org/2020/11/regulatory-and-supervisory-issues-relating-to-outsourcing-and-third-party-relationships-discussion-paper/>
- Diario Oficial de la Unión Europea (2022). *Reglamento (UE) 2022/2554, resiliencia operativa digital*. EUR-Lex. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32022R2554>
- CMF. *Sistema de Finanzas Abiertas: normativa y anexo técnico*. <https://www.cmfchile.cl/>
- Banco Mundial. *Open Banking: Comparative Study on Regulatory Approaches*. <https://www.worldbank.org/>
- Verificación local: caso sintético; cifras supuestas. La existencia de una figura de proveedor tecnológico crítico depende del régimen y de la fecha. **Fecha de verificación: 2026-08-12.** No constituye asesoría legal.
