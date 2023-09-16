# Demonstração do método transpose

import sys
sys.path.append("..")
from LinearAlgebra import LinearAlgebra
from Matrix import Matrix

A = [
	[1, 2, 1],
	[1, 3, 0],
]

linear = LinearAlgebra()
matriz = Matrix(2, 3, A)

matriz_transposta = linear.transpose(matriz)

linear.print_matrix(matriz_transposta)