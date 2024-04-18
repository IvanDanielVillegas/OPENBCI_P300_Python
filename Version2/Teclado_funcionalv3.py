import sys
import random
import time
import asyncio
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
from time import time, sleep
from datetime import datetime
import pandas as pd
import csv
import os.path
import threading
import Todos_los_datosv2

gd = []
timestamp_actual=[]
muestra = 0
datos = []
datoMostrado = 100
guardar_datos = []
# Configuración del teclado virtual
teclado = [['A', 'B', 'C', 'D', 'E'],
           ['F', 'G', 'H', 'I', 'J'],
           ['K', 'L', 'M', 'N', 'Ñ'],
           ['O', 'P', 'Q', 'R', 'S'],
           ['T', 'U', 'V', 'W', 'X'],
           ['Y', 'Z', '.', ',', '-'],
           ['0']]


def sig_muestra():
    global muestra
    muestra += 1


def find(elemento, lista):
    for i in range(len(lista)):
        if elemento in lista[i]:
            # Devuelve el índice como una tupla
            indice = (i, lista[i].index(elemento))
        if elemento in lista[i]=='0':
            indice = (i, lista[i].index(elemento))
           
    return indice


def organizar_aleatoria():
    elemento = []
    # Organizar aleatoriamente los elementos de la lista
    elementos_aleatorios = [elemento for sublista in teclado for elemento in sublista]
    random.shuffle(elementos_aleatorios)
    
    indice = 0
    
    elementos_aleatorios.remove('0')
    while indice < len(elementos_aleatorios):
        if elementos_aleatorios!='0':
            elemento.append(elementos_aleatorios[indice])
            indice += 1
         
    elemento.append('0')
    
    print(elemento)
    sleep(3)

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
        # , QColor(200, 200, 200)]
        self.colores_filas = [QColor(255, 255, 255)]
        self.colores_columnas = [QColor(255, 255, 255)]
        # Crear botones del teclado
        self.botones = []
        
        for fila in range(len(teclado)):
            for columna in range(len(teclado[fila-1])):
                boton = QPushButton(teclado[fila-1][columna])
                grid.addWidget(boton, fila-1, columna)
                boton.clicked.connect(self.boton_presionado)
                boton.setStyleSheet("background-color: rgb(255, 255, 255)")
                self.botones.append(boton)
       
        self.thread = threading.Thread(target=self.start_data_acquisition)
        self.thread.start()
       
        self.setWindowTitle('Teclado Virtual')
        
    
    # Cambiar colores de filas y columnas con el tiempo
        self.timer = QTimer()
        self.timer.timeout.connect(self.mostrar_lista)
        self.timer.start(800)  # Cambiar cada 1000 ms (1 segundo)
        self.show()

    def Temp_botones(self):
        # Cambiar colores de filas y columnas con el tiempo
        self.timer = QTimer()
        self.timer.timeout.connect(self.mostrar_lista)
        self.timer.start(1000)  # Cambiar cada 1000 ms (1 segundo)
        self.setWindowTitle('Teclado Virtual')
        self.show()

    def boton_presionado(self):
        boton = self.sender()
        letra = boton.text()
        print("Letra seleccionada:", letra)
   
    def encender_apagar(self, indice,letra):

        datoMostrado = indice
        boton = self.botones[indice]
        boton.setStyleSheet("background-color: rgb(200, 200, 200)")
        QApplication.processEvents()
        sleep(0.1)
        # Obtener la marca de tiempo actual
        timestamp_actual = datetime.timestamp(datetime.now())
        datos_dic = letra
        guardar_datos = dict.fromkeys(datos_dic, timestamp_actual)
        gd.append(guardar_datos)
        #print(gd , indice)
        ruta_archivo = 'teclado_funcionalv2.txt'

        if os.path.exists(ruta_archivo):
            #print('El archivo existe')
            f = open(ruta_archivo, 'a')
            with open(ruta_archivo, 'a') as f:
                for line in gd:
                    f.write(str(gd))
                    f.write(' ')
                    f.write(str(indice))
                    f.write('\n')         
                f.close()
                guardar_datos.clear()
                gd.clear()
        else:
            print('El archivo no existe')
            f = open(ruta_archivo, 'w')
            with open(ruta_archivo, 'w') as f:
                for line in gd:
                    f.write(str(gd))
                    f.write(' ')
                    f.write(str(indice))
                    f.write('\n')
                f.close()
                guardar_datos.clear()
                gd.clear()
        datoMostrado = 100
        boton.setStyleSheet("background-color: rgb(255, 255, 255)")
        QApplication.processEvents()
        
        
    def mostrar_lista(self):

        for i in range(15):
            orden = organizar_aleatoria()
            for letra in orden:
                inde = find(letra, teclado)
                # row = inde[0]   col = inde[1]
                indice = inde[0] * len(teclado[inde[0]]) + inde[1]
                if letra=='0':
                    indice = 30
                datos.append([sig_muestra(), datoMostrado])
                sleep(0.1)
                self.encender_apagar(indice,letra)

    def start_data_acquisition(self):
        Todos_los_datosv2.obtenerdatos_casco(Board_datos)

# Ejecutar la aplicación
if __name__ == '__main__':
  Board_datos = Todos_los_datosv2.conf_casco()
  app = QApplication(sys.argv)
  ventana = TecladoVirtual()
   
  sys.exit(app.exec_())
   
