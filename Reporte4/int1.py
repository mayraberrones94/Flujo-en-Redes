from random import random, uniform, randint
from math import sqrt, pi, sin, cos
import time

class Grafo:

	def __init__(self):
		self.V = set()
		self.E = dict()
		self.vecinos = dict()
		self.n = None
		self.P = []
		self.A = []
		self.B = []
		self.nodos = []

		self.nod2 = []
		self.nod3 = []

	def puntos (self, num):

		self.n = num
		th = 2*(pi)/self.n
		with open ("grafica.dat", 'w') as salida:
			for i in range(self.n):
				x = sin(th*i)
				y = cos(th*i)
				self.P.append((x, y, i))
				print (x, y, i, file = salida)

	def agrega (self, v):
		self.V.add(v)
		self.nodos.append(v)
		if not v in self.vecinos:
			self.vecinos[v] = set()

	def conecta (self, prob):
		for i in range(self.n -1):
			self.nod2.append(self.P[i])
		for i in range(self.n):
			self.nod3.append(self.P[i])

		for(x1, y1, u) in self.nod2:
			del self.nod3[0]
			for(x2, y2, v) in self.nod3:
				if random() < prob:
					self.agrega(u)
					self.agrega(v)
					self.vecinos[v].add(u)
					self.vecinos[u].add(v)
					self.A.append((x1, y1, x2, y2, u, v))



	def graficar (self, eps = True):
		with open("nodos.plot", 'w') as salida:
			if eps:
				print("set term postscript color eps", file = salida)
				print('set output "nodos.eps"', file = salida)
			else:
				print('set term png', file = salida)
				print('set output "nodos.png"', file = salida)
			print('set size square', file = salida)
			print('set key off', file = salida)
			print('set xrange [-1.1:1.1]', file = salida)
			print('set yrange [-1.1:1.1]', file = salida)
			id = 1
			for i in range (len(self.A)):
				print('set arrow', id, 'from', self.A[i][0], ',', self.A[i][1] , 'to', self.A[i][2] , ',', self.A[i][3] , 'nohead filled lw 1 lc 2', file = salida)
				id += 1
			print('plot "grafica.dat" using 1:2:3 with points pt 7 ps 2 lc var ', file = salida)
			print('quit()', file = salida)




