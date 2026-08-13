# Caso · La interfaz que se cayó un martes 1

**Tema:** finanzas abiertas · **Parte relacionada:** 17 · **Naturaleza:** caso
sintético compuesto · **Fecha de verificación:** 2026-08-12

Una interfaz de cuentas deja de responder durante cinco horas. El banco cumple su
acuerdo de nivel de servicio mensual y el agregador pierde el día de mayor
tráfico del mes. Las dos cosas son ciertas a la vez, y esa contradicción es el
caso.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · caída de 5 h 12 min, un día 1 de mes
  · el acuerdo de nivel de servicio fija
    99,5 % de disponibilidad MENSUAL
  · 5 h 12 min sobre 720 h = 0,72 %
    → disponibilidad del mes: 99,28 %
  · pero el banco mide sobre 24×7 y el
    agregador solo opera en horario diurno
  · medido sobre horario diurno, la caída
    fue del 2,3 % del mes

SUPUESTO DEL EJERCICIO
  · el día 1 concentra el 11 % de las
    consultas del mes: es el día de las
    nóminas y de los recibos
  · consultas perdidas          412 000
  · clientes afectados           58 000
  · reclamaciones                 3 100
```

La discrepancia no es un truco contable: es el problema. **Un mismo indicador
medido sobre dos ventanas distintas produce dos verdades incompatibles**, y el
contrato solo definía una de las dos.

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Cliente final | Ver su saldo el día de cobro | Un mensaje de error genérico |
| Agregador | Servicio disponible cuando se usa | Reintentos fallidos, sin causa |
| Banco proveedor | Cumplir su compromiso contractual | Un incidente de infraestructura |
| Proveedor de nube del banco | Restablecer el servicio | Un fallo en una zona |
| Supervisor | Continuidad del servicio financiero | Nada, hasta el informe |
| Otros dos agregadores | Lo mismo que el primero | Nada entre ellos |

Los otros dos agregadores importan más de lo que parece. Los tres estaban caídos
a la vez y ninguno lo sabía, porque no existía canal alguno entre ellos ni
publicación de estado por parte del banco. Cada uno pasó las primeras dos horas
buscando el fallo en su propia infraestructura.

## Decisiones

```text
00:00  el banco detecta el incidente
       decide no publicar aviso hasta
       tener causa
       RAZÓN: evitar alarma
       EFECTO: tres equipos buscando el
       fallo donde no estaba

02:10  el agregador activa reintentos
       agresivos
       EFECTO: amplifica la carga sobre un
       sistema que se está recuperando

03:40  el agregador decide mostrar el
       último saldo conocido, con fecha
       DECISIÓN CORRECTA, tomada tarde

05:12  servicio restablecido

DÍA+2  el banco comunica cumplimiento del
       acuerdo mensual
       Y TIENE RAZÓN
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Ventana de medición inadecuada | Desde la firma | Sí |
| Ausencia de página de estado | Desde el inicio | Sí |
| Reintentos sin control | Desde el diseño | Sí |
| Concentración en una zona de nube | Estructural | Sí |
| Falta de degradación elegante | Desde el diseño | Sí, hasta las 03:40 |
| Concentración de agregadores | Estructural | No visible ese día |

## Regulación

```text
QUÉ ALCANZA

  CONTINUIDAD OPERACIONAL
    la entidad responde de la continuidad
    del servicio que presta, incluida la
    parte que ejecuta un tercero

  NOTIFICACIÓN DE INCIDENTES
    hay umbrales de gravedad y plazos;
    dependen del régimen y de la fecha

  NIVELES DE SERVICIO EN FINANZAS ABIERTAS
    varios regímenes fijan mínimos de
    disponibilidad y de tiempo de respuesta
    para las interfaces reguladas, y exigen
    publicar estadísticas

LÍMITE DE ESTE BLOQUE
  el umbral concreto y el plazo dependen de
  tu jurisdicción y cambian; verifícalos
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Acuerdo de nivel de servicio | Sí | Sí, y fue insuficiente | Ventana horaria y estacional |
| Página de estado pública | No | — | Publicación inmediata, sin causa |
| Límite de reintentos | No | — | Retroceso exponencial y tope |
| Degradación elegante | No | — | Último dato conocido, con fecha |
| Plan de conmutación de zona | Parcial | No | Prueba real, no documental |
| Comunicación al cliente final | No | — | Mensaje que diga qué pasa y cuándo |

## Resultado

```text
COSTE ESTIMADO (supuestos del ejercicio)

  atención de 3 100 reclamaciones
    3 100 × 4,20 =              13 020
  bajas atribuidas al incidente
    920 × valor anual 38 =      34 960
  penalización contractual              0
    (el acuerdo se cumplió)

  TOTAL AGREGADOR                47 980
  TOTAL BANCO                          0

EL QUE SOPORTA EL COSTE NO ES EL QUE
CONTROLA EL RIESGO. Ese desalineamiento
es el hallazgo del caso.
```

## Lecciones

1. **Un acuerdo de nivel de servicio sin ventana horaria ni estacionalidad no
   describe el servicio.** El día 1 de mes no es un día cualquiera y el contrato
   debe saberlo.
2. **La página de estado se publica antes de conocer la causa.** Retrasarla para
   evitar alarma multiplica el trabajo de todos los que dependen del servicio.
3. **La degradación elegante es más barata que la alta disponibilidad** y resuelve
   la mayor parte del daño percibido: un saldo de hace tres horas, con su fecha
   visible, sirve para casi todo.
4. **Reintentar sin control convierte una caída en una caída más larga.**

## Preguntas

1. ¿Cómo redactarías la cláusula de disponibilidad para que el día 1 de mes pese
   lo que realmente pesa?
2. ¿Quién debería soportar el coste de las bajas: quien controla el riesgo o quien
   lo sufre? ¿Y cómo se escribe eso en un contrato?
3. ¿Es razonable que tres agregadores caídos a la vez no puedan saberlo?
4. ¿Qué habría cambiado si el banco hubiera publicado el estado en el minuto cero?
5. ¿A partir de qué duración un incidente de este tipo debería notificarse al
   supervisor, y por qué?

## Fuentes

- Comité de Supervisión Bancaria de Basilea (2021). *Principles for Operational Resilience*. BIS. <https://www.bis.org/bcbs/publ/d516.htm>
- Diario Oficial de la Unión Europea (2022). *Reglamento (UE) 2022/2554, resiliencia operativa digital*. EUR-Lex. <https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX%3A32022R2554>
- CMF. *Normativa sobre continuidad operacional y gestión de riesgo tecnológico*. <https://www.cmfchile.cl/>
- NIST. *SP 800-34, Contingency Planning Guide for Federal Information Systems*. <https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final>
- Verificación local: caso sintético; cifras supuestas. Los umbrales de notificación y los mínimos de disponibilidad dependen de la jurisdicción. **Fecha de verificación: 2026-08-12.** No constituye asesoría legal.
