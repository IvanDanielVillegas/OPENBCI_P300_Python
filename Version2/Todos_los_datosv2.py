import argparse
import time
import pandas as pd
import numpy as np
import csv
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
from brainflow.data_filter import DataFilter, AggOperations
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowPresets
from datetime import datetime


def conf_casco():
    BoardShim.enable_dev_board_logger()
    params = BrainFlowInputParams()
    params.serial_port = 'COM5'
    board = BoardShim(2, params)
    board.prepare_session()
    return board

def obtenerdatos_casco(board):
    board.start_stream()
    BoardShim.log_message(LogLevels.LEVEL_INFO.value,
                          'start sleeping in the main thread')
    #time.sleep(20)
def detenerdatos_casco(board):
    data = board.get_board_data()
    board.stop_stream()
    board.release_session()
    
    for i in data:
        df = pd.DataFrame(data.T)
        df.to_csv('Todos los datos.txt', sep=' ',
                  quoting=csv.QUOTE_NONE, escapechar=' ')


#if __name__ == "__main__":
   
