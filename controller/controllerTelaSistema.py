from __future__ import unicode_literals
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QLabel
from view.telaSistema import  Ui_MainWindow
import random, threading, time, getpass
from pytube import YouTube

class ControllerTelaSistema(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)

        self.tela.buttonBaixar.clicked.connect(self.prepararDownload)
        self.tela.buttonSalvarEm.clicked.connect(self.selecionarDestino)
        self.tela.buttonAbrirPastaDeDestino.clicked.connect(self.abrirDestino)

        threading.Thread(target = self.definirBotoes).start()

    def definirBotoes(self):
        self.folderLocation = "C:/Users/{}/Music/".format(getpass.getuser())
        self.tela.entradaDestino.setText(self.folderLocation)
    def prepararDownload(self):
        self.tela.progresso.setValue(0)
        self.baixar()
    def selecionarDestino(self):
        self.destino = str(QFileDialog.getExistingDirectory(self, "ESCOLHA UM DIRETORIO"))
        if self.destino:
            self.tela.entradaDestino.setText(self.destino)
            self.folderLocation = self.destino

    def baixar(self):
        self.link = self.tela.entradaLinkDeDownload.text()
        try:
            self.musica = YouTube(self.link)
        except:
            self.tela.labelErro.setText("OCORREU UM ERRO!")
        else:
            self.video_type = self.musica.streams.filter(only_audio = True).first()
            self.MaxfileSize = self.video_type.filesize
            threading.Thread(self.musica.register_on_progress_callback(self.show_progress_bar)).start()
            threading.Thread(target=self.DownloadFile).start()

    def DownloadFile(self):
        self.musica.streams.filter(only_audio=True).first().download(self.folderLocation)        

    def show_progress_bar(self, stream=None, chunk=None, file_handle=None, bytes_remaining=None):
        self.tela.progresso.setValue(int(100 - (100*(bytes_remaining/self.MaxfileSize))))
        if (int(100 - (100*(bytes_remaining/self.MaxfileSize)))) == 100:
            threading.Thread(self.adicionarAosFinalizados()).start()

    def adicionarAosFinalizados(self):
        """nessa função vou adicionar os downloads finalizados a listagem da tela"""

        self.tela.listagemDeDownloads.addItem(self.musica.title)
        self.tela.labelErro.setText("")
        self.tela.entradaLinkDeDownload.setText("")
        self.tela.progresso.setValue(0)
        
    def abrirDestino(self):
        """abre a atual pasta de destido das musicas baixadas"""
        path = self.tela.entradaDestino.text()
        path = os.path.realpath(path)
        os.startfile(path)
