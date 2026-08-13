package cl.finanzasbanca.programa

import android.annotation.SuppressLint
import android.content.Intent
import android.net.Uri
import android.os.Bundle
import android.webkit.WebResourceRequest
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.activity.OnBackPressedCallback
import androidx.appcompat.app.AppCompatActivity
import androidx.webkit.WebViewAssetLoader

/**
 * Lector del programa completo.
 *
 * Las 356 clases viajan dentro del APK como HTML ya generado, el mismo que
 * publica el portal. La aplicacion no descarga nada y no necesita conexion:
 * es un visor sobre contenido local.
 *
 * El HTML se sirve por `WebViewAssetLoader` bajo un origen https propio en vez
 * de por `file://`. Con `file://` el navegador aplica un origen opaco y bloquea
 * las peticiones relativas entre paginas; ademas obligaria a habilitar accesos
 * al sistema de archivos que aqui no hacen falta.
 */
class MainActivity : AppCompatActivity() {

    private lateinit var vista: WebView

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(estado: Bundle?) {
        super.onCreate(estado)

        val cargador = WebViewAssetLoader.Builder()
            .setDomain(DOMINIO)
            .addPathHandler("/site/", WebViewAssetLoader.AssetsPathHandler(this))
            .build()

        vista = WebView(this)
        setContentView(vista)

        // El buscador del temario y el renderizado de diagramas necesitan
        // JavaScript. Solo se ejecuta el que viaja en el propio APK.
        vista.settings.javaScriptEnabled = true
        vista.settings.domStorageEnabled = true
        vista.settings.allowFileAccess = false
        vista.settings.allowContentAccess = false
        vista.settings.textZoom = 100

        vista.webViewClient = object : WebViewClient() {
            override fun shouldInterceptRequest(v: WebView, p: WebResourceRequest) =
                cargador.shouldInterceptRequest(p.url)

            /** Lo que no sea contenido local se abre en el navegador del sistema. */
            override fun shouldOverrideUrlLoading(v: WebView, p: WebResourceRequest): Boolean {
                val url = p.url
                if (url.host == DOMINIO) return false
                startActivity(Intent(Intent.ACTION_VIEW, url))
                return true
            }
        }

        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                if (vista.canGoBack()) vista.goBack() else finish()
            }
        })

        if (estado == null) vista.loadUrl(INICIO) else vista.restoreState(estado)
    }

    override fun onSaveInstanceState(estado: Bundle) {
        super.onSaveInstanceState(estado)
        vista.saveState(estado)
    }

    private companion object {
        const val DOMINIO = "programa.finanzasbanca.cl"
        const val INICIO = "https://$DOMINIO/site/index.html"
        val Uri.host: String? get() = this.getHost()
    }
}
