---
title: Cenário 1
author: João Felipe Ribeiro, Matheus Vasconselos, Samir Albano, Maria Karime Nóbrega, Erich Lima Schlaepfer
date: FRI 2023, 2023-09-15
theme: serif
header-includes: |
    <style>
      .reveal {
      font-size: 20pt;
      line-height: 1.2em;
    }
     .reveal pre code {
      font-size: 16pt;
      line-height: 1.2em;
    }
    </style>
...

## Biblioteca de Álgebra Linear em Python

###

Equipe: João Felipe Ribeiro, Matheus Vasconselos, Samir Albano, Maria Karime Nóbrega, Erich Lima Schlaepfer

# Classe Matrix

##

```python
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

```

