from sys import argv
from csv import reader, writer
from vector import Vector
from tortuga import Tortuga
from pila import Pila
from trazo import Trazo
import math
import copy

#Indices
PROGRAMA = 0
ARCHIVO_SL = 1
ITERACIONES = 2
ARCHIVO_SVG = 3

DISTANCIA_BASE = 100 #Distancia avanzada por la primer tortuga
FACTOR_EXPANSION = 1.0 #Porcentaje como decimal de incremento o disminución de la distancia avanzada por cada tortuga apilada

COLORS = {
    "a": "#F44336", #Material Red
    "b": "#FF5722", #Material Deep Orange
    "c": "#FF9800", #Material Orange
    "d": "#FFC107", #Material Amber
    "e": "#FFEB3B", #Material Yellow
    "f": "#CDDC39", #Material Lime
    "g": "#8BC34A", #Material Light Green
    "h": "#4CAF50", #Material Green
    "i": "#009688", #Material Teal
    "j": "#00BCD4", #Material Cyan
    "k": "#03A9F4", #Material Light Blue
    "l": "#2196F3", #Material Blue
    "m": "#3F51B5", #Material Indigo
    "n": "#673AB7", #Material Deep Purple
    "o": "#9C27B0", #Material Purple
    "p": "#E91E63", #Material Pink
    "q": "#795548", #Material Brown
    "r": "#607D8B", #Material Blue Grey
    "s": "#9E9E9E", #Material Grey
    "t": "#000000", #Black
}

def main():
    """Ejecución del programa.
    El programa recibe por la línea de comandos la ruta de un archivo con la información de un sistema-L, la cantidad de iteraciones y la ruta de un archivo svg.
    Se crea un archivo svg con la codificación de la imagen generada. Si el archivo svg ya existe, se sobreescribe."""
    try:
        validar_parametros()
        angulo, axioma, reglas = cargar_archivo(argv[ARCHIVO_SL])
    except Exception as e:
        print(e)
        return

    codificaciones = {
        "+" : angulo,
        "-" : -angulo,
        "|" : math.pi,
    }

    resultado = obtener_resultado(axioma, reglas, int(argv[ITERACIONES]))

    trazos, coordenada_min, coordenada_max = analizar_secuencia(resultado, codificaciones)

    crear_svg(argv[ARCHIVO_SVG], trazos, coordenada_min, coordenada_max)

def validar_parametros():
    """Si alguno de los parámetros recibidos por la línea de comandos falta o el valor no es válido, se eleva una excepción."""
    if len(argv) != 4:
        raise IndexError(f"El programa {argv[PROGRAMA]} debe recibir 3 parámetros.")
    elif argv[ARCHIVO_SL][-3:].lower() != ".sl":
        raise Exception("El primer parámetro debe ser el nombre de un archivo .sl")
    elif not argv[ITERACIONES].isdigit():
        raise TypeError("El segundo parámetro debe ser un número entero mayor o igual a cero.")
    elif argv[ARCHIVO_SVG][-4:].lower() != ".svg":
        raise Exception("El tercer parámetro debe ser el nombre de un archivo .svg")

def cargar_archivo(ruta_archivo):
    """Se recibe la ruta de una archivo con la información de un sistema-L con el siguiente formato:
    <angulo>
    <axioma>
    <predecesor1> <sucesor1>
    <predecesor2> <sucesor2>
    <predecesor3> <sucesor3>
    ...
    Devuelve el ángulo (float), el axioma (cadena de caracteres) y un diccionario conteniendo las reglas, con el predecesor como clave y el sucesor como valor."""
    reglas = {}
    try:
        with open(ruta_archivo) as archivo:
            lector = reader(archivo, delimiter = " ")
            try:
                angulo = float(archivo.readline().rstrip()) * math.pi / 180
            except ValueError:
                raise ValueError("El valor del ángulo no es válido.")
            axioma = archivo.readline().rstrip()
            try:
                for predecesor, sucesor in lector:
                    reglas[predecesor] = sucesor
            except:
                raise Exception("El formato de las reglas no es válido.")
            return angulo, axioma, reglas
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo {ruta_archivo} no existe.")
    except IOError:
        raise IOError(f"El archivo {ruta_archivo} no se encuentra disponible.")

