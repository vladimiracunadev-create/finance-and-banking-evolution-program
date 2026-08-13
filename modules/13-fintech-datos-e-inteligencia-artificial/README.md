# Parte 14: Fintech, datos e inteligencia artificial

La Parte 13 trató el negocio bancario con empresas. Esta trata de quién se lo
está quitando y cómo, y es la que introduce todo lo que la Etapa 5 desarrolla en
profundidad.

Su valor está en dar el marco antes que el detalle. La competencia fintech no
ataca al banco entero: ataca los eslabones donde la ventaja del banco era solo la
infraestructura. Cada clase siguiente trata una pieza que se desprendió del
paquete bancario, y la última decide qué construye el banco y qué compra.

El eje es que **parte de la ventaja de un competidor viene de innovación y parte de
estar menos regulado**, y que solo la primera dura. Separarlas es lo que permite
predecir si una amenaza es real o transitoria.

## Con qué hay que llegar

| Parte | Qué aporta |
|---|---|
| 10 | Medios de pago y su economía |
| 11 | Riesgo de modelo y riesgo tecnológico |
| 12 | Perímetro regulatorio y conducta |

## Qué se aprende

1. **Separar** la ventaja competitiva real de un entrante de la que viene del arbitraje regulatorio.
2. **Distinguir** los tres tipos de dinero que hay detrás de un pago y el riesgo que asume quien lo recibe.
3. **Diseñar** un consentimiento con alcance por finalidad y una cadena de responsabilidad repartida.
4. **Medir** el efecto de una acción con grupo de control, que es lo único que distingue causa de correlación.
5. **Clasificar** un caso de uso de inteligencia artificial por su efecto sobre las personas y definir controles proporcionales.

## Cómo se encadenan las 14 clases

Las catorce clases van de la competencia a la respuesta.

La **clase 1** da el marco de desagregación que ordena la parte entera.

Las **clases 2 y 3** desarrollan los dos eslabones que ya se desprendieron: el
pago, por infraestructura, y los datos, por norma.

Las **clases 4 y 5** entran en el activo que sostiene todo lo demás. La 5 establece
la distinción que más resultados analíticos invalida: predecir quién comprará no
es lo mismo que saber a quién conviene ofrecerle algo.

Las **clases 6 y 7** aplican los modelos a decisiones sobre personas, con la
promesa y el riesgo que eso trae.

Las **clases 8 a 10** cubren el fraude en canales digitales y las dos formas de
dinero nuevo, con el análisis de diseño que decide su efecto.

Las **clases 11 y 12** ponen los límites: equidad algorítmica —que es
matemáticamente imposible de satisfacer en todas sus definiciones a la vez— y
perímetro regulatorio. Las **clases 13 y 14** cierran con cómo adopta esto un banco
que ya existe y qué construye frente a qué compra.

## Secuencia

1. [Qué es fintech y cómo cambia la banca](classes/01-que-es-fintech.md)
2. [Pagos digitales y dinero electrónico](classes/02-pagos-digitales.md)
3. [Banca abierta y APIs](classes/03-banca-abierta-y-apis.md)
4. [Datos en un banco](classes/04-datos-en-un-banco.md)
5. [Analítica aplicada](classes/05-analitica-aplicada.md)
6. [Inteligencia artificial en banca](classes/06-inteligencia-artificial-en-banca.md)
7. [Crédito digital y datos alternativos](classes/07-credito-digital-y-datos-alternativos.md)
8. [Fraude digital](classes/08-fraude-digital.md)
9. [Criptoactivos y registro distribuido](classes/09-criptoactivos-y-registro-distribuido.md)
10. [Monedas digitales de banco central](classes/10-monedas-digitales-de-banco-central.md)
11. [Ética algorítmica y sesgo](classes/11-etica-algoritmica-y-sesgo.md)
12. [Regulación de la tecnología financiera](classes/12-regulacion-de-la-tecnologia-financiera.md)
13. [Transformación digital](classes/13-transformacion-digital.md)
14. [Estrategia tecnológica](classes/14-estrategia-tecnologica.md)

## Cómo se trabaja

Son **14 clases de 90 minutos** —21 horas de sesión— con **6 laboratorios**, **2 evaluaciones** y un proyecto integrador. Cada clase supone la anterior, así que el orden importa: saltarse una deja sin base a las que vienen después.

Los laboratorios se resuelven con datos propios o sintéticos y nunca con datos reales de terceros. Las evaluaciones son dos: una diagnóstica al empezar, que no se califica para aprobar sino para saber qué reforzar, y una final. El proyecto es el entregable que demuestra que la parte se entendió.

## Qué queda como evidencia

- El análisis de tres competidores con su ventaja clasificada.
- El diseño de un consentimiento con alcances y responsabilidades.
- El experimento con grupo de control y su elevación medida.
- La clasificación de casos de uso con sus controles proporcionales.
- La autoevaluación final con lo que quedó flojo.

## Continúa en la Etapa 5

Esta parte es la **introducción** a lo que la Etapa 5 desarrolla. Aquí los
conceptos se presentan para que una dirección bancaria pueda decidir; allí se
implementan, se miden y se regulan. Ninguna de las partes siguientes repite estas
clases: las supone.

**Prerrequisitos que aporta esta parte.** Clase 2, pagos digitales y dinero
electrónico. Clase 3, banca abierta y APIs. Clase 9, criptoactivos y registro
distribuido. Clase 10, monedas digitales de banco central. Clase 12, regulación
de la tecnología financiera.

| Para profundizar | Continuación |
|---|---|
| Banca abierta y APIs, clase 3 | **Parte 17** — consentimiento, autorización, contratos de API e iniciación de pagos |
| Pagos digitales, clase 2 | **Parte 18** — corresponsalía, ISO 20022, liquidez y liquidación internacional |
| Registro distribuido, clase 9 | **Parte 19** — consenso, finalidad, contratos, oráculos y comparación con base centralizada |
| Criptoactivos, clase 9 | **Parte 20** — taxonomía, reservas, redención, custodia y contagio |
| Monedas digitales, clase 10 | **Parte 20**, clase 10 · **Parte 22**, clase 7 |
| Regulación fintech, clase 12 | **Parte 22** — perímetro, autorización, MiCA y regulación comparada |
| Transformación digital, clase 13 | **Parte 21** y **Parte 23** — tokenización y el proyecto completo |

**Casos relacionados:** [`open-finance/consentimiento-invalido`](../../case-studies/open-finance/consentimiento-invalido.md) ·
[`blockchain/falla-de-oraculo`](../../case-studies/blockchain/falla-de-oraculo.md)
