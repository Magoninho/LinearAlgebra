import sys
sys.path.append("..")
from Transformations import Transformations
import numpy as np 
import matplotlib.pyplot as plt
import VectorRenderer

# Declaro um vetor
meu_vetor = [1, 1]

# Renderizo esse vetor na cor azul
VectorRenderer.plot(meu_vetor, color='blue')

# Realizo um cisalhamento na direção do eixo x
sheared_vector = Transformations.shearing(meu_vetor, 2, 0)

# Renderizo esse vetor refletido na cor vermelha
VectorRenderer.plot(sheared_vector, color='red')

# RENDERIZAÇÃO #

# x-lim and y-lim 
plt.xlim(-2, 5) 
plt.ylim(-2, 5)

plt.gca().set_aspect('equal')
  
# Show plot with grid 
plt.grid() 
plt.show()