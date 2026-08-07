# Laboratorio 2: Estafas digitales

## Propósito

Aplicar el control de razonabilidad a seis ofertas y **comprobar que ninguna sobrevive al primer cálculo**.

El laboratorio 1 cerró los accesos. Este trata el fraude que no necesita ninguno, porque la víctima transfiere voluntariamente, y contra el que solo sirve un cálculo hecho a tiempo.

## Escenario

Seis ofertas de inversión con rentabilidades prometidas entre el 3 % y el 40 % mensual, y cuatro solicitudes de transferencia de perfiles distintos.

## Datos

Las seis ofertas y las cuatro solicitudes, todas sintéticas.

## Supuestos del ejercicio

- La rentabilidad de referencia del mercado se entrega como dato.
- Ninguna oferta se contrata: el ejercicio es de análisis.
- Los medios de pago disponibles tienen distinta reversibilidad.

## Pasos

1. Aplica el control de razonabilidad a las seis ofertas y anualiza sus promesas.
2. Compara cada una con la rentabilidad de referencia y calcula el múltiplo.
3. Clasifica cada oferta en uno de los seis patrones conocidos.
4. Ejecuta las tres comprobaciones previas a transferir sobre las cuatro solicitudes.
5. Ordena los medios de pago por reversibilidad y elige el correcto para cada caso.
6. Escribe el protocolo de las primeras horas si la transferencia ya salió.

## Criterios de aceptación

| # | Criterio | Cómo se comprueba |
|---:|---|---|
| 1 | Las seis promesas están anualizadas | En la misma unidad que la referencia |
| 2 | El múltiplo sobre la referencia está calculado | Para las seis |
| 3 | Cada oferta está clasificada en su patrón | Con la señal que la delata |
| 4 | Las tres comprobaciones se aplican | A las cuatro solicitudes |
| 5 | Los medios están ordenados por reversibilidad | Con el elegido en cada caso |

## Errores que se penalizan

| Error | Por qué |
|---|---|
| Evaluar la oferta por su relato | El relato es la parte trabajada; el número, no |
| No anualizar | Un 4 % mensual no se compara con un 7 % anual |
| Elegir el medio de pago por comodidad | La reversibilidad decide si hay algo que hacer después |
| Verificar después de transferir | Las comprobaciones cuestan dos minutos antes y nada después |

## Entregables

- `solution.md` con las seis ofertas analizadas y su múltiplo.
- La clasificación en patrones con su señal.
- Las comprobaciones aplicadas a las cuatro solicitudes.
- El protocolo de las primeras horas.

## Rúbrica

| Criterio | Puntos |
|---|---:|
| Anualización y múltiplo | 30 |
| Clasificación en patrones | 20 |
| Comprobaciones aplicadas | 20 |
| Medios por reversibilidad | 15 |
| Protocolo | 15 |
