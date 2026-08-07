<!-- portada:inicio -->
<div align="center">

# 💻 Aplicación de Windows

**El programa completo en una ventana propia, sin conexión y sin instalar nada: se descomprime y se ejecuta.**

[![clases](https://img.shields.io/badge/clases-352%20embebidas-7c5cff?style=flat-square)](../SYLLABUS.md)
[![formato](https://img.shields.io/badge/formato-portable%20(.zip)-1f6feb?style=flat-square)](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/latest)
[![motor](https://img.shields.io/badge/PySide6-QtWebEngine-41cd52?style=flat-square)](requirements.txt)

[🏠 Inicio](../README.md) ·
[📱 Aplicación de Android](../mobile/README.md) ·
[🌐 Portal](https://vladimiracunadev-create.github.io/finance-and-banking-evolution-program/) ·
[📥 Descargas](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/latest)

</div>
<!-- portada:fin -->

---

## 🎯 Qué es

Un lector de escritorio del programa. Abre el **mismo HTML que publica el portal** en una ventana con su barra de navegación: atrás, adelante, inicio, temario y tamaño de letra.

El material viaja junto al ejecutable, así que funciona sin conexión y sin navegador.

## 📥 Usar

Descarga el `.zip` del [último release](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/latest), descomprímelo donde quieras y ejecuta `FinanzasYBanca.exe`. No hay instalador ni registro del sistema: para desinstalarlo, borra la carpeta.

Verifica la descarga con el `SHA256SUMS.txt` del release:

```bash
sha256sum -c SHA256SUMS.txt --ignore-missing
```

> Windows SmartScreen avisará de un ejecutable sin firmar. El binario se compila en el flujo público [`apps.yml`](../.github/workflows/apps.yml) y su suma de verificación se publica con el release; la firma con certificado quedará para cuando haya uno.

## ⌨️ Atajos

| Atajo | Qué hace |
|---|---|
| `Alt` + `←` / `→` | Atrás y adelante |
| `Ctrl` + `H` | Portada |
| `Ctrl` + `T` | Temario con buscador |
| `Ctrl` + `+` / `-` | Tamaño de letra |

## 🛠️ Ejecutar desde el repositorio

```bash
pip install -r desktop/requirements.txt
```

```bash
python tools/build_site.py
```

```bash
python desktop/programa.py
```

Si el sitio no está generado, la aplicación lo dice al abrirse en vez de mostrar una ventana en blanco.

## 📦 Empaquetar

```bash
pip install pyinstaller
```

```bash
pyinstaller --noconfirm --windowed --name FinanzasYBanca --add-data "site;site" desktop/programa.py
```

> El flujo hace lo mismo y, antes de publicar, **cuenta las clases dentro del paquete**: un ejecutable que arranca puede abrirse vacío si el contenido nunca llegó a copiarse.

<!-- pie:inicio -->
---

<div align="center">

[🏠 Inicio](../README.md) · [📱 Android](../mobile/README.md) · [📚 Programa](../SYLLABUS.md) · [📥 Descargas](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/latest)

</div>
<!-- pie:fin -->
