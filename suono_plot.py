import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import sounddevice as sd

# Parametri del suono
start_freq = 1000  # 1 kHz
end_freq = 22000   # 22 kHz
duration = 5       # Durata in secondi
sample_rate = 44100  # Frequenza di campionamento in Hz

# Genera il suono
time = np.arange(0, duration, 1/sample_rate)
signal = np.zeros_like(time)

for i in range(len(time)):
    current_time = i / sample_rate
    frequency = start_freq + (end_freq - start_freq) * (current_time / duration)
    signal[i] = 0.5 * np.sin(2 * np.pi * frequency * current_time)

    # Riproduci il suono
    sd.play(signal[:i+1], sample_rate)
    sd.wait()

# Salva il suono come file audio
wavfile.write("suono_crescente.wav", sample_rate, signal)

# Plotta il segnale
plt.plot(time, signal)
plt.title('Segnale Sinusoidale con Frequenza Crescente')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.show()
