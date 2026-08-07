# Parte 19: Blockchain y DLT para instituciones financieras

- **Etapa:** 5 — Finanzas digitales, infraestructura y mercados tokenizados
- **Clases:** 14
- **Horas:** 21
- **Laboratorios:** 6
- **Evaluaciones:** 2
- **Proyecto:** 1

## Descripción

La Parte 14, clase 9 introdujo el registro distribuido y su criterio de
evaluación. Esta parte lo abre: qué hay dentro, qué garantiza cada pieza, qué
cuesta y en qué casos una institución financiera obtiene algo que una base de
datos compartida no le da.

El eje es una pregunta que se responde con números, no con adjetivos:

```text
UN REGISTRO DISTRIBUIDO PERMITE QUE PARTES QUE NO CONFÍAN
ENTRE SÍ NI EN UN TERCERO COMÚN MANTENGAN UN REGISTRO
QUE NINGUNA CONTROLA

  eso es lo único que da, y lo da caro:
  redundancia total, lentitud, irreversibilidad

  LA PREGUNTA NO ES «¿SE PUEDE?»
  ES «¿EXISTE AQUÍ UN TERCERO DE CONFIANZA DISPONIBLE?»
  si existe, una base de datos compartida es más rápida,
  más barata y corregible
```

## Prerrequisitos

| Parte | Clase | Qué aporta |
|---|---|---|
| 11 | Gestión integral de riesgos | Riesgo operacional y de modelo |
| 14 | 9 · Criptoactivos y registro distribuido | Criterio de evaluación de casos de uso |
| 17 | 7 · Firma de mensajes | Criptografía aplicada y gestión de claves |
| 18 | 7 y 15 · Liquidación y atomicidad | Finalidad y liquidación condicional |

## Resultados de aprendizaje

- Explicar qué garantiza cada pieza —resumen, firma, árbol, consenso— y qué
  **no** garantiza.
- Distinguir finalidad probabilística de determinística y calcular la espera
  necesaria para un nivel de riesgo dado.
- Comparar redes públicas, privadas y autorizadas por sus propiedades
  observables, no por su etiqueta.
- Evaluar un contrato inteligente como lo que es: código irreversible con
  dinero dentro.
- Decidir con criterio si un caso de uso justifica un registro distribuido,
  midiendo la alternativa que no lo usa.

## Competencias

| Competencia | Nivel esperado |
|---|---|
| Criptografía aplicada | Implementa y verifica |
| Diseño de consenso | Modela y prueba bajo fallos |
| Evaluación de casos de uso | Compara con la alternativa, con números |
| Riesgo de infraestructura | Identifica y controla |
| Gestión de claves | Diseña custodia y recuperación |

## Secuencia

1. [Sistemas distribuidos aplicados a finanzas](classes/01-sistemas-distribuidos-aplicados-a-finanzas.md)
2. [Resúmenes, firmas y árboles de Merkle](classes/02-resumenes-firmas-y-arboles-de-merkle.md)
3. [Claves, direcciones y gestión criptográfica](classes/03-claves-direcciones-y-gestion-criptografica.md)
4. [Transacciones, bloques, nodos y estado](classes/04-transacciones-bloques-nodos-y-estado.md)
5. [Mecanismos de consenso](classes/05-mecanismos-de-consenso.md)
6. [Finalidad, reorganizaciones y tolerancia a fallos](classes/06-finalidad-reorganizaciones-y-tolerancia-a-fallos.md)
7. [Redes públicas, privadas y autorizadas](classes/07-redes-publicas-privadas-y-autorizadas.md)
8. [Contratos inteligentes](classes/08-contratos-inteligentes.md)
9. [Oráculos](classes/09-oraculos.md)
10. [Privacidad y pruebas criptográficas](classes/10-privacidad-y-pruebas-criptograficas.md)
11. [Interoperabilidad y puentes](classes/11-interoperabilidad-y-puentes.md)
12. [Escalabilidad, capas y disponibilidad](classes/12-escalabilidad-capas-y-disponibilidad.md)
13. [Gobernanza, bifurcaciones y recuperación](classes/13-gobernanza-bifurcaciones-y-recuperacion.md)
14. [Proyecto: red financiera autorizada](classes/14-proyecto-red-financiera-autorizada.md)

## Laboratorios

| # | Laboratorio | Entregable principal |
|---:|---|---|
| 1 | [Cadena didáctica en Python](labs/lab-01.md) | Encadenamiento y detección de manipulación |
| 2 | [Firma de transacciones](labs/lab-02.md) | Firma, verificación y ataque de repetición |
| 3 | [Árbol de Merkle](labs/lab-03.md) | Prueba de inclusión y de exclusión |
| 4 | [Consenso con nodos defectuosos](labs/lab-04.md) | Tolerancia medida, no supuesta |
| 5 | [Contrato de depósito en garantía](labs/lab-05.md) | Máquina de estados y fallo irreversible |
| 6 | [Comparación con base centralizada](labs/lab-06.md) | Medición de coste, latencia y recuperación |

## Evaluaciones

- [Diagnóstico](assessments/diagnostic.md)
- [Evaluación final](assessments/final.md)

## Proyecto

- [Red financiera autorizada](project/README.md)

## Evidencias

- Cadena funcional con detección de manipulación demostrada.
- Firma y verificación con su prueba de repetición.
- Prueba de inclusión de Merkle sobre un conjunto grande.
- Consenso ejecutado con nodos defectuosos, con el umbral medido.
- Contrato con su máquina de estados y su caso de fallo irreversible.
- Comparación cuantitativa con la alternativa centralizada.

## Mapa de dependencias

```text
Parte 14, clase 9 (criptoactivos y registro)
   └── Parte 19 — blockchain y DLT
          ├── Parte 20 · el activo que circula sobre el registro
          ├── Parte 21 · el instrumento financiero tokenizado
          ├── Parte 22 · el régimen del registro y de sus participantes
          └── Parte 23 · la infraestructura del mercado tokenizado
```

## Aplicación asociada

- [`apps/dlt_financial_lab/`](../../apps/dlt_financial_lab/README.md)

## Fuentes oficiales de referencia

- Committee on Payments and Market Infrastructures (BIS) — informes sobre
  tecnología de registro distribuido en infraestructuras de mercado.
- Basel Committee on Banking Supervision — tratamiento prudencial y riesgos.
- NIST — publicaciones sobre blockchain y gestión de claves.
- IOSCO — informes sobre finanzas descentralizadas.
- ISO/TC 307 — normalización de tecnologías de registro distribuido.

## Limitaciones

- El laboratorio implementa una cadena **didáctica**: no es segura, no es
  eficiente y no debe usarse para nada real.
- **No se crea ninguna criptomoneda destinada a uso real** ni se despliega nada
  en una red pública.
- Los mecanismos criptográficos se implementan para entenderlos; en producción
  se usan bibliotecas auditadas, nunca una implementación propia.
- La parte no cubre el diseño de activos ni su régimen: eso es la Parte 20.
