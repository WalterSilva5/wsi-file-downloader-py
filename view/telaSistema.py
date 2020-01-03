# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaSistema.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_janelaPrincipal(object):
    def setupUi(self, janelaPrincipal):
        janelaPrincipal.setObjectName("janelaPrincipal")
        janelaPrincipal.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(janelaPrincipal.sizePolicy().hasHeightForWidth())
        janelaPrincipal.setSizePolicy(sizePolicy)
        janelaPrincipal.setMinimumSize(QtCore.QSize(800, 600))
        janelaPrincipal.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(janelaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.login = QtWidgets.QFrame(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.login.setMinimumSize(QtCore.QSize(800, 600))
        self.login.setMaximumSize(QtCore.QSize(800, 600))
        self.login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login.setObjectName("login")
        self.labelErro = QtWidgets.QLabel(self.login)
        self.labelErro.setGeometry(QtCore.QRect(10, 170, 431, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.labelErro.setFont(font)
        self.labelErro.setStyleSheet("background-color: rgb(85, 85, 255);")
        self.labelErro.setText("")
        self.labelErro.setObjectName("labelErro")
        self.labelNome = QtWidgets.QLabel(self.login)
        self.labelNome.setGeometry(QtCore.QRect(20, 20, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.labelNome.setFont(font)
        self.labelNome.setObjectName("labelNome")
        self.labelSenha = QtWidgets.QLabel(self.login)
        self.labelSenha.setGeometry(QtCore.QRect(20, 100, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.labelSenha.setFont(font)
        self.labelSenha.setObjectName("labelSenha")
        self.relogio = QtWidgets.QLabel(self.login)
        self.relogio.setGeometry(QtCore.QRect(470, 320, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.relogio.setFont(font)
        self.relogio.setObjectName("relogio")
        self.formLayoutWidget = QtWidgets.QWidget(self.login)
        self.formLayoutWidget.setGeometry(QtCore.QRect(170, 20, 521, 141))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.entradaNome = QtWidgets.QTextEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.entradaNome.setFont(font)
        self.entradaNome.setObjectName("entradaNome")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.entradaNome)
        self.entradaSenha = QtWidgets.QTextEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.entradaSenha.setFont(font)
        self.entradaSenha.setObjectName("entradaSenha")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.entradaSenha)
        self.botaoEntrar = QtWidgets.QPushButton(self.login)
        self.botaoEntrar.setGeometry(QtCore.QRect(460, 170, 231, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.botaoEntrar.setFont(font)
        self.botaoEntrar.setObjectName("botaoEntrar")
        janelaPrincipal.setCentralWidget(self.centralwidget)

        self.retranslateUi(janelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(janelaPrincipal)

    def retranslateUi(self, janelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        janelaPrincipal.setWindowTitle(_translate("janelaPrincipal", "Sistema De Debitos"))
        self.labelNome.setText(_translate("janelaPrincipal", "LOGIN"))
        self.labelSenha.setText(_translate("janelaPrincipal", "SENHA"))
        self.relogio.setText(_translate("janelaPrincipal", "00:00:00"))
        self.entradaNome.setHtml(_translate("janelaPrincipal", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:28pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.entradaSenha.setHtml(_translate("janelaPrincipal", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:28pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.botaoEntrar.setText(_translate("janelaPrincipal", "Entrar"))

