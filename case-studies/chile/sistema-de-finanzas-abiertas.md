# Caso · El Sistema de Finanzas Abiertas de Chile, por fases

**Tema:** Chile · **Partes relacionadas:** 17 y 22 · **Naturaleza:** análisis de
un régimen público vigente · **Fecha de verificación:** 2026-08-12

Este caso no describe un incidente: describe una decisión de política pública
—implantar las finanzas abiertas por fases y con obligación legal— y las
preguntas de diseño que esa decisión abre. Se estudia porque es el régimen del
país al que este programa dedica más atención, y porque su calendario es la
variable que más condiciona a quien tiene que cumplirlo.

## Hechos

```text
HECHO VERIFICADO (fuente oficial)

  · la Ley N.º 21.521, publicada el 4 de
    enero de 2023, crea el Sistema de
    Finanzas Abiertas y el registro de
    prestadores de servicios financieros
  · la ley enumera actividades sujetas:
    plataformas de financiamiento
    colectivo, sistemas alternativos de
    transacción, intermediación, custodia,
    asesoría crediticia y de inversión,
    enrutamiento de órdenes
  · el desarrollo normativo corresponde a
    la CMF mediante normas de carácter
    general, con disposiciones transitorias
  · el detalle técnico del Sistema de
    Finanzas Abiertas se fija en normativa
    y en un anexo técnico

LO QUE HAY QUE VERIFICAR ANTES DE CITAR
  · qué normas de carácter general están
    vigentes hoy y cuáles se han modificado
  · en qué fase está la exigibilidad para
    cada tipo de participante
  · qué versión del anexo técnico rige
  · qué plazos transitorios siguen abiertos

ESTO NO ES UN DETALLE: es el dato que
decide qué tiene que hacer una entidad
este trimestre.
```

## Actores

| Actor | Qué persigue | Qué decide |
|---|---|---|
| Cliente | Compartir datos para obtener mejor servicio | Si consiente y a quién |
| Institución proveedora de información | Cumplir la obligación de dar acceso | Cómo dimensiona su interfaz |
| Proveedor de servicios basados en información | Construir producto sobre datos ajenos | Qué caso de uso justifica el coste |
| Proveedor de iniciación de pagos | Iniciar pagos por cuenta del cliente | Qué garantías ofrece |
| CMF | Que el sistema funcione y sea seguro | Ritmo, alcance y exigencias |
| Banco Central | Estabilidad y sistema de pagos | Qué observa |
| Proveedor tecnológico | Vender integración | Dónde se posiciona en la cadena |

## Decisiones

```text
DECISIÓN 1 · OBLIGACIÓN, NO VOLUNTARIEDAD
  el acceso a los datos es una obligación
  legal para las instituciones proveedoras
  EFECTO: el sistema no depende de que a
  cada banco le convenga

DECISIÓN 2 · POR FASES
  la exigibilidad se despliega en etapas
  EFECTO: reduce el riesgo de implantación
  y alarga la incertidumbre de quien planifica

DECISIÓN 3 · ESTÁNDAR TÉCNICO COMÚN
  se fija un anexo técnico, no se deja a
  acuerdos bilaterales
  EFECTO: reduce el coste de integración
  del entrante y traslada el coste al
  proveedor de información

DECISIÓN 4 · REGISTRO DE PARTICIPANTES
  con requisitos de gobierno, seguridad y
  continuidad
  EFECTO: eleva la barrera de entrada y la
  confianza a la vez
```

## Riesgos

| Riesgo | Naturaleza | Cómo se vigila |
|---|---|---|
| Calendario que se desplaza | De planificación | Seguimiento de normativa y transitorios |
| Interfaces que cumplen la forma y no el uso | De implantación | Métricas de disponibilidad y latencia |
| Concentración en intermediarios técnicos | Estructural | Mapa técnico, no solo contractual |
| Consentimientos que envejecen con el producto | De conducta | Registro de finalidades y panel |
| Coste desigual entre proveedor y consumidor de datos | Económico | Revisión del modelo de APIs premium |
| Exclusión de quien no tiene producto digital | Social | Medición de cobertura real |

## Regulación

