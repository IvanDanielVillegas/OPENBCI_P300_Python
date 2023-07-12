import sys
import random
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer

# Configuración del teclado virtual
teclado = [['A', 'B', 'C', 'D', 'E'],
           ['F', 'G', 'H', 'I', 'J'],
           ['K', 'L', 'M', 'N', 'Ñ'],
           ['O', 'P', 'Q', 'R', 'S'],
           ['T', 'U', 'V', 'W', 'X'],
           ['Y', 'Z', '.', ',', '-']]

# Clase para la ventana del teclado
class TecladoVirtual(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # Inicializar colores de filas y columnas
        self.colores_filas = [QColor(255, 255, 255), QColor(200, 200, 200)]
        self.colores_columnas = [QColor(255, 255, 255)]

        # Crear botones del teclado
        self.botones = []
        for fila in range(len(teclado)):
            for columna in range(len(teclado[fila])):
                boton = QPushButton(teclado[fila][columna])
                grid.addWidget(boton, fila, columna)
                boton.clicked.connect(self.boton_presionado)
                self.botones.append(boton)
                

        # Cambiar colores de filas y columnas con el tiempo
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_colores)
        self.timer.start(1000)  # Cambiar cada 1000 ms (1 segundo)

        self.setWindowTitle('Teclado Virtual')
        self.show()

    def boton_presionado(self):
        boton = self.sender()
        letra = boton.text()
        print("Letra seleccionada:", letra)
        
    def find(elemento, lista ):
        for i in range(len(lista)):
            if elemento in lista[i]:
                indice = (i, lista[i].index(elemento)) # Devuelve el índice como una tupla
                print(indice)
        return indice

    def actualizar_colores(self):
        # Actualizar los colores de las filas
        self.colores_filas = self.colores_filas[1:] + [self.colores_filas[0]]

        # Actualizar los colores de las columnas
        self.colores_columnas = self.colores_columnas[1:] + [self.colores_columnas[0]]
        
        for i in range(15):
            matriz = [['A', 'B', 'C', 'D', 'E'],
                    ['F', 'G', 'H', 'I', 'J'],
                    ['K', 'L', 'M', 'N', 'Ñ'],
                    ['O', 'P', 'Q', 'R', 'S'],
                    ['T', 'U', 'V', 'W', 'X'],
                    ['Y', 'Z', '.', ',', '-']]  
            while len(matriz) > 0:
                fila = random.choice(matriz)
                while len(fila) > 0:
                    time.sleep(0.1)
                    letra = random.choice(fila)
                    for i in range(len(teclado)):
                        if letra in teclado[i]:
                            row, col = (i, teclado[i].index(letra)) # Devuelve el índice como una tupla
                            indice = row * len(teclado[row]) + col
                            print([row, col])
                            
                    boton = self.botones[indice]
                    boton.setStyleSheet("background-color: rgb(255, 255, 255)")
                    fila.remove(letra)
                    QApplication.processEvents()
                    time.sleep(0.1)
                    boton.setStyleSheet("background-color: rgb(200, 200, 200)")
                    QApplication.processEvents()
                    #print(columna)
                
                matriz.index(fila)
                matriz.remove(fila)

                

        # Actualizar los colores de los botones
        #for fila in range(len(teclado)):
        #    for columna in range(len(teclado[fila])):
        #        indice = fila * len(teclado[fila]) + columna
        #        if indice < len(self.botones):
        #            boton = self.botones[indice]
        #            color_fila = self.colores_filas[fila % len(self.colores_filas)]
        #            color_columna = self.colores_columnas[columna % len(self.colores_columnas)]
        #            color_final = QColor(color_fila.red(), color_columna.green(), color_fila.blue())
        #            boton.setStyleSheet("background-color: " + color_final.name())




# Ejecutar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = TecladoVirtual()
    sys.exit(app.exec_())
