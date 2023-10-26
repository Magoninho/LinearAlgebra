import sys
sys.path.append("..")
from Transformations import Transformations
import numpy as np 
import matplotlib.pyplot as plt
import VectorRenderer

# Declaro um vetor
meu_vetor = [2, 2, 1]

# Renderizo esse vetor na cor azul
VectorRenderer.plot(meu_vetor, color='blue')

# Projeto esse vetor em relação ao eixo x
projected_vector = Transformations.project3DZ(meu_vetor)

print(projected_vector)