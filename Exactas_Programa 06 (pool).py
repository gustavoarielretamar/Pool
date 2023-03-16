# %% LIBRERIAS:
import matplotlib.pyplot as plt
import numpy as np
import random


# %% MUEVE LA BOLA UNA Y RETORNA LA POSICION NUEVA:
def dar_pasito(x, y, vx, vy, dt, debug=False):
    x = x + vx * dt
    y = y + vy * dt
    if debug:
        print(x, y)
    return x, y


# %% DERECHA.
def rebotar_der(x, vx, x_max):
    if x > x_max:
        x = x - 2 * (x - x_max)
        vx = -vx
    return x, vx


# %% IZQUIERDA:
def rebotar_izq(x, vx, x_min):
    if x < x_min:
        x = x - 2 * (x - x_min)
        vx = -vx
    return x, vx


# %% ARRIBA:
def rebotar_arriba(y, vy, y_max):
    if y > y_max:
        y = y - 2 * (y - y_max)
        vy = -vy
    return y, vy


# %% ABAJO:
def rebotar_abajo(y, vy, y_min):
    if y < y_min:
        y = y - 2 * (y - y_min)
        vy = -vy
    return y, vy


# %% SIMULAR BOLA 8:
def simular_bola_ocho(x, y, vx, vy, dt, L, n_pasos, debug=False):
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


# %% PELICULA UNA BOLA:
def pelicula_bola_ocho(x, y, vx, vy, dt, L, n_pasos, nombre):
    archivo = open(nombre + ".txt", "w")
    print(1, "\n", file=archivo)
    posiciones_x, posiciones_y = simular_bola_ocho(x, y, vx, vy, dt, L, n_pasos)
    for i in range(len(posiciones_x)):
        print(1, posiciones_x[i], posiciones_y[i], file=archivo)
    archivo.close()


# %% MUCHAS BOLAS:
def cond_ini(L, v_max, n_bolas, debug=False):
    posiciones_x = []
    posiciones_y = []
    velocidades_x = []
    velocidades_y = []
    tupla = (posiciones_x, posiciones_y, velocidades_x, velocidades_y)
    for i in range(n_bolas):
        # esto me da un numero, posicion o velocidad, entre -L y L o entre -v_max y v_max
        x = (random.random() * 2 - 1) * L
        y = (random.random() * 2 - 1) * L
        vx = (random.random() * 2 - 1) * v_max
        vy = (random.random() * 2 - 1) * v_max
        posiciones_x.append(x)
        posiciones_y.append(y)
        velocidades_x.append(vx)
        velocidades_y.append(vy)
    if debug:
        print(tupla)
    return tupla
# %% PELICULA MUCHAS:
def pelicula_muchas(dt, L, v_max, n_pasos, n_bolas, nombre):
    archivo = open(nombre + ".txt", "w")
    print(n_bolas,"\n",file=archivo)
    posiciones_x, posiciones_y, velocidades_x, velocidades_y = cond_ini(L, v_max, n_bolas)
    for j in range(n_pasos):
        for i in range(n_bolas):
            x, y, vx, vy = posiciones_x[i], posiciones_y[i], velocidades_x[i], velocidades_y[i]
            print(i, x, y, file=archivo)
            x, y = dar_pasito(x, y, vx, vy, dt)
            x, vx = rebotar_der(x, vx, L)
            x, vx = rebotar_izq(x, vx, -L)
            y, vy = rebotar_arriba(y, vy, L)
            y, vy = rebotar_abajo(y, vy, -L)
            posiciones_x[i], velocidades_x[i], posiciones_y[i], velocidades_y[i] = x, vx, y, vy
    archivo.close()
# %% PARAMETROS:
x = 0
y = 0
vx = 1.0
vy = 1.35
dt = 0.01
L = 5
v_max = 2
n_bolas = 10
n_pasos = 200
# nombre = "trayectoria_larga"
nombre = "trayectorias_muchas_bolas"
# %% GRAFICO:
# posiciones_x, posiciones_y = simular_bola_ocho(x, y, vx, vy, dt, L, n_pasos)
# fig, ax = plt.subplots() #Creamos una figura y un eje de matplotlib
# ax.plot(posiciones_x, posiciones_y) #Grafica la pelotita (COMPLETAR)
# ax.set_aspect("equal") #Hace que la escala de los ejes sea la misma
# #Graficamos los bordes de la mesa: vlines y hlines dibujan rectas verticales
# # y horizontales respectivamente:
# ax.vlines(-5, ymin=-5, ymax=5, color="black") #Izquierda
# ax.vlines(5, ymin=-5, ymax=5, color="black") #Derecha
# ax.hlines(-5, xmin=-5, xmax=5, color="black") #Abajo
# ax.hlines(5, xmin=-5, xmax=5, color="black") #Arriba
# #Seteamos ticks (las lineas en los numeros de la posicion)
# #Largos cada dos metros:
# ax.set_xticks(np.arange(-6, 7, 2))
# ax.set_yticks(np.arange(-6, 7, 2))
# #Cortos (por eso el minor=True) cada 0.5 metros:
# ax.set_xticks(np.arange(-7, 7, 0.5), minor=True)
# ax.set_yticks(np.arange(-7, 7, 0.5), minor=True)
# ax.grid(which="both") #Dibujamos la grilla
# ax.set_xlim([-7, 7]) #Seteamos limites del grafico en x
# ax.set_ylim([-7, 7]) #idem en y
# plt.show()
# %% LLAMADAS:
# intento  = simular_bola_ocho(x, y, vx, vy, dt, L, n_pasos, True)
# pelicula_bola_ocho(x, y, vx, vy, dt, L, n_pasos, nombre)
pelicula_muchas(dt, L, v_max, n_pasos, n_bolas, nombre)
