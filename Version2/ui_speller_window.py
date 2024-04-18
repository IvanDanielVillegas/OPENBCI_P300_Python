from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFrame, QGridLayout,QLineEdit
from PyQt5.QtCore import QTimer
from datetime import datetime
from PyQt5.QtCore import Qt
import random
import os.path
from time import sleep
import threading
import Todos_los_datosv2
import SaveData as SD
import speller_casco
import pickle
bandera=False
ronda1=True
iniciar=False
data_casco=[]
board = None
bandera_1=True

teclado = [['A', 'B', 'C', 'D', 'E'],
           ['F', 'G', 'H', 'I', 'J'],
           ['K', 'L', 'M', 'N', 'Ñ'],
           ['O', 'P', 'Q', 'R', 'S'],
           ['T', 'U', 'V', 'W', 'X'],
           ['Y', 'Z', '.', ',', '-'],
           ['0','*']]

muestra = 0
datos = []
gd = []
datoMostrado = 100


def sig_muestra():
    global muestra
    muestra += 1


def espera_inica_grabacion():
    elemento = []
    elementos_aleatorios = [
        elemento for sublista in teclado for elemento in sublista]
    elemento += ['0']*len(elementos_aleatorios)
    return elemento


def organizar_aleatoria():
    elemento = []
    # Organizar aleatoriamente los elementos de la lista
    elementos_aleatorios = [
        elemento for sublista in teclado for elemento in sublista]
    random.shuffle(elementos_aleatorios)
    elementos_aleatorios.remove('0')
    elementos_aleatorios.remove('*')
    elementos_aleatorios.append('0')
    
    return elementos_aleatorios


def find(elemento, lista):
    for i in range(len(lista)):
        if elemento in lista[i]:
            # Devuelve el índice como una tupla
            indice = (i, lista[i].index(elemento))

    return indice




def mostrar_lista():
    global ronda1,iniciar,gd,data_casco,board,bandera
    
    
    for i in range(15):
        if (ronda1 and iniciar):
            orden = espera_inica_grabacion()
            ronda1 = False
        elif (iniciar):
            sleep(1)
            orden = organizar_aleatoria()
        # print(orden)
        for letra in orden:
            inde = find(letra, teclado)
            # row = inde[0]   col = inde[1]
            indice = inde[0] * len(teclado[inde[0]]) + inde[1]
            if letra == '0':
                indice = 30
                
                
                    
            datos.append([sig_muestra(), datoMostrado])
            sleep(0.1)
            encender_apagar(indice, letra)
            #print(bandera)
        bandera=True
        data_casco=board.get_board_data()
        clasificar_datos(data_casco,gd)
        #print(data_casco.shape)
    
        
                
        



def mostrar_lista_ceros():
    for i in range(15):
        orden = organizar_aleatoria()
        for letra in orden:
            letra = "*"
            inde = find(letra, teclado)
            # row = inde[0]   col = inde[1]
            indice = inde[0] * len(teclado[inde[0]]) + inde[1]
            if letra == '*':
                indice = 30
            datos.append([sig_muestra(), datoMostrado])
            sleep(0.1)
            encender_apagar_final(indice, letra)


def encender_apagar(indice, letra):
    global datoMostrado, gd
    datoMostrado = indice
    boton = TecladoVirtual.botones[indice]
    boton.setStyleSheet(
        "background-color: rgb(57, 255, 20); font-size: 20px; font-weight: bold;")
    QApplication.processEvents()
    sleep(0.1)
    # Obtener la marca de tiempo actual
    timestamp_actual = datetime.timestamp(datetime.now())
    datos_dic = letra
    guardar_datos = dict.fromkeys(datos_dic, timestamp_actual)
    gd.append(guardar_datos)
    
    datoMostrado = 100
    boton.setStyleSheet(
        "background-color: rgb(255, 255, 255); font-size: 20px; font-weight: bold;")
    
    QApplication.processEvents()
    


def encender_apagar_final(indice, letra):
    global datoMostrado, gd
    datoMostrado = indice
    boton = TecladoVirtual.botones[indice]
    boton.setStyleSheet(
        "background-color: rgb(255, 255, 255); font-size: 20px; font-weight: bold;")
    QApplication.processEvents()
    sleep(0.1)
    boton.setStyleSheet(
        "background-color: rgb(255, 255, 255); font-size: 20px; font-weight: bold;")
    QApplication.processEvents()


