class Pila:
	"""Representa una pila con los métodos: apilar, desapilar, esta_vacia y ver_tope."""

	def __init__(self):
		"""Crea una pila vacía."""
		self.tope = None
		self.len = 0

	def apilar(self, dato):
		"""Agrega un elemento al tope de la pila."""
		self.len += 1
		nodo = _Nodo(dato, self.tope)
		self.tope = nodo

	def desapilar(self):
		"""Desapila el elemento que se encuentra en el tope de la pila y lo devuelve."""
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
<<<<<<< HEAD
		return self.tope.dato

	def __len__(self):
		return self.len

class EmptyStack(Exception):
    pass

class _Nodo:
	def __init__(self, dato, prox = None):
		self.dato = dato
		self.prox = prox
=======
		if self.esta_vacia():
			return
		return self.items[-1]

	def __len__(self):
		"""Devuelve la cantidad de elementos de una pila."""
		return len(self.items)
>>>>>>> aa8d87784114dd33bb6fa01011fd4bd9cfde4803
