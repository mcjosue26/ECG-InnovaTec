import numpy as np
import pylab as pl
import time as tm
from biosppy import storage
from socketIO_client import SocketIO

# Definir la dirección IP y puerto del servidor
HOST = '34.125.27.216'  # '127.0.0.1' es una dirección IP local
PORT = 5001        # Puerto de escucha del servidor

# Crear una instancia de SocketIO y conectarse al servidor
socket = SocketIO(HOST, PORT)

signal, mdata = storage.load_txt('./ecg.txt')

Fs = mdata['sampling_rate']
N = len(signal)  # number of samples
T = (N - 1) / Fs  # duration
ts = np.linspace(0, T, N, endpoint=False)  # relative timestamps
"""
pl.plot(ts, signal, lw=2)
pl.grid()
pl.show()
"""
# Enviar un número entero al servidor
while True:
    for i in range(0,len(signal)):
        socket.emit('nuevo_mensaje', signal[i])
        tm.sleep(0.00085)

# Cerrar la conexión con el servidor
socket.disconnect()