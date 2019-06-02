class Pluma:
    """ Pluma para la tortuga.

    Attributes:
        color (string): color en formato RGB.
        grosor (int): ancho del trazo.
        estado (bool): booleano representando si la pluma esta apoyada, True, o levantada, False.
    """
    def __init__(self, color="#000000", grosor=1, estado=True):
        """ Crea una instancia de Pluma.

        Args: 
            color (string): Color en formato RGB. Negro por default.
            grosor (int): ancho del trazo. 1 por default.
            estado (bool): estado inicial de la pluma. True por default.
        """
        self.color = color
        self.grosor = grosor
        self.estado = estado

    def cambiar_color(self, color):
        """ Devuelve una nueva instancia de Pluma igual, pero con el color pasado."""
        return Pluma(color, self.grosor, self.estado)

    def cambiar_grosor(self, grosor):
        """ Devuelve una nueva instancia de Pluma, pero con el nuevo grosor."""
        return Pluma(self.color, grosor, self.estado)

    def cambiar_estado(self, estado):
        """ Devuelve una nueva instancia de Pluma, pero con el nuevo estado."""
        return Pluma(self.color, self.grosor, estado)

    def conseguir_color(self):
        """ Devuelve el color de la Pluma."""
        return self.color

    def conseguir_grosor(self):
        """ Devuelve el grosor de la Pluma."""
        return self.grosor

    def conseguir_estado(self):
        """ Devuelve el estado de la Pluma."""
        return self.estado

    def clonar(self):
        """ Devuelve una nueva instancia de Pluma, con los mismos atributos."""
        return Pluma(self.color, self.grosor, self.estado)