def obtener_resultado(cadena, reglas, cantidad):
    """Recibe una cadena de caracteres, un diccionario con reglas y la cantidad de iteraciones (número entero mayor o igual a cero).
    Devuelve la cadena de caracteres generada en base a los parámetros recibidos."""
    if cantidad == 0:
        return cadena
    resultado = ""
    for c in cadena:
        resultado += reglas.get(c, c)
    cantidad -= 1
    resultado = obtener_resultado(resultado, reglas, cantidad)
    return resultado

def analizar_secuencia(instrucciones, codificaciones):
    """ Recibe un string con instrucciones y un diccionario que contiene la codificación para algunas instrucciones variables. 
    Devuelve un set de trazos correspondientes al análisis del string, la distancia máxima y la distancia mínima con la que ha de crearse
    el svg.
    """
    coordenada_min = Vector()
    coordenada_max = Vector()

    pila_de_tortugas = Pila()
    pila_de_tortugas.apilar(Tortuga())

    tortuga_tope = pila_de_tortugas.ver_tope()
    profundidad = len(pila_de_tortugas)

    trazos = set()

    for c in instrucciones:
        if c == "[":
            nueva_tortuga = tortuga_tope.clonar()
            pila_de_tortugas.apilar(nueva_tortuga)

            tortuga_tope = pila_de_tortugas.ver_tope()
            profundidad = len(pila_de_tortugas)
        elif c == "]":
            pila_de_tortugas.desapilar()

            tortuga_tope = pila_de_tortugas.ver_tope()
            profundidad = len(pila_de_tortugas)
        elif c == "F":
            ultima_posicion = tortuga_tope.conseguir_posicion()

            tortuga_tope.avanzar( DISTANCIA_BASE * (FACTOR_EXPANSION ** profundidad) )

            nueva_posicion = tortuga_tope.conseguir_posicion()

            coordenada_min = calcular_min(coordenada_min, nueva_posicion)
            coordenada_max = calcular_max(coordenada_max, nueva_posicion)

            nuevo_trazo = Trazo(ultima_posicion, nueva_posicion, tortuga_tope.conseguir_grosor(), tortuga_tope.conseguir_color())

            trazos.add(nuevo_trazo)
        elif c == "f":
            tortuga_tope.levantar_pluma()
            tortuga_tope.avanzar(DISTANCIA_BASE * (FACTOR_EXPANSION ** profundidad))
            tortuga_tope.bajar_pluma()
        elif c in "+-|":
            tortuga_tope.girar(codificaciones[c])
        elif c in COLORS:
            tortuga_tope.cambiar_color_pluma(COLORS[c])
        elif c in "0123456789":
            print(c)
            tortuga_tope.cambiar_grosor_pluma(c)
        
    return trazos, coordenada_min + Vector(-50, -50), coordenada_max + Vector(50, 50)

def calcular_min(vectorA, vectorB):
    """Recibe dos vectores y devuelve un vector con las mínimas componentes presentes en los dos vectores."""
    x_min = min(vectorA[0], vectorB[0])
    y_min = min(vectorA[1], vectorB[1])

    return Vector(x_min, y_min)

def calcular_max(vectorA, vectorB):
    """Recibe dos vectores y devuelve un vector con las máximas componentes presentes en los dos vectores."""
    x_max = max(vectorA[0], vectorB[0])
    y_max = max(vectorA[1], vectorB[1]) 

    return Vector(x_max, y_max)

def crear_svg(ruta_archivo, trazos, coord_min, coord_max):
    """Recibe la ruta de un archivo svg, un conjunto de objetos Trazo y las coordenadas mínimas y máximas, ambas objetos Vector.
    Crea un archivo svg con la codificación de la imagen generada. Si el archivo svg ya existe, lo sobreescribe."""
    with open(ruta_archivo, 'w') as archivo:
        archivo.write(f'<svg viewBox="{coord_min[0]} {coord_min[1]} {coord_max[0] - coord_min[0]} {coord_max[1] - coord_min[1]}" xmlns="http://www.w3.org/2000/svg">' + "\n")
        for trazo in trazos:
            archivo.write(f'<line x1="{trazo.coord_inicial[0]}" y1="{trazo.coord_inicial[1]}" x2="{trazo.coord_final[0]}" y2="{trazo.coord_final[1]}" stroke-width="{trazo.grosor}" stroke="{trazo.color}" />' + "\n")
        archivo.write('</svg>' + "\n")
main()
