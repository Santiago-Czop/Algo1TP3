from sys import argv
from csv import reader
from vector import Vector
from tortuga import Tortuga
from pila import Pila
import math
import copy

PROGRAMA = 0
ARCHIVO_SL = 1
ITERACIONES = 2
ARCHIVO_SVG = 3

DISTANCIA = 100
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

    acciones = {
        "+" : angulo,
        "-" : -angulo,
        "|" : math.pi,
        "F" : DISTANCIA,
        "f" : 
    }

    resultado = obtener_resultado(axioma, reglas, int(argv[ITERACIONES]))
    escribir_svg(resultado)

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

def recorrer_lista(instrucciones, dict_acciones):
    coordenada_min = Vector()
    coordenada_max = Vector()


    pila_de_tortugas = list()
    pila_de_tortugas.append(Tortuga())

    tortuga_tope = pila_de_tortugas[-1]
    profundidad = len(pila_de_tortugas)

    for c in lista:
        if c == "[":
            nueva_tortuga = copy.deepcopy(tortuga_tope)
            pila_de_tortugas.append(nueva_tortuga)
            tortuga_tope = pila_de_tortugas[-1]
            profundidad = len(pila_de_tortugas)
        elif c == "]":
            pila_de_tortugas.pop()
            tortuga_tope = pila_de_tortugas[-1]
            profundidad = len(pila_de_tortugas)
        elif c == "F":
            tortuga_tope.avanzar(dict_acciones[c])
        elif c == "f":
            tortuga_tope.levantar_pluma()
            tortuga_tope.avanzar(DISTANCIA*FACTOR_EXPANSION*profundidad))
        elif c in "+-|":
            tortuga_tope.girar(dict_acciones[c])
        elif c 
        

    """
    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0
    
    #TODO Crear clase vector para facilitar

    pila_con_posiciones_donde_aparecen_tortugas

    for nodo in lista:
        #PROCESAMIENTO
        if nodo in "[]":
            apilar_o_desapilar
            continue
        if nodo in "+-":
            girar_tortuga
            continue
        tortuga = leer_tope_pila  
        posicion nueva = calcular_posicion_nueva(nodo, len_pila)
        calcular si es nuevo maximo o minimo
        guardar_informacion_trazo
        cambiar_posicion_tortuga = posicion_nueva
    """

def escribir_svg(lista):
    """
    crear_Viewbox()
    pila_de_tortugas Pila()#TODO len
    trazos = Lista_De_trazos #TODO Crear clase trazo
    recorrer_lista(lista, pila)
    for trazo in trazos:
        dibujar_linea()
    """
     
def calcular_posicion_nueva():
    """
    NORMA_BASE = Cte
    norma_tortuga = norma_base/len_pila * factor de achicamiento
    posicion_original = posicion_tortuga
    posicion_nueva = posicion_original + (x= sin alfa * norma_tortuga, y= cos alfa * norma tortuga)
    return posicion_nueva
    
"""

main()
