from vector import Vector
from pluma import Pluma
import math

class Tortuga:
    """ Tortuga utilizada como metáfora para llevar a cabo operaciones de dibujado."""
    def __init__(self, posicion=Vector(), orientacion=3*math.pi/2, pluma=Pluma()):
        """ Crea una instancia de Tortuga.

        Args:
            posicion (Vector): posición inicial de la tortuga.
            orientacion (float): sentido hacia donde apunta la tortuga. Se mide en sentido antihorario y con radianes. 
            pluma (Pluma): pluma que agarra la tortuga.
        """
        self.posicion = posicion
        self.orientacion = orientacion
        self.pluma = pluma

    def avanzar(self, distancia):
        """ Avanza la tortuga en distancia unidades en la orientacion actual."""
        avance = Vector( math.cos(self.orientacion) * distancia, math.sin(self.orientacion) * distancia )
        self.posicion = self.posicion + avance
        
    def girar(self, angulo):
        """ Cambia la orientacion de la tortuga según angulo"""
        self.orientacion += angulo

    def bajar_pluma(self):
        """ Hace que la tortuga apoye su pluma."""
        self.pluma = self.pluma.cambiar_estado(True)

    def levantar_pluma(self):
        """ Hace que la tortuga levante su pluma."""
        self.pluma = self.pluma.cambiar_estado(False)

    def clonar(self):
        """ Devuelve una nueva instancia de Tortuga con los mismos atributos."""
        return Tortuga(self.posicion, self.orientacion, self.pluma.clonar())

    def conseguir_posicion(self):
        """ Devuelve la posición de la tortuga."""
        return self.posicion

    def conseguir_color(self):
        """ Devuelve el color de la pluma de la tortuga."""
        return self.pluma.conseguir_color()

    def conseguir_grosor(self):
        """ Devuelve el grosor de la pluma de la tortuga."""
        return self.pluma.conseguir_grosor()




