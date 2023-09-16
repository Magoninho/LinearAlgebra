# Demonstração do método solve

import sys
sys.path.append("..")
from LinearAlgebra import LinearAlgebra
from Matrix import Matrix

A = [
	[2, 2, 3, 1],
	[1, 2, 1, 0],
	[1, -1, 1, 0]
]

# essa é impossivel
B = [
	[1, 2, 3, 1],
	[4, 7, 7, 3],
	[2, 3, 1, 0]
]

linear = LinearAlgebra()
matriz = Matrix(3, 4, A)

matriz_escalonada = linear.solve(matriz)

linear.print_matrix(matriz_escalonada)