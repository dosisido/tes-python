import numpy as np
import matplotlib.pyplot as plt


# Parametri del segnale
fs = 2000  # Frequenza di campionamento in Hertz
t = np.arange(0, 1, 1/fs)  # Vettore del tempo

# Generazione di un segnale con più componenti in frequenza
# signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)
frequencies = [5, 50, 500]  # Frequenze delle sinusoidi
modules = [1, 0.5, 0.2]  # Moduli delle sinusoidi

# Somma delle due sinusoidi
signal = np.zeros(len(t))
for i in range(min(len(frequencies), len(modules))):
    # signal += np.sign(np.sin(2 * np.pi * fre * t))
    signal += modules[i] * np.sin(2 * np.pi * frequencies[i] * t)
# signal = np.ones(len(t))

# Calcolo della trasformata di Fourier
fft_result = np.fft.fft(signal)

# Frequenze nel dominio della frequenza
freq = np.fft.fftfreq(len(t), 1/fs)
freq2 = np.fft.fftfreq(10*len(t), 1/fs/10)


# fft_result_shifted = np.roll(fft_result, desired_frequency)

# Plot del segnale e della sua trasformata di Fourier spostata
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, signal)
plt.title('Segnale nel dominio del tempo')

plt.subplot(3, 1, 2)
plt.plot(freq, np.abs(fft_result))
plt.title(f'Trasformata di Fourier originale')

plt.subplot(3, 1, 3)
# Aggiungi zeri a fft_result in modo che abbia la stessa dimensione di freq
zeros = np.zeros((len(freq2) - len(freq))//2)
fft_result = np.concatenate((zeros, fft_result, zeros))
# fft_result = np.pad(fft_result, (len(freq2) - len(t))//2, 'constant')
plt.plot(freq2, np.abs(fft_result))
plt.title(f'Trasformata di Fourier allargata')

plt.tight_layout()
plt.show()
