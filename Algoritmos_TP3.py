from sys import argv
from csv import reader, writer
from vector import Vector
from tortuga import Tortuga
from pila import Pila
from trazo import Trazo
import math
import copy

PROGRAMA = 0
ARCHIVO_SL = 1
ITERACIONES = 2
ARCHIVO_SVG = 3

DISTANCIA_BASE = 100
FACTOR_EXPANSION = 1.0

def main():
    """Ejecución del programa.
    El programa recibe por la línea de comandos la ruta de un archivo con la información de un sistema-L, la cantidad de iteraciones y la ruta de un archivo svg.
    Si alguno de los parámetros falta o el valor no es válido, se le muestra un mensaje al usuario y se interrumpe el programa.
    Se crea un archivo svg con la codificación de la imagen generada. Si el archivo svg ya existe, se sobreescribe."""

    if len(argv) != 4:
        print(f"El programa {argv[PROGRAMA]} debe recibir 3 parámetros.")
        return
    elif argv[ARCHIVO_SL][-3:].lower() != ".sl":
        print("El primer parámetro debe ser el nombre de un archivo .sl")
        return
    elif not argv[ITERACIONES].isdigit():
        print("El segundo parámetro debe ser un número entero mayor o igual a cero.")
        return
    elif argv[ARCHIVO_SVG][-4:].lower() != ".svg":
        print("El tercer parámetro debe ser el nombre de un archivo .svg")
        return

    try:
        angulo, axioma, reglas = cargar_archivo(argv[ARCHIVO_SL])
    except FileNotFoundError:
        print(f"El archivo {argv[ARCHIVO_SL]} no existe.")
        return
    except IOError:
        print(f"El archivo {argv[ARCHIVO_SL]} no se encuentra disponible.")
        return
    except ValueError as e:
        print(e)
        return

    codificaciones = {
        "+" : angulo,
        "-" : -angulo,
        "|" : math.pi,
    }

    secuencia = obtener_secuencia(axioma, reglas, int(argv[ITERACIONES]))

    trazos, coordenada_min, coordenada_max = analizar_secuencia(secuencia, codificaciones)

    crear_svg(argv[ARCHIVO_SVG], trazos, coordenada_min, coordenada_max)

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
        except ValueError:
            raise ValueError("El formato de las reglas no es válido.")
        return angulo, axioma, reglas

def obtener_secuencia(axioma, reglas, iteraciones):
    """Recibe un axioma (cadena de caracteres), un diccionario con reglas de transformación y la cantidad de iteraciones a procesar (número entero mayor o igual a cero).
    Devuelve la cadena de caracteres resultante de reemplazar cada caracter del axioma por los caracteres incluidos en las reglas de transformación, la cantidad de veces indicada en el parámetro iteraciones."""
    if iteraciones == 0:
        return axioma
    for n in range(iteraciones):
        secuencia = ""
        for c in axioma:
            secuencia += reglas.get(c, c)
        axioma = secuencia
    return secuencia

def analizar_secuencia(instrucciones, codificaciones):
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
            ultima_posicion = tortuga_tope.conseguir_posicion() #Preguntar a Essaya para que sirven los métodos de tipo "class.getA()"

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
        
    return trazos, coordenada_min + Vector(-50, -50), coordenada_max + Vector(50, 50)

def calcular_min(vectorA, vectorB):
    x_min = min(vectorA[0], vectorB[0])
    y_min = min(vectorA[1], vectorB[1])

    return Vector(x_min, y_min)

def calcular_max(vectorA, vectorB):
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
