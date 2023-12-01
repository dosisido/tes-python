import numpy as np
from scipy.io import wavfile
import sounddevice as sd
import matplotlib.pyplot as plt
from time import sleep

start_freq = 0
end_freq = 15000
duration = 10
sample_rate = 200

def axes():
    plt.title('Segnale Sinusoidale con Frequenza Crescente')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')



single_freq_duration = (end_freq - start_freq) / duration

plt.ion()


for f in range(start_freq if start_freq>0 else 1, end_freq):

    time = np.arange(0, single_freq_duration, 1/sample_rate)
    # frequency = np.linspace(f, f+1, len(time))
    signal = 0.5 * np.sin(2 * np.pi * f * time)

    
    plt.clf()
    axes()
    plt.plot(time, signal)
    plt.show()
    sd.play(signal, 100000)
    # sleep(single_freq_duration)




# Riproduci il suono
# sd.play(signal, sample_rate)
# sd.wait()

# Salva il suono come file audio
# wavfile.write("suono_crescente.wav", sample_rate, signal)
