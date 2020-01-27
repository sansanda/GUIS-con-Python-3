# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ejemplo_menu.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import Ejercicios.recursos.recursos_1_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 674, 21))
        self.menubar.setObjectName("menubar")
        self.menuInsertar = QtWidgets.QMenu(self.menubar)
        self.menuInsertar.setObjectName("menuInsertar")
        self.menuBorrar = QtWidgets.QMenu(self.menubar)
        self.menuBorrar.setObjectName("menuBorrar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionInsertar_la_imagen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Iconos/Balcón.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInsertar_la_imagen.setIcon(icon)
        self.actionInsertar_la_imagen.setObjectName("actionInsertar_la_imagen")
        self.actionBorrar_la_imagen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Iconos/Compás.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBorrar_la_imagen.setIcon(icon1)
        self.actionBorrar_la_imagen.setObjectName("actionBorrar_la_imagen")
        self.menuInsertar.addAction(self.actionInsertar_la_imagen)
        self.menuBorrar.addAction(self.actionBorrar_la_imagen)
        self.menubar.addAction(self.menuInsertar.menuAction())
        self.menubar.addAction(self.menuBorrar.menuAction())
        self.toolBar.addAction(self.actionInsertar_la_imagen)
        self.toolBar.addAction(self.actionBorrar_la_imagen)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuInsertar.setTitle(_translate("MainWindow", "Insertar"))
        self.menuBorrar.setTitle(_translate("MainWindow", "Borrar"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionInsertar_la_imagen.setText(_translate("MainWindow", "insertar_la_imagen"))
        self.actionBorrar_la_imagen.setText(_translate("MainWindow", "borrar_la_imagen"))

