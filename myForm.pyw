import sys

sys.path.append(r"E:\repos\GUIS-con-Python-3\Ejercicios")
from Ejercicios.App1.ejemplo_menu_py import *
from Ejercicios.recursos.recursos_1_rc import *
from PyQt5.QtWidgets import QMainWindow, QStatusBar, QLabel
from PyQt5.QtGui import *


class MyForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.barra_menus = self.menuBar()
        self.widget_central = self.centralWidget()
        self.barra_estado = self.statusBar()
        self.ui.actionBorrar_la_imagen.triggered.connect(self.borra_imagen)
        self.ui.actionInsertar_la_imagen.triggered.connect(self.saca_imagen)

    def borra_imagen(self):
        mi_imagen = QPixmap(':/Imagenes/Reina_tréboles.jpeg')
        mi_etiqueta = QLabel()
        mi_etiqueta.setAlignment(QtCore.Qt.AlignCenter)
        mi_etiqueta.setPixmap(mi_imagen)
        self.centralWidget(mi_etiqueta)
        self.barra_estado.showMessage('La imagen ha sido representada en pantalla')

    def saca_imagen(self):

        etiqueta_central = self.centralWidget()
        if type(etiqueta_central) == QLabel and etiqueta_central.pixmap() != None:
            etiqueta_central.clear()
            self.barra_estado.showMessage('La imagen ha sido removida de la pantalla')
        else:
            self.barra_estado.showMessage('No hay imagen que eliminar...')



def main():
    app = QtGui.QGuiApplication(sys.argv)
    myApp = MyForm()
    myApp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()