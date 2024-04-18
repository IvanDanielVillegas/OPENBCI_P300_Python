import time as tm
import sys
import random
import pygame as p
import random
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
################################################################
turn = 'x'

move = True
won = False
win_control = False
compMove = 5
square_group = p.sprite.Group()
squares = []
startX = 0
startY = 0
endX = 0
endY = 0
background = p.image.load('Background.png')
WIDTH = 500
HEIGHT = 500
background = p.transform.scale(background, (WIDTH, HEIGHT))
winners = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
           [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
board = [' ' for i in range(10)]

dangerPos1 = ['', 'x', '', '', '', 'o', '', '', '', 'x']
dangerPos2 = ['', '', '', 'x', '', 'o', '', 'x', '', '']
dangerPos3 = ['', '', '', 'x', 'x', 'o', '', '', '', '']
dangerPos4 = ['', 'x', '', '', '', 'o', 'x', '', '', '']
dangerPos5 = ['', '', '', '', 'x', 'o', '', '', '', 'x']
dangerPos6 = ['', '', '', '', '', 'o', 'x', 'x', '', '']
dangerPos7 = ['', '', '', '', '', 'o', 'x', '', 'x', '']
dangerPos8 = ['', 'x', '', '', '', 'o', '', '', 'x', '']
dangerPos9 = ['', '', '', 'x', '', 'o', '', '', 'x', '']


################################################################
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
        # self.SPELLER_BUTTON.clicked.connect()
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
    
    
    def CONTROL_TRIQUI_BUTTON(self):
        p.init()
        win = p.display.set_mode((WIDTH, HEIGHT))
        p.display.set_caption('Tic Tac Toe')
        clock = p.time.Clock()
        blank_image = p.image.load('Blank.png').convert_alpha()
        x_image = p.image.load('x.png')
        o_image = p.image.load('o.png')
        illuminated_image = p.image.load('illuminated.png').convert_alpha()

        blank_image = p.transform.scale(blank_image, (120, 120))
        x_image = p.transform.scale(x_image, (120, 120))
        o_image = p.transform.scale(o_image, (120, 120))
        illuminated_image = p.transform.scale(illuminated_image, (120, 120))
        global turn
        class Square(p.sprite.Sprite):
            def __init__(self, x_id, y_id, number):
                super().__init__()
                self.width = 120
                self.height = 120
                self.x = x_id * self.width
                self.y = y_id * self.height
                self.content = ' '
                self.number = number
                self.image = blank_image
                self.image = p.transform.scale(self.image, (self.width, self.height))
                self.rect = self.image.get_rect()
                self.illuminated = False

            def update(self):
                self.rect.center = (self.x, self.y)

            def illuminate(self):
                illuminated_image = p.image.load('illuminated.png').convert_alpha()
                illuminated_image = p.transform.scale(
                illuminated_image, (self.width, self.height))
                self.image.fill((255, 255, 255, 0))
                self.image.blit(illuminated_image, (0, 0))

            def reset(self):
                self.image = blank_image
                self.image = p.transform.scale(self.image, (self.width, self.height))
                self.illuminated = False

            def clicked(self, x_val, y_val):
                global turn, won

                if self.content == ' ':
                    if self.rect.collidepoint(x_val, y_val):
                        self.content = turn
                        board[self.number] = turn

                        if turn == 'x':
                            self.image = x_image
                            self.image = p.transform.scale(
                                self.image, (self.width, self.height))
                            turn = 'o'
                            checkWinner('x')
                            if not won:
                                CompMove()

                        else:
                            self.image = o_image
                            self.image = p.transform.scale(
                                self.image, (self.width, self.height))
                            turn = 'x'
                            checkWinner('o')


        def checkWinner(player):
            global background, won, startX, startY, endX, endY, win_control

            for i in range(8):
                if board[winners[i][0]] == player and board[winners[i][1]] == player and board[winners[i][2]] == player:
                    won = True
                    getPos(winners[i][0], winners[i][2])
                    break

            if won:
                Update()
                drawLine(startX, startY, endX, endY)
                square_group.empty()
                background = p.image.load(player.upper() + ' Wins.png')
                background = p.transform.scale(background, (WIDTH, HEIGHT))
                win_control = True


        def Winner(player):
            global compMove, move

            for i in range(8):
                if board[winners[i][0]] == player and board[winners[i][1]] == player and board[winners[i][2]] == ' ':
                    compMove = winners[i][2]
                    move = False

                elif board[winners[i][0]] == player and board[winners[i][1]] == ' ' and board[winners[i][2]] == player:
                    compMove = winners[i][1]
                    move = False

                elif board[winners[i][0]] == ' ' and board[winners[i][1]] == player and board[winners[i][2]] == player:
                    compMove = winners[i][0]
                    move = False


        def CompMove():
            global move, background, win_control

            move = True

            if move:
                Winner('o')
            if move:
                Winner('x')
            if move:
                checkDangerPos()
            if move:
                checkCentre()

            if move:
                checkCorner()

            if move:
                checkEdge()

            if not move:
                for square in squares:
                    if square.number == compMove:
                        square.clicked(square.x, square.y)

            else:
                Update()
                tm.sleep(1)
                square_group.empty()
                background = p.image.load('Tie Game.png')
                background = p.transform.scale(background, (WIDTH, HEIGHT))
                background = p.transform.scale(background, (WIDTH, HEIGHT))
                win_control = True


        def checkDangerPos():
            global move, compMove

            if board == dangerPos1:
                compMove = 2
                move = False

            elif board == dangerPos2:
                compMove = 4
                move = False

            elif board == dangerPos3:
                compMove = 1
                move = False

            elif board == dangerPos4:
                compMove = 4
                move = False

            elif board == dangerPos5:
                compMove = 7
                move = False

            elif board == dangerPos6:
                compMove = 9
                move = False

            elif board == dangerPos7:
                compMove = 9
                move = False

            elif board == dangerPos8:
                compMove = 7
                move = False

            elif board == dangerPos9:
                compMove = 9
                move = False


        def checkCentre():
            global compMove, move

            if board[5] == ' ':
                compMove = 5
                move = False


        def checkCorner():
            global compMove, move

            for i in range(1, 11, 2):
                if i != 5:
                    if board[i] == ' ':
                        compMove = i
                        move = False
                        break


        def checkEdge():
            global compMove, move

            for i in range(2, 10, 2):
                if board[i] == ' ':
                    compMove = i
                    move = False
                    break


        def getPos(n1, n2):
            global startX, startY, endX, endY

            for sqs in squares:
                if sqs.number == n1:
                    startX = sqs.x
                    startY = sqs.y

                elif sqs.number == n2:
                    endX = sqs.x
                    endY = sqs.y


        def drawLine(x1, y1, x2, y2):
            p.draw.line(win, (0, 0, 0), (x1, y1), (x2, y2), 15)
            p.display.update()
            tm.sleep(2)


        def Update():
            win.blit(background, (0, 0))
            square_group.draw(win)
            square_group.update()
            p.display.update()


        

        
        
        
        num = 1
        for y in range(1, 4):
            for x in range(1, 4):
                sq = Square(x, y, num)
                square_group.add(sq)
                squares.append(sq)
                num += 1

        run = True
        illumination_frequency = 25

        while run:
            clock.tick(illumination_frequency)
            for event in p.event.get():
                if event.type == p.QUIT:
                    #print(win_control)
                    run = False
                    #p.quit()
                if win_control:
                    #print(win_control)
                    tm.sleep(1)
                    run = False
                    #p.quit()
                if event.type == p.MOUSEBUTTONDOWN and turn == 'x':
                    mx, my = p.mouse.get_pos()
                    for s in squares:
                        s.clicked(mx, my)

            non_illuminated_squares = [
                sq for sq in squares if not sq.illuminated and sq.content == ' ']
            if non_illuminated_squares and random.random() < (illumination_frequency / 10):
                random_square = random.choice(non_illuminated_squares)
                random_square.illuminated = True
                random_square.illuminate()
                # Muestra el número del cuadrado iluminado en la consola
                print(f"Cuadrado iluminado: {random_square.number}")
                Update()
                delay_time = round(1000 / illumination_frequency)
                p.time.delay(delay_time)
                random_square.reset()
            
            Update()

        

  

##########################################################################
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec_())
