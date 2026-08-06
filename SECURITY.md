# Política de seguridad

## Naturaleza del repositorio

Este repositorio contiene **material educativo y datos exclusivamente sintéticos**. No
almacena, procesa ni transmite información de personas reales, y las herramientas que
incluye son didácticas: no están endurecidas para uso en producción.

---

## Qué nunca debe subirse

| ❌ Prohibido | Por qué |
|---|---|
| Números de documento de identidad | Dato personal identificable |
| Números de cuenta, tarjeta o IBAN | Dato financiero identificable |
| Cartolas, estados de cuenta o movimientos reales | Aun anonimizados, son reidentificables |
| Antecedentes crediticios de terceros | Dato sensible |
| Credenciales, claves, tokens o certificados | Riesgo directo |
| Cadenas de conexión o archivos de configuración con secretos | Riesgo directo |
| Capturas de pantalla de sistemas productivos | Suelen contener datos de terceros |
| Bases descargadas de sistemas bancarios | Prohibido sin excepción |

> **La seudonimización no es suficiente.** La combinación de edad, zona y productos
> contratados identifica a personas concretas (ver Parte 12, clase 10).

Si detectas que alguno de estos elementos entró al repositorio, **repórtalo de inmediato
por el canal privado**: la corrección exige reescribir el historial, no solo borrar el
archivo.

---

## Alcance de un reporte de seguridad

### Dentro del alcance

- Secretos, credenciales o datos personales presentes en el repositorio o en su historial.
- Vulnerabilidades en las herramientas de `tools/` o en las aplicaciones de `apps/`
  (inyección, ejecución arbitraria, escritura fuera del directorio esperado).
- Dependencias con vulnerabilidades conocidas y explotables en el uso previsto.
- Configuración de la integración continua que permita ejecución no autorizada.
- Contenido que facilite un uso indebido del sistema financiero.

### Fuera del alcance

- Que las aplicaciones didácticas no tengan autenticación: es su diseño.
- Que la base SQLite del simulador no esté cifrada: contiene datos sintéticos.
- Errores de contenido o fuentes desactualizadas → usa un
  [issue](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/issues).
- Recomendaciones genéricas de análisis automático sin un escenario de explotación.

---

## Cómo reportar

| Tipo de hallazgo | Canal |
|---|---|
| **Secreto o dato personal expuesto** | Canal privado del mantenedor. **No abras un issue público.** |
| **Vulnerabilidad en las herramientas** | Canal privado; si no es sensible, un issue con la etiqueta `security` |
| **Dependencia vulnerable** | Issue público con la referencia del aviso |
| **Contenido de uso indebido** | Issue, o canal privado si su publicación agravaría el problema |

### Qué incluir

1. Descripción del problema y su efecto.
2. Pasos para reproducirlo.
3. Versión o confirmación afectada.
4. Si aplica, una propuesta de corrección.

**No publiques pruebas de concepto que incluyan secretos o datos reales.** Descríbelas.

---

## Compromiso de respuesta

| Etapa | Plazo objetivo |
|---|---|
| Acuse de recibo | 72 horas |
| Evaluación inicial | 7 días |
| Corrección de datos o secretos expuestos | Inmediata al confirmarse |
| Corrección de vulnerabilidad en herramientas | Según severidad |
| Comunicación pública | Tras la corrección, salvo acuerdo distinto |

Quien reporte de buena fe no sufrirá represalias y se le acreditará si lo desea.

---

## Buenas prácticas para quien contribuye

```bash
# Revisa qué vas a confirmar antes de hacerlo
git diff --staged
```

- Ejecuta las herramientas con datos de `datasets/`, no con datos propios de trabajo.
- Verifica que los archivos generados por las aplicaciones no contengan datos reales.
- Los artefactos locales (`*.db`, `*.sqlite`, `.env`) están en `.gitignore`; no los fuerces.
- Si dudas de si algo es un dato personal, **trátalo como si lo fuera**.

---

**Ver también:** [Ética y limitaciones](docs/etica-y-limitaciones.md) ·
[Contribuir](CONTRIBUTING.md) · [Código de conducta](CODE_OF_CONDUCT.md)
