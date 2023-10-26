import sys
sys.path.append("..")
from Transformations import Transformations
import numpy as np 
import matplotlib.pyplot as plt
import VectorRenderer

# Declaro um vetor
meu_vetor = [2, 1, 2]

# Rotaciono esse vetor em 90 graus em torno do eixo z
rotated_vector = Transformations.rotation3DZ(meu_vetor, 90)


print(rotated_vector)