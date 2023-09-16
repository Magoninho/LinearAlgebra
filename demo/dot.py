# Demonstração do método dot

import sys
sys.path.append("..")
from LinearAlgebra import LinearAlgebra
from Matrix import Matrix

A = [
	[2, 2, 3],
	[1, 2, 1],
	[1, -1, 1]
]

B = [
	[1, 2, 3, 1],
	[4, 7, 7, 3],
	[2, 3, 1, 0]
]

linear = LinearAlgebra()
matriz1 = Matrix(3, 3, A)
matriz2 = Matrix(3, 4, B)

matriz_multiplicada = linear.dot(matriz1, matriz2)

linear.print_matrix(matriz_multiplicada)