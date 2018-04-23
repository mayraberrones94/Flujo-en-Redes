from random import random, uniform, randint
from math import sqrt, ceil, floor

class Grafo:

	def __init__(self):
		self.k = None
		self.nodos = []
		self.aristas = dict()
		self.vecinos = dict()

	def puntos(self, k):
		self.k = k
		with open("grafica.dat", 'w') as salida:

			for i in range(0, k):
				for j in range(0, k):
					x = i
					y = j
					self.nodos.append((x, y))
					print(x, y, file = salida)
					if not (x, y) in self.vecinos:
						self.vecinos[(x,y)] = []

	def conexiones(self):
		for i in range(0, self.k):
			for j in range(0, self.k):
				u = self.nodos[i]
				v = self.nodos[j]
				


	def grafica(self, eps = True):
		with open("nodos.plot", 'w') as salida:

			if eps:
				print("set term postscript color eps", file = salida)
				print('set output "nodos.eps"', file = salida)
			else:
				print('set term png', file = salida)
				print('set output "nodos.png"', file = salida)
			print('set size square', file = salida)
			print('set key off', file = salida)
			print('set xrange [-1:', self.k , ']', file = salida)
			print('set yrange [-1:', self.k , ']', file = salida)
			print('plot "grafica.dat" using 1:2 with points pt 7 ps 2 ', file = salida)
			print('quit()', file = salida)

p = Grafo()
p.puntos(5)
p.grafica()



