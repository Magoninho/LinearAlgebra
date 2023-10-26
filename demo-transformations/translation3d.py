import sys
sys.path.append("..")
from Transformations import Transformations
import numpy as np 
import matplotlib.pyplot as plt
import VectorRenderer

# Declaro um vetor
meu_vetor = [3, 2, 1]

# Translaciono esse vetor em 1 dx, 1 dy e 2 dz
translated_vector = Transformations.translate3D(meu_vetor, 1, 1, 2)

print(translated_vector)