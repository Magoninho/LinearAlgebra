import sys
sys.path.append("..")
from Transformations import Transformations
import numpy as np 
import matplotlib.pyplot as plt
import VectorRenderer

# Declaro um vetor
meu_vetor = [4, 0]

# Renderizo esse vetor na cor azul
VectorRenderer.plot(meu_vetor, color='blue')

# Rotaciono esse vetor em 90 graus
rotated_vector = Transformations.rotation2D(meu_vetor, 45)

# Renderizo esse vetor rotacionado na cor vermelha
VectorRenderer.plot(rotated_vector, color='red')

# RENDERIZAÇÃO #

# x-lim and y-lim 
plt.xlim(-2, 5) 
plt.ylim(-2, 5)

plt.gca().set_aspect('equal')
  
# Show plot with grid 
plt.grid() 
plt.show()