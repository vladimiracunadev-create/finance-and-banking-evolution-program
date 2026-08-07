# Evaluación final: Tokenización, FX on-chain y mercados programables

## Instrucciones

Responde sin consultar las soluciones de los laboratorios. Puedes usar las
clases y las fuentes oficiales. Declara los supuestos que necesites: un supuesto
explícito suma; uno oculto resta.

**Puntaje total:** 100 puntos. **Aprobación:** 70. **Tiempo sugerido:** 3 horas.

## Sección A — Arquitectura y régimen (25 puntos)

**1.** (8 pts) Un fondo tokeniza sus participaciones. El registro oficial sigue
siendo el del administrador.

- **a)** Di qué configuración es y si permite liquidación atómica.
- **b)** Enumera las seis causas de divergencia y señala cuáles vienen de fuera
  del sistema.
- **c)** Propón la configuración alternativa y di qué elimina y qué no.

**2.** (7 pts) Una emisión de participaciones fija 1 voto por participación y
fracciona el token en milésimas. El promotor conserva el 30 % en participaciones
enteras y el resto se reparte en fracciones entre 9 500 tenedores.

- **a)** Calcula cuántos votos se pierden si se redondea a la baja.
- **b)** Calcula el peso relativo del promotor con y sin redondeo.
- **c)** Propón dos correcciones.

**3.** (5 pts) Un producto se presenta como «bono digital sin intermediarios».
Enumera qué obligaciones de una oferta pública **no** cambian por tokenizar.

**4.** (5 pts) Explica por qué un derecho de rescate es imprescindible y qué tres
elementos lo hacen real.

## Sección B — Cálculo (30 puntos)

**5.** (10 pts) Una emisión de 25 000 000 con mínimo de 15 000 000 recibe demanda
por 88 000 000 en 5 200 órdenes iguales.

- **a)** Resuelve la adjudicación con prorrateo simple y con tramo mínimo de
  2 000.
- **b)** Estima la demanda genuina suponiendo un factor de exageración de 2,4 y
  declara el supuesto.
- **c)** Calcula el coste de bloquear una orden de 400 000 durante 12 días al
  4,2 % anual, y di qué efecto tiene sobre el libro.

**6.** (10 pts) Una plataforma liquida 300 000 000 diarios con ciclo T+2, una
probabilidad de incumplimiento a 2 días del 0,005 % y una recuperación del 40 %.

- **a)** Calcula la pérdida esperada anual por riesgo de principal.
- **b)** Con liquidación atómica, calcula el coste de liquidez si el saldo
  necesario pasa del 6 % al 20 % del volumen, a un coste del 4,5 % anual.
- **c)** Repite con neteo, que deja el saldo necesario en el 10 %, y concluye.

**7.** (10 pts) Un mecanismo automatizado tiene reservas de 800 000 y 2 400 000
unidades, con comisión del 0,3 %.

- **a)** Calcula el precio marginal y el precio efectivo de entregar 32 000
  unidades del primer activo.
- **b)** Verifica la regla del deslizamiento.
- **c)** Con 9 000 de comisiones anuales sobre una aportación de 60 000, calcula
  el neto si el precio se mueve con r = 1,6 y di si compensa.

## Sección C — Riesgo y control (25 puntos)

**8.** (9 pts) Una tesorería cambia divisas con pago irrevocable a las 09:00 en
la divisa entregada y confirmación a las 15:00 en la recibida, con 9 horas de
diferencia horaria.

- **a)** Calcula la ventana un día normal y un viernes.
- **b)** Con 25 000 000 diarios, una probabilidad del 0,004 % y recuperación del
  50 %, calcula la pérdida esperada anual.
- **c)** Compara neteo (al 20 % del bruto), PvP bruto y PvP neteado con
  prefinanciación del 25 % al 4,5 %, **contra la misma base**.

**9.** (8 pts) Un sistema de colateral tiene 200 posiciones, ratio exigido del
150 %, umbral de liquidación del 120 % y profundidad al 1 % de 1 800 000.

