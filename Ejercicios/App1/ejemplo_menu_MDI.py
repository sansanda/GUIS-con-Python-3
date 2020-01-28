import os
import sys

from PyQt5.QtCore import QSize

sys.path.append(r"E:\repos\GUIS-con-Python-3\Ejercicios")
from Ejercicios.App1.ejemplo_MDI_ui import *
from Ejercicios.recursos.recursos_1_rc import *
from PyQt5.QtWidgets import QMainWindow, QStatusBar, QLabel, QListWidget, QDialog, QFileDialog, QAction, QMdiSubWindow, \
    QTextEdit, QDesktopWidget
from PyQt5.QtGui import *


class Ventana_Principal(QMainWindow):
    def __init__(self, parent=None):

        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.num_ventanas = 0
        self.setWindowTitle('Ejemplo de aplicacio MDI')
        self.setGeometry(0,0,800,600)
        self.centraEnPantalla()

        self.central_widget = self.ui.centralwidget
        self.mdi_area = self.ui.mdiArea
        self.menu_bar = self.ui.menubar

        self.menu_bar.triggered[QAction].connect(self.maneja_acciones)

    def maneja_acciones(self, mi_accion):
        if (mi_accion.text()=='Nueva Ventana'):
            self.num_ventanas += 1
            subventana = QMdiSubWindow()
            subventana.setWidget(QTextEdit())
            subventana.setWindowTitle('Subventana nº {}'.format(self.num_ventanas))
            self.mdi_area.addSubWindow(subventana)
            subventana.show()
            return
        if (mi_accion.text()=='Distribuir Cascada'):
            self.mdi_area.cascadeSubWindows()
        if (mi_accion.text()=='Distribuir Mosaico'):
            self.mdi_area.tileSubWindows()

    def centraEnPantalla(self):
        resolucion_pantalla = QDesktopWidget().screenGeometry()
        self.move(int(resolucion_pantalla.width()/2 - self.frameSize().width()/2),int(resolucion_pantalla.height()/2 - self.frameSize().height()/2))




def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = Ventana_Principal()
    mw.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()