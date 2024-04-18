import numpy as np
import sounddevice as sd
import time

def karplus_strong(note_freq, duration, decay_factor, fs=44100):
    buffer_length = int(fs / note_freq)
    buffer = np.random.uniform(-1, 1, buffer_length)
    
    samples = int(fs * duration)
    output = np.zeros(samples)
    
    for i in range(samples):
        new_sample = 0.5 * (buffer[0] + buffer[1])
        buffer = np.roll(buffer, -1)
        buffer[-1] = new_sample * decay_factor
        output[i] = new_sample
        
    return output

def play_sound(sound):
    sd.play(sound)
    sd.wait()

# Ajusta los parámetros según tus preferencias
fs = 44100
decay_factor = 0.995
chord_duration = 1.5

# Definir las frecuencias de las cuerdas al aire de una guitarra estándar
open_string_frequencies = [329.63, 246.94, 196.00, 146.83, 110.0, 82.41]  # E4, B3, G3, D3, A2, E2

# Definir la progresión de acordes (en este caso, C, G, Am, F)
chord_progression = [
    [open_string_frequencies[2], open_string_frequencies[1], open_string_frequencies[0]],
    [open_string_frequencies[3], open_string_frequencies[2], open_string_frequencies[1]],
    [open_string_frequencies[4], open_string_frequencies[3], open_string_frequencies[2]],
    [open_string_frequencies[5], open_string_frequencies[4], open_string_frequencies[3]],
]

# Generar y reproducir la canción
for chord in chord_progression:
    chord_sound = np.zeros(0)
    for freq in chord:
        note_sound = karplus_strong(freq, chord_duration, decay_factor, fs)
        chord_sound = np.concatenate((chord_sound, note_sound))
    
    play_sound(chord_sound)
    time.sleep(chord_duration)

print("¡Canción terminada!")
#Este ejemplo generará una progresión de acordes simple y reproducirá los acordes utilizando el algoritmo de Karplus-Strong para simular las cuerdas de una guitarra. Puedes ajustar la progresión de acordes, la duración de los acordes y otros parámetros para personalizar la canción según tus preferencias. Recuerda que este es solo un ejemplo básico, y puedes expandir y mejorar el código para crear composiciones más elaboradas y realistas.







