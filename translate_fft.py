import numpy as np
import matplotlib.pyplot as plt

def repliche_segnale(signal, freq, number):
    if number%2 == 1: return repliche_segnale(signal, freq, number+1)

    res = np.zeros(len(signal))
    for i in range(-number//2, number//2 + 1):
        if i == 0: continue
        if abs(i * FS) > len(signal)//2: continue
        shift = np.roll(fft_result, i * FS)
        res += np.abs(shift)
    return res



# Parametri del segnale
fs = 2000  # Frequenza di campionamento in Hertz
FS = 300
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

# Aggiungi zeri a fft_result in modo che abbia la stessa dimensione di freq

# Scegli la frequenza intorno alla quale vuoi spostare il segnale
desired_frequency = 200  # Scegli la frequenza desiderata in Hertz

# Calcola l'indice della frequenza desiderata
# desired_index = int(desired_frequency * len(t) / fs)

# Spostamento del segnale in modo che la frequenza desiderata sia al centro
fft_result_shifted = np.roll(fft_result, desired_frequency)

# Plot del segnale e della sua trasformata di Fourier spostata
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, signal)
plt.title('Segnale nel dominio del tempo')

plt.subplot(3, 1, 2)
plt.plot(freq, np.abs(fft_result))
plt.plot(freq, np.abs(fft_result_shifted))
plt.title(f'Trasformata di Fourier con frequenza {desired_frequency} al centro')

plt.subplot(3, 1, 3)
plt.plot(freq, np.abs(fft_result))
res = repliche_segnale(signal, freq, 10)
plt.plot(freq, np.abs(res))
plt.title(f'Trasformata di Fourier con repliche')

plt.tight_layout()
plt.show()
