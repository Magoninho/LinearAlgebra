from Matrix import Matrix
from Vector import Vector

A = [
	[1, 2, 1],
	[1, 3, 0],
]


B = [
	[2, 5],
	[6, 7],
	[1, 8]
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

		rows = a.get_elements()
		cols = a.get_elements()

		if len(a) != len(b) and len(a[0]) != len(b[0]):
			print("Erro: Matrizes/Vetores com ordens diferentes! Estude mais!")
			return
		

		# Se forem dois vetores sendo somados
		if isinstance(a, Vector) and isinstance(b, Vector):
			arr = []
			for i in range(len(a)):
				arr.append([])
				for j in range(len(a)):
					arr[i].append(0)
			final_sum = Vector(len(a), arr)

			final_sum.set(0, 1, 1)
			for i in range(len(a)):
				for j in range(len(a)):
					final_sum.set(i, j, a[i][j] + b[i][j])

			return final_sum

		# Se forem matrizes
		else:
			# Somando os elementos

			# Criando um array para ser passado para a matriz final_sum,
			# onde vai ser armazenado a soma das duas matrizes.
			arr = []
			for i in range(len(a)):
				arr.append([])
				for j in range(len(a)):
					arr[i].append(0)
			final_sum = Matrix(len(a), len(a), arr)

			final_sum.set(0, 1, 1)
			for i in range(len(a)):
				for j in range(len(a)):
					final_sum.set(i, j, a[i][j] + b[i][j])

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
				print("Não foi possível escalonar a matriz. Sistema Impossível.")
				exit()
				return None

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
	

	def times(self, a, b):
		if isinstance(a, Matrix) and isinstance(b, Matrix):
			# TODO: fazer a checagem
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

	
	def print_matrix(self, matrix):
		for row in matrix.get_matrix():
			print(row)

linear = LinearAlgebra()
# minha_matriz = Matrix(len(A), len(A[0]), A)
# minha_matriz2 = Matrix(len(B), len(B[0]), B)

# # linear.print_matrix(linear.gauss(minha_matriz))

# linear.print_matrix(linear.times(minha_matriz, minha_matriz2))

# # print(linear.sum(minha_matriz.get_matrix(), minha_matriz2.get_matrix()).get_matrix())


meu_vetor1 = Vector(3, [1, 2, 3])
meu_vetor2 = Vector(3, [3, 2, 1])

linear.sum(meu_vetor1, meu_vetor2)