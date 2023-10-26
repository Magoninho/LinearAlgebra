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

# Projeto esse vetor em relação ao eixo x
projected_vector = Transformations.project2DX(meu_vetor)

# Renderizo esse vetor refletido na cor vermelha
VectorRenderer.plot(projected_vector, color='red')

# RENDERIZAÇÃO #

# x-lim and y-lim 
plt.xlim(-2, 5) 
plt.ylim(-2, 5)

plt.gca().set_aspect('equal')
  
# Show plot with grid 
plt.grid() 
plt.show()