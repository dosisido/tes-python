import numpy as np
import matplotlib.pyplot as plt

# Creazione di un segnale sinusoidale
fs = 500  # Frequenza di campionamento
t = np.linspace(0, 1, fs, endpoint=False)  # Tempo da 0 a 1 secondi
frequencies = [5, 50, 100]  # Frequenze delle sinusoidi

# Somma delle due sinusoidi
signal = np.zeros(len(t))
for fre in frequencies:
    # signal += np.sign(np.sin(2 * np.pi * fre * t))
    signal += np.sin(2 * np.pi * fre * t)

    

# Calcolo della trasformata di Fourier
fft_result = np.fft.fft(signal)

# Spostamento delle frequenze
fft_shifted = np.fft.fftshift(fft_result)

# Frequenze nel dominio della frequenza
freq = np.fft.fftfreq(len(t), 1/fs)

# zero = np.zeros(len(freq))
# fft_result = zero + fft_result
# fft_shifted = zero + fft_shifted

# Plot del segnale e della sua trasformata di Fourier
plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.plot(t, signal)
plt.title('Segnale nel dominio del tempo')

plt.subplot(3, 1, 2)
plt.plot(freq, np.abs(fft_result))
plt.title('Trasformata di Fourier non spostata')

plt.subplot(3, 1, 3)
plt.plot(freq, np.abs(fft_shifted))
plt.plot(freq, np.abs(fft_result))
plt.title('Trasformata di Fourier spostata')

plt.tight_layout()
plt.show()
