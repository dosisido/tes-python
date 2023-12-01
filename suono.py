import numpy as np
from scipy.io import wavfile
import sounddevice as sd

# Parametri del suono
start_freq = 0
end_freq = 22000   
duration = 10       
sample_rate_in = 5000  
sample_rate_out = 100 * 10**1  

# Genera l'array dei campioni con frequenza crescente
time = np.arange(0, duration, 1/sample_rate_in)
frequency = np.linspace(start_freq, end_freq, len(time))
signal = 0.5 * np.sin(2 * np.pi * frequency * time)

# Riproduci il suono
sd.play(signal, sample_rate_in)
sd.wait()

# Salva il suono come file audio
# wavfile.write("suono_crescente.wav", sample_rate, signal)
