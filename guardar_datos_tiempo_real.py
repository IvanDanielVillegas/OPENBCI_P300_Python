import argparse
import logging
import numpy as np
import pandas as pd
import pyqtgraph as pg
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes, DetrendOperations
from pyqtgraph.Qt import QtGui, QtCore



def cargar_board(puerto,Id_board):
    params = BrainFlowInputParams()
    params.serial_port = 'COM5' # Cambie esto al puerto serial correcto
    board = BoardShim(2, params)
    return(board)

def iniciar_stream(board):
    sample_rate=BoardShim.get_sampling_rate(2)
    board.start_stream()
    return 
    
def detener_stream(board):
    board.stop_stream()

class Graph:
    def __init__(self, board_shim):
        self.board_id = board_shim.get_board_id()
        self.board_shim = board_shim
        self.exg_channels = BoardShim.get_exg_channels(self.board_id)
        self.sampling_rate = BoardShim.get_sampling_rate(self.board_id)
        self.update_speed_ms = 50
        self.window_size = 4
        self.num_points = self.window_size * self.sampling_rate

        self.app = QtGui.QApplication([])
        self.win = pg.GraphicsWindow(title='BrainFlow Plot', size=(800, 600))

        self._init_timeseries()

        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(self.update_speed_ms)
        QtGui.QApplication.instance().exec_()
        self.guardar_datos()

    def _init_timeseries(self):
        self.plots = list()
        self.curves = list()
        for i in range(len(self.exg_channels)):
            p = self.win.addPlot(row=i, col=0)
            p.showAxis('left', False)
            p.setMenuEnabled('left', False)
            p.showAxis('bottom', False)
            p.setMenuEnabled('bottom', False)
            if i == 0:
                p.setTitle('TimeSeries Plot')
            self.plots.append(p)
            curve = p.plot()
            self.curves.append(curve)

    def update(self):
        data = self.board_shim.get_current_board_data(self.num_points)
        for count, channel in enumerate(self.exg_channels):
            #FILTROS
            self.curves[count].setData(data[channel].tolist())

        self.app.processEvents()

    def guardar_datos(self):
        data=[]
        segundos=1
        data=self.board_shim.get_current_board_data(segundos*self.sampling_rate) 
        eeg_channels= BoardShim.get_eeg_channels(2)
        eeg_channels_cv= eeg_channels*(1) #((4.5/24)/(pow(2, 23) - 1))    
        MATRIZ= np.ones([16,125*segundos])
        
        for count, channel in enumerate(eeg_channels_cv):
            print(data[channel].shape)
            #print(MATRIZ[channel-1].shape)
            MATRIZ[channel-1]=data[channel]
        
        diccionario = {'ch1': MATRIZ[0], 'ch2': MATRIZ[1], 'ch3': MATRIZ[2] , 'ch4': MATRIZ[3], 'ch5': MATRIZ[4], 'ch6': MATRIZ[5], 'ch7': MATRIZ[6], 'ch8': MATRIZ[7], 'ch9': MATRIZ[8], 'ch10': MATRIZ[9], 'ch11': MATRIZ[10], 'ch12': MATRIZ[11], 'ch13': MATRIZ[12], 'ch14': MATRIZ[13], 'ch15': MATRIZ[14], 'ch16': MATRIZ[15]}

        # Creación DataFrame:
        df_numeros = pd.DataFrame(diccionario)

        # Guarda datos en CSV:
        df_numeros.to_csv('numeros.csv', header=True, index=False)    
      
        print(MATRIZ)
        
        




def main():
    
    board_shim = cargar_board("COM5",2)
    try:
        board_shim.prepare_session()
        iniciar_stream(board_shim) ##board_shim.start_stream(450000, args.streamer_params)
        Graph(board_shim)
    except BaseException:
        logging.warning('Exception', exc_info=True)
    finally:
        logging.info('End')
        if board_shim.is_prepared():
            logging.info('Releasing session')
            detener_stream(board_shim)
            board_shim.release_session()
            
    

if __name__ == '__main__':
    main()