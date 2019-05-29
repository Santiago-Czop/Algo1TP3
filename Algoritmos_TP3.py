from sys import argv
from csv import reader
from vector import Vector
from tortuga import Tortuga
import math
import copy

PROGRAMA = 0
ARCHIVO_SL = 1
ITERACIONES = 2
ARCHIVO_SVG = 3

DISTANCIA_BASE = 100
FACTOR_EXPANSION = 1.0

class ListaEnlazada:
    #Sirve de algo esta clase o la borramos?

    """
    def __init__(self):
        self.prim = None #AXIOMA

    def append(self, dato, prox = None):
        actual = self.prim
        nodo = _Nodo(dato)

        if not actual:
            self.prim = nodo
        else:
            while actual.prox:
                actual = actual.prox
            
            actual.prox = nodo
        
    def reemplazar(self, anterior, nodo, nuevo_dato):
        nuevo_bloque = ListaEnlazada()

        for c in nuevo_dato:
            nuevo_bloque.append(c)

        if not anterior:
            self.prim = nuevo_bloque[0]
        else:
            anterior.prox = nuevo_bloque[0]
        #TODO Hacer el reemplazador

    def __iter__(self):
        #TODO Hacer el iterador     
        return
    """

class _Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox

class Pila:
    #Preguntar si implementamos la nuestra o está permitido usar listas
    def __init__(self):
        self.prim = None

class Trazo:
    #Preguntar como trabajar bien el viewBox
    def __init__(self):
        self.grosor = 1
        self.vector_inicial = Vector()

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

    trazos, coordenada_min, coordenada_max = analizar_secuencia(instrucciones, codificaciones)

    escribir_svg(trazos, coordenada_min, coordenada_max)

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

    for c in lista:
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

def escribir_svg(trazos, coord_min, coord_max):
    
    crear_Viewbox()
    pila_de_tortugas = Pila()#TODO len
    trazos = Lista_De_trazos #TODO Crear clase trazo
    recorrer_lista(lista, pila)
    for trazo in trazos:
        dibujar_linea()
    
     
def calcular_posicion_nueva():
    
    NORMA_BASE = Cte
    norma_tortuga = norma_base/len_pila * factor de achicamiento
    posicion_original = posicion_tortuga
    posicion_nueva = posicion_original + (x= sin alfa * norma_tortuga, y= cos alfa * norma tortuga)
    return posicion_nueva
    
main()
