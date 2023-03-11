#%% LIBRERIAS:
import matplotlib.pyplot as plt
import numpy as np

#%% MUEVE LA BOLA UNA Y RETORNA LA POSICION NUEVA:
def dar_pasito(x, y, vx, vy, dt, debug = False):
    x = x + vx * dt
    y = y + vy * dt
    if debug:
        print(x,y)
    return x,y

#%% BOLA 8:
def simular_bola_ocho(x, y, vx, vy, dt, L, n_pasos, debug = False):
    posiciones_x = [x]
    posiciones_y = [y]
    i = 0
    while i < n_pasos:
        x, y = dar_pasito(x, y, vx, vy, dt)
        posiciones_x.append(x) 
        posiciones_y.append(y)
        i += 1
    if debug:
        print(posiciones_x)
        print(posiciones_y)
    return posiciones_x, posiciones_y

#%% 
fig, ax = plt.subplots() #Creamos una figura y un eje de matplotlib
ax.plot( ... , ... , 'o') #Grafica la pelotita (COMPLETAR)
ax.set_aspect("equal") #Hace que la escala de los ejes sea la misma
#Graficamos los bordes de la mesa: vlines y hlines dibujan rectas verticales
# y horizontales respectivamente:
ax.vlines(-5, ymin=-5, ymax=5, color="black") #Izquierda
ax.vlines(5, ymin=-5, ymax=5, color="black") #Derecha
ax.hlines(-5, xmin=-5, xmax=5, color="black") #Abajo
ax.hlines(5, xmin=-5, xmax=5, color="black") #Arriba
#Seteamos ticks (las lineas en los numeros de la posicion)
#Largos cada dos metros:
ax.set_xticks(np.arange(-6, 7, 2))
ax.set_yticks(np.arange(-6, 7, 2))
#Cortos (por eso el minor=True) cada 0.5 metros:
ax.set_xticks(np.arange(-7, 7, 0.5), minor=True)
ax.set_yticks(np.arange(-7, 7, 0.5), minor=True)
ax.grid(which="both") #Dibujamos la grilla
ax.set_xlim([-7, 7]) #Seteamos limites del grafico en x
ax.set_ylim([-7, 7]) #idem en y
plt.show()
#%% LLAMADAS:

#simular_bola_ocho(0.25, -3.5, 1.5, 2.0, 1.0, 5, 3, True)