import os
import sys

from PyQt5.QtCore import QSize

sys.path.append(r"E:\repos\GUIS-con-Python-3\Ejercicios")
from Ejercicios.App1.ejemplo_menu3_ui import *
from Ejercicios.recursos.recursos_1_rc import *
from PyQt5.QtWidgets import QMainWindow, QStatusBar, QLabel, QListWidget, QDialog, QFileDialog
from PyQt5.QtGui import *


class MyForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.barra_menus = self.ui.menubar
        self.widget_central = self.ui.centralwidget
        self.barra_estado = self.ui.statusbar
        self.ventana_acoplada = self.ui.dockWidget

        self.dim_widget_central = (0,0)
        self.ventana_acoplada.setWidget(QListWidget())

        self.ui.actionBorrar_la_imagen.triggered.connect(self.borra_imagen)
        self.ui.actionInsertar_la_imagen.triggered.connect(self.saca_imagen)
        self.ui.actionBuscar_imagen.triggered.connect(self.busca_saca_imagen)

    def saca_imagen(self):

        if self.dim_widget_central == (0,0):
            self.dim_widget_central = (self.widget_central.height(),self.widget_central.width())

        mi_imagen = QPixmap(':/Imagenes/Reina_tréboles.jpeg')
        mi_etiqueta = QLabel()
        mi_etiqueta.setAlignment(QtCore.Qt.AlignCenter)
        mi_etiqueta.setPixmap(mi_imagen)
        self.setCentralWidget(mi_etiqueta)
        self.barra_estado.showMessage('La imagen ha sido representada en pantalla')

        miLista = QListWidget()
        miLista.addItem("Altura de la imagen: {} pixeles".format(mi_imagen.height()))
        miLista.addItem("Anchura de la imagen: {} pixeles".format(mi_imagen.width()))
        miLista.addItem("La imagen tiene {} bit por pixel".format(mi_imagen.depth()))
        self.ventana_acoplada.setWidget(miLista)

    def busca_saca_imagen(self):

        if self.dim_widget_central == (0,0):
            self.dim_widget_central = (self.widget_central.height(),self.widget_central.width())
        dialogo_ficheros = QFileDialog(self)
        dialogo_ficheros.setDirectory(r'C:\Users\DavidS\Pictures')
        ruta_mi_fichero = dialogo_ficheros.getOpenFileName()
        if ruta_mi_fichero == ('',''): return
        mi_imagen = QPixmap(ruta_mi_fichero[0])
        mi_etiqueta = QLabel()
        mi_etiqueta.setFixedSize(QSize(self.dim_widget_central[0],self.dim_widget_central[1]))
        mi_etiqueta.setAlignment(QtCore.Qt.AlignCenter)
        mi_etiqueta.setScaledContents(True)
        self.setCentralWidget(mi_etiqueta)
        mi_etiqueta.setPixmap(mi_imagen)

        datos_fichero = os.stat(ruta_mi_fichero[0])
        mi_lista = QListWidget()
        mi_lista.addItem("Altura de la imagen: {} pixeles".format(mi_imagen.height()))
        mi_lista.addItem("Anchura de la imagen: {} pixeles".format(mi_imagen.width()))
        mi_lista.addItem("La imagen tiene {} bit por pixel".format(mi_imagen.depth()))
        mi_lista.addItem("La imagen tiene un tamaño de {:.2f} KB".format(datos_fichero.st_size/1024))

        self.ventana_acoplada.setWidget(mi_lista)

        self.barra_estado.showMessage("La imagen elegida ha sido representada en pantalla", 3000)



    def borra_imagen(self):

        etiqueta_central = self.centralWidget()
        if type(etiqueta_central) == QLabel and etiqueta_central.pixmap() != None:
            etiqueta_central.clear()
            self.barra_estado.showMessage('La imagen ha sido removida de la pantalla')
        else:
            self.barra_estado.showMessage('No hay imagen que eliminar...')
        self.ventana_acoplada.setWidget(QListWidget())



def main():
    app = QtWidgets.QApplication(sys.argv)
    mf = MyForm()
    mf.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()