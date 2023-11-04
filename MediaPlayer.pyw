import sys
import os
import time
import threading
import pygame
from mutagen.mp3 import MP3
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QProgressBar, QWidget, QGridLayout, QSlider
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QIcon

def limpar():
    os.system("cls")
pygame.init()


class App(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
       #self.grid = QGridLayout(self.cw)
        #self.setCentralWidget(self.cw)
        self.resize(300, 300)
        
        #botões
        self.pause = QPushButton(self)#este botão não quer aparecer
        self.pause.setText("Play/Pause")
        self.pause.setStyleSheet('font-size: 40px;')
        #self.grid.addWidget(self.pause, 0, 1, 1, 1)
        self.pause.setGeometry(0, 0, 200, 60)
        #self.pause.setGeometry(pixel_x, pixel_y, largura, altura)
        #self.teste = QPushButton('Posição')
        #self.teste.setStyleSheet('font-size: 20px;')
        
        #açoes dos botões
        self.pause.clicked.connect(self.pause_unpause)
        #self.bt.clicked.connect(self.testes_duracao)
        #self.grid.addWidget(self.teste, 0, 1, 1, 1)
        
        #barra de progresso
        self.progressao = QSlider(self)
        self.progressao.setOrientation(Qt.Horizontal)
        self.progressao.setGeometry(0, 60, 200, 10)
        self.progressao.setRange(0, 100)
        self.progressao.setSingleStep(1)
        self.progressao.setStyleSheet("QSlider::groove:horizontal { background: #dddddd; height: 10px; } QSlider::handle:horizontal { background: green; width: 15px; margin: -4px 0; border-radius: 7px; } QSlider::sub-page:horizontal { background: #00cc00; }")
        self.progressao.setValue(0)
        self.progressao.valueChanged.connect(self.set_posicao)
        #self.progressao.sliderPressed.connect(self.get_posicao)
        #self.progressao.sliderPressed.connect(self.get_posicao)
        #self.progressao.sliderReleased.connect(self.get_posicao)
        self.__progressaoPrecionada=None
        #self.grid.addWidget(self.progressao, 1, 1, 1, 1)
        
        #iniciando a música
        self.musica="Three Days Grace - I Hate Everything About You (Of.mp3"
        pygame.mixer.music.load(self.musica)
        pygame.mixer.music.play()
        pygame.mixer.music.pause()
        self.__play=False

        #duracao
        audio=MP3(self.musica)
        audio=int(audio.info.length)
        #self.__minutos=audio//60
        #self.__segundos=audio%60
        self.__total=audio

        
        #uso futuro
        self.percentual=0
        #serve para definir quanto tempo a thread vai dormir

        self.sleep=self.__total//100
        #print(f"Duração   {self.__minutos}:{self.__segundos}")

    
    #calcula o progresso da musica
    def progress_update(self):
        while self.__play:
            time.sleep(self.sleep)
            self.progressao.blockSignals(True)
            self.progressao.setValue(self.progressao.value()+1)
            self.progressao.blockSignals(False)
            if self.percentual == 100:
                print('Música encerrada')
                break
            """permite que o processo só execulte quando a barra precisar
            se mover, permitindo que possa ser usado a
            barra durante a reprodução"""
            
        else:
            print('Pausado e Thread encerrada')
        
    #acao de pause e unpause funcionando
    def pause_unpause(self):
        self.__play=not(self.__play)
        if self.__play!=True:
            pygame.mixer.music.pause()
        else:
            self.t=threading.Thread(target=self.progress_update)
            self.t.start()
            pygame.mixer.music.unpause()
        
    def set_posicao(self):
        if not pygame.mixer.music.get_busy():
            self.__play=False
            self.pause_unpause()
            print("Música despausada pela barra")
        pygame.mixer.music.set_pos(self.sleep*self.progressao.value())
    
    #teste para ver duração do áudio      
    '''def testes_duracao(self):
        limpar()
        print(f"Duração  {self.__minutos}:{self.__segundos}")
        #pygame.mixer.music.fadeout()
        posicao=pygame.mixer.music.get_pos()//1000
        percential=int((posicao/self.__total)*100)
        print(f'{posicao}s')
        print(f"posicao relativa:{percential}%")
        #print(pygame.mixer.music.get_busy())'''
        
 

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.setFixedSize(210, 200)
    app.setWindowIcon(QIcon("icone.png"))
    app.show()
    qt.exec_()
    
