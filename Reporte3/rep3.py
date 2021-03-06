from random import random
from math import sqrt
class Grafo:
 
	def __init__(self):
		self.n = None	
		self.x = dict()		#
		self.y = dict()	
		self.vecinos = dict()
		self.E = dict()	#
		self.P = []	
		self.pesos = []
		self.nodo2 = []
		self.nodo3 = []	
		self.Ari = []	#
		self.archivo = None	#

	def puntos(self, num):
		for nodo in range(num):
			self.n.add(num)
			self.x[nodo] = random() 
			self.y[nodo] = random() 
			self.P.append((self.x[nodo], self.y[nodo], nodo))
			if not nodo in self.vecinos:
				self.vecinos[nodo] = set()

	def aristas(self, prob):
		for i in range(self.n - 1):
			self.nodo2.append(self.P[i])
		for i in range(self.n):
			self.nodo3.append(self.P[i])
		for(x1, y1, i) in self.nodo2:
			del self.nodo3[0]
			for(x2, y2, j) in self.nodo3:
				if random() < prob:
					self.Ari.append((x1, y1, x2, y2))
					self.pesos.append((sqrt((x2 - x1) ** 2 + (y2 - y1 )** 2)*100, (x1+x2)/2, (y1+y2)/2))
					self.E[(x1, y1),(x2, y2)] = self.E[(x2, y2), (x1, y1)] = (sqrt((x2 - x1) ** 2 + (y2 - y1 )** 2)*100)
					self.vecinos[(x1, y1)].add(x2, y2)
					self.vecinos[(x2, y2)].add(x1, y1)
		print(len(self.Ari))

		


	def imprimir(self, arch):
		self.archivo = arch
		with open (self.archivo, "w") as salida:
			for nodo in range(self.n):
				print(self.P[nodo][0], self.P[nodo][1], (random() * 10),  file = salida)
		print(self.archivo)

	#di = 1 es simple
	#di = 2 es dirigido
	#di = 3 es ponderado
	#di = 4 es dirigido y ponderado

	def grafica (self, di):
		assert self.archivo is not None
		with open("nodos.plot", 'w') as salida: 
			print('set term png', file = salida)
			print('set output "nodos.png"', file = salida)
	
			print('set size square', file = salida)
			print('set key off', file = salida)
			print ('set xrange [-.1:1.1]', file = salida)
			print ('set yrange [-.1:1.1]', file = salida)
			id = 1
			for i in range(len(self.Ari)):
				if di is 2 :
					print('set arrow', id, 'from', self.Ari[i][0], ',', self.Ari[i][1], 'to', self.Ari[i][2], ',', self.Ari[i][3], 'head filled lw 1',  file = salida)
					id +=1
				elif di is 1:
					print('set arrow', id, 'from', self.Ari[i][0], ',', self.Ari[i][1], 'to', self.Ari[i][2], ',', self.Ari[i][3], 'nohead filled lw 1', file = salida)
					id +=1
				elif di is 3:
					print('set arrow', id, 'from', self.Ari[i][0], ',', self.Ari[i][1], 'to', self.Ari[i][2], ',', self.Ari[i][3], 'nohead filled lw 1', file = salida)
					print('set label', "'", int(self.pesos[i][0]), "'", 'at', self.pesos[i][1], ',', self.pesos[i][2], file = salida)
					id +=1
				elif di is 4:
					print('set arrow', id, 'from', self.Ari[i][0], ',', self.Ari[i][1], 'to', self.Ari[i][2], ',', self.Ari[i][3], 'head filled lw 1', file = salida)
					print('set label', "'", int(self.pesos[i][0]), "'", 'at', self.pesos[i][1], ',', self.pesos[i][2], file = salida)
					id +=1
			print('plot "nodos.dat" using 1:2:3 with points pt 8 lc var ps 2 ', file = salida)
			print('quit()', file =  salida)

	def floydw(self):
		d = {}
		for v in self.P:
			d[(v, v)] = 0
			for u in self.vecinos[v]:
				d[(v, u)] = self.E[(v, u)]
		for intermedio in self.P:
			for desde in self.P:
				for hasta in self.P:
					di = None
					if (desde, intermedio) in d:
						di = d[(desde, intermedio)]
					ih = None
					if (intermedio, hasta) in d:
						ih = d[(intermedio, hasta)]
					if di is not None and ih is not None:
						c = di + ih
						if (desde, hasta) not in d or c < d[(desde, hasta)]:
							d[(desde, hasta)] = c
		return d





