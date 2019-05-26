class ListaEnlazada:
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

class _Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox

class Tortuga:
    def __init():

class Vector:
    def __init__():
        self.x
        self.y

    def __add__(self, norma, angulo)
        return Vector() #Operar

class Pluma:
    def __init__():
        self.estado
        self.grosor
        self.color

class Pila:
    def __init__():

class Trazo:
    def __init__():
        self.grosor
        self.vector_inicial

def main():
    procesar_y_leer_archivos()
    
    func()

    escribir_svg()

def procesar_y_leer_archivos():
    leer_sl()
    crear_diccionario()
    
    return diccionario_de_reglas, axioma, angulo, alfabeto

def func(anterior, lista, d, n):
    #Llevar la cuenta
    if n == 0:
        return


    for nodo in listaenlazada:
        lista.reemplazar(anterior, nodo, d[nodo.dato])
        n -= 1
        func(anterior, lista, d, n)

        anterior = nodo

def recorrer_lista(lista)
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

def escribir_svg(lista):
    crear_Viewbox()
    pila_de_tortugas Pila()#TODO len
    trazos = Lista_De_trazos #TODO Crear clase trazo
    recorrer_lista(lista, pila)
    for trazo in trazos:
        dibujar_linea()
     
def calcular_posicion_nueva()
    NORMA_BASE = Cte
    norma_tortuga = norma_base/len_pila * factor de achicamiento
    posicion_original = posicion_tortuga
    posicion_nueva = posicion_original + (x= sin alfa * norma_tortuga, y= cos alfa * norma tortuga)
    return posicion_nueva
