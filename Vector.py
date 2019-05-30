import math

class Vector:
    def __init__(self, *coordenadas):
        self.coordenadas = tuple(coordenadas) if len(coordenadas) > 0 else (0, 0)
    
    def __add__(self, vector):
        """ Devuelve la suma de self y vector."""
        suma = tuple(a + b for a, b in zip(self, vector))
        return Vector(*suma)

    def __getitem__(self, componente):
        """ Devuelve el valor de la componente pedida."""
        return self.coordenadas[componente]