- **a)** Calcula el recorte con volatilidad diaria del 2,1 %, factor 2,33,
  impacto del 0,2 % y coste de operación del 0,05 %.
- **b)** Explica en qué se diferencia del colchón implícito del ratio.
- **c)** Si una caída dispara 40 liquidaciones de 420 000 de colateral medio,
  calcula el impacto con liquidación entera y estima el de la parcial.

**10.** (8 pts) Un custodio propone cuenta ómnibus para 1 500 titulares y 200
000 000 custodiados, con conciliación semanal dos a dos.

- **a)** Calcula el coste de pasar a cuenta segregada a 0,4 por posición y mes, y
  exprésalo como porcentaje del custodiado.
- **b)** Construye el caso en que una conciliación dos a dos oculta una
  diferencia.
- **c)** Enumera los seis elementos del plan de sustitución.

## Sección D — Expediente y decisión (20 puntos)

**11.** (12 pts) Redacta el expediente resumido de diseño de un mercado primario
y secundario para el instrumento de la pregunta 5. Incluye al menos: registro de
referencia, mecanismo de adjudicación, tramo de dinero, estructura de mercado,
compromiso de liquidez y custodia. **Cada decisión con su alternativa medida.**

**12.** (8 pts) El folleto de ese instrumento contiene cinco promesas: liquidación
atómica, liquidez secundaria, acceso desde 1 000, menos intermediarios y cupón
automático. Para cada una, di si se mantiene, se reformula o se retira, con su
evidencia.

## Rúbrica

| Sección | Criterio | Puntos |
|---|---|---:|
| A | Arquitectura justificada y régimen correcto | 25 |
| B | Cálculos correctos con supuestos declarados | 30 |
| C | Identifica el riesgo que la cifra publicada oculta | 25 |
| D | Expediente con alternativas medidas y promesas con evidencia | 20 |

### Criterios transversales

| Criterio | Efecto |
|---|---|
| Decisión con su alternativa medida | Suma |
| Decisión justificada por «es más adecuado» | No puntúa |
| Supuesto oculto | Resta el doble de lo que valía la cifra |
| Recomendación de inversión | Anula la pregunta |
| Promesa sin evidencia mantenida en el folleto | Resta |
| Conclusión de que no procede tokenizar, bien fundada | Vale lo mismo |

## Guía de corrección

| Pregunta | Idea que debe aparecer |
|---:|---|
| 1 | Espejo · no permite atomicidad · evento corporativo y decisión judicial vienen de fuera · bloqueo de origen |
| 2 | ≈ 4 997 votos perdidos · promotor pasa del 30 % al 37,9 % · voto proporcional exacto y agrupación |
| 3 | Calificación, folleto, responsabilidad, publicidad, idoneidad, información periódica, prevención |
| 4 | Salida que no dependa de la plataforma: copia en un tercero, procedimiento con plazo y ejecutor alternativo |
| 5 | Fracción 28,4 % · el tramo mínimo redistribuye · coste ≈ 560 · el libro empieza a informar |
| 6 | 750 000 de pérdida esperada · 1 890 000 de coste bruto · 540 000 con neteo · el neteo lo hace viable |
| 7 | Marginal 3,0 · efectivo ≈ 2,88 · deslizamiento ≈ 4 % ≈ tamaño relativo · con r = 1,6 la divergencia es −2,7 % |
| 8 | Ventana 15 h y 63 h · pérdida ≈ 74 400 · comparar los tres contra 74 400, no entre sí |
| 9 | Recorte ≈ 5,14 % · el colchón cubre lo anterior a decidir · impacto ≈ 9,3 % frente a ≈ 2,3 % |
| 10 | 7 200 al año = 0,0036 % · el custodio ajusta al depositario sin avisar al token · los seis elementos |
| 11 | Cada decisión con la alternativa y el número |
| 12 | Al menos una retirada y una reformulada, con su evidencia |
