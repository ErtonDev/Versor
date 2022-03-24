# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

################################################################################
##
## VERSOR - Unit conversor
## Main executable file
## By ErtonDev
## Fundació Llor - Informàtica 4t ESO
##
################################################################################

## MODULES
################################################################################
import sys
import random
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

## CLIENT
################################################################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        ## FRONTEND
        ########################################################################
        # window name
        MainWindow.setObjectName("MainWindow")

        # window icon
        MainWindow.setWindowIcon(QIcon("logoVersor.png"))

        # other window settings
        MainWindow.resize(400, 500)
        MainWindow.setMinimumSize(QtCore.QSize(400, 500))
        MainWindow.setMaximumSize(QtCore.QSize(400, 500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(55, 55, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)

        # widgets
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 80, 361, 401))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(47, 49, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frame.setPalette(palette)
        self.frame.setStyleSheet("QFrame {\n"
"    \n"
"    background-color: #2F3136;\n"
"\n"
"    border-radius: 20px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.glow = QtWidgets.QFrame(self.frame)
        self.glow.setGeometry(QtCore.QRect(10, 10, 341, 381))
        self.glow.setStyleSheet("QFrame {\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(114, 116, 183, 111), stop:1 rgba(255, 255, 255, 0));\n"
"}")
        self.glow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.glow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.glow.setObjectName("glow")
        self.msgLabel = QtWidgets.QLabel(self.glow)
        self.msgLabel.setGeometry(QtCore.QRect(10, 50, 331, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.msgLabel.setFont(font)
        self.msgLabel.setStyleSheet("QLabel {\n"
"    color: rgb(255,255,255);\n"
"    background-color: none;\n"
"}")
        self.msgLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.msgLabel.setObjectName("msgLabel")
        self.valInput = QtWidgets.QLineEdit(self.glow)
        self.valInput.setGeometry(QtCore.QRect(10, 80, 321, 31))
        self.valInput.setStyleSheet("QLineEdit {\n"
"    border-radius: 12px;\n"
"    color: rgb(126, 126, 198);\n"
"    padding: 0 8px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(182, 180, 255);\n"
"}")
        self.valInput.setObjectName("valInput")
        self.fromChoice = QtWidgets.QComboBox(self.glow)
        self.fromChoice.setGeometry(QtCore.QRect(120, 120, 101, 31))
        self.fromChoice.setStyleSheet("QComboBox {\n"
"    color: rgb(126, 126, 198);\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding: 0 10px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(182, 180, 255);\n"
"}\n"
"QComboBox:hover {\n"
"    border-width: 2px;\n"
"    border-style: solid;\n"
"    border-color: rgb(182, 180, 255);\n"
"}\n"
"QComboBox::drop-down {\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-color: rgb(182, 180, 255);\n"
"}\n"
"QComboBox::down-arrow: {\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-color: rgb(182, 180, 255);\n"
"}\n"
"QComboBox::down-arrow:on { \n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.fromChoice.setObjectName("fromChoice")
        self.fromChoice.addItem("")
        self.fromChoice.addItem("")
        self.fromChoice.addItem("")
        self.toChoice = QtWidgets.QComboBox(self.glow)
        self.toChoice.setGeometry(QtCore.QRect(10, 120, 101, 31))
        self.toChoice.setStyleSheet("QComboBox {\n"
"    color: rgb(126, 126, 198);\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding: 0 10px;\n"
"    selection-color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(182, 180, 255);\n"
"}\n"
"QComboBox:hover {\n"
"    border-width: 2px;\n"
"    border-style: solid;\n"
"    border-color: rgb(182, 180, 255);\n"
"}\n"
"QComboBox::drop-down {\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-color: rgb(182, 180, 255);\n"
"}\n"
"QComboBox::down-arrow: {\n"
"    background-color: rgb(255, 255, 255);\n"
"    selection-color: rgb(182, 180, 255);\n"
"}\n"
"QComboBox::down-arrow:on { \n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.toChoice.setObjectName("toChoice")
        self.toChoice.addItem("")
        self.toChoice.addItem("")
        self.toChoice.addItem("")
        self.mainBtn = QtWidgets.QPushButton(self.glow)
        self.mainBtn.setGeometry(QtCore.QRect(230, 120, 101, 31))
        font = QtGui.QFont()
        font.setItalic(True)
        self.mainBtn.setFont(font)
        self.mainBtn.setStyleSheet("QPushButton {\n"
"    color: rgb(126, 126, 198);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    border-color: rgb(182, 180, 255);\n"
"    background-color: rgb(126, 126, 198);\n"
"}\n"
"QPushButton:pressed{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(126, 126, 198);\n"
"}")
        self.mainBtn.setObjectName("mainBtn")
        self.infoLabel = QtWidgets.QLabel(self.glow)
        self.infoLabel.setGeometry(QtCore.QRect(20, 340, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.infoLabel.setFont(font)
        self.infoLabel.setStyleSheet("color: rgba(255, 255, 255, 0.8);\n"
"background-color: none;\n"
"border-radius: 0px;")
        self.infoLabel.setScaledContents(False)
        self.infoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setObjectName("infoLabel")
        self.resultLabel = QtWidgets.QLabel(self.glow)
        self.resultLabel.setGeometry(QtCore.QRect(10, 160, 321, 171))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.resultLabel.setFont(font)
        self.resultLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 116));\n"
"\n"
"color: rgb(255, 255, 255);")
        self.resultLabel.setScaledContents(True)
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultLabel.setWordWrap(True)
        self.resultLabel.setObjectName("resultLabel")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(150, 20, 111, 111))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logoVersor.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.backglow = QtWidgets.QFrame(self.centralwidget)
        self.backglow.setGeometry(QtCore.QRect(10, 10, 381, 481))
        self.backglow.setStyleSheet("QFrame {\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0.00995025, y2:0, stop:0 rgba(111, 112, 175, 119), stop:0.512438 rgba(58, 58, 58, 62), stop:1 rgba(114, 116, 183, 87));\n"
"\n"
"    border-radius: 20px;\n"
"}")
        self.backglow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backglow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backglow.setObjectName("backglow")
        self.vectorName = QtWidgets.QLabel(self.backglow)
        self.vectorName.setGeometry(QtCore.QRect(10, 30, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(66)
        font.setBold(True)
        font.setWeight(75)
        self.vectorName.setFont(font)
        self.vectorName.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: none;")
        self.vectorName.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.vectorName.setAlignment(QtCore.Qt.AlignCenter)
        self.vectorName.setObjectName("vectorName")
        self.backglow.raise_()
        self.frame.raise_()
        self.logo.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.fromChoice.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # btn input
        self.mainBtn.clicked.connect(lambda: self.conversion(self.valInput.text(), self.toChoice.currentText(), self.fromChoice.currentText()))

    ## BACKEND
    ############################################################################
    # main function to convert units
    def conversion(self, userValue, fromUnit, toUnit):

        conversionValues = [1, 1000, 100000]
        x = str(fromUnit)
        y = str(toUnit)

        if userValue != "":

            if x == y:
                toPrint = "You can't\nconvert the\nsame unit!"
            else:
                # for x
                if x == "km":
                    xUnit = conversionValues[0]
                if x == "m":
                    xUnit = conversionValues[1]
                if x == "cm":
                    xUnit = conversionValues[2]
                # for y
                if y == "km":
                    yUnit = conversionValues[0]
                if y == "m":
                    yUnit = conversionValues[1]
                if y == "cm":
                    yUnit = conversionValues[2]

                # factor conversion
                try:
                    operation = float(userValue) * yUnit
                    result = operation / xUnit

                    # convert to int if possible
                    definitive = '%g'%(result)

                    toPrint = str(definitive)
                except ValueError:
                    toPrint = "Use numeric values!"

        else:
            if x == y:
                toPrint = "You can't\nconvert the\nsame unit!"
            else:
                toPrint = "..."

        self.printText(toPrint)

    # adjust text on self.resultLabel depending on its len
    def printText(self, textToPrint):
        if textToPrint != "...":
            if len(textToPrint) <= 10:
                textSize = 41
            elif len(textToPrint) <= 15:
                textSize = 27
            elif len(textToPrint) <= 20:
                textSize = 20
            elif len(textToPrint) <= 25:
                textSize = 15
            elif len(textToPrint) <= 30:
                textSize = 10
            elif textToPrint == "You can't convert the same unit!":
                textSize = 14
            elif textToPrint == "Use numeric values!":
                textSize = 25
            else:
                textSize = 7
        else:
            textSize = 30

        if self.valInput.text() == "":
            if textToPrint == "You can't convert the same unit!":
                textSize = 14
            elif textToPrint == "Use numeric values!":
                textSize = 25
            else:
                textSize = 30
        else:
            textSize = 30

        newFont = QtGui.QFont()
        newFont.setPointSize(textSize)
        newFont.setBold(True)
        newFont.setWeight(75)

        self.resultLabel.setFont(newFont)
        self.resultLabel.setText(textToPrint)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Versor"))
        self.msgLabel.setText(_translate("MainWindow", "Ready to convert?"))
        self.valInput.setPlaceholderText(_translate("MainWindow", "What are you willing to convert?"))
        self.fromChoice.setItemText(0, _translate("MainWindow", "km"))
        self.fromChoice.setItemText(1, _translate("MainWindow", "m"))
        self.fromChoice.setItemText(2, _translate("MainWindow", "cm"))
        self.toChoice.setItemText(0, _translate("MainWindow", "km"))
        self.toChoice.setItemText(1, _translate("MainWindow", "m"))
        self.toChoice.setItemText(2, _translate("MainWindow", "cm"))
        self.mainBtn.setText(_translate("MainWindow", "Convert!"))
        self.infoLabel.setText(_translate("MainWindow", "Versor is an offline free to use unit conversor to make your operations simpler while working on your mathematical problems and helping you to use with different units."))
        self.resultLabel.setText(_translate("MainWindow", "..."))
        self.vectorName.setText(_translate("MainWindow", "VERSOR"))

# main function
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
