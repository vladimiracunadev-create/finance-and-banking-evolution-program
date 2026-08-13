# Caso · El puente y la firma que sobraba

**Tema:** blockchain y DLT · **Parte relacionada:** 19 · **Naturaleza:** caso
sintético compuesto · **Fecha de verificación:** 2026-08-12

Un puente entre dos redes custodia el activo en una y emite una representación en
la otra. La seguridad del conjunto no es la de la red más fuerte ni la de la más
débil: es la del comité que autoriza las emisiones. Este caso es sobre ese comité.

## Hechos

```text
HECHO VERIFICADO (del expediente del caso)

  · el puente bloquea el activo en la red A
    y emite un representante en la red B
  · las emisiones las autoriza un comité de
    9 validadores, con 5 firmas necesarias
  · 4 de los 9 pertenecían al mismo operador
  · un quinto validador usaba la misma
    imagen de servidor y la misma clave de
    despliegue que esos cuatro

SUPUESTO DEL EJERCICIO
  · valor bloqueado           118 000 000
  · emisión no autorizada      41 500 000
  · tiempo hasta la detección       37 min
  · recuperado posteriormente   6 200 000
```

El diseño declaraba «5 de 9». El diseño real era «1 de 1»: comprometer la clave
de despliegue común daba las cinco firmas. **La descentralización se mide por
independencia de fallo, no por número de participantes.**

## Actores

| Actor | Qué persigue | Qué información tenía |
|---|---|---|
| Usuario del puente | Mover su activo entre redes | «5 de 9 validadores» |
| Operador mayoritario | Operar el puente con eficiencia | La configuración real |
| Otros validadores | Cobrar por validar | Su propia parte |
| Atacante | El valor bloqueado | La configuración real, también |
| Auditor del contrato | Verificar el código | El código, no la infraestructura |
| Mercado de la red B | Liquidez del representante | El precio, al caer |

## Decisiones

```text
DISEÑO
  comité de 9 con umbral de 5
  DECISIÓN CORRECTA EN EL PAPEL

OPERACIÓN
  el operador aporta 4 validadores
  «para garantizar disponibilidad»
  RAZÓN OPERATIVA REAL Y RIESGO NO EVALUADO

OPERACIÓN
  se despliega el quinto con la misma
  plantilla, por comodidad
  AQUÍ SE PIERDE LA INDEPENDENCIA

AUDITORÍA
  alcance: el contrato inteligente
  FUERA DE ALCANCE: quién controla las
  claves y cómo se despliegan

INCIDENTE
  emisión no autorizada en la red B y
  venta inmediata contra la liquidez
  existente
```

## Riesgos

| Riesgo | Estaba presente | Se materializó |
|---|---|---|
| Correlación de fallo entre validadores | Desde el despliegue | Sí |
| Alcance de auditoría limitado al código | Desde el inicio | Sí |
| Ausencia de límite de emisión por ventana | Desde el diseño | Sí |
| Liquidez de salida en la red B | Estructural | Sí |
| Irreversibilidad de las transferencias | Estructural | Sí |
| Riesgo de contagio a protocolos que aceptaban el representante | Estructural | Parcialmente |

## Regulación

```text
QUÉ ALCANZA

  CUSTODIA
    el puente custodia activos de terceros
    aunque no se llame custodio: la función
    define el régimen, no el nombre

  INFORMACIÓN AL USUARIO
    describir el esquema como «5 de 9» sin
    revelar la correlación puede constituir
    información engañosa

  PREVENCIÓN Y TRAZABILIDAD
    la salida de los fondos activa
    obligaciones de análisis de cadena y de
    comunicación en los intermediarios que
    los reciban

LÍMITE
  el tratamiento de los puentes es
  desigual entre jurisdicciones y sigue
  en construcción
```

## Controles

| Control | Existía | Funcionó | Qué faltaba |
|---|---|---|---|
| Umbral de firmas | Sí | No, por correlación | Independencia acreditada |
| Auditoría | Sí | Sí, en su alcance | Ampliar a claves e infraestructura |
| Límite de emisión por ventana | No | — | Tope horario y diario |
| Retardo en emisiones grandes | No | — | Ventana de impugnación |
| Vigilancia de anomalías | Parcial | Tarde | Alerta en el minuto 1, no en el 37 |
| Plan de respuesta con pausa | No | — | Quién pausa, y en cuánto tiempo |

El tercero y el cuarto son los que más habrían limitado la pérdida. Un tope de
emisión por hora y un retardo obligatorio para importes grandes no impiden el
ataque: **acotan cuánto se lleva y dan tiempo a reaccionar**, que es de lo que se
trata cuando la reversión no existe.

## Resultado

```text
PÉRDIDA (supuestos)

  emitido sin autorización     41 500 000
  vendido antes de la pausa    35 300 000
  recuperado                    6 200 000
  PÉRDIDA NETA                 29 100 000

EFECTO EN LA RED B
  el representante pierde su paridad con
  el activo original
  protocolos que lo aceptaban como
  colateral quedan infracolateralizados
  → SEGUNDA RONDA DE LIQUIDACIONES,
    no incluida en la cifra anterior
```

## Lecciones

1. **Contar validadores no mide descentralización.** Lo que se mide es la
   probabilidad de que fallen a la vez, y eso depende de claves, imágenes,
   proveedores y personas.
2. **El alcance de una auditoría es parte del control.** Auditar el contrato y no
   la infraestructura deja fuera exactamente donde estaba el fallo.
3. **Cuando no hay reversión, el control es el límite.** Topes por ventana y
   retardos para importes grandes convierten una pérdida total en una pérdida
   acotada.
4. **Un representante que pierde paridad contagia a todo lo que lo aceptaba.** El
   perímetro del incidente es mayor que el puente.

## Preguntas

1. ¿Cómo se acredita la independencia de nueve validadores? ¿Qué evidencia pedirías?
2. ¿Qué tope por ventana habrías fijado sobre 118 millones bloqueados, y con qué
   criterio?
3. ¿Es aceptable un retardo en emisiones grandes desde el punto de vista del
   usuario? ¿Qué se pierde?
4. ¿Quién debía haber pausado el puente, y en cuánto tiempo?
5. ¿Debe un protocolo que acepta un representante evaluar el puente que lo emite?
   ¿Con qué información?

## Fuentes

- Financial Stability Board (2023). *The Financial Stability Risks of Decentralised Finance*. <https://www.fsb.org/2023/02/the-financial-stability-risks-of-decentralised-finance/>
- IOSCO (2023). *Policy Recommendations for Decentralized Finance*. <https://www.iosco.org/library/pubdocs/pdf/IOSCOPD754.pdf>
- NIST. *SP 800-57, Recommendation for Key Management*. <https://csrc.nist.gov/publications/detail/sp/800-57-part-1/rev-5/final>
- Comité de Supervisión Bancaria de Basilea. *Prudential treatment of cryptoasset exposures*. <https://www.bis.org/bcbs/publ/d545.htm>
- Verificación local: caso sintético; cifras supuestas. El tratamiento regulatorio de los puentes es desigual entre jurisdicciones. **Fecha de verificación: 2026-08-12.** No constituye asesoría legal.
