from random import random, uniform, randint, normalvariate, expovariate
from math import sqrt, ceil, floor
def distancia (a, b):
	return (abs(a[0] - b[0]) + abs(a[1] - b[1]))

class Grafo:

	def __init__(self):
		self.k = None
		self.nodos = []
		self.aristas = dict()
		self.vecinos = dict()


	def puntos(self, k):
		self.k = k
		with open("grafica.dat", 'w') as salida:
			for x in range(0, k):
				for y in range(0, k):
					self.nodos.append((x, y))
					if x==0 and y==k-1:
						print(x, y, 1, file = salida)
					elif x==k-1 and y==0:
						print(x, y, 6, file = salida)
					else:
						print(x, y, 7, file = salida)

	def conexiones(self, l):
		self.l = l
		with open ("conexiones.dat", 'w') as salida:
			for i in self.nodos:
				for j in self.nodos:
					if i is not j:
						if distancia (i, j) < l +1:
							self.aristas[i, j] = self.aristas[j, i] = floor(normalvariate(4, 0.5))+1

	def aleatorio(self, proba):
		self.rand = 0
		for i in self.nodos:
			for j in self.nodos:
				if i is not j:
					if j is not self.nodos[0]:
						w = random()
						if w < proba and (i, j) not in self.aristas:
							self.aristas[i, j] = ceil(expovariate(.1))
							self.rand += 1

	def perNodos(self,o):
		num = randint(1, len(self.nodos) - 1)	
		if num != self.nodos[0] and num != self.nodos[len(self.nodos) - 1]:
			for y in range (len(self.nodos)):
				if ((self.nodos[num][0],self.nodos[num][1]), (self.nodos[y][0],self.nodos[y][1])) in self.aristas:
					del self.aristas[(self.nodos[num][0],self.nodos[num][1]), (self.nodos[y][0],self.nodos[y][1])]
				if ((self.nodos[y][0],self.nodos[y][1]), (self.nodos[num][0],self.nodos[num][1])) in self.aristas:
					del self.aristas[(self.nodos[y][0],self.nodos[y][1]), (self.nodos[num][0],self.nodos[num][1])]
			self.nodos.pop(num)
		with open("grafica"+str(o)+".dat", 'w') as salida:
			for (x,y) in self.nodos:
				if x==0 and y==self.k -1:
					print(x, y, 1, file = salida)
				elif x==self.k-1 and y==0:
					print(x, y, 6, file = salida)
				else:
					print(x, y, 7, file = salida)

	def perAristas(self, o):
		for i in range(0, 20):
			y = randint(1, len(self.nodos) - 1)
			num = randint(1, len(self.nodos) - 1)
			if y is not num:
				if num is not self.nodos[0]:
					if ((self.nodos[num][0],self.nodos[num][1]), (self.nodos[y][0],self.nodos[y][1])) in self.aristas:
						del self.aristas[(self.nodos[num][0],self.nodos[num][1]), (self.nodos[y][0],self.nodos[y][1])]
					if ((self.nodos[y][0],self.nodos[y][1]), (self.nodos[num][0],self.nodos[num][1])) in self.aristas:
						del self.aristas[(self.nodos[y][0],self.nodos[y][1]), (self.nodos[num][0],self.nodos[num][1])]

	def camino(self): #construccion de camino aumentante
		cola = [self.s]
		usados = set()
		camino = dict()
		while len(cola) > 0:
			u = cola.pop(0)
			usados.add(u)
			for (w, v) in self.aristas:
				if w == u and v not in cola and v not in usados:
					actual = self.f.get((u, v), 0)
					dif = self.aristas[(u, v)] - actual
					if dif > 0:
						cola.append(v)
						camino[v] = (u, dif)
		if self.t in usados:
			return camino
		else: # no se alcanzo
			return None	


	def ford_fulkerson(self, ty): 
		if ty is 1:
			self.file = "FulkersonNodos.csv" 
		else:
			self.file = "FulkersonAristas.csv"

		with open (self.file, 'at') as salida:
			self.s = self.nodos[0]
			self.t = self.nodos[len(self.nodos) - 1]

			if self.s == self.t:
				return 0; #O puedes poner mensaje de que start and target son iguales.
			maximo = 0
			self.f = dict()
			while True:
				aum = self.camino()
				if aum is None:
					break #ya no hay
				incr = min(aum.values(), key = (lambda k: k[1]))[1]
				u = self.t
				while u in aum:
					v = aum [u][0]
					actual = self.f.get((v, u), 0) #cero si no hay
					inverso = self.f.get((u, v), 0)
					self.f[(v, u)] = actual + incr
					self.f[(u, v)] = inverso - incr
					u = v
				maximo += incr
			print(maximo, file = salida)
			return maximo

	def grafica(self, m, eps = True):
		with open("nodos"+str(m)+".plot", 'w') as salida:

			if eps:
				print("set term postscript color eps", file = salida)
				print('set output "nodos'+str(m)+'.eps"', file = salida)
			else:
				print('set term png', file = salida)
				print('set output "nodos',m,'.png"', file = salida)
			print('set size square', file = salida)
			print('set key off', file = salida)
			print('set xrange [-1:', self.k , ']', file = salida)
			print('set yrange [-1:', self.k , ']', file = salida)
			print('unset xtics', file = salida)
			print('unset ytics', file = salida)
			id = 1
			for z in self.aristas:
				x1 = z[0][0]
				y1 = z[0][1]
				x2 = z[1][0]
				y2 = z[1][1]
				p = self.aristas[z]
				if id < (len(self.aristas) - (self.rand - 1)):
					print('set arrow', id, 'from', x1, ',', y1 , 'to', x2 , ',', y2 , 'nohead lw 2 ', file = salida)
				else:
					print('set arrow', id, 'from', x1, ',', y1 , 'to', x2 , ',', y2 , 'head filled lw 1 lc 3', file = salida)
				id += 1
			print('plot "grafica'+str(m)+'.dat" using 1:2:3 with points pt 7 lc var ps 2  ', file = salida)
			print('quit()', file = salida)

