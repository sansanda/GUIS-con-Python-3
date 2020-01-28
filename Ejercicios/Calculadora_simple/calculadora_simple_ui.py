# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculadora_simple.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 383)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(280, 62, 201, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.Number1TE = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Number1TE.setFont(font)
        self.Number1TE.setObjectName("Number1TE")
        self.horizontalLayout.addWidget(self.Number1TE)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(280, 140, 201, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.Number2TE = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Number2TE.setFont(font)
        self.Number2TE.setObjectName("Number2TE")
        self.horizontalLayout_2.addWidget(self.Number2TE)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(200, 210, 361, 81))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.plusPB = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.plusPB.setObjectName("plusPB")
        self.horizontalLayout_3.addWidget(self.plusPB)
        self.minusPB = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.minusPB.setObjectName("minusPB")
        self.horizontalLayout_3.addWidget(self.minusPB)
        self.multiplyPB = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.multiplyPB.setObjectName("multiplyPB")
        self.horizontalLayout_3.addWidget(self.multiplyPB)
        self.dividePB = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.dividePB.setObjectName("dividePB")
        self.horizontalLayout_3.addWidget(self.dividePB)
        self.resultTE = QtWidgets.QTextEdit(self.centralwidget)
        self.resultTE.setGeometry(QtCore.QRect(200, 310, 361, 39))
        self.resultTE.setObjectName("resultTE")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Number 1: "))
        self.label_2.setText(_translate("MainWindow", "Number 2: "))
        self.plusPB.setText(_translate("MainWindow", "+"))
        self.minusPB.setText(_translate("MainWindow", "-"))
        self.multiplyPB.setText(_translate("MainWindow", "*"))
        self.dividePB.setText(_translate("MainWindow", "/"))

import Ejercicios.recursos.recursos_1_rc
