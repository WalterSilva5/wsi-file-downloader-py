from __future__ import unicode_literals
from PyQt5.QtWidgets import QMainWindow
from view.telaSistema import  Ui_MainWindow
import random, threading, time
from pytube import YouTube
import threading

class ControllerTelaSistema(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.tela = Ui_MainWindow()
        self.tela.setupUi(self)
    
        self.tela.buttonBaixar.clicked.connect(self.baixar)

    def baixar(self):
        self.downloader(self.tela.entradaLinkDeDownload.text())        
    


    def downloader(self, link):
        self.completed = 0

        # creating YouTube object
        musica = YouTube(link, on_progress_callback=self.acrescentarProgresso)
        stream = musica.streams.filter(only_audio=True).first()
        stream.download()

        progredir = threading.Thread(target = self.acrescentarProgresso)
        progredir.daemon = True
        progredir.start()  
    
    def acrescentarProgresso(self,stream, chunk,file_handle, bytes_remaining):
        self.completed+=1
        self.tela.progresso.setValue(self.completed)