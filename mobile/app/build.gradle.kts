plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    namespace = "cl.finanzasbanca.programa"
    compileSdk = 35

    defaultConfig {
        applicationId = "cl.finanzasbanca.programa"
        minSdk = 24
        targetSdk = 35
        versionCode = (System.getenv("VERSION_CODE") ?: "1").toInt()
        versionName = System.getenv("VERSION_NAME") ?: "2.1.0"
    }

    buildTypes {
        release {
            // Sin ofuscar: la aplicacion es un lector de contenido propio, no
            // tiene logica que proteger, y el mapa de simbolos solo complicaria
            // depurar un fallo del WebView.
            isMinifyEnabled = false
            isShrinkResources = false
        }
    }

    // El material ya viene comprimido en el APK; volver a comprimir el HTML
    // ahorraria poco y ralentizaria la apertura de cada clase.
    androidResources { noCompress += listOf("pdf") }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions { jvmTarget = "17" }
}

dependencies {
    implementation("androidx.core:core-ktx:1.15.0")
    implementation("androidx.appcompat:appcompat:1.7.0")
    implementation("androidx.activity:activity:1.9.3")
    implementation("androidx.webkit:webkit:1.12.1")
}
