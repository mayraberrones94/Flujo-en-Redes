from random import random, uniform, randint
from math import sqrt, pi, sin, cos, ceil, floor
import time

class Grafo:

	def __init__(self):
		self.V = set()
		self.E = dict()
		self.vecinos = dict()
		self.aristas = dict()
		self.n = None
		self.k = None
		self.techo = None

		self.P = []
		self.A = []
		self.B = []
		self.nodos = []

		self.nod2 = []
		self.nod3 = []

	def puntos (self, num, k):
		self.n = num
		self.k = k
		
		th = 2*(pi)/self.n
		with open ("grafica.dat", 'w') as salida:
			for i in range(self.n):
				x = sin(th*i)
				y = cos(th*i)
				self.P.append((x, y, i))

				print (x, y, i, file = salida)

	def k_conect(self, k):
		for uno in range(1, k +1):
			for dos in range(0, self.n):
				u = self.P[dos]
				v = self.P[dos - uno]
				self.aristas[(u, v)] = self.aristas[(v, u)] = uno
				self.agrega(u)
				self.agrega(v)
				self.vecinos[v].add(u)
				self.vecinos[u].add(v)


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
				if random() < prob and ((x1, y1),(x2,y2)) not in self.aristas and ((x2, y2), (x1,y1)) not in self.aristas:
					self.kmax = floor(self.n/2)
					d = abs(u-v)
					if d > self.kmax:
						d2 = self.n - d
						self.aristas[((x1, y1),(x2,y2))] = self.aristas[((x2, y2), (x1,y1))] = d2
					else:
						self.aristas[((x1, y1),(x2,y2))] = self.aristas[((x2, y2), (x1,y1))] = d
					self.agrega((x1, y1))
					self.agrega((x2, y2))
					self.vecinos[(x1, y1)].add((x2, y2))
					self.vecinos[(x2, y2)].add((x1, y1))
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
			for z in self.aristas:
				x1 = z[0][0]
				y1 = z[0][1]
				x2 = z[1][0]
				y2 = z[1][1]
				p = self.aristas[z]
				if p > self.k:
					print('set arrow', id, 'from', x1, ',', y1 , 'to', x2 , ',', y2 , 'nohead lw 1 lc 3', file = salida)
				else:
					print('set arrow', id, 'from', x1, ',', y1 , 'to', x2 , ',', y2 , 'nohead lw 1', file = salida)
				id += 1
			print('plot "grafica.dat" using 1:2:3 with points pt 7 ps 2 lc var ', file = salida)
			print('quit()', file = salida)




