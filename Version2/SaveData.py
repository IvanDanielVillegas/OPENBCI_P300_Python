import numpy as np
import matplotlib.pyplot as plt
import datetime
import pandas as pd
from pybv import write_brainvision
import ui_mainwindow 
from datetime import date
import re

#Instancia_ui_mainwindow=ui_mainwindow.Ui_MainWindow()
#Instancia_ui_mainwindow.iniciar_teclado()
#sabo = Instancia_ui_mainwindow.iniciar_teclado.texto_ingresado()
#print(sabo)
#Instancia_ui_mainwindow.iniciar_teclado()
#print(Instancia_ui_mainwindow.text_input.text())


def find_closest_number(num, arr):
    return arr[np.abs(np.array(arr) - num).argmin()]
def setP300Label(df2, palabra):
  indices_ceros = df2.index[df2[0] == '0'].tolist()
  inicial = 0
  final = indices_ceros[1]
  p300 = []
  for i in indices_ceros:
    final = i
    df_filtrado = df2.loc[inicial:final]
    print(df_filtrado)
    indice = df_filtrado[0].index[df_filtrado[0] == palabra[0]].to_list()
    if (indice != []):
      p300.append(indice)
    # print(p300)
    inicial = final
    if (len(p300) > 0):
      palabra = palabra[1:]
    if (len(palabra) == 0):
      break

  df2['P300'] = 0
  print(p300)
  for idx in p300:
      df2.at[idx[0], 'P300'] = 1
  return df2

def transformar_archivo(palabra):
    ruta_archivo1 = 'Todos los datos.txt'  # Poner la ruta del archivo
    pd.set_option('display.float_format', lambda x: '%.7f' % x)
    df1 = pd.read_csv(ruta_archivo1, sep=' ')
    # Poner la ruta del archivo
    ruta_archivo = 'teclado_funcionalv2.txt'
    df2 = pd.read_csv(ruta_archivo, sep=' ', encoding='ISO-8859-1', header=None)
    # Se quitan los caracteres especiales
    df2.replace({':': '', '{': '', '}': ''}, regex=True, inplace=True)
    df2.replace({'\'': '', '\[': '', '\]': ''}, regex=True, inplace=True)
    df2 = setP300Label(df2, palabra)


    # Asociación del evento con  muestra más cercana
    df1 = df1.rename(columns={'30': 'timestamp'})
    df2 = df2.rename(columns={1: 'timestamp'})
    df2['timestamp'] = df2['timestamp'].astype('float64')
    df1['timestamp'].dtypes, df2['timestamp'].dtypes


    df_new1 = pd.DataFrame({'timestamp1': df1['timestamp'].round(8)})
    df_new2 = pd.DataFrame({'timestamp2': df2['timestamp'].round(3)})


    df = pd.DataFrame({'col1': df1['timestamp']})
    df = df.dropna()
    # Crea una nueva columna en el dataframe que contenga la lista modificada
    df1['timestamp'] = [df['col1'][0] + i * 0.008 for i in range(len(df))]


    df_1 = pd.DataFrame({'col1': df2['timestamp']})
    df_2 = pd.DataFrame({'col2': df1['timestamp']})

# Define una función para encontrar el número con la menor diferencia





# Asocia el número de la segunda lista que tiene la menor diferencia con cada número de la primera lista
    df_1['col2'] = df_1['col1'].apply(
        lambda x: find_closest_number(x, df_2['col2'].tolist()))


    # Devuelve los índices de los números del dataframe 2 que se asociaron con los números del dataframe 1
    df_1['index'] = df_1['col2'].apply(lambda x: df_2[df_2['col2'] == x].index[0])

    data = df1.iloc[:, 2:18].to_numpy()
    eventos = df_1['index'][df_1['index'] <= len(data)-12]
    # eventos = df_1['index']
    df_events = pd.DataFrame({'onset': eventos})
    tipos = df2['P300']
    tipos = tipos[:len(eventos)]
    dur = 12*np.ones([len(eventos)])
    des = []
    des += ['Stimulus']*len(eventos)


    df_event = pd.DataFrame({'description': tipos})
    df_event = df_event.assign(onset=eventos)
    df_event = df_event.assign(duration=dur)
    df_event['duration'] = df_event['duration'].astype('int64')
    df_event['description'] = df_event['description'].astype('int64')
    df_event = df_event.assign(type=des)
    df_event = df_event[['onset', 'duration', 'description', 'type']]
    events = df_event.to_dict(orient='records')
    
    unit = []   
    unit += ['µV']*16

    print(unit)
    

    sfreq = 125

    # Definir electrodos


    ch_names = ['P7', 'P3', 'O1', 'Pz', 'Oz', 'O2', 'P8',
                'P4', 'C3', 'Cz', 'C4', 'F3', 'Fz', 'F4', 'Fp1', 'Fp2']

    today = datetime.datetime.now()
    today = re.sub(r'[^a-zA-Z0-9]+', '', str(today))
    write_brainvision(data=data.T, sfreq=sfreq, ch_names=ch_names,
                      folder_out="Data/pybv/",
                      fname_base="pybv_file"+ today,
                      events=events,
                      unit=unit,
                      overwrite=True)
