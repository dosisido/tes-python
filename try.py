import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Funzione per generare dati del seno con frequenza variabile
def generate_data(frame):
    frequency = frame + .1  # Incrementa la frequenza progressivamente
    x = np.linspace(0, 4 * np.pi, 1000)
    y = np.sin(frequency * x)
    return x, y

# Funzione di inizializzazione del grafico
def init():
    line.set_data([], [])
    return line,

# Funzione chiamata ad ogni frame dell'animazione
def update(frame):
    x, y = generate_data(frame)
    line.set_data(x, y)
    return line,

# Creazione della figura e dell'asse
fig, ax = plt.subplots()
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-1, 1)

# Creazione della linea iniziale
line, = ax.plot([], [], lw=2)

# Creazione dell'animazione
animation = FuncAnimation(fig, update, frames=1, init_func=init, blit=True)

# Mostra l'animazione
plt.show()
