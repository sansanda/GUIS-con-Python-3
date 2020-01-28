import sys

sys.path.append(r"E:\repos\GUIS-con-Python-3\Ejercicios")
from Ejercicios.Calculadora_simple.calculadora_simple_ui import *
from Ejercicios.recursos.recursos_1_rc import *
from PyQt5.QtWidgets import QMainWindow, QStatusBar, QLabel
from PyQt5.QtGui import *


class MyForm(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Number1TE.setText('0.0')
        self.ui.Number2TE.setText('0.0')
        self.n1 = float(self.ui.Number1TE.toPlainText())
        self.n2 = float(self.ui.Number2TE.toPlainText())
        self.ui.resultTE.setText('Text will be displayed here when click one of the four buttons')


        self.ui.plusPB.released.connect(self.calculatePlus)
        self.ui.minusPB.released.connect(self.calculateMinus)
        self.ui.multiplyPB.released.connect(self.calculateProduct)
        self.ui.dividePB.released.connect(self.calculateDivision)


    def calculatePlus(self):

        try:
            self.testTextEditText()
            result = self.n1 + self.n2
        except ValueError:
            self.ui.resultTE.setText('Text must follow float format. Try again.')
            return

        self.ui.resultTE.setText('The result of the operation is {}'.format(str(result)))

    def calculateMinus(self):
        try:
            self.testTextEditText()
            result = self.n1 - self.n2
        except ValueError:
            self.ui.resultTE.setText('Text must follow float format. Try again.')
            return

        self.ui.resultTE.setText('The result of the operation is {}'.format(str(result)))

    def calculateProduct(self):
        try:
            self.testTextEditText()
            result = self.n1 * self.n2
        except ValueError:
            self.ui.resultTE.setText('Text must follow float format. Try again.')
            return

        self.ui.resultTE.setText('The result of the operation is {}'.format(str(result)))

    def calculateDivision(self):
        try:
            self.testTextEditText()
            result = self.n1 / self.n2
        except ValueError:
            self.ui.resultTE.setText('Text must follow float format. Try again.')
            return
        except ZeroDivisionError:
            self.ui.resultTE.setText('Number 2 can\'t be zero')
            return

        self.ui.resultTE.setText('The result of the operation is {}'.format(str(result)))

    def testTextEditText(self):
        try:
            self.n1 = float(self.ui.Number1TE.toPlainText())
            self.n2 = float(self.ui.Number2TE.toPlainText())
        except ValueError:
            raise ValueError


def main():
    app = QtWidgets.QApplication(sys.argv)
    mf = MyForm()
    mf.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()