from abc import ABC, abstractmethod
import numpy as np
# Clase abstracta
import matplotlib.pyplot as plt
class EntidadMatematica(ABC):
    @abstractmethod
    def evaluar(self, t):
        pass

    @abstractmethod
    def sumar(self, otra):
        pass

    @abstractmethod
    def escalar(self, factor):
        pass

def Fuerza(k):
    v_scalar = lambda t: k * t**3
    v_array = lambda t: k * t**3
    return v_scalar, v_array

class Funcion(EntidadMatematica):
    def __init__(self, f):
        self.f = f
    def evaluar(self, t):
        return self.f(t)
    def escalar(self, factor):
        return Funcion(lambda t: factor * self.f(t))

    def representar(self, a, b):
        x_vals = np.linspace(a, b, 200)  # Más puntos para suavizar la curva
        y_vals = np.array([self.func(t) for t in x_vals])

        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, linestyle='--', color='darkorange', linewidth=2)
        plt.fill_between(x_vals, y_vals, alpha=0.2, color='orange')  # Área bajo la curva

        plt.xlabel("Eje X", fontsize=12)
        plt.ylabel("Eje Y", fontsize=12)
        plt.title("Visualización alternativa de la función", fontsize=14)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        plt.axhline(0, color='gray', linewidth=0.8)
        plt.axvline(0, color='gray', linewidth=0.8)
        plt.grid(visible=True, linestyle=':', alpha=0.5)
        plt.legend(["Curva"], loc='upper left')
        plt.tight_layout()
        plt.show()

class Vector(EntidadMatematica):
    def __init__(self, components):
        if len(components) != 1:
            raise ValueError("Un vector debe tener una dimension.")
        self.x = components[0]

    def sumar(self, other):
        return Vector([self.x + other.x])

    def escalar(self, escalar):
        return Vector([self.x * escalar])

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El factorial solo está definido para enteros no negativos.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def obtener_aceleracion(tiempo, masa_objeto, k):
    fuerza_escalar, _ = Fuerza(k)  # k va aquí, no tiempo
    aceleracion = fuerza_escalar(tiempo) / masa_objeto
    return aceleracion

def trapecio(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return h * (y[0]/2 + np.sum(y[1:-1]) + y[-1]/2)

def simpson(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("n debe ser par para Simpson")
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return h/3 * (y[0] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-2:2]) + y[-1])

def calcular_velocidad(aceleracion_func, a, b, n, Mass, k):
    x_vals = np.linspace(a, b, n + 1)
    v_vals = [trapecio(lambda t: obtener_aceleracion(t, Mass, k), a, t, n) for t in x_vals]
    return x_vals, v_vals

def calcular_posicion(velocidad_func, a, b, n, Mass, k):
    x_vals = np.linspace(a, b, n + 1)
    v_vals = [trapecio(lambda t: obtener_aceleracion(t, Mass, k), a, t, n) for t in x_vals]
    return x_vals, v_vals

#ejemplo
Mass = 10
k = 5
a = 0
b = 10
n = 100
aceleracion_func = lambda t: obtener_aceleracion(t, Mass, k)
t_vals = np.linspace(a, b, n + 1)
a_vals = [aceleracion_func(t) for t in t_vals]

# Corrección aquí: directamente usa los valores ya calculados
x_vals, v_vals = calcular_velocidad(aceleracion_func, a, b, n, Mass, k)
_, p_vals = calcular_posicion(lambda t: np.interp(t, x_vals, v_vals), a, b, n, Mass, k)

fig, axs = plt.subplots(3, 1, figsize=(8, 12))

axs[0].plot(t_vals, a_vals)
axs[0].set_title("Acceleration")
axs[0].set_xlabel("Time (t)")
axs[0].set_ylabel("Acceleration (a)")

axs[1].plot(x_vals, v_vals)
axs[1].set_title("Velocity")
axs[1].set_xlabel("Time (t)")
axs[1].set_ylabel("Velocity (v)")

axs[2].plot(x_vals, p_vals)
axs[2].set_title("Position")
axs[2].set_xlabel("Time (t)")
axs[2].set_ylabel("Position (x)")

plt.tight_layout()
plt.show()










