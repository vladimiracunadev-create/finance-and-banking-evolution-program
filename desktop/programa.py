"""Lector de escritorio del programa completo.

Muestra las 356 clases —el mismo HTML que publica el portal— en una ventana
propia, sin conexion y sin navegador. El material viaja junto al ejecutable.

Se ejecuta igual desde el repositorio que empaquetado:

    python desktop/programa.py

Requiere PySide6. En el repositorio se instala con:

    pip install -r desktop/requirements.txt
"""

from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtCore import QUrl, Qt
from PySide6.QtGui import QAction, QDesktopServices, QIcon, QKeySequence, QPixmap
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QToolBar

TITULO = "Finance & Banking Evolution Program"
MARCA = "#0969da"


def raiz_del_contenido() -> Path | None:
    """Directorio del sitio, tanto en el repositorio como empaquetado.

    PyInstaller descomprime los datos en `sys._MEIPASS`; ejecutado desde el
    repositorio, el sitio esta en `site/`, que genera `tools/build_site.py`.
    """
    candidatos = []
    empaquetado = getattr(sys, "_MEIPASS", None)
    if empaquetado:
        candidatos.append(Path(empaquetado) / "site")
    aqui = Path(__file__).resolve().parent
    candidatos += [aqui.parent / "site", aqui / "site"]
    for candidato in candidatos:
        if (candidato / "index.html").exists():
            return candidato
    return None


class Pagina(QWebEnginePage):
    """Mantiene la navegacion dentro del contenido local.

    Un enlace a GitHub o a una fuente oficial se abre en el navegador del
    sistema: la ventana es un lector del programa, no un navegador.
    """

    def __init__(self, raiz: Path, padre=None) -> None:
        super().__init__(padre)
        self._raiz = raiz.resolve()

    def acceptNavigationRequest(self, url: QUrl, tipo, es_marco_principal: bool) -> bool:
        if url.isLocalFile():
            try:
                Path(url.toLocalFile()).resolve().relative_to(self._raiz)
                return True
            except ValueError:
                pass
        if url.scheme() in ("http", "https"):
            QDesktopServices.openUrl(url)
            return False
        return True


class Ventana(QMainWindow):
    def __init__(self, raiz: Path) -> None:
        super().__init__()
        self.setWindowTitle(TITULO)
        self.resize(1180, 820)
        self._raiz = raiz

        self.vista = QWebEngineView(self)
        self.vista.setPage(Pagina(raiz, self.vista))
        self.setCentralWidget(self.vista)

        barra = QToolBar("Navegación", self)
        barra.setMovable(False)
        self.addToolBar(barra)

        for texto, atajo, accion in (
            ("← Atrás", QKeySequence.Back, self.vista.back),
            ("Adelante →", QKeySequence.Forward, self.vista.forward),
            ("Inicio", "Ctrl+H", lambda: self._ir("index.html")),
            ("Temario", "Ctrl+T", lambda: self._ir("temario.html")),
        ):
            item = QAction(texto, self)
            item.setShortcut(atajo)
            item.triggered.connect(accion)
            barra.addAction(item)

        barra.addSeparator()
        for texto, atajo, delta in (("A−", "Ctrl+-", -0.1), ("A+", "Ctrl++", 0.1)):
            item = QAction(texto, self)
            item.setShortcut(atajo)
            item.triggered.connect(lambda _=False, d=delta: self._zoom(d))
            barra.addAction(item)

        self.vista.titleChanged.connect(
            lambda t: self.setWindowTitle(f"{t} · {TITULO}" if t else TITULO)
        )
        self._ir("index.html")

    def _ir(self, nombre: str) -> None:
        self.vista.setUrl(QUrl.fromLocalFile(str(self._raiz / nombre)))

    def _zoom(self, delta: float) -> None:
        self.vista.setZoomFactor(min(2.5, max(0.5, self.vista.zoomFactor() + delta)))


def icono() -> QIcon:
    mapa = QPixmap(64, 64)
    mapa.fill(Qt.GlobalColor.transparent)
    return QIcon(mapa)


def main() -> int:
    aplicacion = QApplication(sys.argv)
    aplicacion.setApplicationName(TITULO)
    aplicacion.setWindowIcon(icono())

    raiz = raiz_del_contenido()
    if raiz is None:
        QMessageBox.critical(
            None, TITULO,
            "No se encontró el contenido del programa.\n\n"
            "Desde el repositorio, genéralo antes con:\n"
            "    python tools/build_site.py",
        )
        return 1

    ventana = Ventana(raiz)
    ventana.show()
    return aplicacion.exec()


if __name__ == "__main__":
    raise SystemExit(main())
