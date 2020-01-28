# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\GetPhones\FichaPersona.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FichaPersona(object):
    def setupUi(self, FichaPersona):
        FichaPersona.setObjectName("FichaPersona")
        FichaPersona.resize(330, 175)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FichaPersona.sizePolicy().hasHeightForWidth())
        FichaPersona.setSizePolicy(sizePolicy)
        FichaPersona.setMinimumSize(QtCore.QSize(300, 150))
        self.personDataLW = QtWidgets.QListWidget(FichaPersona)
        self.personDataLW.setGeometry(QtCore.QRect(170, 10, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.personDataLW.sizePolicy().hasHeightForWidth())
        self.personDataLW.setSizePolicy(sizePolicy)
        self.personDataLW.setMinimumSize(QtCore.QSize(100, 150))
        self.personDataLW.setObjectName("personDataLW")
        self.personPhotoL = QtWidgets.QLabel(FichaPersona)
        self.personPhotoL.setGeometry(QtCore.QRect(10, 10, 150, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.personPhotoL.sizePolicy().hasHeightForWidth())
        self.personPhotoL.setSizePolicy(sizePolicy)
        self.personPhotoL.setMinimumSize(QtCore.QSize(100, 150))
        self.personPhotoL.setFrameShape(QtWidgets.QFrame.Box)
        self.personPhotoL.setMidLineWidth(1)
        self.personPhotoL.setText("")
        self.personPhotoL.setObjectName("personPhotoL")

        self.retranslateUi(FichaPersona)
        QtCore.QMetaObject.connectSlotsByName(FichaPersona)

    def retranslateUi(self, FichaPersona):
        _translate = QtCore.QCoreApplication.translate
        FichaPersona.setWindowTitle(_translate("FichaPersona", "Ficha Persona"))
