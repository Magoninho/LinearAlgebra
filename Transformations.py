import numpy as np
import math

class Transformations:
	# Translation
	@staticmethod
	def translate2D(vector, dx, dy):
		homogeneous_vector = vector.copy()
		homogeneous_vector.append(1)

		translation_matrix = np.array([
			[1, 0, dx],
			[0, 1, dy],
			[0, 0, 1]
		])

		return np.delete(np.matmul(translation_matrix, homogeneous_vector), -1)

	@staticmethod
	def translate3D(vector, dx, dy, dz):
		homogeneous_vector = vector.copy()
		homogeneous_vector.append(1)
		
		translation_matrix = np.array([
			[1, 0, 0, dx],
			[0, 1, 0, dy],
			[0, 0, 1, dz],
			[0, 0, 0, 1]
		])

		return np.delete(np.matmul(translation_matrix, homogeneous_vector), -1)

	# Rotation
	@staticmethod
	def rotation2D(vector, angle):
		angle_radians = math.radians(angle)
		rotation_matrix = np.array([
			[math.cos(angle_radians), -math.sin(angle_radians)],
			[math.sin(angle_radians), math.cos(angle_radians)]
		])

		return np.matmul(rotation_matrix, vector)
	
	@staticmethod
	def rotation3DX(vector, angle):
		angle_radians = math.radians(angle)
		rotation_matrix = np.matrix([
			[1, 0, 0],
			[0, math.cos(angle_radians), -math.sin(angle_radians)],
			[0, math.sin(angle_radians), math.cos(angle_radians)]
		])

		return np.matmul(rotation_matrix, vector)
	
	@staticmethod
	def rotation3DY(vector, angle):
		angle_radians = math.radians(angle)
		rotation_matrix = np.matrix([
			[math.cos(angle_radians), 0, math.sin(angle_radians)],
			[0, 1, 0],
			[-math.sin(angle_radians), 0, math.cos(angle_radians)]
		])

		return np.matmul(rotation_matrix, vector)

	@staticmethod
	def rotation3DZ(vector, angle):
		angle_radians = math.radians(angle)
		rotation_matrix = np.matrix([
			[math.cos(angle_radians), -math.sin(angle_radians), 0],
			[math.sin(angle_radians), math.cos(angle_radians), 0],
			[0, 0, 1]
		])

		return np.matmul(rotation_matrix, vector)
	
	# Reflection
	@staticmethod
	def reflection2DX(vector):
		reflection_matrix = np.array([
			[1,  0],
			[0, -1]
		])

		return np.matmul(reflection_matrix, vector)

	@staticmethod
	def reflection2DY(vector):
		reflection_matrix = np.array([
			[-1, 0],
			[ 0, 1]
		])

		return np.matmul(reflection_matrix, vector)
	
	@staticmethod
	def reflection3DX(vector):
		reflection_matrix = np.array([
			[-1, 0, 0],
			[ 0, 1, 0],
			[ 0, 0, 1]
		])

		return np.matmul(reflection_matrix, vector)

	@staticmethod
	def reflection3DY(vector):
		reflection_matrix = np.array([
			[1, 0, 0],
			[0,-1, 0],
			[0, 0, 1]
		])

		return np.matmul(reflection_matrix, vector)

	@staticmethod
	def reflection3DZ(vector):
		reflection_matrix = np.array([
			[1, 0, 0],
			[0, 1, 0],
			[0, 0,-1]
		])

		return np.matmul(reflection_matrix, vector)

	# Projection
	@staticmethod
	def project2DX(vector):
		projection_matrix = np.array([
			[1, 0],
			[0, 0],
		])

		return np.matmul(projection_matrix, vector)

	@staticmethod
	def project2DY(vector):
		projection_matrix = np.array([
			[0, 0],
			[0, 1],
		])

		return np.matmul(projection_matrix, vector)

	@staticmethod
	def project3DX(vector):
		projection_matrix = np.array([
			[0, 0, 0],
			[0, 1, 0],
			[0, 0, 1],
		])

		return np.matmul(projection_matrix, vector)

	@staticmethod
	def project3DY(vector):
		projection_matrix = np.array([
			[1, 0, 0],
			[0, 0, 0],
			[0, 0, 1],
		])

		return np.matmul(projection_matrix, vector)

	@staticmethod
	def project3DZ(vector):
		projection_matrix = np.array([
			[1, 0, 0],
			[0, 1, 0],
			[0, 0, 0],
		])

		return np.matmul(projection_matrix, vector)

	@staticmethod
	def shearing(vector, kx, ky):
		shearing_matrix = np.array([
			[1, kx],
			[ky, 1],
		])

		return np.matmul(shearing_matrix, vector)


