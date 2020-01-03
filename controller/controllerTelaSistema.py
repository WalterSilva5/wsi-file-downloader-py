from PyQt5.QtWidgets import QMainWindow
from view.telaSistema import Ui_janelaPrincipal as Ui_MainWindow
import random, threading, time
from datetime import datetime


class ControllerTelaSistema(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)
        self.tela.botaoEntrar.clicked.connect(self.exibirConteudo)
        contar = threading.Thread(target = self.contarSegundos)
        contar.daemon = True
        contar.start()

    def exibirConteudo(self):
        login = self.tela.entradaNome.toPlainText()
        senha = self.tela.entradaSenha.toPlainText()
        self.tela.labelErro.setText("logado!")

    def contarSegundos(self):
        while True:
            now = datetime.now()
            self.tela.relogio.setText(now.strftime("%H:%M:%S"))
            time.sleep(1)

