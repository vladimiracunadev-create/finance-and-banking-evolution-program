# Caso · Terra, UST y LUNA: paridad reflexiva e intervención no revelada

**Tema:** stablecoins algorítmicas, reservas y liquidez · **Parte relacionada:**
20 · **Naturaleza:** caso real documentado · **Fecha de verificación:** 2026-09-28

Este caso separa dos planos: una arquitectura reflexiva puede ser económicamente
frágil sin que eso pruebe fraude; aquí, además, existen un veredicto civil, una
declaración de culpabilidad penal y una sentencia por conductas documentadas.

## Hechos

- UST buscaba mantener USD 1 mediante conversión con LUNA e incentivos de mercado.
- En mayo de 2021 la paridad se recuperó después de compras de un tercero. El DOJ
  documentó que esa intervención contradijo la explicación pública de recuperación
  autónoma del protocolo.
- En mayo de 2022 UST perdió nuevamente la paridad y UST y LUNA colapsaron.
- Un jurado declaró civilmente responsables a Terraform Labs y Do Kwon en abril de
  2024. Kwon se declaró culpable en agosto de 2025 y fue sentenciado el 11 de
  diciembre de 2025 a 15 años de prisión.

### Lectura financiera en once preguntas

| Pregunta | Respuesta documentada o límite |
|---|---|
| Producto o servicio | Stablecoin algorítmica UST y token absorbente LUNA dentro de un ecosistema. |
| Qué entendía el cliente | Que la conversión y los incentivos podían sostener la paridad de forma autónoma. |
| Flujo económico | Salir de UST exigía demanda, conversión a LUNA o reservas/intervención externa. |
| Activos | Reservas y otros activos controlados por entidades del ecosistema; no equivalían a respaldo uno a uno. |
| Pasivos | Promesa económica de paridad, aunque su forma jurídica no fuera un depósito tradicional. |
| Control de fondos | Terraform y Luna Foundation Guard tuvieron controles que debían revelarse y gobernarse. |
| Riesgo | Reflexividad, liquidez, mercado, concentración, gobernanza y conducta. |
| Qué ocurrió | La demanda de salida superó la capacidad del mecanismo; aumentó la emisión de LUNA y cayó su precio. |
| Qué está documentado | Intervención de 2021, representaciones engañosas, veredicto civil, culpabilidad y sentencia penal. |
| Controles pertinentes | Reserva externa, límites de emisión, gatillos de pausa, transparencia de intervenciones y estrés conjunto. |
| Qué no permite concluir | Que toda pérdida de paridad sea fraude o que una reserva garantice liquidez ilimitada. |

## Actores

Tenedores de UST, tenedores de LUNA, Terraform, Luna Foundation Guard, proveedores
de liquidez y plataformas tenían incentivos no alineados. El token que absorbía el
choque era también el que perdía capacidad de absorción cuando aumentaba la venta.

## Decisiones

La decisión pedagógica es modelar la salida antes de confiar en la etiqueta
«estable». Toda intervención externa debe registrarse como tal: si el sistema
necesita un comprador coordinado, esa dependencia forma parte del producto.

## Riesgos

```text
venta de UST → conversión/emisión de LUNA → oferta de LUNA sube
→ precio de LUNA baja → se requiere más LUNA por cada salida
→ empeora la confianza → aumenta la venta de UST
```

Una tasa atractiva acelera el crecimiento del pasivo económico y puede concentrar
la demanda de salida cuando cambia la confianza.

## Regulación

La calificación jurídica dependió del foro y del instrumento. Este análisis no
extrapola la conclusión estadounidense a toda stablecoin ni confunde el fallo del
mecanismo con los engaños probados sobre su funcionamiento.

## Controles

Preventivos: límite de crecimiento frente a liquidez de salida, reserva externa de
alta calidad, independencia real de quien la administra y prohibición de presentar
intervención discrecional como algoritmo autónomo. Detectivos: desviación de paridad,
profundidad, concentración, ritmo de emisión y publicación de cada intervención.

## Resultado y ejercicio sintético

```text
UST sintética en circulación              1 000
liquidez de mercado a ±1 %                  120
reserva externa líquida                     180
ventas en 24 h, escenario base              220
ventas en 24 h, estrés                       520
capacidad base observada             120 + 180 = 300
brecha bajo estrés                   520 − 300 = 220
```

Simula tres rondas en que el precio del token absorbente cae 30 % por ronda.
Calcula cuántas unidades deben emitirse para absorber 100 unidades de salida y
explica cuándo el mecanismo se vuelve reflexivo.

## Lecciones

1. Paridad es una relación de mercado; redención es un derecho y un proceso.
2. La reserva solo sirve en la medida en que sea líquida, controlable y accesible.
3. Una intervención externa no es un detalle si la comunicación prometía autonomía.
4. Fragilidad económica y fraude acreditado son categorías distintas que pueden
   coexistir en un caso sin volverse sinónimos.

## Preguntas

1. ¿Qué parte del mecanismo es activo y cuál es promesa económica?
2. ¿Cómo medirías la profundidad necesaria para una corrida?
3. ¿Qué cambia cuando el token absorbente cae al mismo tiempo?
4. ¿Qué intervención debe revelar el emisor y con qué frecuencia?
5. ¿Qué hecho adicional necesitarías para pasar de «frágil» a «fraudulento»?

## Fuentes

- U.S. Department of Justice (2025). *Crypto-Enabled Fraudster Sentenced for
  Orchestrating $40 Billion Fraud*.
  <https://www.justice.gov/usao-sdny/pr/crypto-enabled-fraudster-sentenced-orchestrating-40-billion-fraud>
- U.S. Securities and Exchange Commission (2024). *Terraform and Kwon to Pay
  $4.5 Billion Following Fraud Verdict*.
  <https://www.sec.gov/newsroom/press-releases/2024-73>
- U.S. Securities and Exchange Commission (2024). *In the Matter of Tai Mo Shan
  Limited*, Administrative Proceeding No. 3-22382.
  <https://www.sec.gov/enforcement-litigation/distributions-harmed-investors/tai-mo-shan-limited>
- Verificación local: se distinguen fragilidad del diseño, veredicto civil,
  declaración de culpabilidad y sentencia penal. No constituye asesoría legal o
  de inversión.
