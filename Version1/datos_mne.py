import numpy as np
import pybv
# Crear un np.array con datos aleatorios
data = np.random.randn(2, 1000)

# Especificar la frecuencia de muestreo y los nombres de los canales
sfreq = 100
ch_names = ['C3', 'C4']

# Crear una lista de eventos con el formato [onset, duration, description]
events = [{'onset': 100, 'duration': 0, 'type': 'Response', 'description': 1},
          {'onset': 200, 'duration': 0, 'type': 'Stimulus', 'description': 2},
          {'onset': 300, 'duration': 0, 'type': 'Comment', 'description': 3}]
# Escribir los archivos BrainVision
pybv.write_brainvision(data=data, sfreq=sfreq, ch_names=ch_names,
                  folder_out="./",
                  fname_base="pybv_test_file",
                  events = events)

# Imprimir información sobre Raw
#print(raw.info)