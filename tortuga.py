from vector import Vector
from pluma import Pluma
import math

class Tortuga:
    def __init__(self, posicion=Vector(), orientacion=3*math.pi/2, pluma=Pluma()):
        self.posicion = posicion
        self.orientacion = orientacion
        self.pluma = pluma

    def avanzar(self, distancia):
        avance = Vector( math.cos(self.orientacion) * distancia, math.sin(self.orientacion) * distancia )
        self.posicion = self.posicion + avance
        
    def girar(self, angulo):
        self.orientacion += angulo

    def cambiar_color(self, color):
        self.pluma = self.pluma.cambiar_color(color)

    def cambiar_grosor(self, grosor):
        self.pluma = self.pluma.cambiar_grosor(grosor)

    def bajar_pluma(self):
        self.pluma = self.pluma.cambiar_estado(True)

    def levantar_pluma(self):
        self.pluma = self.pluma.cambiar_estado(False)

    def alternar_pluma(self):
        self.pluma = self.pluma.alternar_estado()

    def clonar(self):
        return Tortuga(self.posicion, self.orientacion, self.pluma)
        #Aca self.grosor, self.color y self.pluma, apuntarian a exactamente el mismo valor?
        #Idem en clonar de tortuga. Tener cuidado y venir aca si surgen errores al ejecutar

    def conseguir_posicion(self):
        return self.posicion

    def conseguir_color(self):
        return self.pluma.color

    def conseguir_grosor(self):
        return self.pluma.grosor




