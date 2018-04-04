from random import random
from math import sqrt

class Grafo:

	def __init__(self):
		self.V = set()
		self.E = dict()
		self.vecinos = dict()
		self.n = None
		self.P = []
		self.nod2 = []
		self.nod3 = []
		self.A = [] #para las aristas
		self.archivo = None # donde guardo mis puntos
		self.pesos = []

		self.nodos = [] #conjunto que ocupo para los puntos finales.

	def puntos (self, num):
		self.n = num
		for nodo in range (self.n):
			x = random()
			y = random()
			self.P.append((x, y, nodo))

	def agrega (self, v):
		self.V.add(v)
		self.nodos.append(v)
		if not v in self.vecinos:
			self.vecinos[v] = set()

	def conecta (self, prob):
		for i in range(self.n - 1):
			self.nod2.append(self.P[i])
		for i in range(self.n):
			self.nod3.append(self.P[i])
		for(x1, y1, u) in self.nod2:
			del self.nod3[0]
			for(x2, y2, v) in self.nod3:
				if random() < prob:
					self.agrega(u)
					self.agrega(v)
					self.E[(u, v)] = self.E[(u,v)] = int(sqrt((x2 - x1) ** 2 + (y2 - y1 )** 2)*100) #esto lo puedes quitar luego para hacer los ponderados
					self.vecinos[v].add(u)
					self.vecinos[u].add(v)
					self.A.append((x1, y1, x2, y2, u, v))
					self.pesos.append((sqrt((x2 - x1) ** 2 + (y2 - y1 )** 2)*100, (x1+x2)/2, (y1+y2)/2))

	def distancia (self, x1, y1, x2, y2):
		d = (sqrt((x2 - x1)**2 + (y2 - y1)**2)*100) -0.1
		return d

	def complemento (self):
		comp = Grafo()
		for v in self.V:
			for w in self.V:
				if v != w and (v, w) not in self.E:
					comp.conecta(v, w, 1)
			return comp

	def imprimir(self, arch):
		self.archivo = arch
		with open (self.archivo, "w") as salida:
			for nodo in range(self.n):
				print(self.P[nodo][0], self.P[nodo][1], (random() * 10), file = salida) #lo de random es nadamas para darle colorsitos si quieres

#di = 1 es simple
#di = 2 es dirigido
#di = 3 es ponderado

	def grafica(self, di, eps = True):
		assert self.archivo is not None
		with open ("nodos.plot", 'w') as salida:
			if eps:
				print("set term postscript color eps", file = salida)
				print('set output "nodos.eps"', file = salida)
			else:
				print('set term png', file = salida)
				print('set output "nodos.png"', file = salida)

			print('set size square', file = salida)
			print('set key off', file = salida)
			print('set xrange [-.1:1.1]', file = salida)
			print('set yrange [-.1:1.1]', file = salida)
			for n in range(len(self.P)):
				print('set label', "'" , int(self.P[n][2]), "'", 'at', self.P[n][0], ",", self.P[n][1],  file = salida )
				print('set object circle at ', self.P[n][0], ',' , self.P[n][1], ' size scr 0.01 fc rgb "navy" ' , file = salida)
			id = 1
			for i in range(len(self.A)):
				d = self.distancia(self.A[i][0], self.A[i][1], self.A[i][2], self.A[i][3])

				xNod = 0.01 * (self.A[i][2] - self.A[i][0]) / d 
				yNod = 0.01 * (self.A[i][3] - self.A[i][1]) / d 

				xVec = 0.01 * (self.A[i][0] - self.A[i][2]) / d
				yVec = 0.01 * (self.A[i][1] - self.A[i][3]) / d

				x1 = self.A[i][0] + xNod
				x2 = self.A[i][2] + xVec
				y1 = self.A[i][1] + yNod
				y2 = self.A[i][3] + yVec

				if di is 2:
					print('set arrow', id, 'from', x1, ',', y1, 'to', x2 , ',', y2 , 'head filled lw 1', file = salida)
					id +=1
				elif di is 1:
					print('set arrow', id, 'from', self.A[i][0], ',', self.A[i][1] , 'to', self.A[i][2] , ',', self.A[i][3] , 'nohead filled lw 1', file = salida)
					id +=1
				elif di is 3:
					print('set arrow', id, 'from', self.A[i][0], ',', self.A[i][1] , 'to', self.A[i][2] , ',', self.A[i][3] , 'nohead filled lw 1', file = salida)
					print('set label', "'", int(self.pesos[i][0]), "'", 'at', self.pesos[i][1], ',', self.pesos[i][2], file = salida)
					id +=1
				elif di is 4:
					print('set arrow', id, 'from', self.A[i][0], ',', self.A[i][1] , 'to', self.A[i][2] , ',', self.A[i][3] , 'head filled lw 1', file = salida)
					print('set label', "'", int(self.pesos[i][0]), "'", 'at', self.pesos[i][1], ',', self.pesos[i][2], file = salida)
					id +=1
			print('plot "nodos.dat" using 1:2:3 with points pt 7 lc var ps 1 ', file = salida)
			print('quit()', file = salida)




	def floyd_warshall (self): 
		d = {}
		for v in self.V:
			d[(v, v)] = 0 # distancia reflexiva es cero
			for u in self.vecinos[v]: # para vecinos, la distancia es el peso
				d[(v, u)] = self.E[(v, u)]
		for intermedio in self.V:
			for desde in self.V:
				for hasta in self.V:
					di = None
					if (desde, intermedio) in d:
						di = d[(desde, intermedio)]
					ih = None
					if (intermedio, hasta) in d:
						ih = d[(intermedio, hasta)]
					if di is not None and ih is not None:
						c = di + ih # largo del camino via "i"
						if (desde, hasta) not in d or c < d[(desde, hasta)]:
							d[(desde, hasta)] = c # mejora al camino actual
		return d

		def camino(self, s, t, c, f): #construccion de camino aumentante
			cola = [s]
			usados = set()
			camino = dict()
			while len(cola) > 0:
				u = cola.pop(0)
				usados.add(u)
				for (w, v) in c:
					if w == u and v not in cola and v not in usados:
						actual = f.get((u, v), 0)
						dif = c[(u, v)] - actual
						if dif > 0:
							cola.append(v)
							camino[v] = (u, dif)
			if t in usados:
				return camino
			else: # no se alcanzo
				return None

#c = p.E
#s = Start, nodo de inicio que le voy a dar.
#t = Target, nodo al que tiene que llegar. 

		def ford_fulkerson(self, c, s, t): 
			if s == t:
				return 0; #O puedes poner mensaje de que start and target son iguales.
			maximo = 0
			f = dict()
			while True:
				aum = self.camino(s, t, c, f)
				if




	