class Vector:
	def __init__(self, dim, elements) -> None:
		self.dim = dim
		if len(elements) > self.dim:
			raise ValueError("Erro: Número de elementos maior que a dimensão do vetor.")
		self.elements = elements
	
	def get(self, i):
		return self.elements[i]
	
	def get_elements(self):
		return self.elements

	def set(self, i, value):
		self.elements[i] = value