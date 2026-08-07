# Proyecto integrador: Comparador de productos financieros

## De qué se trata

Este proyecto construye la herramienta que las trece clases anteriores hacían
falta: algo que lleve dos ofertas a la misma base y muestre cuál conviene, sin
inclinar la decisión.

Lo difícil no es el cálculo. Es el diseño de la salida: la misma comparación,
correcta en todos sus números, puede empujar hacia un producto según qué se
destaque, en qué orden se muestre y qué supuestos se omitan. La rúbrica reparte
la mitad de los puntos a esa parte.

El proyecto **puede concluir que dos productos no son comparables**, y decirlo con
su razón vale más que forzar una comparación que induce a error.

## Contexto

Una persona compara ofertas de tres entidades para la misma necesidad. Cada
entidad presenta su producto con la métrica que mejor le sienta, ninguna usa la
misma base y las tres omiten algún componente del costo. Necesita una herramienta
propia que las ponga en la misma escala.

## Alcance

| Incluido | Excluido |
|---|---|
| Cuentas, créditos de consumo e hipotecarios | Recomendación de entidades concretas |
| Depósitos a plazo y fondos | Carga anual equivalente normativa por país |
| Conversión a base homogénea | Datos de ofertas reales de mercado |
| Salida con supuestos incorporados | Proyección de rentabilidades |
| Declaración de límites | Asesoría de inversión de ningún tipo |

## Entregables

| # | Entregable | Qué debe contener |
|---:|---|---|
| 1 | Requisitos como casos de prueba | Con valores esperados calculados a mano en los laboratorios |
| 2 | Motor de conversión a base común | Costo total por peso obtenido, o rendimiento neto por peso invertido |
| 3 | Comparador de créditos | Con todos los componentes: tasa, comisiones, seguros y monto líquido |
| 4 | Comparador de ahorro | Con remuneración, impuestos e inflación supuesta |
| 5 | Diseño de la salida | Dos versiones, con lo que cambia entre inducir y no inducir |
| 6 | Supuestos en la salida | Visibles junto al resultado, no en un anexo |
| 7 | Sección de límites | Al menos cinco cosas que no compara, con su razón |
| 8 | Validación | Contra los resultados de los laboratorios 3, 4 y 5 |

## Rúbrica

| Criterio | Puntos | Qué se valora |
|---|---:|---|
| Base homogénea correcta | 25 | Que lo comparado sea comparable |
| Componentes completos del costo | 20 | Ninguno omitido |
| Salida que no induce | 20 | Y la explicación de qué habría inducido |
| Supuestos visibles | 15 | En la salida misma |
| Límites declarados | 10 | Con su razón |
| Validación independiente | 10 | Contra cálculos manuales |

**Total:** 100 puntos. **Aprobación:** 70.

## Restricciones

- **No** se usan datos de ofertas reales de entidades identificables.
- **No** se recomienda ninguna entidad ni ningún producto concreto.
- **No** se calcula la carga anual equivalente normativa: se declara como límite.
- **No** se proyectan rentabilidades: los supuestos se declaran y se muestran.
- La herramienta declara sus límites en su propia salida.

## Cómo se comprueba

```bash
python -m pytest -q
```

## Aviso

Material **docente**. El comparador es un ejercicio de formación y **no
constituye asesoría financiera ni recomendación de productos**. Las cifras son
sintéticas y la carga anual equivalente normativa debe obtenerse de la entidad o
del supervisor de cada país.
