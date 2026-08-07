# Proyecto integrador: Protocolo personal de seguridad

## De qué se trata

Este proyecto reúne las trece clases en un documento que se ejecuta bajo presión
y en un simulacro que lo valida. Es el único proyecto del programa cuyo criterio
principal no es la calidad del documento sino que funcione cuando no se tiene
acceso a lo que normalmente se tiene.

Esa restricción es lo que descarta la mayoría de los diseños razonables. Un
protocolo guardado en el gestor de contraseñas no sirve si lo comprometido es el
gestor; una lista de teléfonos en el correo no sirve si el correo está tomado. El
simulacro es lo que lo revela.

El proyecto **puede concluir que la pérdida máxima residual sigue siendo
inaceptable**, y en ese caso lo que se entrega es el plan para reducirla.

## Contexto

Una persona con cuatro cuentas, dos tarjetas y una decena de accesos quiere estar
preparada para el día en que uno de ellos caiga. Nunca ha comprobado si sus
controles están realmente activos ni ha ensayado qué haría.

## Alcance

| Incluido | Excluido |
|---|---|
| Inventario de accesos y pérdida máxima | Datos reales de terceros |
| Controles con evidencia de configuración | Credenciales de ninguna clase |
| Protocolo de respuesta cronometrado | Herramientas ofensivas o de intrusión |
| Simulacro y su corrección | Asesoría legal sobre un caso real |
| Calendario de vigencia | Datos personales de otras personas |

## Entregables

| # | Entregable | Qué debe contener |
|---:|---|---|
| 1 | Inventario | Accesos, dispositivos y cuentas alcanzables desde cada uno |
| 2 | Controles con evidencia | Los siete, cada uno con la prueba de que está activo y su fecha |
| 3 | Pérdida máxima | Antes y después de los controles, por acceso |
| 4 | Protocolo cronometrado | Qué se hace en los primeros minutos, en las primeras horas y en los primeros días |
| 5 | Evidencia y plazos | Qué capturar durante el incidente y qué plazo tiene cada vía |
| 6 | Calendario de vigencia | Fechas fijas de revisión y qué se revisa en cada una |
| 7 | Simulacro | Ejecutado sin acceso a lo comprometido, con lo que falló |
| 8 | Segundo simulacro | Tras la corrección, con el resultado |

## Rúbrica

| Criterio | Puntos | Qué se valora |
|---|---:|---|
| Controles con evidencia | 20 | Comprobados, no declarados |
| Accesibilidad bajo presión | 20 | El protocolo se alcanza sin lo comprometido |
| Simulacro ejecutado | 20 | Con lo que falló registrado |
| Corrección reprobada | 15 | Segundo simulacro con el fallo resuelto |
| Pérdida máxima cuantificada | 15 | Antes y después |
| Calendario de vigencia | 10 | Con fechas fijas |

**Total:** 100 puntos. **Aprobación:** 70.

## Restricciones

- **No** se usan credenciales reales en ningún entregable, ni propias ni ajenas.
- **No** se incluyen datos personales de otras personas.
- **No** se construyen ni se describen herramientas de intrusión.
- El protocolo se guarda de forma que siga siendo alcanzable si el acceso principal cae.
- Si se usan datos propios, **no salen del equipo** de quien los escribe.

## Aviso

Material **docente**. No constituye asesoría legal ni de seguridad informática
profesional. Los organismos, plazos y causales de reclamo varían por país y deben
verificarse en la fuente oficial vigente.
