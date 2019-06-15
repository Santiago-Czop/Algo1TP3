import math

class Vector:
    """ Vector de R2

    Attributes:
        coordenadas (tuple): tupla que contiene cada componente del vector.
    """

    def __init__(self, x = 0, y = 0):
        """ Crea una instancia del vector en R2.

        Si no se pasan argumentos, se crea una instancia del vector nulo de R2.

        Args:
            x (float): primera componente.
            y (float): segunda componente.
        """
        self.coordenadas = (x, y)
    
    def __add__(self, vector):
        """ Devuelve la suma de self y vector."""
        x = self[0] + vector[0]
        y = self[1] + vector[1]
        return Vector(x, y)

    def __getitem__(self, componente):
        """ Devuelve el valor de la componente pedida."""
        return self.coordenadas[componente]
