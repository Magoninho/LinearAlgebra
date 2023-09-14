from Matrix import Matrix
A = [
	[2, 2, 3, 1],
	[1, 2, 1, 0],
	[1, -1, 1, 0],
]

def gauss(a):
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
			print("Não foi possível escalonar a matriz")
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
		

	return matrix


def solve(a):
	# Escalonamos a matriz usando o método de Gauss
	reducted_matrix = gauss(a)

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
	return reducted_matrix

minha_matriz = Matrix(3, 4, A)
print(solve(minha_matriz))
# print(gauss(minha_matriz))