# Licencias y procedencia de datos

Esta tabla se aplica a la distribución desde el **22 de septiembre de 2026**.
Las fichas individuales en `datasets/schemas/` indican origen, fecha, supuestos
y limitaciones. Consulta [docs/LICENSING_HISTORY.md](docs/LICENSING_HISTORY.md)
para las copias anteriores.

| Fuente y rutas | Procedencia | Régimen |
|---|---|---|
| `datasets/*.csv` y `datasets/synthetic/*.csv` | Datos sintéticos creados para el programa; ninguna fila representa un cliente real | CC BY-NC-SA 4.0 sobre la selección, estructura y expresión original en la medida en que existan derechos protegibles; cifras y hechos aislados no adquieren derechos por esta declaración |
| `datasets/schemas/*.md` y `datasets/README.md` | Diccionarios y explicación originales | CC BY-NC-SA 4.0 |
| `apps/**/data/*.json` y otros fixtures de simuladores | Entradas técnicas sintéticas de las aplicaciones | MIT junto con el código, salvo aviso específico en el archivo |
| `datasets/raw/` y `datasets/processed/` | Sin archivos de datos actualmente | Ninguna licencia anticipada: registrar cada futura fuente, permiso, atribución, fecha y transformación antes de incorporar datos |
| `sources/bibliography.json` | Registro de referencias bibliográficas, no copia de las obras | La estructura y anotaciones originales siguen CC BY-NC-SA 4.0; títulos, identificadores, hechos bibliográficos y sitios enlazados conservan su propio régimen |
| `regulatory/**/*.yml` | Fichas originales que resumen instrumentos oficiales | CC BY-NC-SA 4.0 sobre la redacción original de la ficha; el instrumento y su fuente oficial mantienen su régimen propio |

Licencia del contenido: [LICENSE-CONTENT.md](LICENSE-CONTENT.md). Los datos
sintéticos son para formación; no sirven para calibrar decisiones sobre personas
ni reflejan tasas o comportamientos reales. Una fuente externa futura exige una
entrada nueva aquí y su aviso en [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)
antes de distribuirla. No se presume que los datos públicos sean de dominio
público ni que su licencia permita redistribución comercial o adaptación.
