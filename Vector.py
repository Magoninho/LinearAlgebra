import numpy as np 
import matplotlib.pyplot as plt

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

	def plot(self, origin_vector, color='b'):
		plt.quiver(origin_vector.elements[0], origin_vector.elements[1], self.elements[0], self.elements[1], color='b', units='xy', angles='xy', scale_units='xy', scale=1) 