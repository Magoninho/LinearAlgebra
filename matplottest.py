import numpy as np 
import matplotlib.pyplot as plt 
from Vector import Vector
  
# Vector origin location 
origin_vector = Vector(2, [0, 0])
  
# Directional vectors 
my_vector = Vector(2, [2, 0])

rotated_vector = Vector(2, [0, 2])
  
# Creating plot 
my_vector.plot(origin_vector)
rotated_vector.plot(origin_vector)

# x-lim and y-lim 
plt.xlim(-2, 5) 
plt.ylim(-2, 3)
  
# Show plot with grid 
plt.grid() 
plt.show()