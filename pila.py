class Pila:
	"""Representa una pila con los métodos: apilar, desapilar, esta_vacia y ver_tope."""

	def __init__(self):
		"""Crea una pila vacía."""
		self.items = []

	def apilar(self, elemento):
		"""Agrega un elemento al tope de la pila."""
		self.items.append(elemento)

	def desapilar(self):
		"""Desapila el elemento que se encuentra en el tope de la pila y lo devuelve."""
		if self.esta_vacia():
			return
		return self.items.pop()

	def esta_vacia(self):
		"""Devuelve True si la pila está vacía. De lo contrario, devuelve False."""
		return len(self.items) == 0

	def ver_tope(self):
		"""Devuelve el elemento que se encuentra en el tope de la pila."""
		if self.esta_vacia():
			return
		return self.items[-1]

	def len(self):
		"""Devuelve la cantidad de elementos de una pila."""
		return len(self.items)
