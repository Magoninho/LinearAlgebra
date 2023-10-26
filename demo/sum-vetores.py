# Demonstração do método sum

import sys
sys.path.append("..")
from LinearAlgebra import LinearAlgebra
# from Matrix import Matrix
from Vector import Vector

import matplotlib.pyplot as plt
import numpy as np

A = [1, 2]

B = [2,	4]

linear = LinearAlgebra()
vetor1 = Vector(2, A)
vetor2 = Vector(2, B)

soma = linear.sum(vetor1, vetor2)

linear.print_vector(soma)

xpoints = np.array([soma.elements[0]])
ypoints = np.array([soma.elements[1]])

plt.xlim(0, 10) 
plt.ylim(0, 10) 

plt.grid()
plt.quiver([0], [0], [3], [6], color='b', units='xy', angles='xy', scale_units='xy', scale=1)
plt.show()