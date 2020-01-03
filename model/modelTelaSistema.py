from PyQt5.QtCore import QObject
class ModelTelaSistema(QObject):
    @property
    def mensagemErro(self):
        return mensagemErro

    @mensagemErro.setter
    def mensagemErro(self, mensagem):
        self.mensagemErro = mensagem
        