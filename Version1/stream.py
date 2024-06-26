import time
import asyncio
import random
import sys
from time import time, sleep
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer


i=0
muestra_funcion=0
muestreo=0.014
muestra = 0
datos = []
datoMostrado = 100
tic_time = 0
def tic():
    global tic_time
    tic_time = time()
def toc():
    return time() - tic_time

teclado = [['A', 'B', 'C', 'D', 'E'],
          ['F', 'G', 'H', 'I', 'J'],
          ['K', 'L', 'M', 'N', 'Ñ'],
           ['O', 'P', 'Q', 'R', 'S'],
           ['T', 'U', 'V', 'W', 'X'],
          ['Y', 'Z', '.', ',', '-']]

def sig_muestra():
    global muestra
    muestra += 1

def find(elemento, lista):
    for i in range(len(lista)):
        if elemento in lista[i]:
            indice = (i, lista[i].index(elemento)) # Devuelve el índice como una tupla
            #print(indice)
    return indice

def organizar_aleatoria():
    elemento = []
    # Organizar aleatoriamente los elementos de la lista
    elementos_aleatorios = [elemento for sublista in teclado for elemento in sublista]
    random.shuffle(elementos_aleatorios)

    # Recorrer los elementos sin repetir
    indice = 0
    while indice < len(elementos_aleatorios):
        elemento.append( elementos_aleatorios[indice])
        indice += 1
    return elemento


# Clase para la ventana del teclado
class TecladoVirtual(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        # Inicializar colores de filas y columnas
        self.colores_filas = [QColor(255, 255, 255)]#, QColor(200, 200, 200)]
        self.colores_columnas = [QColor(255, 255, 255)]
        # Crear botones del teclado
        self.botones = []
        for fila in range(len(teclado)):
            for columna in range(len(teclado[fila])):
                boton = QPushButton(teclado[fila][columna])
                grid.addWidget(boton, fila, columna)
                boton.clicked.connect(self.boton_presionado)
                boton.setStyleSheet("background-color: rgb(255, 255, 255)")
                self.botones.append(boton)
                

        # Cambiar colores de filas y columnas con el tiempo
        self.timer = QTimer()
        self.timer.timeout.connect(self.mostar_lista)
        self.timer.start(1000)  # Cambiar cada 1000 ms (1 segundo)

        self.setWindowTitle('Teclado Virtual')
        self.show()
    def boton_presionado(self):
        boton = self.sender()
        letra = boton.text()
        print("Letra seleccionada:", letra)


    async def encender_apagar(self,indice):
        datoMostrado = indice
        boton = self.botones[indice]
        boton.setStyleSheet("background-color: rgb(200, 200, 200)")
        QApplication.processEvents()
        sleep(0.1)
        datoMostrado=100
        boton.setStyleSheet("background-color: rgb(255, 255, 255)")
        QApplication.processEvents()

    def mostar_lista(self):
        for i in range(15):
            orden = organizar_aleatoria()
            #print (orden)
            for letra in orden:
                inde = find(letra, teclado)
                indice = inde[0] * len(teclado[inde[0]]) + inde[1] #row = inde[0]   col = inde[1]
                #muestra = muestra + 1
                datos.append([sig_muestra(), datoMostrado])
                sleep(0.008)
                #print(teclado.index(letra))
                asyncio.run(self.encender_apagar(indice))
        #print(datos)
    



async def clock():
            task= asyncio.create_task(datos(Ejecutar))
            start = time.monotonic()
            time.sleep(0.014)
            end = time.monotonic()
            await task
            muestra=end-start
            return (muestra_funcion)
valor=clock()           
async def datos(Ejecutar):
        if (Ejecutar):
    #Funcion para guardar los datos
            print(orden) 
            await clock()
        return True

Ejecutar=True    




if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ventana = TecladoVirtual()
    sys.exit(app.exec_())
    #asyncio.run(datos(Ejecutar))
   




