
import  numpy as np
from abc import ABC, abstractmethod
from scipy.integrate import quad
import math
#from mpmath import *
import matplotlib.pyplot as plt

class EntidadMatematica(ABC):
    @abstractmethod
    def evaluar(self,t):
        pass
    @abstractmethod
    def sumar(self,s):
        pass
    @abstractmethod
    def escalar(self,e):
        pass
    @abstractmethod
    def trapecio(self, a, b, n):
        pass
    @abstractmethod
    def simpson(self, a, b, n):
        pass
    @abstractmethod
    def factorial(self,x):
        pass
class Vector1D(EntidadMatematica):
    def __init__(self, x) -> None:
        super().__init__(x)
    def sumar(self, s):
        x = self.components[0]+s
        return Vector1D(x)
    def escalar(self, e):
            x = self.components[0]*e
            return Vector1D(x)

class Acel(EntidadMatematica):
    def __call__(self, x):
        return x**3
    def evaluar(self,t):
        return t**3
    def trapecio(self, a, b, n):
        x = np.linspace(a, b, n + 1)
        y = self(x)
        h = (b - a) / n
        return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    def simpson(self, a, b, n):
        if n % 2 == 1:
            raise ValueError("n debe ser par para Simpson")
        x = np.linspace(a, b, n + 1)
        y = self(x)
        h = (b - a) / n
        return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

class FuncionFactorial(EntidadMatematica):
        def factorial(self,x):
            if isinstance(x, np.ndarray):
                return np.array([math.gamma(xi + 1) for xi in x])
            else:
                return math.gamma(x + 1)


def integrar_trapecio(entidadMatematica: EntidadMatematica, a, b, n):
    print(entidadMatematica.trapecio(a, b, n))
def integrar_simpson(entidadMatematica: EntidadMatematica, a, b, n):
    print(entidadMatematica.simpson(a, b, n))
def evaluar_funcion(entidadMatematica: EntidadMatematica, t):
    print(entidadMatematica.evaluar(t))
def factorial_n(entidadMatematica: EntidadMatematica, j):
    print(entidadMatematica.factorial(j))

a, b, n = 0, 1, 100
m = 4
k= 3
t=2
# factorial_func = FuncionFactorial()
x = Acel()
# h = Acel.evaluar(x,t)
integrar_trapecio(x,a,b,n)
# factorial_n(t)