# Demonstração do método sum

import sys
sys.path.append("..")
from LinearAlgebra import LinearAlgebra
# from Matrix import Matrix
from Vector import Vector

A = [1, 2, 1]

B = [2,	4, 2]

linear = LinearAlgebra()
vetor1 = Vector(3, A)
vetor2 = Vector(3, B)

soma = linear.sum(vetor1, vetor2)

linear.print_vector(soma)