class Ui_MainWindow(object):
    
    grabando=False
    texto_ingresado=""
    def setupUi(self, MainWindow):
        global board
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(839, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QVBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_menu = QFrame(self.frame)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMaximumSize(16777215, 100)
        self.frame_menu.setStyleSheet(u"")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        
        self.horizontalLayout_2 = QVBoxLayout(self.frame_menu)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setAlignment(Qt.AlignCenter)
        self.btn_iniciarfin = QPushButton(self.frame_menu)
        self.btn_iniciarfin.setObjectName(u"btn_iniciarfin")
        self.horizontalLayout_2.addWidget(self.btn_iniciarfin) 
        
        self.text_input = QLineEdit(self.frame_menu)
        self.text_input.setPlaceholderText("       Ingrese aqui la palabra deseada  ")
       
        self.text_input.setClearButtonEnabled(True)
        self.text_input.setObjectName(u"text_input")
        self.text_input.setMaximumWidth(200)
        self.horizontalLayout_2.addWidget(self.text_input)

        self.verticalLayout_2.addWidget(self.frame_menu)
        self.frame_teclado = QFrame(self.frame)
        self.frame_teclado.setObjectName(u"frame_teclado")
        self.frame_teclado.setFrameShape(QFrame.StyledPanel)
        self.frame_teclado.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_teclado)
        self.gridLayout.setObjectName(u"gridLayout")
        board = speller_casco.conf_casco()
        
        

        # Crear el TecladoVirtual
        self.wd_teclado = TecladoVirtual()
        
        

        # Agregar TecladoVirtual al gridLayout
        self.gridLayout.addWidget(self.wd_teclado, 0, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.frame_teclado)

        self.verticalLayout_2.setStretch(0, 2)

        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

    def start_data_acquisition(self):
        global board
        speller_casco.obtenerdatos_casco(board)
    def finish_data_acquisition(self):
        global board
        speller_casco.detenerdatos_casco(board)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("MainWindow")
        self.btn_iniciarfin.setText("INICIAR/FINALIZAR")
        self.btn_iniciarfin.setStyleSheet(
            "background-color: rgb(255, 255, 255); font-size: 15px; font-weight: bold;")
        
         
        # Conectar el botón a la función de inicialización
        self.btn_iniciarfin.clicked.connect(self.iniciar_teclado)
        

        
    def iniciar_teclado(self):
        # Crear y mostrar una instancia de TecladoVirtual
        global ronda1,iniciar,bandera
        ronda1 = True
        
        iniciar=not iniciar
        if not self.grabando:
            self.thread = threading.Thread(target=self.start_data_acquisition)
            if bandera == False:                    
                self.thread.start()
            self.teclado_virtual = TecladoVirtual()
            self.teclado_virtual.iniciar_mostrar_lista()
            self.grabando=True
            self.text_input.setReadOnly(True)
            
        else:
            
            
            #self.grabando=False
            self.finish_data_acquisition()
            mostrar_lista_ceros()
            
         
        

            

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  CODIGO TECLADO XXXXXXXXXXXXXXXXXXXXXXXXXX



class TecladoVirtual(QWidget):
    botones = []
    

    def __init__(self):
        super().__init__()
        # Crear un layout de cuadrícula para organizar los botones
        layout = QGridLayout()

        for fila, fila_botones in enumerate(teclado):
            for columna, texto_boton in enumerate(fila_botones):
                if texto_boton != '0' and texto_boton!='*':  # Verifica si el texto del botón no es '0'
                    boton = QPushButton(texto_boton)
                    boton.setStyleSheet(
                        "background-color: rgb(255, 255, 255); font-size: 20px; font-weight: bold;")
                    boton.setMaximumSize(300, 300)
                    layout.addWidget(boton, fila, columna)
                    TecladoVirtual.botones.append(boton)
        

        # Establecer el layout para el widget TecladoVirtual
        self.setLayout(layout)
        self.setWindowTitle('Teclado Virtual')
        # Inicialmente, no está inicializado
        self.inicializado = False

    def iniciar_mostrar_lista(self):
        global bandera
        # Cambiar colores de filas y columnas con el tiempo
        self.inicializado = True
        self.timer = QTimer(self)
        self.timer.timeout.connect(mostrar_lista)
        self.timer.start(800)  # Cambiar cada 800 ms (0.8 segundos)
       
        #self.show()
       


if __name__ == "__main__":
    import sys
    
    
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow() 
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


