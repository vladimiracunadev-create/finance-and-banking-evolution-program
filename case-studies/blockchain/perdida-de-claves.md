# Caso · Las claves de un custodio y el empleado que se fue

**Tema:** blockchain y DLT · **Parte relacionada:** 19 · **Naturaleza:** caso
sintético compuesto · **Fecha de verificación:** 2026-08-12

Un custodio institucional descubre que dos de las tres partes necesarias para
firmar están bajo el control efectivo de la misma persona. El esquema es
formalmente de tres firmas; en la práctica, es de una. Nadie robó nada: el
problema es que podrían haberlo hecho, y durante catorce meses nadie lo vio.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · esquema declarado: 2 de 3 firmas
  · custodio A · custodio B · custodio C
  · A y B en dispositivos ubicados en la
    misma sala, con el mismo control de
    acceso
  · el responsable de operaciones tenía
    acceso físico a esa sala y era el
    titular de A

SUPUESTO DEL EJERCICIO
  · activos bajo custodia    240 000 000
  · clientes institucionales         18
  · meses con la configuración         14
  · el responsable causa baja en el mes 14
```

Al causar baja se plantea la pregunta que nadie había hecho: si esta persona hubiera
querido, ¿podía firmar sola? La respuesta documentada es sí. Y con eso basta:
**en custodia, la pregunta no es si alguien lo hizo, sino si podía hacerlo sin que
nadie lo impidiera.**

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Cliente institucional | Que sus activos estén separados y seguros | Un informe de esquema 2 de 3 |
| Responsable de operaciones | Que las firmas salgan a tiempo | El acceso a la sala |
| Dirección del custodio | Escalar el negocio | El esquema en el papel |
| Auditor externo | Verificar el control declarado | Comprobó el esquema, no la ubicación |
| Aseguradora | Cubrir un riesgo definido | La póliza suponía separación |
| Supervisor | Segregación efectiva | El informe anual |

## Decisiones

```text
MES 0   se diseña 2 de 3
        DISEÑO CORRECTO

MES 1   por agilidad operativa, A y B se
        instalan juntos
        «es temporal, hasta abrir la
         segunda sede»
        LA SEGUNDA SEDE NO SE ABRE

MES 6   auditoría: comprueba que existen
        tres partes y que se requieren dos
        NO COMPRUEBA DÓNDE ESTÁN

MES 14  baja del responsable
        se revisa el acceso y aparece
        el hallazgo
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Colusión innecesaria: una sola persona basta | Desde el mes 1 | Como capacidad, sí |
| Riesgo de concentración física | Desde el mes 1 | Sí |
| Pérdida simultánea por siniestro en la sala | Desde el mes 1 | No |
| Auditoría de forma, no de sustancia | Desde el mes 6 | Sí |
| Cobertura de seguro invalidada | Desde el mes 1 | Probablemente |
| Falta de rotación de claves | Desde el mes 0 | Sí |

El tercero suele pasarse por alto y es el más grave en términos de continuidad:
un incendio en esa sala destruye dos de las tres partes, y con una sola no se
puede firmar. **El mismo defecto que permite el robo impide la recuperación.**

## Regulación

```text
QUÉ ALCANZA

  CUSTODIA Y SEGREGACIÓN
    los regímenes de custodia exigen
    segregación efectiva y controles que
    impidan la disposición unilateral

  GOBIERNO Y SEPARACIÓN DE FUNCIONES
    quien opera no controla; quien controla
    no opera

  CONTINUIDAD
    la pérdida de material criptográfico es
    un escenario de continuidad, no solo
    de seguridad

LÍMITE
  el régimen concreto de custodia de
  activos digitales depende de la
  jurisdicción y está en evolución
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Esquema de firma múltiple | Sí | No en la práctica | Separación geográfica exigida |
| Separación de funciones | Sí, en el papel | No | Que el titular de A no acceda a B |
| Auditoría del esquema | Sí | Parcialmente | Verificar ubicación y acceso físico |
| Rotación periódica de claves | No | — | Calendario y prueba de rotación |
| Prueba de recuperación | No | — | Ejercicio con una parte inutilizada |
| Registro de accesos a la sala | Parcial | No | Revisión periódica, no solo registro |

## Resultado

```text
NO HUBO PÉRDIDA DE ACTIVOS.
HUBO ESTO:

  · rotación completa de material
    criptográfico            180 000
  · reubicación de una parte y
    contratación de sede      95 000
  · auditoría extraordinaria    60 000
  · notificación a 18 clientes
    y a la aseguradora
  · 4 clientes retiran fondos
    (supuesto)              62 000 000
  · pérdida de ingreso anual
    asociada                 310 000

  COSTE TOTAL              ~645 000
  MÁS EL 26 % DE LOS ACTIVOS
  BAJO CUSTODIA
```

## Lecciones

1. **Un esquema de firma múltiple sin separación física es un esquema de una
   firma.** El número de partes no dice nada si el control converge.
2. **Lo temporal se convierte en permanente** salvo que tenga fecha de caducidad
   registrada y un responsable que la persiga.
3. **La auditoría debe comprobar la sustancia, no la existencia.** Verificar que
   hay tres partes es trivial; verificar que están separadas es el trabajo.
4. **La recuperación y el robo comparten el mismo defecto.** Un diseño que impide
   la disposición unilateral también debe permitir recuperar sin la parte perdida.

## Preguntas

1. ¿Qué habrías exigido en la auditoría del mes 6 para detectarlo?
2. ¿Cómo se prueba una recuperación sin poner en riesgo los activos?
3. ¿Debe notificarse a los clientes un fallo de control que no produjo pérdida?
   ¿Y al supervisor?
4. ¿Qué esquema propondrías para un custodio con dieciocho clientes y 240
   millones? ¿Cambia con el tamaño?
5. ¿Con qué frecuencia rotarías las claves, y qué coste operativo aceptas por ello?

## Fuentes

- NIST. *SP 800-57, Recommendation for Key Management*. <https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final>
- CPMI-IOSCO (2012). *Principles for Financial Market Infrastructures*. BIS. <https://www.bis.org/cpmi/publ/d101.htm>
- Comité de Supervisión Bancaria de Basilea. *Prudential treatment of cryptoasset exposures*. <https://www.bis.org/bcbs/publ/d545.htm>
- IOSCO (2023). *Policy Recommendations for Crypto and Digital Asset Markets*. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD747.pdf>
- Verificación local: caso sintético; cifras supuestas. El régimen de custodia de activos digitales depende de la jurisdicción y está en evolución. **Fecha de verificación: 2026-08-12.** No constituye asesoría legal.