```text
LA ARQUITECTURA, EN TRES NIVELES

  LEY
    define el sistema, los participantes y
    las actividades sujetas

  NORMAS DE CARÁCTER GENERAL DE LA CMF
    convierten la ley en obligaciones
    exigibles: qué presentar, con qué
    patrimonio, en qué plazo

  ANEXO TÉCNICO
    fija el detalle de las interfaces, la
    seguridad y los formatos

DÓNDE ESTÁ EL CALENDARIO REAL
  en las disposiciones transitorias de las
  normas, no en el cuerpo de la ley

Y ESA ES LA CONFUSIÓN MÁS FRECUENTE
```

## Controles

| Control | Para quién | Qué verifica |
|---|---|---|
| Registro y autorización | Participantes | Idoneidad, gobierno y capital |
| Requisitos de seguridad de la interfaz | Proveedores de información | Autenticación, cifrado y firma |
| Gestión del consentimiento | Todos | Otorgamiento, vigencia y revocación |
| Continuidad operacional | Todos | Disponibilidad y plan de contingencia |
| Prevención de lavado | Según actividad | Sujetos obligados y reportes |
| Protección de datos | Todos | Finalidad, minimización y conservación |

## Resultado

```text
QUÉ SE PUEDE AFIRMAR HOY

  · el marco existe y es obligatorio
  · el despliegue es progresivo
  · la carga inicial recae sobre las
    instituciones que deben abrir sus datos
  · el valor para el cliente depende de que
    aparezcan casos de uso que compensen
    el coste de integración

QUÉ NO SE PUEDE AFIRMAR SIN DATOS
  · cuántos clientes han consentido
  · qué proporción de esos consentimientos
    sigue activa a los doce meses
  · qué casos de uso han superado la fase
    piloto
  · si la competencia ha aumentado

Y ESA DISTINCIÓN ES EL EJERCICIO:
un régimen se evalúa con indicadores, y
los indicadores hay que definirlos antes.
```

## Lecciones

1. **La obligación legal resuelve el problema de arranque** —el banco no elige si
   abre— y no resuelve el de adopción, que depende de los casos de uso.
2. **Un estándar técnico común traslada el coste** desde el entrante hacia el
   proveedor de información, y esa es una decisión distributiva explícita.
3. **El calendario vive en las disposiciones transitorias.** Quien planifique
   leyendo solo la ley planificará mal.
4. **Sin indicadores públicos definidos, el éxito del sistema se discutirá sin
   datos**, exactamente como ocurre en otros casos de esta biblioteca.

## Preguntas

1. ¿Qué cinco indicadores públicos pedirías para evaluar el sistema a los tres
   años?
2. ¿Es justo que el coste de abrir los datos recaiga sobre quien los tiene?
   ¿Qué alternativas existen?
3. ¿Qué caso de uso crees que justifica antes la integración: agregación,
   iniciación de pagos o scoring alternativo? Justifícalo con números.
4. ¿Cómo se evita que la implantación por fases se convierta en una espera
   permanente?
5. ¿Qué papel deberían tener los intermediarios técnicos, y qué exigencias?

## Fuentes

- Biblioteca del Congreso Nacional de Chile. *Ley N.º 21.521*. <https://www.bcn.cl/leychile/navegar?idNorma=1187323>
- Comisión para el Mercado Financiero. *Normativa de desarrollo de la Ley 21.521 y Sistema de Finanzas Abiertas*. <https://www.cmfchile.cl/portal/principal/613/w3-channel.html>
- Banco Central de Chile. *Informe de Estabilidad Financiera y normativa de sistemas de pago*. <https://www.bcentral.cl/>
- Fichas normativas del repositorio: [`ley-21521`](../../regulatory/chile/ley-21521.yml) · [`ncg-502`](../../regulatory/chile/ncg-502-prestadores-fintec.yml)
- Verificación local: este caso describe un régimen vigente cuyo calendario y detalle **cambian**. Antes de usar cualquier plazo o requisito, comprueba en el sitio de la CMF qué normas están vigentes y en qué fase está la exigibilidad para tu actividad. **Fecha de verificación: 2026-08-12.** No constituye asesoría legal.
