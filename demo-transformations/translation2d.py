import sys
sys.path.append("..")
from Transformations import Transformations
import numpy as np 
import matplotlib.pyplot as plt
import VectorRenderer

# Declaro um vetor
meu_vetor = [2, 2]

# Renderizo esse vetor na cor azul
VectorRenderer.plot(meu_vetor, color='blue')

# Translaciono esse vetor em 2 dx e 1 dy
translated_vector = Transformations.translate2D(meu_vetor, 2, 1)

# Renderizo esse vetor rotacionado na cor vermelha
VectorRenderer.plot(translated_vector, color='red')

# RENDERIZAÇÃO #

# x-lim and y-lim 
plt.xlim(-2, 5) 
plt.ylim(-2, 5)

plt.gca().set_aspect('equal')
  
# Show plot with grid 
plt.grid() 
plt.show()