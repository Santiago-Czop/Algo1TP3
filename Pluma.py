class Pluma:
    def __init__(self, color="#000000", grosor=1, estado=True):
        self.color = color
        self.grosor = grosor
        self.estado = estado

    def cambiar_color(self, color):
        return Pluma(color, self.grosor, self.estado)

    def cambiar_grosor(self, grosor):
        return Pluma(self.color, grosor, self.estado)

    def alternar_estado(self):
        return Pluma(self.color, self.grosor, not self.estado)