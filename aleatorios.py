"""
Cuarta tarea : Generación de números aleatorios
Nom i cognoms: Ramon Llobet Duch

Este fichero implementa un generador de números pseudoaleatorios usando el algoritmo
de Generación Lineal Congruente (LGC). Contiene dos formas de generar la secuencia:
una clase iterable llamada `Aleat` y una función generadora `aleat()`.

>>> rand = Aleat(m=32, a=9, c=13, x0=11)
>>> for _ in range(4):
...     print(next(rand))
...
16
29
18
15
>>> rand(29)
>>> for _ in range(4):
...     print(next(rand))
...
18
15
20
1
>>> rand = aleat(m=64, a=5, c=46, x0=36)
>>> for _ in range(4):
...     print(next(rand))
...
34
24
38
44
>>> rand.send(24)
38
>>> for _ in range(4):
...     print(next(rand))
...
44
10
32
14
"""

class Aleat:
    """
    Clase generadora de números pseudoaleatorios usando LGC.

    Parámetros:
    - m (int): módulo (>0)
    - a (int): multiplicador (0 < a < m)
    - c (int): incremento (0 <= c < m)
    - x0 (int): semilla inicial (0 <= x0 < m)

    Uso:
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> print(next(rand))
    16
    """

    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, nueva_semilla):
        self.x = nueva_semilla

    def send(self, nueva_semilla):
        self.x = nueva_semilla
        return next(self)


def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Función generadora de números pseudoaleatorios mediante el algoritmo LGC.

    Argumentos:
    - m (int): Módulo (> 0)
    - a (int): Multiplicador (0 < a < m)
    - c (int): Incremento (0 <= c < m)
    - x0 (int): Semilla inicial (0 <= x0 < m)

    Salida:
    - Generador infinito de números pseudoaleatorios (enteros)

    Se puede reiniciar la secuencia usando el método send(nueva_semilla).

    Ejemplo de uso:
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44
    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    x = x0
    while True:
        x = (a * x + c) % m
        num = yield x
        if num is not None:
            x = num




if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)  