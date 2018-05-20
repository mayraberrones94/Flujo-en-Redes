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

#c = p.E
#s = Start, nodo de inicio que le voy a dar.
#t = Target, nodo al que tiene que llegar. 

	def ford_fulkerson(self): 
		self.s = self.nodos[0]
		self.t = self.nodos[randint(1, self.n - 1)]

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
		with open("Fulkerson.dat", "at") as archivo:
			print(maximo, file = archivo)
		return maximo

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
				if not (x, y) in self.vecinos:
					self.vecinos[(x,y)] = []
				print (x, y, i, file = salida)
				print (self.nodos[i], i)

	def k_conect(self, k):
		for uno in range(1, k +1):
			for dos in range(0, self.n):
				u = self.nodos[dos]
				v = self.nodos[dos - uno]
				self.aristas[(u, v)] = self.aristas[(v, u)] = uno
				if not u in self.vecinos[v]:
					if u is not v:
						if v is not u:
							self.vecinos[v].append(u)
				if not v in self.vecinos[u]:
					if v is not u:
						if u is not v:
							self.vecinos[u].append(v)


	def conecta (self, prob):
		for(x1, y1) in self.nodos:
			for(x2, y2) in self.nodos:
				if random() < prob:
					if ((x1, y1),(x2,y2)) not in self.aristas:
				 		if ((x2, y2), (x1,y1)) not in self.aristas:
				 			self.kmax = floor(((self.n/2) * 3) - (self.n/4))
				 			u = self.nodos.index((x1,y1))
				 			v = self.nodos.index((x2,y2))
				 			if u is not v:
				 				d = abs(u-v)
				 				if d > self.kmax:
				 					d2 = self.n - d
				 					self.aristas[((x1, y1),(x2,y2))] = self.aristas[((x2, y2), (x1,y1))] = d2
				 				else:
				 					self.aristas[((x1, y1),(x2,y2))] = self.aristas[((x2, y2), (x1,y1))] = d

				 				if (x1, y1) not in self.vecinos[(x2, y2)]:
				 					if(x1, y1) is not (x2, y2):
				 						if(x2, y2) is not (x1, y1):
				 							self.vecinos[(x2, y2)].append((x1, y1))
				 				if (x2, y2) not in self.vecinos[(x1, y1)]:
				 					if(x2, y2) is not (x1, y1):
				 						if(x1, y1) is not (x2, y2):
				 							self.vecinos[(x1, y1)].append((x2, y2))


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

	def graf (self, nume, eps = True):
		with open("nodos.plot", 'w') as salida:
			if eps:
				print("set term postscript color eps", file = salida)
				print('set output "nodos'+str(nume)+'.eps"', file = salida)
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
p = Grafo()
p.puntos(10, 3)
p.k_conect(3)
p.conecta(.009)
p.graficar()
print(p.ford_fulkerson())





