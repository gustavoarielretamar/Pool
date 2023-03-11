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

#%% DERECHA.
def rebotar_der(x, vx, x_max):
    if x > x_max:
        x = x - 2*(x - x_max)
        vx = -vx
    return x, vx
#%% IZQUIERDA:
def rebotar_izq(x, vx, x_min):
        if x < x_min:
            x = x - 2*(x - x_min)
            vx = -vx
        return x, vx

#%% ARRIBA:
def rebotar_arriba(y, vy, y_max):
        if y > y_max:
            y = y - 2*(y - y_max)
            vy= -vy
        return y, vy

#%% ABAJO:
def rebotar_abajo(y, vy, y_min):
        if y < y_min:
            y = y - 2*(y - y_min)
            vy= -vy
        return y, vy

#%% BOLA 8:
def simular_bola_ocho(x, y, vx, vy, dt, L, n_pasos, debug = False):
    posiciones_x = [x]
    posiciones_y = [y]
    i = 0
    while i < n_pasos:
        x, y = dar_pasito(x, y, vx, vy, dt)
        x, vx = rebotar_der(x, vx, L)
        x, vx = rebotar_izq(x, vx, -L)
        y, vy = rebotar_arriba(y, vy, L)
        y, vy = rebotar_abajo(y, vy, -L)
        posiciones_x.append(x) 
        posiciones_y.append(y)
        i += 1
    if debug:
        print(posiciones_x)
        print(posiciones_y)
    return posiciones_x, posiciones_y

#%% PELICULA UAN BOLA:
def pelicula_bola_ocho(x, y, vx, vy, dt, L, n_pasos, nombre, debug = False):
    archivo = open(nombre + ".txt", "w")  # Abrimos el archivo en modo escritura ("w" es de write)
    
    posiciones_x, posiciones_y = simular_bola_ocho(x, y, vx, vy, dt, L, n_pasos)
    lista = [(x,y)]
    i = 0
    while i < n_pasos:
        x, y = dar_pasito(x, y, vx, vy, dt)
        x, vx = rebotar_der(x, vx, L)
        x, vx = rebotar_izq(x, vx, -L)
        y, vy = rebotar_arriba(y, vy, L)
        y, vy = rebotar_abajo(y, vy, -L)
        lista.append(x,y)
        i += 1
    if debug:
        print(lista)
    return plista

#%% PARAMETROS:
x = 0
y = 0
vx = 1.0
vy = 1.35
dt = 0.01
L = 5
v_max = 2
n_bolas = 10
n_pasos = 10000
nombre = "pelicula_bola_ocho"

#%% LLAMADAS:
#posiciones_x, posiciones_y = simular_bola_ocho(x, y, vx, vy, dt, L, n_pasos)
pelicula_bola_ocho(x, y, vx, vy, dt, L, n_pasos, nombre)
#%% 
fig, ax = plt.subplots() #Creamos una figura y un eje de matplotlib
ax.plot(posiciones_x, posiciones_y) #Grafica la pelotita (COMPLETAR)
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


