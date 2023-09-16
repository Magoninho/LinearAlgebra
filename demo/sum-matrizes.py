# Demonstração do método sum

import sys
sys.path.append("..")
from LinearAlgebra import LinearAlgebra
from Matrix import Matrix

A = [
	[1, 2, 1],
	[1, 3, 0],
]

B = [
	[2,	4, 2],
	[2,	4, 2]
]

linear = LinearAlgebra()
matriz1 = Matrix(2, 3, A)
matriz2 = Matrix(2, 3, B)

soma = linear.sum(matriz1, matriz2)

linear.print_matrix(soma)