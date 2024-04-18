import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import QRunnable, QThreadPool, pyqtSlot
import time

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Ventana")
        self.setGeometry(100, 100, 300, 200)
        self.etiqueta = QLabel("¡Hola desde la ventana!", self)
        self.etiqueta.setGeometry(50, 50, 200, 30)


   
class MiTarea(QRunnable):
        def __init__(self):
            super().__init__()

        @pyqtSlot()
        def run(self):
            print("Tarea en paralelo iniciada")
            #time.sleep(10)  # Simulación de una tarea que toma tiempo
            for i in range(10):
                 print(i)
                 time.sleep(1)
            print("Tarea en paralelo completada")

if __name__ == "__main__":
        app = QApplication(sys.argv)
        ventana = MiVentana()

        # Crear una instancia de la tarea
        tarea = MiTarea()

        # Agregar la tarea al QThreadPool
        pool = QThreadPool()
        pool.start(tarea)

        ventana.show()
        sys.exit(app.exec_())
