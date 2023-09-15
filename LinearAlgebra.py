from Matrix import Matrix
from Vector import Vector

A = [
	[1, 2, 1],
	[1, 3, 0],
]


B = [
	[2],
	[6],
	[1]
]

class LinearAlgebra:
	def transpose(self, a):
		rows = len(a)
		cols = len(a[0])

		temp = a.copy()
		for i in range(rows):
			temp[i] = a[i].copy()
			for j in range(cols):
				a[i][j] = temp[j][i]

		return a

	def sum(self, a, b):

		# Se forem dois vetores sendo somados
		if isinstance(a, Vector) and isinstance(b, Vector):
			rows_a = len(a.get_elements())
			rows_b = len(b.get_elements())

			if rows_a != rows_b and cols_a != cols_b:
				raise ValueError("Erro: Vetores com ordens diferentes! Estude mais!")
		

			arr = []
			for i in range(rows_a):
				arr.append(0)
			final_sum = Vector(rows_a, arr)

			for i in range(rows_a):
				final_sum.set(i, a.get_elements()[i] + b.get_elements()[i])

			return final_sum

		# Se forem matrizes
		else:

			rows_a = len(a.get_matrix())
			cols_a = len(a.get_matrix()[0])

			rows_b = len(b.get_matrix())
			cols_b = len(b.get_matrix()[0])

			if rows_a != rows_b and cols_a != cols_b:
				raise ValueError("Erro: Matrizes com ordens diferentes! Estude mais!")

			# Somando os elementos

			# Criando um array para ser passado para a matriz final_sum,
			# onde vai ser armazenado a soma das duas matrizes.
			arr = []
			for i in range(rows_a):
				arr.append([])
				for j in range(cols_a):
					arr[i].append(0)
			final_sum = Matrix(rows_a, cols_a, arr)


			for i in range(rows_a):
				for j in range(cols_a):
					final_sum.set(i, j, a.get_matrix()[i][j] + b.get_matrix()[i][j])
			return final_sum

	def gauss(self, a):
		matrix = a.get_matrix()
		rows = len(matrix)
		cols = len(matrix[0])

		for row in range(rows):
			# Armazenar o pivô diagonal para dividir a linha por ele, com o objetivo de deixá-lo sempre com o valor 1.
			pivot = matrix[row][row]

			# Se o pivô for 0, trocar a posição da linha atual com a debaixo e terminar o loop, se esta não for zero também.
			# Caso na linha de baixo o valor também seja zero, então avance para a proxima linha.
			if pivot == 0:
				for i in range(row + 1, rows):
					if matrix[i][row] != 0:
						# Trocando de posição as linhas
						matrix[row], matrix[i] = matrix[i], matrix[row]
						pivot = matrix[row][row] # Atualizando o pivô
						break
			
			# Mesmo se depois de todas essas trocas de linha, o pivô continuar zero,
			# então a matriz não pode ser escalonada
			if pivot == 0:
				raise ValueError("Não foi possível escalonar a matriz. Sistema Impossível.")

			# Se o pivô inicial não for zero, então podemos continuar
			# Precisamos dividir toda a linha atual pelo pivô, a fim de transformar o pivô em 1
			for j in range(cols):
				matrix[row][j] /= pivot
					
			# Vamos precisar realizar operações nas linhas para zerar os valores abaixo do pivô atual
			# Linha[row + 1] - Linha[row] * Matriz[row + 1][row]

			# Para cada linha abaixo do pivô...
			for i in range(row + 1, rows):
				factor = matrix[i][row]
				for j in range(cols):
					matrix[i][j] -= factor * matrix[row][j]
		return Matrix(rows, cols, matrix)
	

	def solve(self, a):
		# Escalonamos a matriz usando o método de Gauss
		reducted_matrix = self.gauss(a).get_matrix()

		rows = a.rows
		cols = a.cols

		# Agora, para obtermos a solução das icógnitas do sistema
		# precisamos multiplicar cada linha da matriz pelo fator novamente, porém,
		# dessa vez, vamos multiplicar para elementos acima do pivô também
		for row in range(rows):
			for i in range(rows):
				if row != i:
					factor = reducted_matrix[i][row]
					for j in range(cols):
						reducted_matrix[i][j] -= factor * reducted_matrix[row][j]
		return Matrix(rows, cols, reducted_matrix)
	

	def dot(self, a, b):

		# Se duas matrizes forem multiplicadas.

		if isinstance(a, Matrix) and isinstance(b, Matrix):
			rows_a = a.rows
			cols_a = a.cols

			rows_b = b.rows
			cols_b = b.cols

			if rows_b != cols_a:
				raise ValueError("Erro: Matrizes não encaixam para multiplicação! Estude mais!")

			result = []
			rows = a.rows
			cols = b.cols

			matrix_a = a.get_matrix()
			matrix_b = b.get_matrix()
			# Criando um array para o resultado e preenchendo com zeros
			arr = []
			for i in range(rows):
				arr.append([])
				for j in range(cols):
					arr[i].append(0)

			for i in range(rows):
				for j in range(cols):
					for k in range(b.rows):
						arr[i][j] += matrix_a[i][k] * matrix_b[k][j]

			for r in arr:
				result.append(r)

			return Matrix(len(result), len(result[0]), result)

		
		
		
		
		# Se uma matriz for multiplicada por um vetor.
		
		elif isinstance(a, Matrix) and isinstance(b, Vector):
			rows_a = a.rows
			cols_a = a.cols

			rows_b = b.dim

			if cols_a != rows_b:
				raise ValueError("Erro: Matriz fornecida não possui número de colunas igual ao número de linhas do vetor. Estude mais!")
			
			result = []
			for _ in range(rows_a):
				result.append(0)
			
			for i in range(rows_a):
				for j in range(cols_a):
					result[i] += a.get_matrix()[i][j] * b.get_elements()[j]

			return Matrix(len(result), 1, result)
	

	def times(self, a, b) -> Matrix | Vector:
		"""
		matriz - matriz (v)
		matriz - vetor (v)
		escalar - matriz (v)
		escalar - vetor (v)

		"""
		# Se duas matrizes forem multiplicadas elemento a elemento

		if isinstance(a, Matrix) and isinstance(b, Matrix):
			rows_a = a.rows
			cols_a = a.cols

			rows_b = b.rows
			cols_b = b.cols

			if rows_a != rows_b or cols_a != cols_b:
				raise ValueError("Erro: Não é possivel multiplicar essas matrizes elemento a elemento. Não possuem as mesmas ordens. Estude mais!")
			
			result = []
			for i in range(rows_a):
				result.append([])
				for j in range(cols_a):
					result[i].append(0)
			
			for i in range(rows_a):
				for j in range(cols_a):
					result[i][j] = a.get(i, j) * b.get(i, j)
			
			return Matrix(len(result), len(result[0]), result)
					
			
		# Se uma escalar for multiplicada por um vetor
		
		elif isinstance(a, (int, float)) and isinstance(b, Vector):
			rows_b = b.dim

			for i in range(rows_b):
				b.set(i, b.get(i) * a)

			return b
			
		# Se uma escalar for multiplicada por uma matriz

		elif isinstance(a, (int, float)) and isinstance(b, Matrix):
			rows_b = b.rows
			cols_b = b.cols

			for i in range(rows_b):
				for j in range(cols_b):
					b.set(i, j, b.get(i, j) * a)

			return b
		
		# Se uma matriz for multiplicada por um vetor.
		
		elif isinstance(a, Matrix) and isinstance(b, Vector):
			rows_a = a.rows
			cols_a = a.cols

			rows_b = b.dim

			if rows_a != rows_b or cols_a != 1:
				raise ValueError("Erro: Não é possivel multiplicar essas matrizes elemento a elemento. Não possuem as mesmas ordens. Estude mais!")
			
			result = []
			for i in range(rows_a):
				result.append([])
				for j in range(cols_a):
					result[i].append(0)

			for i in range(rows_a):
				element1 = a.get(i, 0)
				element2 = b.get(i)

				result[i][0] = element1 * element2

			return Matrix(len(result), len(result[0]), result)


	def print_matrix(self, matrix):
		for row in matrix.get_matrix():
			print(row)

	def print_vector(self, vector):
		print(vector.get_elements())

linear = LinearAlgebra()
minha_matriz = Matrix(len(A), len(A[0]), A)
minha_matriz2 = Matrix(len(B), len(B[0]), B)

# # linear.print_matrix(linear.gauss(minha_matriz))

# linear.print_matrix(linear.times(minha_matriz, minha_matriz2))

# # print(linear.sum(minha_matriz.get_matrix(), minha_matriz2.get_matrix()).get_matrix())


meu_vetor1 = Vector(3, [1, 2, 3])
meu_vetor2 = Vector(3, [3, 2, 1])

# linear.print_matrix(linear.times(minha_matriz, minha_matriz2))
linear.print_vector(linear.times(2, meu_vetor1))