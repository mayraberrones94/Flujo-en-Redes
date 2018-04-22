from random import random, uniform, randint
from math import sqrt, pi, sin, cos, ceil, floor
import time

class Grafo:

	def __init__(self):
		self.V = set()
		self.vecinos = dict()
		self.aristas = dict()
		self.n = None
		self.k = None
		self.P = []
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
				self.nodos.append((x,y))
				print (x, y, i, file = salida)

	def k_conect(self, k):
		for uno in range(1, k +1):
			for dos in range(0, self.n):
				u = self.nodos[dos]
				v = self.nodos[dos - uno]
				self.aristas[(u, v)] = self.aristas[(v, u)] = uno
				self.agrega(u)
				self.agrega(v)
				self.vecinos[u].add(v)
				self.vecinos[v].add(u)


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


	def floyd_warshall (self): 
		self.d = {}
		for (x,y) in self.nodos:
			self.d[((x, y), (x, y))] = 0 # distancia reflexiva es cero
			for u in self.vecinos[(x, y)]: # para vecinos, la distancia es el peso
				self.d[((x,y),u)] = self.aristas[((x,y),u)]
		for intermedio in self.nodos:
			for desde in self.nodos:
				for hasta in self.nodos:
					di = None
					if (desde, intermedio) in self.d:
						di = self.d[(desde, intermedio)]
					ih = None
					if (intermedio, hasta) in self.d:
						ih = self.d[(intermedio, hasta)]
					if di is not None and ih is not None:
						c = di + ih # largo del camino via "i"
						if (desde, hasta) not in self.d or c < self.d[(desde, hasta)]:
							self.d[(desde, hasta)] = c # mejora al camino actual
		with open("Warshall.dat", "at") as archivo:
			print(self.d, file = archivo)
		return self.d

	def argdist(self):
		self.sumaDist = 0
		for i in self.d:
			self.sumaDist += self.d[i]
		self.promDist = self.sumaDist/len(self.d)
		self.promDist2 = self.sumaDist/((self.n * (self.n - 1))/ 2)
		self.arg = self.promDist / (self.n - 1)
		self.arg2 = self.promDist2 / (self.n - 1)
		print(self.arg)
		print(self.promDist)
		print(self.arg2)
		print(self.promDist2)

	def clustercoef (self):
		cluster = 0
		for nodo in self.vecinos:
			m = 0
			for i in self.vecinos[nodo]:
				for j in self.vecinos[nodo]:
					if i in self.vecinos[j]:
						m+=1
			n = len(self.vecinos[nodo])
			if n >1:
				cluster += m /(n * (n-1))
		print (cluster / len(self.V))
		return cluster/len(self.V)


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




