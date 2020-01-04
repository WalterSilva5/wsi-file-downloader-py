from __future__ import unicode_literals
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from view.telaSistema import  Ui_MainWindow
import random, threading, time
from pytube import YouTube
import threading
import os

class ControllerTelaSistema(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)

        threading.Thread(target=self.baixar, daemon = True).start()
        self.tela.buttonBaixar.clicked.connect(self.baixar)
        self.tela.buttonSalvarEm.clicked.connect(self.selecionarDestino)

    def selecionarDestino(self):
        self.destino =file = str(QFileDialog.getExistingDirectory(self, "ESCOLHA UM DIRETORIO"))
        if self.destino:
            self.tela.entradaDestino.setText(self.destino)
            self.FolderLocation = self.destino

    def baixar(self):
        self.link = self.tela.entradaLinkDeDownload.text()

        # pytube
        self.musica = YouTube(self.link)

        video_type = self.musica.streams.filter(only_audio = True).first()

        # file size of a file
        self.MaxfileSize = video_type.filesize

        threading.Thread(target=self.musica.register_on_progress_callback(self.show_progress_bar), daemon = True).start()

        # call Download file func
        threading.Thread(target=self.downloadFile, daemon = True).start()



    def downloadFile(self):


        self.musica.streams.filter(only_audio=True).first().download(self.folderLocation)

    # func count precent of a file
    def show_progress_bar(self, stream=None, chunk=None, file_handle=None, bytes_remaining=None):

        # loadingPercent label configure value %
        self.tela.progresso.setValue(int(100 - (100*(bytes_remaining/self.MaxfileSize))))
