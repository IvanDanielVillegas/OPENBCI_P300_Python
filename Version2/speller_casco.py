import argparse
import time
import pandas as pd
import numpy as np
import csv
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
from brainflow.data_filter import DataFilter, AggOperations
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
from datetime import datetime
import ui_speller_window
bandera=ui_speller_window.bandera
#def conf_casco():
   # BoardShim.enable_dev_board_logger()
   # params = BrainFlowInputParams()
   # params.serial_port = 'COM5'
   # board = BoardShim(2, params)
   # board.prepare_session()
   # return board

#def obtenerdatos_casco(board):
   # board.start_stream()
   # BoardShim.log_message(LogLevels.LEVEL_INFO.value,
                         # 'start sleeping in the main thread')
    #time.sleep(20)
#def detenerdatos_casco(board):
 #   data = board.get_board_data()
  #  board.stop_stream()
   # board.release_session()
    
    

#if __name__ == "__main__":
def conf_casco():
    BoardShim.enable_dev_board_logger()
    params = BrainFlowInputParams()
    params.serial_port = 'COM5'
    board = BoardShim(2, params)
    return board



    
def reiniciardatos_casco(board):
    data = board.get_board_data()
    #board.release_session()
    print("finalizo hilo 1")
    #print(data)
    return data
    #obtenerdatos_casco(board)
    #print(board.get_board_data())
    #data="aaa"
    #return data


def obtenerdatos_casco(board):
    board.prepare_session()
    board.start_stream()
    board.get_board_data()
    
    print(" Inicio hilo 1")
    #if bandera==True:
        #reiniciardatos_casco(board)
def detenerdatos_casco(board):
    data = board.get_board_data()
    board.stop_stream()
    board.release_session()

    for i in data:
        df = pd.DataFrame(data.T)
        df.to_csv('Todos los datos.txt', sep=' ',
                  quoting=csv.QUOTE_NONE, escapechar=' ')

def stopdatos_stream(board):
    board.stop_stream()
    board.release_session()
