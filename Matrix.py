class Matrix:
	def __init__(self, rows, cols, elements) -> None:
		self.rows = rows
		self.cols = cols
		self.matrix = elements


	def get(self, i, j):
		return self.matrix[i][j]
	
	def get_matrix(self):
		return self.matrix

	def set(self, i, j, value):
		self.matrix[i][j] = value