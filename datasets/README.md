# Datasets

Todos los conjuntos de datos del repositorio son **sintéticos** y sirven
únicamente para aprendizaje. No representan personas, bancos, tasas ni
comportamientos reales, y **no deben usarse para calibrar ningún modelo que
tome decisiones sobre personas**.

## Organización

```text
datasets/
├── raw/          origen sin transformar, tal como se generó o descargó
├── processed/    derivado de raw, con la transformación documentada
├── synthetic/    generado con semilla fija y patrón conocido
└── schemas/      una ficha por conjunto: diccionario, supuestos y límites
```

Los tres conjuntos históricos (`personal_budget_synthetic.csv`,
`loan_applications_synthetic.csv`, `transactions_synthetic.csv`) permanecen en
la raíz de `datasets/` porque las clases de las Partes 1 a 16 los enlazan por
esa ruta. Sus fichas están en `schemas/`, igual que las de los demás.

## Conjuntos disponibles

| Conjunto | Filas | Ficha | Usado en |
|---|---:|---|---|
| `personal_budget_synthetic.csv` | 84 | [ficha](schemas/personal_budget_synthetic.md) | Partes 1 y 2 |
| `loan_applications_synthetic.csv` | 100 | [ficha](schemas/loan_applications_synthetic.md) | Parte 9, `apps/credit_scoring/` |
| `transactions_synthetic.csv` | 300 | [ficha](schemas/transactions_synthetic.md) | Partes 11 y 14 |
| `synthetic/open_finance_consents.csv` | 1 200 | [ficha](schemas/open_finance_consents.md) | Parte 17, labs 1 y 5 |

## Reglas

1. **Todo CSV tiene ficha.** Un conjunto sin diccionario es un archivo que
   alguien tendrá que adivinar. `tools/validate_datasets.py` lo exige.
2. **Toda columna aparece en la ficha**, con su significado y —cuando importa—
   con la línea «NO significa», que evita la mitad de los errores de integración.
3. **Toda ficha declara sus límites.** Un conjunto presentado sin límites se lee
   como representativo, y ninguno de estos lo es.
4. **Ningún dato personal real.** `tools/detect_pii.py` lo comprueba en CI:
   RUT con dígito verificador válido, tarjetas que pasan Luhn, IBAN y correos
   con dominio real.
5. **Generación reproducible.** Los conjuntos nuevos se generan con semilla
   fija y la semilla se documenta en la ficha.

## Verificación

```bash
python tools/validate_datasets.py
```

```bash
python tools/detect_pii.py
```
