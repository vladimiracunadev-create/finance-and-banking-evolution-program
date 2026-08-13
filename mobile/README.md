<!-- portada:inicio -->
<div align="center">

# 📱 Aplicación de Android

**Las 356 clases en el teléfono, sin conexión y sin telemetría: el APK no declara permiso de red.**

[![clases](https://img.shields.io/badge/clases-356%20embebidas-7c5cff?style=flat-square)](../SYLLABUS.md)
[![permiso de red](https://img.shields.io/badge/INTERNET-no%20declarado-2e8b57?style=flat-square)](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/blob/main/mobile/app/src/main/AndroidManifest.xml)
[![mínimo](https://img.shields.io/badge/Android-7.0%20o%20superior-3ddc84?style=flat-square)](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/blob/main/mobile/app/build.gradle.kts)

[🏠 Inicio](../README.md) ·
[💻 Aplicación de Windows](../desktop/README.md) ·
[🌐 Portal](https://vladimiracunadev-create.github.io/finance-and-banking-evolution-program/) ·
[📥 Descargas](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/latest)

</div>
<!-- portada:fin -->

---

## 🎯 Qué es

Un lector del programa completo. Muestra el **mismo HTML que publica el portal**, empaquetado dentro del APK: portada, temario con buscador, las 356 clases, los índices de las 23 partes y toda la documentación.

No es un navegador ni un cliente de nada. No descarga contenido, no pide cuenta y no guarda nada fuera del teléfono.

## 🔐 Por qué no declara permiso de red

El [manifiesto](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/blob/main/mobile/app/src/main/AndroidManifest.xml) **no incluye `android.permission.INTERNET`**. Es una decisión, no un olvido: sin ese permiso el sistema operativo impide cualquier conexión, así que «esta aplicación no envía datos» deja de ser una promesa y pasa a ser algo que se puede comprobar desde los ajustes del teléfono.

La consecuencia es que un enlace externo —una fuente oficial, el repositorio— se abre en el navegador del sistema, que sí tiene red.

## 🧩 Cómo funciona

El contenido se sirve con `WebViewAssetLoader` bajo un origen `https://` propio en lugar de `file://`. Con `file://` el motor aplica un origen opaco y bloquea las peticiones relativas entre páginas, que es justo lo que necesita un sitio con enlaces internos.

```text
site/                      generado por tools/build_site.py
  └── se copia a  mobile/app/src/main/assets/site/   (en el flujo, no en git)
        └── se sirve en  https://programa.finanzasbanca.cl/site/...
```

El contenido **no se versiona aquí**: lo copia el flujo desde `site/` antes de compilar, para que el mismo material no viva en dos sitios del repositorio.

## 📥 Instalar

Descarga el APK del [último release](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/latest) y ábrelo en el teléfono. Es una instalación **fuera de Play Store**, así que Android pedirá permitir «orígenes desconocidos» para la aplicación desde la que lo abras.

> El APK va firmado con la **clave de desarrollo de Gradle**, que es lo que lo hace instalable de forma lateral. No es una firma de identidad: no acredita quién lo compiló. Lo que sí acredita el origen es que el binario sale del flujo público [`apps.yml`](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/blob/main/.github/workflows/apps.yml) y que su suma de verificación se publica con el release. Una firma con clave propia llegará cuando haya un almacén de claves que custodiar.

Verifica la descarga con el `SHA256SUMS.txt` del release:

```bash
sha256sum -c SHA256SUMS.txt --ignore-missing
```

## 🛠️ Compilar

Necesitas JDK 17 y el SDK de Android.

```bash
python tools/build_site.py
```

```bash
cp -r site mobile/app/src/main/assets/site
```

```bash
cd mobile && gradle assembleRelease
```

El APK queda en `app/build/outputs/apk/release/`.

> El flujo [`apps.yml`](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/blob/main/.github/workflows/apps.yml) hace exactamente esto y, antes de publicar, **abre el APK y cuenta las clases que hay dentro**: un artefacto que compila puede instalarse vacío si el contenido nunca llegó a empaquetarse.

<!-- pie:inicio -->
---

<div align="center">

[🏠 Inicio](../README.md) · [💻 Windows](../desktop/README.md) · [📚 Programa](../SYLLABUS.md) · [📥 Descargas](https://github.com/vladimiracunadev-create/finance-and-banking-evolution-program/releases/latest)

</div>
<!-- pie:fin -->
