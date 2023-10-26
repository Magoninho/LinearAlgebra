import sys
sys.path.append("..")
from Transformations import Transformations
import numpy as np 
import matplotlib.pyplot as plt
import VectorRenderer

# Declaro um vetor
meu_vetor = [1, 2, 3]

# Renderizo esse vetor na cor azul
VectorRenderer.plot(meu_vetor, color='blue')

# Reflito esse vetor em relação ao eixo z
reflected_vector = Transformations.reflection3DZ(meu_vetor)

print(reflected_vector)