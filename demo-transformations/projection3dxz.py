import sys
sys.path.append("..")
from Transformations import Transformations
import numpy as np 
import matplotlib.pyplot as plt
import VectorRenderer

# Declaro um vetor
meu_vetor = [2, 2, 2]

# Projeto esse vetor no plano xz
rotated_vector = Transformations.project3DXZ(meu_vetor)


print(rotated_vector)