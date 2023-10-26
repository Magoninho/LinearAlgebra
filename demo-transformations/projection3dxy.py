import sys
sys.path.append("..")
from Transformations import Transformations
import numpy as np 
import matplotlib.pyplot as plt
import VectorRenderer

# Declaro um vetor
meu_vetor = [2, 2, 2]

# Projeto esse vetor no plano xy
projected_vector = Transformations.project3DXY(meu_vetor)


print(projected_vector)