class Pila:
	"""Representa una pila con los métodos: apilar, desapilar, esta_vacia, ver_tope y len."""

	def __init__(self):
		"""Crea una pila vacía con los atributos tope y len."""
		self.tope = None
		self.len = 0

	def apilar(self, dato):
		"""Agrega un elemento al tope de la pila."""
		self.len += 1
		nodo = _Nodo(dato, self.tope)
		self.tope = nodo

	def desapilar(self):
		"""Desapila el elemento que se encuentra en el tope de la pila y lo devuelve. Si la pila está vacía, se muestra un mensaje."""
		if self.esta_vacia():
			raise EmptyStack("La pila no tiene elementos.")
		self.len -= 1
		elemento = self.tope.dato
		self.tope = self.tope.prox
		return elemento
		
	def esta_vacia(self):
		"""Devuelve True si la pila está vacía. De lo contrario, devuelve False."""
		return self.len == 0

	def ver_tope(self):
		"""Devuelve el elemento que se encuentra en el tope de la pila."""
		return self.tope.dato

	def __len__(self):
		"""Devuelve la cantidad de elementos que se encuentran en la pila."""
		return self.len

class EmptyStack(Exception):
    pass

class _Nodo:
	""" Representa un nodo con un dato y una conexión al elemento siguiente."""
	def __init__(self, dato, prox = None):
		""" Crea una instancia de Nodo."""
		self.dato = dato
		self.prox = prox
