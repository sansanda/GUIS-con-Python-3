# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\qWebView\QWebView.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1127, 890)
        self.pagina_web = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.pagina_web.setGeometry(QtCore.QRect(40, 80, 1041, 771))
        self.pagina_web.setProperty("url", QtCore.QUrl("https://www.python.org/"))
        self.pagina_web.setObjectName("pagina_web")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 1041, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.direccion = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.direccion.setObjectName("direccion")
        self.horizontalLayout.addWidget(self.direccion)
        self.boton_cargar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.boton_cargar.setObjectName("boton_cargar")
        self.horizontalLayout.addWidget(self.boton_cargar)

        self.retranslateUi(Dialog)
        self.direccion.returnPressed.connect(self.boton_cargar.click)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ejemplo de página web incrustada en aplicación PyQt"))
        self.label.setText(_translate("Dialog", "Dirección: "))
        self.direccion.setText(_translate("Dialog", "https://www.python.org/"))
        self.boton_cargar.setText(_translate("Dialog", "Cargar"))
