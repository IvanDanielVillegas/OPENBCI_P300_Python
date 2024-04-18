



import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math 

import argparse
import time
import brainflow.board_shim

from brainflow.board_shim import BoardShim, BrainFlowInputParams,BoardIds,LogLevels
from brainflow.data_filter import DataFilter, WindowOperations, WaveletTypes







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


def detener_stream(board):
    board.stop_stream()
    

def data_canales(data,Id_Board):
    from math import floor,pow
    a=(4.5/24)/(pow(2,23) - 1)
    eeg_channels = BoardShim.get_eeg_channels(2)
    eeg_channels_cv=  eeg_channels
    
    for count, channel in enumerate(eeg_channels_cv):
            
            print('Original data for channel %d:' % channel)
            chanf=np.vectorize(np.float_)
            chand=data[channel]
            channel_f=chanf(chand)*a
            print(channel_f)
            #plt.plot(channel_f,label= "EEC")
            #plt.legend(loc="upper left")
            #plt.title("Grafica EEC")
            #plt.xlabel("Tiempo")
            #plt.xlabel("Voltaje")
            #plt.show()
           
        
board=cargar_board("COM5",2)
data=iniciar_stream(board)
time.sleep(2)
board.stop_stream()
board.release_session()
data_canales(data,2)
