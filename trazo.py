class Trazo:
    """ Representa un trazo lineal de color y grosor específico.
    
    Attributes:
        coord_inicial (Vector): posición inicial.
        coord_final (Vector): posición final.
        grosor (int): ancho del trazo.
        color (string): color del ancho en formato RGB.
    """
    def __init__(self, coord_inicial, coord_final, grosor, color):
        """ Crea una instancia de Trazo.

        Args:
            coord_inicial (Vector): posición inicial.
            coord_final (Vector): posición final.
            grosor (int): ancho del trazo.
            color (string): color del ancho en formato RGB.
        """
        self.coord_inicial = coord_inicial
        self.coord_final = coord_final
        self.grosor = grosor
        self.color = color