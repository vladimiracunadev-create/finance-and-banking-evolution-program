# Guía de laboratorios digitales

Cómo son, cómo se ejecutan y cómo se corrigen los laboratorios de la Etapa 5.

## Qué distingue a estos laboratorios

Los de las Partes 1 a 16 piden analizar, calcular y concluir. Los de la Etapa 5
piden además **construir algo que falle donde debe fallar**. La diferencia es
deliberada: en infraestructura financiera, el conocimiento que importa no es
saber que un control existe, sino haber visto qué pasa cuando no está.

```text
UN LABORATORIO DE LA ETAPA 5 NO ESTÁ TERMINADO
CUANDO EL CAMINO FELIZ FUNCIONA

  está terminado cuando existe una prueba negativa
  por cada control, y esa prueba falla
  si alguien quita el control
```

## Estructura fija

Cada laboratorio tiene las mismas catorce secciones, en el mismo orden:

| Sección | Qué contiene |
|---|---|
| Propósito | Qué se aprende, en una frase |
| Escenario | La situación, con una tensión real |
| Contexto | Por qué el problema existe |
| Datos | Conjunto sintético concreto, con su ficha |
| Supuestos del ejercicio | Lo que se da por cierto y su efecto si cambia |
| Requisitos | Versión de Python y laboratorios previos |
| Pasos | Numerados y verificables |
| Arquitectura | Diagrama del flujo o del sistema |
| Criterios de aceptación | Condiciones **comprobables**, no opinables |
| Amenazas a considerar | Amenaza, efecto y mitigación esperada |
| Pruebas | Comandos exactos |
| Entregables | Qué se guarda en el portafolio |
| Rúbrica | Puntos por criterio |
| Solución de referencia | Enlace a `solutions/` |

## Entorno

Todos funcionan con **Python 3.11 o superior y la biblioteca estándar**. Las
únicas dependencias del repositorio son `pytest` para las pruebas y `markdown`
para generar el portal.

```bash
python -m pip install -r requirements.txt
```

No hace falta red, ni cuenta en ningún servicio, ni contenedor, ni base de
datos. Un laboratorio que necesitara cualquiera de esas cosas quedaría fuera del
alcance de quien más lo necesita.

## Reglas de datos y seguridad

1. **Solo datos sintéticos**, generados con semilla fija y documentados en
   `datasets/schemas/`.
2. **Ninguna credencial real.** Las claves de los laboratorios son de juguete y
   están versionadas a propósito; `tools/detect_secrets.py` distingue el valor
   de ejemplo del secreto real.
3. **Ningún dato personal.** `tools/detect_pii.py` comprueba RUT con dígito
   verificador válido, tarjetas que pasan Luhn, IBAN y correos con dominio real.
4. **Ningún fondo real, ninguna red pública, ningún servicio de pago.**
5. **Ninguna herramienta ofensiva.** Los ataques se implementan como *pruebas
   que deben fallar*, nunca como utilidades reutilizables.

## Cómo se corrige

La rúbrica de todos ellos reparte los puntos con el mismo criterio de fondo:

| Bloque | Peso típico | Qué distingue el nivel alto |
|---|---:|---|
| Funcionamiento | 25–30 % | El camino feliz y los caminos infelices |
| Pruebas negativas | 20–30 % | Una por control, no una por función |
| Decisión y justificación | 20 % | Se registró la alternativa descartada |
| Trazabilidad y evidencia | 15 % | Otra persona puede reproducirlo |
| Límites declarados | 10–15 % | Se dice qué no se cubrió, antes de que lo pregunten |

**Un laboratorio con todo en verde y sin pruebas negativas no aprueba.** Es la
regla que más sorprende y la que mejor resume la etapa.

## Las soluciones de referencia

Están en `modules/<parte>/solutions/`. Son material **docente**:

- sirven para corregir y para desbloquear;
- **no** sustituyen el trabajo del estudiante;
- explican *por qué* cada decisión, no solo *qué* decisión;
- declaran sus propios límites, igual que los laboratorios.

Un trabajo que reproduce la solución de referencia sin decisiones propias
obtiene el mínimo de la franja de aprobación. La solución muestra un camino
válido, no el único.

## Comandos que se usan

```bash
python -m pytest -q
```

```bash
python apps/open_finance_sandbox/conformance_tests/run.py
```

```bash
python tools/validate_openapi.py
```

```bash
python tools/detect_secrets.py && python tools/detect_pii.py
```

```bash
python tools/validate_datasets.py && python tools/validate_metadata.py
```

## Errores frecuentes al hacerlos

| Síntoma | Causa | Corrección |
|---|---|---|
| «Ya funciona» sin pruebas negativas | Se probó lo que se construyó | Una prueba por control |
| Supuestos no escritos | Se dieron por obvios | Tabla de supuestos, siempre |
| Solución copiada | Se buscó terminar, no aprender | La rúbrica lo detecta y lo penaliza |
| Datos propios reales | Comodidad | Solo sintéticos; el detector falla |
| Sin sección de límites | Se creyó que resta | Declarar fortalece |
| Prueba que comprueba un campo | Se verificó el estado, no el efecto | Comprueba la consecuencia |

---

**Ver también:** [Etapa 5](etapa-5-finanzas-digitales.md) ·
[Guía docente](guia-docente.md) ·
[Mapa de finanzas abiertas](mapa-finanzas-abiertas.md) ·
[Ética y limitaciones](etica-y-limitaciones.md)
