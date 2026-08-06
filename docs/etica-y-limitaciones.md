# Ética y limitaciones

Qué es este material, qué no es, y qué obligaciones asume quien lo usa. **Lee esta página
antes de aplicar cualquier contenido a una decisión real.**

---

## 1 · Qué es y qué no es este material

<table>
<tr><th width="50%">✅ Qué es</th><th width="50%">❌ Qué no es</th></tr>
<tr><td>

- Material **formativo** de acceso abierto
- Explicación de marcos internacionales y su lógica
- Casos con datos **sintéticos** para practicar
- Herramientas de cálculo con fines didácticos
- Referencias a fuentes oficiales verificables

</td><td>

- Asesoría financiera, tributaria o legal
- Sustituto de títulos, certificaciones o autorizaciones
- Norma aplicable en ningún país
- Recomendación de inversión, de producto o de proveedor
- Sistema apto para decidir sobre personas reales

</td></tr>
</table>

> Todos los nombres, montos, instituciones y casos son **educativos** salvo indicación
> expresa. El «Banco Austral» de la Parte 16 no existe.

---

## 2 · Verificación local: la regla central

Cada clase con contenido normativo cierra con una línea de **verificación local**.

```text
- Verificación local: revisa los requerimientos de liquidez y de riesgo de tasa
  del libro de banca que aplica tu supervisor.
```

**El programa describe marcos internacionales. La norma que obliga es siempre la
nacional.** Lo que cambia por país y por fecha:

| Ámbito | Qué varía |
|---|---|
| Capital y liquidez | Colchones activados, deducciones, discrecionalidades nacionales |
| Provisiones | Normas locales suelen ser más estrictas que NIIF 9 |
| Protección al consumidor | Plazos, instancias, carga de la prueba, tasas máximas |
| Prevención de lavado | Umbrales de reporte, plazos, autoridad receptora |
| Protección de datos | Bases de licitud, plazos de notificación, derechos |
| Insolvencia | Orden de prelación, mayorías, tratamiento del dinero nuevo |
| Licenciamiento | Capital mínimo, umbrales de accionista significativo |

---

## 3 · Datos

### Prohibiciones absolutas

> **No uses datos reales de personas en ningún ejercicio de este programa**, ni siquiera
> anonimizados. La seudonimización no elimina la reidentificación
> (Parte 12, clase 10).

- ❌ Datos de clientes de tu institución
- ❌ Números de cuenta, documentos de identidad, antecedentes crediticios ajenos
- ❌ Bases descargadas de sistemas productivos
- ❌ Capturas de pantalla con información de terceros

### Lo que sí se usa

- ✅ Los datos sintéticos incluidos en `datasets/`
- ✅ Tus propios datos personales, bajo tu responsabilidad
- ✅ Información pública de empresas cotizadas y de organismos oficiales
- ✅ Datos que generes tú mismo, con semilla documentada

---

## 4 · Modelos y decisiones automatizadas

Las Partes 9, 11, 14 y 16 desarrollan modelos de riesgo y decisión. Su uso educativo
exige reconocer que:

| Principio | Consecuencia práctica |
|---|---|
| **Un modelo educativo no decide sobre personas** | Los de este repositorio no están validados para producción |
| **Automatiza lo que beneficia, no lo que perjudica** | Aprobar puede ser automático; rechazar exige revisión humana |
| **Todo rechazo exige explicación** | Motivos concretos y accionables, no fórmulas genéricas |
| **Quitar el atributo protegido no elimina el sesgo** | Las variables sustitutas siguen actuando (Parte 14, clase 11) |
| **La elección de una definición de equidad es normativa** | No la tome un equipo técnico sin mandato |
| **Un modelo tiene dominio de aplicación** | Fuera de él, sus resultados no son válidos |
| **La supervisión humana debe ser significativa** | Con información, tiempo y autoridad para discrepar |

### Atributos que nunca deben usarse para decidir

Ni directamente ni a través de variables sustitutas: **origen étnico o nacional, género,
orientación sexual, religión, opinión política, afiliación sindical, estado de salud,
discapacidad, embarazo**, y los demás que la normativa antidiscriminación de tu país
proteja.

