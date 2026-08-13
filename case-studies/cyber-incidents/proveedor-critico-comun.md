# Caso · Veintidós entidades y un solo cable

**Tema:** incidentes y resiliencia · **Parte relacionada:** 22 · **Naturaleza:**
caso sintético compuesto · **Fecha de verificación:** 2026-08-12

Veintidós entidades cumplen su normativa de externalización. Cada una tiene su
contrato, su evaluación de proveedor y su plan de continuidad. Un martes por la
mañana, diecinueve de ellas dejan de operar a la vez, y ninguna había identificado
la razón: sus proveedores, que eran distintos, se apoyaban en el mismo.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · 22 entidades supervisadas
  · contratan servicios de procesamiento a
    7 proveedores distintos
  · 5 de esos 7 alojan su servicio en la
    misma región de un mismo proveedor de
    infraestructura
  · incidente en esa región: 4 h 20 min
  · entidades afectadas: 19
  · entidades que habían identificado la
    dependencia común: 0

SUPUESTO DEL EJERCICIO
  · operaciones no cursadas       1 240 000
  · clientes afectados            3 100 000
  · concentración real medida
    después                            86 %
```

El mapa contractual mostraba siete proveedores; el mapa técnico tenía un cuello.
**La diversificación era real en la factura y falsa en la infraestructura**, y esa
es la definición operativa del riesgo de tercero crítico.

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Entidad supervisada | Cumplir su norma de externalización | Su contrato y su proveedor directo |
| Proveedor de procesamiento | Prestar el servicio | Su propia dependencia |
| Proveedor de infraestructura | Disponibilidad regional | Todo el mapa, y solo él |
| Cliente final | Operar | Un mensaje de error |
| Supervisor | Continuidad del sistema | 22 informes que no se cruzaban |
| Competidor no afectado | Ventaja del día | Nada especial |

## Decisiones

```text
DE CADA ENTIDAD
  evaluar a su proveedor directo
  DECISIÓN CORRECTA Y PARCIAL:
  la norma pedía eso

DE CADA ENTIDAD
  no exigir declaración de subcontratación
  en cadena
  RAZÓN: no era exigible, y el proveedor
  lo consideraba información comercial

DE LOS PROVEEDORES
  concentrar en una región por coste y
  latencia
  DECISIÓN RACIONAL INDIVIDUALMENTE

DEL SUPERVISOR
  recibir 22 informes de externalización
  y no cruzarlos
  DECISIÓN DE PROCESO, NO DE CRITERIO
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Concentración oculta en la cadena | Desde años | Sí |
| Ausencia de declaración de subcontratación | Desde los contratos | Sí |
| Planes de continuidad con el mismo destino | Desde el diseño | Sí |
| Supervisión por entidad, no por sistema | Estructural | Sí |
| Ausencia de vigilancia sobre el proveedor | Estructural | Sí |
| Efecto reputacional sectorial | Latente | Sí |

El tercero es el más doloroso: varias entidades tenían plan de continuidad y
varios de esos planes apuntaban a un proveedor alternativo que estaba en la misma
región. **Un plan de continuidad que comparte destino con el sistema principal no
es un plan.**

## Regulación

```text
QUÉ ALCANZA

  EXTERNALIZACIÓN
    la responsabilidad no se delega; la
    entidad responde del servicio que
    ejecuta un tercero

  DECLARACIÓN DE LA CADENA
    algunos regímenes exigen conocer y
    notificar la subcontratación; otros
    solo el primer nivel

  VIGILANCIA DE TERCEROS CRÍTICOS
    hay regímenes que designan proveedores
    críticos y los someten a vigilancia
    directa de la autoridad; sin esa
    figura, el riesgo común no tiene
    destinatario

LÍMITE
  la existencia de esa figura y su alcance
  dependen de la jurisdicción y de la fecha
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Evaluación del proveedor directo | Sí | Sí, insuficiente | Cadena completa |
| Cláusula de auditoría | Parcial | No | Extensiva a subcontratistas |
| Plan de continuidad | Sí | No | Alternativa en dominio de fallo distinto |
| Prueba de conmutación real | No | — | Ejercicio anual con desconexión |
| Registro sectorial de dependencias | No | — | Agregado y anónimo |
| Vigilancia del proveedor común | No | — | Figura de tercero crítico |

## Resultado

```text
COSTE DEL INCIDENTE (supuestos)

  operaciones no cursadas   1 240 000
  coste de reproceso
    1 240 000 × 0,40 =        496 000
  atención de reclamaciones
    41 000 × 4,20 =           172 200
  penalizaciones contractuales
    de las entidades a sus clientes
                              610 000
  TOTAL SECTOR              1 278 200

  COSTE PARA EL PROVEEDOR DE
  INFRAESTRUCTURA
    créditos de servicio        38 000

  RELACIÓN                      33 : 1

QUIEN CONTROLA EL RIESGO SOPORTA
EL 3 % DEL COSTE.
```

## Lecciones

1. **La diversificación se mide en la infraestructura, no en la factura.** Siete
   contratos pueden ser un solo punto de fallo.
2. **Un plan de continuidad debe apuntar a un dominio de fallo distinto**, y eso
   exige conocer la cadena, no solo al proveedor.
3. **Supervisar entidad por entidad no ve el riesgo del sistema.** Hace falta
   agregar, aunque sea de forma anónima.
4. **El desalineamiento entre quien controla el riesgo y quien lo soporta explica
   por qué no se corrige solo**, y es la razón por la que existen las figuras de
   vigilancia directa.

## Preguntas

1. ¿Cómo obligarías a declarar la cadena completa sin revelar información
   comercial sensible?
2. ¿Qué es un «dominio de fallo distinto»? Defínelo de forma verificable para un
   contrato.
3. ¿Qué haría un supervisor con un registro sectorial de dependencias? ¿Y qué no
   podría hacer sin la figura de proveedor crítico?
4. ¿Cómo se prueba una conmutación real sin interrumpir el servicio?
5. ¿Debería el proveedor de infraestructura soportar más que 38 000? ¿Cómo se
   escribe eso?

## Fuentes

- Financial Stability Board (2023). *Enhancing Third-Party Risk Management and Oversight*. <https://www.fsb.org/2023/12/enhancing-third-party-risk-management-and-oversight-a-toolkit-for-financial-institutions-and-financial-authorities/>
- Diario Oficial de la Unión Europea (2022). *Reglamento (UE) 2022/2554, resiliencia operativa digital*. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32022R2554>
- Comité de Supervisión Bancaria de Basilea (2021). *Principles for Operational Resilience*. <https://www.bis.org/bcbs/publ/d516.htm>
- CMF. *Normativa sobre gestión de riesgo operacional y externalización*. <https://www.cmfchile.cl/>
- Verificación local: caso sintético; cifras supuestas. La existencia de una figura de proveedor crítico y su alcance dependen de la jurisdicción. **Fecha de verificación: 2026-08-12.** No constituye asesoría legal.
