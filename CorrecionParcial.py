from abc import ABC, abstractmethod

# Clase abstracta
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

class Funcion(EntidadMatematica):
    def __init__(self, f):
        self.f = f  # f debe ser una función de una variable (por ejemplo, lambda t: -k * t**3)

    def evaluar(self, t):
        return self.f(t)

    def sumar(self, otra):
        return Funcion(lambda t: self.f(t) + otra.evaluar(t))

    def escalar(self, factor):
        return Funcion(lambda t: factor * self.f(t))

class Vector(EntidadMatematica):
    def __init__(self, x, v, a):
        self.x = x  # posición
        self.v = v  # velocidad
        self.a = a  # aceleración

    def evaluar(self, t):
        return (self.x.evaluar(t), self.v.evaluar(t), self.a.evaluar(t))

    def sumar(self, otro):
        return Vector(
            self.x.sumar(otro.x),
            self.v.sumar(otro.v),
            self.a.sumar(otro.a)
        )

    def escalar(self, factor):
        return Vector(
            self.x.escalar(factor),
            self.v.escalar(factor),
            self.a.escalar(factor)
        )
def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El factorial solo está definido para enteros no negativos.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)