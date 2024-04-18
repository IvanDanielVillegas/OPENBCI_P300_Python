import pygame as p
import random
import time

p.init()


class Square(p.sprite.Sprite):
    def __init__(self, x_id, y_id, number):
        super().__init__()
        self.width = 120
        self.height = 120
        self.x = x_id * self.width
        self.y = y_id * self.height
        self.content = ' '
        self.number = number
        self.image = None
        self.rect = None
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
        self.image = None
        self.illuminated = False

    def clicked(self, x_val, y_val, turn, board, x_image, o_image, checkWinner, CompMove, won):
        if self.content == ' ':
            if self.rect.collidepoint(x_val, y_val):
                self.content = turn
                board[self.number] = turn

                if turn == 'x':
                    self.image = x_image
                    self.image = p.transform.scale(
                        self.image, (self.width, self.height))
                    turn = 'o'
                    checkWinner('x', won)
                    if not won[0]:
                        CompMove(won)

                else:
                    self.image = o_image
                    self.image = p.transform.scale(
                        self.image, (self.width, self.height))
                    turn = 'x'
                    checkWinner('o', won)


class TicTacToeGame:
    def __init__(self):
        self.WIDTH = 500
        self.HEIGHT = 500
        self.win = p.display.set_mode((self.WIDTH, self.HEIGHT))
        p.display.set_caption('Tic Tac Toe')
        self.clock = p.time.Clock()
        self.blank_image = p.image.load('Blank.png').convert_alpha()
        self.x_image = p.image.load('x.png')
        self.o_image = p.image.load('o.png')
        self.background = p.image.load('Background.png')
        self.background = p.transform.scale(
        self.background, (self.WIDTH, self.HEIGHT))
        self.move = True
        self.won = False
        self.win_control = False
        self.compMove = 5
        self.square_group = p.sprite.Group()
        self.squares = []
        self.winners = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                        [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        self.board = [' ' for i in range(10)]
        self.dangerPos1 = ['', 'x', '', '', '', 'o', '', '', '', 'x']
        self.dangerPos2 = ['', '', '', 'x', '', 'o', '', 'x', '', '']
        self.dangerPos3 = ['', '', '', 'x', 'x', 'o', '', '', '', '']
        self.dangerPos4 = ['', 'x', '', '', '', 'o', 'x', '', '', '']
        self.dangerPos5 = ['', '', '', '', 'x', 'o', '', '', '', 'x']
        self.dangerPos6 = ['', '', '', '', '', 'o', 'x', 'x', '', '']
        self.dangerPos7 = ['', '', '', '', '', 'o', 'x', '', 'x', '']
        self.dangerPos8 = ['', 'x', '', '', '', 'o', '', '', 'x', '']
        self.dangerPos9 = ['', '', '', 'x', '', 'o', '', '', 'x', '']
        self.startX = 0
        self.startY = 0
        self.endX = 0
        self.endY = 0
        self.illumination_frequency = 25
        self.turn = 'x'
        self.run = True

    def run_game(self):
        while self.run:
            self.clock.tick(self.illumination_frequency)
            for event in p.event.get():
                if event.type == p.QUIT:
                    self.run = False
                if self.win_control:
                    time.sleep(1)
                    self.run = False
                if event.type == p.MOUSEBUTTONDOWN and self.turn == 'x':
                    mx, my = p.mouse.get_pos()
                    for s in self.squares:
                        s.clicked(
                            mx, my, self.turn, self.board, self.x_image, self.o_image, self.checkWinner, self.CompMove, [self.won])

    def checkWinner(self, player, won):
        for i in range(8):
            if self.board[self.winners[i][0]] == player and self.board[self.winners[i][1]] == player and self.board[self.winners[i][2]] == player:
                won[0] = True
                self.getPos(self.winners[i][0], self.winners[i][2])
                break

        if won[0]:
            self.Update()
            self.drawLine(self.startX, self.startY, self.endX, self.endY)
            self.square_group.empty()
            self.background = p.image.load(player.upper() + ' Wins.png')
            self.background = p.transform.scale(
                self.background, (self.WIDTH, self.HEIGHT))
            self.win_control = True

    def Winner(self, player, won):
        for i in range(8):
            if self.board[self.winners[i][0]] == player and self.board[self.winners[i][1]] == player and self.board[self.winners[i][2]] == ' ':
                self.compMove = self.winners[i][2]
                self.move = False

            elif self.board[self.winners[i][0]] == player and self.board[self.winners[i][1]] == ' ' and self.board[self.winners[i][2]] == player:
                self.compMove = self.winners[i][1]
                self.move = False

            elif self.board[self.winners[i][0]] == ' ' and self.board[self.winners[i][1]] == player and self.board[self.winners[i][2]] == player:
                self.compMove = self.winners[i][0]
                self.move = False

    def CompMove(self, won):
        self.move = True

        if self.move:
            self.Winner('o', won)
        if self.move:
            self.Winner('x', won)
        if self.move:
            self.checkDangerPos()
        if self.move:
            self.checkCentre()

        if self.move:
            self.checkCorner()

        if self.move:
            self.checkEdge()

        if not self.move:
            for square in self.squares:
                if square.number == self.compMove:
                    square.clicked(square.x, square.y, self.turn, self.board,
                                   self.x_image, self.o_image, self.checkWinner, self.CompMove, [self.won])

        else:
            self.Update()
            time.sleep(1)
            self.square_group.empty()
            self.background = p.image.load('Tie Game.png')
            self.background = p.transform.scale(
                self.background, (self.WIDTH, self.HEIGHT))
            self.background = p.transform.scale(
                self.background, (self.WIDTH, self.HEIGHT))
            self.win_control = True

    def checkDangerPos(self):
        if self.board == self.dangerPos1:
            self.compMove = 2
            self.move = False

        elif self.board == self.dangerPos2:
            self.compMove = 4
            self.move = False

        elif self.board == self.dangerPos3:
            self.compMove = 1
            self.move = False

        elif self.board == self.dangerPos4:
            self.compMove = 4
            self.move = False

        elif self.board == self.dangerPos5:
            self.compMove = 7
            self.move = False

        elif self.board == self.dangerPos6:
            self.compMove = 9
            self.move = False

        elif self.board == self.dangerPos7:
            self.compMove = 9
            self.move = False

        elif self.board == self.dangerPos8:
            self.compMove = 7
            self.move = False

        elif self.board == self.dangerPos9:
            self.compMove = 9
            self.move = False

    def checkCentre(self):
        if self.board[5] == ' ':
            self.compMove = 5
            self.move = False

    def checkCorner(self):
        for i in range(1, 11, 2):
            if i != 5:
                if self.board[i] == ' ':
                    self.compMove = i
                    self.move = False
                    break

    def checkEdge(self):
        for i in range(2, 10, 2):
            if self.board[i] == ' ':
                self.compMove = i
                self.move = False
                break

    def getPos(self, n1, n2):
        for sqs in self.squares:
            if sqs.number == n1:
                self.startX = sqs.x
                self.startY = sqs.y

            elif sqs.number == n2:
                self.endX = sqs.x
                self.endY = sqs.y

    def drawLine(self, x1, y1, x2, y2):
        p.draw.line(self.win, (0, 0, 0), (x1, y1), (x2, y2), 15)
        p.display.update()
        time.sleep(2)

    def Update(self):
        self.win.blit(self.background, (0, 0))
        self.square_group.draw(self.win)
        self.square_group.update()
        p.display.update()

    def init_game(self):
        num = 1
        for y in range(1, 4):
            for x in range(1, 4):
                sq = Square(x, y, num)
                self.square_group.add(sq)
                self.squares.append(sq)
                num += 1

        self.arrancar_triqui()

    def arrancar_triqui(self):
        while self.run:
            self.clock.tick(self.illumination_frequency)
            for event in p.event.get():
                if event.type == p.QUIT:
                    self.run = False
            self.run_game()


game = TicTacToeGame()
game.init_game()
