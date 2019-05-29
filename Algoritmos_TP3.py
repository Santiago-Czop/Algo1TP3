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
    if len(argv) != 4:
        raise IndexError(f"El programa {argv[PROGRAMA]} debe recibir 3 parámetros.")
    elif argv[ARCHIVO_SL][-3:].lower() != ".sl":
        raise Exception("El primer parámetro debe ser el nombre de un archivo .sl")
    elif not argv[ITERACIONES].isdigit():
        raise TypeError("El segundo parámetro debe ser un número entero mayor o igual a cero.")
    elif argv[ARCHIVO_SVG][-4:].lower() != ".svg":
        raise Exception("El tercer parámetro debe ser el nombre de un archivo .svg")

def cargar_archivo(ruta_archivo):
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
    if cantidad == 0:
        return cadena
    else:
        resultado = ""
        for c in cadena:
            resultado += reglas.get(c, c)
        cantidad -= 1
        resultado = obtener_resultado(resultado, reglas, cantidad)
        return resultado

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
    vectores = (vectorA, vectorB)
    x_min = min(vectores, key=lambda v: v[0])
    y_min = min(vectores, key=lambda v: v[1])

    return Vector(x_min, y_min)

def calcular_max(vectorA, vectorB):
    vectores = (vectorA, vectorB)
    x_max = max(vectores, key=lambda v: v[0])
    y_max = max(vectores, key=lambda v: v[1]) 

    return Vector(x_max, y_max)

def crear_svg(ruta_archivo, trazos, coord_min, coord_max):
    with open(ruta_archivo, 'w') as archivo:
        archivo.write(f'<svg viewBox="{coord_min[0]} {coord_min[1]} {coord_max[0] - coord_min[0]} {coord_max[1] - coord_min[1]}" xmlns="http://www.w3.org/2000/svg">' + "\n")
        for trazo in trazos:
            archivo.write(f'<line x1="{trazo.coord_inicial[0]}" y1="{trazo.coord_inicial[1]}" x2="{trazo.coord_final[0]}" y2="{trazo.coord_final[1]}" stroke-width="{trazo.grosor}" stroke="{trazo.color}" />' + "\n")
        archivo.write('</svg>' + "\n")

main()
