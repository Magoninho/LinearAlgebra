import numpy as np 
import matplotlib.pyplot as plt 


def plot(vector, originx=0, originy=0, color='b'):
	plt.quiver(originx, originy, vector[0], vector[1], color=color, units='xy', angles='xy', scale_units='xy', scale=1) 