import sys
import random
import time
import asyncio
import threading
import math
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
from time import time, sleep

tic_time = 0

def tic():
    global tic_time
    tic_time = time()

def toc():
    return time() - tic_time

def find(elemento, lista):
        for i in range(len(lista)):
            if elemento in lista[i]:
                indice = (i, lista[i].index(elemento)) # Devuelve el índice como una tupla
                #print(indice)
        return indice


# Clase para la ventana del teclado
class TecladoVirtual(QWidget):
    muestra = 0
    datos = []
    datoMostrado = 100
    # Configuración del teclado virtual
    teclado = [['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'Ñ'],
            ['O', 'P', 'Q', 'R', 'S'],
            ['T', 'U', 'V', 'W', 'X'],
            ['Y', 'Z', '.', ',', '-']]
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # Inicializar colores de filas y columnas
        #self.colores_filas = [QColor(255, 255, 255), QColor(200, 200, 200)]
        #self.colores_columnas = [QColor(255, 255, 255)]

        # Crear botones del teclado
        self.botones = []
        for fila in range(len(self.teclado)):
            for columna in range(len(self.teclado[fila])):
                boton = QPushButton(self.teclado[fila][columna])
                grid.addWidget(boton, fila, columna)
                #boton.clicked.connect(self.boton_presionado)
                boton.setStyleSheet("background-color: rgb(255, 255, 255)")
                self.botones.append(boton) 
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.mostar_lista())
        self.timer.start(1000)
        tic()

        self.setWindowTitle('Teclado Virtual')
        self.show()
        
    def organizar_aleatoria(self):
        elemento = []
        # Organizar aleatoriamente los elementos de la lista
        elementos_aleatorios = [elemento for sublista in self.teclado for elemento in sublista]
        random.shuffle(elementos_aleatorios)

        # Recorrer los elementos sin repetir
        indice = 0
        while indice < len(elementos_aleatorios):
            elemento.append( elementos_aleatorios[indice])
            indice += 1
        return elemento


    def sig_muestra(self, tiempo,frec_muestreo):
        for i in range(math.floor(tiempo*frec_muestreo)):
                    self.datos.append([self.muestra, self.datoMostrado, toc()])
                    self.muestra += 1
                    sleep(1/frec_muestreo)
        
    def encender(self,indice):
        global datoMostrado
        datoMostrado = indice
        boton = self.botones[indice]
        boton.setStyleSheet("background-color: rgb(200, 200, 200)")
        QApplication.processEvents()
        
        

    def apagar(self,indice):
        global datoMostrado
        datoMostrado = indice
        boton = self.botones[indice]
        datoMostrado=100
        boton.setStyleSheet("background-color: rgb(255, 255, 255)")
        QApplication.processEvents()

        
            
    def mostar_lista(self):
        for i in range(15):
            orden = self.organizar_aleatoria()
            print (orden)
            for letra in orden:
                inde = find(letra, self.teclado)
                indice = inde[0] * len(self.teclado[inde[0]]) + inde[1] #row = inde[0]   col = inde[1]
                self.encender(indice)
                self.sig_muestra(0.1,125)
                self.apagar(indice)
                self.sig_muestra(0.1,125)
            print(self.datos)
        self.sig_muestra(1,125)
        




# Ejecutar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = TecladoVirtual()
    sys.exit(app.exec_())
    
    
