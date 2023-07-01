import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QWidget


class AlphabetMatrixWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
        row_count = 5
        column_count = 6

        for i, letter in enumerate(alphabet):
            row = i % row_count
            column = i // row_count
            button = QPushButton(letter)
            if(i=="C"):
                button.setStyleSheet("background-color: #FF0000; font-size: 50px")  # Cambiar el tamaño de las letras
            else:
                button.setStyleSheet("background-color: #000000; font-size: 50px")  # Cambiar el tamaño de las letras
            layout.addWidget(button, row, column)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    alphabet_matrix_widget = AlphabetMatrixWidget()
    window.setCentralWidget(alphabet_matrix_widget)
    window.setWindowTitle('Matriz de letras del abecedario')
    window.setStyleSheet("background-color: #000000")  # Establecer el fondo negro
    window.show()
    sys.exit(app.exec_())
