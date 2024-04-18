import sys
import random
import time
import threading
import pygame as p
import random
import time
import Triqui_terminadooo
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer
from time import time, sleep
from datetime import datetime
from ui_mainwindow import Ui_MainWindow
import threading
import Todos_los_datosv2


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('DISEÑO_2.ui', self)
        self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        self.ventana_interfaz = None

        self.MINIMIZAR_BUTTON.clicked.connect(self.CONTROL_MINIMIZAR_BUTTON)
        self.MAXIMIZAR_BUTTON.clicked.connect(self.CONTROL_MAXIMIZAR_BUTTON)
        self.CERRAR_BUTTON.clicked.connect(lambda: self.close())
        self.MENU_BUTTON.clicked.connect(self.mover_menu)
        self.SAVE_DATA_BUTTON.clicked.connect(self.CONTROL_SAVE_DATA_BUTTON)
        self.SPELLER_BUTTON.clicked.connect(self.CONTROL_SPELLER_BUTTON)
        self.TRIQUI_BUTTON.clicked.connect(self.CONTROL_TRIQUI_BUTTON)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

    def CONTROL_MINIMIZAR_BUTTON(self):
        self.showMinimized()

    def CONTROL_MAXIMIZAR_BUTTON(self):
        if True:
            self.showMaximized()
            # self.showNormal()
            # cont+=1
            # if cont==2 :
            # self.showNormal()
            # cont=0

    def mover_menu(self):
        if True:
            width = self.frame_menu.width()
            normal = 0
            if width == 0:
                extender = 200
                # self.MENU_BUTTON.hide()
            else:
                self.MENU_BUTTON.show()
                extender = normal
            self.animacion = QPropertyAnimation(
                self.frame_menu, b"maximumWidth")
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setDuration(50)
            self.animacion.setEasingCurve(QEasingCurve.OutInBack)
            self.animacion.start()

    def CONTROL_SAVE_DATA_BUTTON(self):
        if self.ventana_interfaz is None:
            self.ventana_interfaz = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.ventana_interfaz)
            # Mostrar la ventana de la interfaz

            self.ventana_interfaz.show()
    
    def CONTROL_SPELLER_BUTTON(self):
        print("")
    
    def CONTROL_TRIQUI_BUTTON(self):

        Triqui_terminadooo.arrancar_triqui(True)
        






  

##########################################################################
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec_())
