from random import random
from sys import stdout

class Grafo:
 
	def __init__(self):
		self.n = None
		self.x = dict()
		self.y = dict()
		self.P = []
		self.archivo = None

	def puntos(self, num):
		self.n = num
		for nodo in range(self.n):
			self.x[nodo] = random() 
			self.y[nodo] = random() 

	def imprimir(self, arch):
		self.archivo = arch
		with open (self.archivo, "w") as salida:
			for nodo in range(self.n):
				print(self.x[nodo], self.y[nodo], file = salida)
		print(self.archivo)

	def aristas(self, prob):
		for nodo in range(self.n - 1):
			for nodo2 in range(nodo + 1, self.n):
				if random() < prob:
					self.P.append((nodo, nodo2))
		print(len(self.P))


	def grafica(self, plot):
		assert self.archivo is not None
		with open(plot, 'w') as salida: 
			print('set term poscript eps', file = salida)
			print('set output "nodos.eps"', file = salida)
			print('set size square', file = salida)
			print('set key off', file = salida)
			print ('set xrange [-.1:1.1]', file = salida)
			print ('set yrange [-.1:1.1]', file = salida)
			id = 1
			for(v, w) in self.P:
				x1 = self.x[v]
				x2 = self.x[w]
				y1 = self.y[v]
				y2 = self.y[w]
				print('set arrow', id, 'from', x1, ',', y1, 'to', x2, ',', y2, 'nohead', file = salida)
				id +=1
			print('plot', self.archivo, 'using 1:2 with points pt 7', file = salida)
			print('quit()', file =  salida)


