# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaSistema.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(725, 525)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelLink = QtWidgets.QLabel(self.centralwidget)
        self.labelLink.setGeometry(QtCore.QRect(50, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelLink.setFont(font)
        self.labelLink.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.labelLink.setObjectName("labelLink")
        self.entradaLinkDeDownload = QtWidgets.QLineEdit(self.centralwidget)
        self.entradaLinkDeDownload.setGeometry(QtCore.QRect(140, 20, 471, 31))
        self.entradaLinkDeDownload.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border-radius: 5px;")
        self.entradaLinkDeDownload.setObjectName("entradaLinkDeDownload")
        self.buttonBaixar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonBaixar.setGeometry(QtCore.QRect(620, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buttonBaixar.setFont(font)
        self.buttonBaixar.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: white;\n"
"border-radius: 5px;")
        self.buttonBaixar.setObjectName("buttonBaixar")
        self.buttonRemover = QtWidgets.QPushButton(self.centralwidget)
        self.buttonRemover.setGeometry(QtCore.QRect(20, 100, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buttonRemover.setFont(font)
        self.buttonRemover.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: white;\n"
"border-radius: 5px;")
        self.buttonRemover.setObjectName("buttonRemover")
        self.frameListagemDeDownloads = QtWidgets.QFrame(self.centralwidget)
        self.frameListagemDeDownloads.setGeometry(QtCore.QRect(10, 210, 701, 311))
        self.frameListagemDeDownloads.setStyleSheet("background-color: rgb(61, 61, 61);")
        self.frameListagemDeDownloads.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameListagemDeDownloads.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameListagemDeDownloads.setObjectName("frameListagemDeDownloads")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frameListagemDeDownloads)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 701, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.ListarDownloads = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.ListarDownloads.setContentsMargins(0, 0, 0, 0)
        self.ListarDownloads.setObjectName("ListarDownloads")
        self.labelLink_2 = QtWidgets.QLabel(self.centralwidget)
        self.labelLink_2.setGeometry(QtCore.QRect(270, 180, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelLink_2.setFont(font)
        self.labelLink_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.labelLink_2.setObjectName("labelLink_2")
        self.progresso = QtWidgets.QProgressBar(self.centralwidget)
        self.progresso.setGeometry(QtCore.QRect(270, 140, 471, 31))
        self.progresso.setProperty("value", 0)
        self.progresso.setObjectName("progresso")
        self.labelLink_3 = QtWidgets.QLabel(self.centralwidget)
        self.labelLink_3.setGeometry(QtCore.QRect(20, 140, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.labelLink_3.setFont(font)
        self.labelLink_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.labelLink_3.setObjectName("labelLink_3")
        self.buttonSalvarEm = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSalvarEm.setGeometry(QtCore.QRect(20, 60, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.buttonSalvarEm.setFont(font)
        self.buttonSalvarEm.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"color: white;\n"
"border-radius: 5px;")
        self.buttonSalvarEm.setObjectName("buttonSalvarEm")
        self.entradaDestino = QtWidgets.QLineEdit(self.centralwidget)
        self.entradaDestino.setGeometry(QtCore.QRect(140, 60, 471, 31))
        self.entradaDestino.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color:black;\n"
"border-radius: 5px;")
        self.entradaDestino.setObjectName("entradaDestino")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sertec Video Downloader"))
        self.labelLink.setText(_translate("MainWindow", "LINK"))
        self.buttonBaixar.setText(_translate("MainWindow", "BAIXAR"))
        self.buttonRemover.setText(_translate("MainWindow", "REMOVER"))
        self.labelLink_2.setText(_translate("MainWindow", "DOWNLOADS"))
        self.labelLink_3.setText(_translate("MainWindow", "PROGRESSO ATUAL"))
        self.buttonSalvarEm.setText(_translate("MainWindow", "SALVAR EM"))
