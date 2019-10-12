from MathAppStubCode import *
import sys
import time

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

class MathAppRun(Ui_MainWindow):

    def __init__(self, window):

        self.operations = []
        self.numbers = []
        self.bases = []

        self.setupUi(window)

        self.menubar.setNativeMenuBar(False)
        self.swap_button.clicked.connect(self.swap)
        self.reset_button.clicked.connect(self.reset)
        self.bc_clear.clicked.connect(self.clear)
        self.bo_clear.clicked.connect(self.clear)
        self.convert_button.clicked.connect(self.convert)

        self.bo_add.clicked.connect(self.add_button)
        self.bo_minus.clicked.connect(self.minus_button)
        self.bo_mult.clicked.connect(self.mult_button)
        self.bo_divide.clicked.connect(self.divide_button)
        self.bo_equal.clicked.connect(self.equal_button)

        self.calculate1.clicked.connect(self.crossProduct)

    def crossProduct(self):
        list1 = [int(self.x1.text()), int(self.y1.text()), int(self.z1.text())]
        list2 = [int(self.x2.text()), int(self.y2.text()), int(self.z2.text())]
        crossProduct = []
        num1 = 0
        num2 = 0
        num3 = 0
        if isinstance(list1 or list2, (list)):
            if len(list1) != 3 or len(list2) != 3:
                return ("it is not possible to take the cross product of your vectors")
            else:
                num1 = list1[1] * list2[2] - list1[2] * list2[1]
                num2 = list1[2] * list2[0] - list1[0] * list2[2]
                num3 = list1[0] * list2[1] - list1[1] * list2[0]
                crossProduct.append(num1)
                crossProduct.append(num2)
                crossProduct.append(num3)

        else:
            return ("error, one or more of your entries is not a list")
        self.output1.setText(str(crossProduct))

    def dotProduct(list1, list2):
        import math
        i = 0
        num1 = 0
        num2 = 0
        product = 0
        if isinstance(list1 or list2, (list)):
            if len(list1) != len(list2):
                return ("it is not possible to take the dot product of your vectors")
            else:
                while i < len(list1):
                    num1 = list1[i]
                    num2 = list2[i]
                    product += num1 * num2
                    i += 1
        else:
            return ("error, one or more of your entries is not a list")
        return product

    def convert(self):
        if self.bc_to_base.currentIndex() == 0 or self.bc_from_base.currentIndex() == 0 or self.bc_number.text() == '0':
            QtWidgets.QMessageBox.warning(None, "Parameters", "Some or all of the parameters " +
                                          "do not have assigned values. Please assign them in the given fields."
                                          , QtWidgets.QMessageBox.Ok)
        baseFrom = int (self.bc_from_base.currentText())
        baseTo = int (self.bc_to_base.currentText())
        number = self.bc_number.text()

        numToAlpha = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H',
                        18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P',
                        26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}
        stringed = str(number)
        decRes = int(stringed, baseFrom)
        highExpo = 0
        while baseTo ** highExpo <= decRes:
            highExpo += 1
        listRes = []
        for exp in reversed(range(0, highExpo)):
            curCoef = 1
            if (baseTo ** exp <= decRes):
                while (curCoef * baseTo ** exp <= decRes):
                    curCoef += 1
                curCoef -= 1
                decRes -= curCoef * baseTo ** exp
                if curCoef >= 10:
                    curCoef = numToAlpha[curCoef]
                listRes.append(str(curCoef))
            else:
                listRes.append('0')
        strRes = ''
        for w in listRes:
            strRes += w
        self.bc_result.setText(strRes)

    def swap(self):
        index = self.bc_from_base.currentIndex()
        self.bc_from_base.setCurrentIndex(self.bc_to_base.currentIndex())
        self.bc_to_base.setCurrentIndex(index)

    def reset(self):
        self.bc_to_base.setCurrentIndex(0)
        self.bc_from_base.setCurrentIndex(0)

    def clear(self):
        self.bc_result.clear()
        self.bo_result.clear()

    def add_button(self):
        if self.statusbar.currentMessage() == '':
            self.numbers.append(self.bo_number.text())
            self.bases.append(int(self.bo_from_base.currentText()))
            self.statusbar.showMessage(self.bo_number.text() + '')
        elif self.bo_number.text() != '': # and satisfies condition of being under base
            self.statusbar.showMessage(self.statusbar.currentMessage() + '+' + self.bo_number.text())
            self.operations.append('+')
            self.numbers.append(self.bo_number.text())
            self.bases.append(int(self.bo_from_base.currentText()))

    def minus_button(self):
        if self.statusbar.currentMessage() == '':
            self.numbers.append(self.bo_number.text())
            self.bases.append(int(self.bo_from_base.currentText()))
            self.statusbar.showMessage(self.bo_number.text() + '')
        elif self.bo_number.text() != '':  # and satisfies condition of being under base
            self.statusbar.showMessage(self.statusbar.currentMessage() + '-' + self.bo_number.text())
            self.operations.append('-')
            self.numbers.append(self.bo_number.text())
            self.bases.append(int(self.bo_from_base.currentText()))

    def mult_button(self):
        if self.statusbar.currentMessage() == '':
            self.statusbar.showMessage(self.bo_number.text() + '')
            self.bases.append(int(self.bo_from_base.currentText()))
            self.numbers.append(self.bo_number.text())
        elif self.bo_number.text() != '':  # and satisfies condition of being under base
            self.statusbar.showMessage(self.statusbar.currentMessage() + '×' + self.bo_number.text())
            self.operations.append('×')
            self.numbers.append(self.bo_number.text())
            self.bases.append(int(self.bo_from_base.currentText()))

    def divide_button(self):
        if self.statusbar.currentMessage() == '':
            self.statusbar.showMessage(self.bo_number.text() + '')
            self.bases.append(int(self.bo_from_base.currentText()))
            self.numbers.append(self.bo_number.text())
        elif self.bo_number.text() != '':  # and satisfies condition of being under base
            self.statusbar.showMessage(self.statusbar.currentMessage() + '÷' + self.bo_number.text())
            self.operations.append('÷')
            self.numbers.append(self.bo_number.text())
            self.bases.append(int(self.bo_from_base.currentText()))

    def equal_button(self):
        if not (len(self.numbers) == len(self.operations) + 1 == len(self.bases)):
            self.statusbar.showMessage('Base(s) not specified')
            self.numbers = []
            self.operations = []
            self.bases = []
            self.statusbar.showMessage('')
            return
        print(self.numbers)
        print(self.operations)
        print(self.bases)
        self.bo_result.setText(self.statusbar.currentMessage() + ' = ' + self.calculate(self.numbers, self.operations, self.bases, int(self.bo_to_base.currentText())))
        self.statusbar.showMessage('')

        self.numbers = []
        self.operations = []
        self.bases = []

    def convertParam(self, baseFrom, baseTo, number):
        # note: this function does not check that the number is valid in the given base
        # note2: baseFrom and BaseTo must be within the inclusive range [2, 36]
        alphaToNum = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17,
                      'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25,
                      'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35}
        numToAlpha = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H',
                      18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P',
                      26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z'}
        stringed = str(number)
        decRes = int(stringed, baseFrom)
        highExpo = 0
        while baseTo ** highExpo <= decRes:
            highExpo += 1
        listRes = []
        for exp in reversed(range(0, highExpo)):
            curCoef = 1
            if (baseTo ** exp <= decRes):
                while (curCoef * baseTo ** exp <= decRes):
                    curCoef += 1
                curCoef -= 1
                decRes -= curCoef * baseTo ** exp
                if curCoef >= 10:
                    curCoef = numToAlpha[curCoef]
                listRes.append(str(curCoef))
            else:
                listRes.append('0')
        strRes = ''
        for w in listRes:
            strRes += w
        return strRes

    def calculate(self, numbers, operations, bases, baseRes):
        # all parameters must be lists, and len(numbers) == len(bases) == len(operations) + 1 must be true
        for i in range(0, len(numbers)):
            numbers[i] = int(self.convertParam(bases[i], 10, numbers[i]))
        ops_left = True
        while ops_left:
            ops_left = False
            for i in range(0, len(operations)):
                if (operations[i] == '×'):
                    numbers[i] = numbers[i] * numbers[i + 1]
                    del numbers[i + 1]
                    del operations[i]
                    ops_left = True
                    break
                if (operations[i] == '÷'):
                    numbers[i] = numbers[i] / numbers[i + 1]
                    del numbers[i + 1]
                    del operations[i]
                    ops_left = True
                    break
        while len(operations) > 0:
            for i in range(0, len(operations)):
                if (operations[i] == '-'):
                    numbers[i] = numbers[i] - numbers[i + 1]
                    del numbers[i + 1]
                    del operations[i]
                    break
                if (operations[i] == '+'):
                    numbers[i] = numbers[i] + numbers[i + 1]
                    del numbers[i + 1]
                    del operations[i]
                    break
        return self.convertParam(10, baseRes, int(numbers[0] + .5))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MathAppRun(MainWindow)
    MainWindow.show()
    app.exec_()
    print(operations)
    print(numbers)