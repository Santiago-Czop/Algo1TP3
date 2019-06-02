import math

class Vector:
    """ Vector 

    Attributes:
        coordenadas (tuple): tupla que contiene cada componente del vector.
    """

    def __init__(self, *coordenadas):
        """ Crea una instancia del vector.

        Si no se pasan argumentos, se crea una instancia del vector nulo de R2.

        Args:
            *coordenadas (float): valor de cada componente, por separado.  
        """
        self.coordenadas = tuple(coordenadas) if len(coordenadas) > 0 else (0, 0)
    
    def __add__(self, vector):
        """ Devuelve la suma de self y vector."""
        suma = tuple(a + b for a, b in zip(self, vector))
        return Vector(*suma)

    def __getitem__(self, componente):
        """ Devuelve el valor de la componente pedida."""
        return self.coordenadas[componente]
