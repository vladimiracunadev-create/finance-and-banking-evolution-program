# Proyecto integrador: Motor de valoración

## De qué se trata

Este proyecto construye el motor que resuelve las catorce clases anteriores y
produce un informe que un comité puede discutir. Reúne dos exigencias que hasta
aquí iban por separado: que el cálculo sea correcto y que otra persona pueda
auditarlo sin preguntar nada.

La segunda es la que se evalúa más. Un modelo con supuestos incrustados en las
fórmulas puede dar el resultado correcto y ser inservible, porque nadie —incluido
quien lo hizo tres meses después— puede saber de dónde sale. Las capas separadas
y los controles automáticos son la respuesta.

El informe **presenta rangos y no cifras**, y declara de qué depende el resultado.
Un valor actual neto con seis decimales y sin sensibilidad se devuelve.

## Contexto

Un comité de inversiones evalúa cuatro proyectos mutuamente excluyentes con
horizontes y escalas distintas. El analista anterior entregó cuatro cifras sin
sensibilidad, y el comité devolvió el informe pidiendo saber de qué dependen.

## Alcance

| Incluido | Excluido |
|---|---|
| Valoración de series, despejes y amortización | Valoración de empresas reales |
| Criterios de decisión y sus correcciones | Recomendación de inversión |
| Sensibilidad, escenarios y simulación | Datos de mercado no verificables |
| Controles automáticos y casos de prueba | Proyección de tasas o precios |
| Informe de comité con rangos | Asesoría financiera de ningún tipo |

## Entregables

| # | Entregable | Qué debe contener |
|---:|---|---|
| 1 | Casos de prueba | Escritos antes del código, con valores de cálculos manuales |
| 2 | Capa de supuestos | Separada, editable y documentada con sus unidades |
| 3 | Capa de cálculo | Funciones puras, probables sin la presentación |
| 4 | Controles automáticos | Cierre en cero, suma de flujos, rangos válidos y coherencia de unidades |
| 5 | Criterios de decisión | Valor actual, tasa interna, tasa modificada, recuperación descontada e índice |
| 6 | Sensibilidad | Tornado, valores de equilibrio y una bivariante |
| 7 | Informe de comité | Una página, con rango, supuestos y de qué depende |
| 8 | Documentación del modelo | Qué hace, qué supone, qué no puede hacer y quién lo validó |

## Rúbrica

| Criterio | Puntos | Qué se valora |
|---|---:|---|
| Corrección del cálculo | 20 | Contrastado con los laboratorios |
| Capas separadas | 20 | Supuestos fuera de las fórmulas |
| Controles automáticos | 15 | Avisan antes de que el error se use |
| Sensibilidad | 15 | Tornado y valores de equilibrio |
| Informe con rangos | 15 | Sin precisión falsa |
| Auditabilidad | 15 | Un tercero lo reproduce sin preguntar |

**Total:** 100 puntos. **Aprobación:** 70.

## Restricciones

- **No** se valoran empresas o proyectos reales identificables.
- **No** se recomienda ninguna inversión: el motor calcula, no aconseja.
- Todos los supuestos se declaran en la capa de supuestos, nunca en las fórmulas.
- El informe presenta rangos y declara de qué dependen.
- El modelo documenta qué no puede hacer.

## Cómo se comprueba

```bash
python -m pytest -q
```

## Aviso

Material **docente**. El motor es un ejercicio de formación y **no constituye
asesoría de inversión ni valoración profesional**. Sus resultados dependen por
completo de supuestos declarados y sintéticos.
