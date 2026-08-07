# Proyecto integrador: Calculadora financiera personal

## De qué se trata

Este proyecto construye la herramienta que resuelve las trece clases anteriores
y la deja en un estado en que otra persona puede usarla y verificarla. No es un
ejercicio de programación: es el primer entregable del programa que tiene que
sostenerse ante alguien que pregunte de dónde sale cada número.

La diferencia entre una calculadora que funciona y una que se puede defender está
en tres cosas: los casos de prueba se escribieron antes que el código, los valores
esperados vienen de un cálculo independiente, y la herramienta declara qué **no**
hace. Las tres se evalúan.

El proyecto **puede concluir que una función no debe incluirse**, y esa conclusión
vale si está justificada.

## Contexto

Una persona quiere decidir sobre sus créditos y sus ahorros sin depender de las
simulaciones de cada entidad, que están construidas para vender. Necesita una
herramienta propia, pequeña y verificable, que calcule lo mismo y le diga en qué
se apoya.

## Alcance

| Incluido | Excluido |
|---|---|
| Interés simple y compuesto con sus despejes | Cálculo de carga anual equivalente normativa |
| Valor presente y futuro de flujos y series | Asesoría o recomendación de productos |
| Cuota, tabla de amortización y prepago | Conexión con datos bancarios reales |
| Conversión entre periodicidades | Datos personales de cualquier persona |
| Validación de entrada y hoja de supuestos | Proyección de rentabilidades |

## Entregables

| # | Entregable | Qué debe contener |
|---:|---|---|
| 1 | Requisitos escritos como casos de prueba | Siete requisitos, cada uno con su caso y su valor esperado independiente |
| 2 | Funciones de cálculo | Puras, sin entrada ni salida, con unidades documentadas |
| 3 | Tabla de amortización | Que cierra en cero, comprobado por una prueba |
| 4 | Validación de entrada | Tasa negativa, plazo cero y capital no positivo rechazados con mensaje |
| 5 | Interfaz de línea de comandos | Separada del cálculo, con ejemplos ejecutables |
| 6 | Hoja de supuestos | Unidades, convención de días, criterio de redondeo y fuente de cada dato |
| 7 | Sección de límites | Al menos cinco cosas que la calculadora no hace, con su razón |
| 8 | Defensa de tres minutos | Dos decisiones de diseño justificadas y una limitación reconocida |

## Rúbrica

| Criterio | Puntos | Qué se valora |
|---|---:|---|
| Casos de prueba antes que código | 20 | Y con valores esperados independientes |
| Corrección de los cálculos | 20 | Contrastados con los laboratorios |
| Validación y manejo de errores | 15 | Ninguna entrada inválida produce un número |
| Trazabilidad | 15 | Hoja de supuestos que permite reproducir |
| Límites declarados | 15 | Lo que no hace, con su razón |
| Defensa | 15 | Decisiones justificadas, no descritas |

**Total:** 100 puntos. **Aprobación:** 70.

## Restricciones

- **No** se usan datos reales de ninguna persona, ni propios ni ajenos.
- **No** se conecta con ninguna entidad ni con ninguna cuenta.
- **No** se presenta como herramienta de asesoría ni se publica como tal.
- Todos los datos son sintéticos y están declarados como tales.
- La herramienta declara sus límites en su propia salida, no en una nota aparte.

## Cómo se comprueba

```bash
python -m pytest -q
```

## Aviso

Material **docente**. La calculadora es un ejercicio de formación y **no
constituye asesoría financiera**. No calcula la carga anual equivalente
normativa, que tiene fórmula legal propia en cada país y debe obtenerse de la
entidad o del supervisor.
