# Demonstração do método times

import sys
sys.path.append("..")
from LinearAlgebra import LinearAlgebra
from Matrix import Matrix

A = [
	[2, 2, 3, 1],
	[1, 2, 1, 0],
	[1, -1, 1, 0]
]

B = [
	[1, 2, 3, 1],
	[4, 7, 7, 3],
	[2, 3, 1, 0]
]

linear = LinearAlgebra()
matriz1 = Matrix(3, 4, A)
matriz2 = Matrix(3, 4, B)

matriz_multiplicada_elemento_a_elemento = linear.times(matriz1, matriz2)

linear.print_matrix(matriz_multiplicada_elemento_a_elemento)