> Ver Parte 14, clase 11 para el análisis completo, incluida la detección de sustitutas.

---

## 5 · Uso profesional del material

Si aplicas estos contenidos en una institución financiera:

1. **Contrasta con tu normativa** antes de aplicar cualquier criterio.
2. **Valida los modelos** de forma independiente antes de usarlos
   (Parte 11, clase 12).
3. **Documenta los supuestos** de cada cálculo y quién los aprobó.
4. **Somete al proceso de gobierno** cualquier decisión que afecte a clientes.
5. **No presentes este material como norma** ni como criterio supervisor.

Los cálculos del programa son ilustrativos. **Los parámetros —PD, LGD, correlaciones,
elasticidades, ponderaciones— deben estimarse con datos propios y validarse.**

---

## 6 · Uso responsable de los contenidos sensibles

El programa cubre materias donde el conocimiento tiene doble uso.

| Materia | Uso previsto | Uso inaceptable |
|---|---|---|
| Prevención de lavado (Parte 12) | Diseñar controles | Diseñar formas de eludirlos |
| Fraude digital (Parte 14) | Detectar y prevenir | Ejecutar fraude |
| Sanciones (Parte 12) | Cumplir el régimen | Identificar vías de elusión |
| Ingeniería social (Parte 4) | Proteger al cliente | Manipular a personas |
| Modelos de decisión (Partes 9, 14) | Evaluar con criterio | Discriminar con apariencia técnica |

El material se presenta desde la perspectiva de **quien construye la defensa**, y esa
orientación es deliberada.

---

## 7 · Conflictos entre objetivos legítimos

El programa expone varias tensiones que no tienen solución técnica. Reconocerlas es parte
del contenido:

| Tensión | Dónde se trata |
|---|---|
| Integridad frente a inclusión financiera | Parte 12, clase 3 · Parte 16, clase 13 |
| Privacidad frente a trazabilidad | Parte 12, clase 10 · Parte 14, clase 10 |
| Prudencia frente a acceso al crédito | Parte 14, clase 7 · Parte 16, clase 7 |
| Eficiencia frente a cobertura territorial | Parte 10, clase 15 |
| Rentabilidad frente a conducta con el cliente | Parte 12, clase 8 · Parte 16, clase 5 |
| Métrica de sostenibilidad frente a efecto real | Parte 15, clase 11 |

> En todas, el programa exige lo mismo: **resolver la tensión de forma explícita,
> cuantificar lo que se cede y declararlo**. Lo inaceptable no es elegir un lado: es
> resolverla en silencio.

---

## 8 · Límites conocidos de este material

Declarados, no descubiertos:

- **No es exhaustivo.** 240 clases cubren mucho y no todo.
- **No cubre ninguna jurisdicción en particular.** Es su diseño, y también su límite.
- **Los datos son sintéticos.** Los patrones son verosímiles, no reales.
- **Los parámetros son ilustrativos.** PD, LGD y correlaciones deben estimarse.
- **Las herramientas son didácticas.** No están endurecidas para producción.
- **Está en un solo idioma.** Las traducciones son bienvenidas.
- **Refleja el estado de las fuentes a su fecha.** Los marcos evolucionan.

---

## 9 · Cómo reportar un problema

| Situación | Canal |
|---|---|
| Error de contenido o fuente incorrecta | [Issue](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/issues) citando la clase |
| Fuente rota o superada | Issue con la referencia vigente |
| Contenido que induzca a un uso indebido | Issue, o [SECURITY.md](../SECURITY.md) si es sensible |
| Sesgo o formulación problemática | Issue; se revisa con prioridad |

---

## 10 · Resumen en cinco líneas

> 1. Material **formativo**: no es asesoría ni norma.
> 2. **Verifica siempre** la norma local vigente.
> 3. **Nunca** uses datos reales de personas.
> 4. **Automatiza lo que beneficia**, no lo que perjudica.
> 5. **Declara los supuestos y los límites** de todo lo que calcules.

---

**Ver también:** [Guía docente](guia-docente.md) · [Fuentes](fuentes.md) ·
[Código de conducta](../CODE_OF_CONDUCT.md) · [Seguridad](../SECURITY.md)
