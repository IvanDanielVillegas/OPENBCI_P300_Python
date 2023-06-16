
import argparse
import time
import brainflow.board_shim


from brainflow.board_shim import BoardShim, BrainFlowInputParams,BoardIds,LogLevels
from brainflow.data_filter import DataFilter, WindowOperations, WaveletTypes
from datetime import datetime
import tkinter as tk
INTERVALO_REFRESCO_RELOJ = 9  # En milisegundos


def obtener_hora_actual():
    return datetime.now().strftime("%H:%M:%S")


def refrescar_reloj():
    #print("Refrescando!")
    variable_data.set(data_canales(board.get_board_data(),2))
    raiz.after(INTERVALO_REFRESCO_RELOJ, refrescar_reloj)
   


def cargar_board(puerto,Id_board):
    params = BrainFlowInputParams()
    params.serial_port = 'COM5' # Cambie esto al puerto serial correcto
    board = BoardShim(2, params)
    board.prepare_session()
    return(board)

def iniciar_stream(board):
    sample_rate=BoardShim.get_sampling_rate(2)
    board.start_stream()
    time.sleep(1)
    # data = board.get_current_board_data (256) # get latest 256 packages or less, doesnt remove them from internal buffer
    data = board.get_board_data()  # get all data and remove it from internal buffer
    return(data)

def data_canales(data,Id_Board):
   print (data[2])
   data_2=data[2]
   return(data_2)



board=cargar_board("COM5",2)
data=iniciar_stream(board)
#time.sleep(2)
#board.stop_stream()
#board.release_session()
#data_canales(data,2)


raiz = tk.Tk()
variable_data = tk.StringVar(raiz, value=data_canales(data,2))
raiz.etiqueta = tk.Label(
    raiz, textvariable=variable_data, font=f"Consolas 10")
raiz.etiqueta.pack(side="top")
app = tk.Frame()
raiz.title("Reloj en Tkinter - By Parzibyte")
refrescar_reloj()
app.pack()
app.mainloop()
