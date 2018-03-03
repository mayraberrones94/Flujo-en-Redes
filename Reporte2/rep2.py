from random import random
from math import sqrt
class Grafo:
 
	def __init__(self):
		self.n = None	
		self.x = dict()		#
		self.y = dict()		#
		self.P = []	
		self.dist = []
		self.nodo2 = []
		self.nodo3 = []	
		self.Ari = []	#
		self.archivo = None	#

	def puntos(self, num):
		self.n = num
		for nodo in range(self.n):
			self.x = random() 
			self.y = random() 
			self.P.append((self.x, self.y, nodo))

	def aristas(self, prob):
		for i in range(self.n - 1):
			self.nodo2.append(self.P[i])
		for i in range(1, self.n):
			self.nodo3.append(self.P[i])
		for(x1, y1, i) in self.nodo2:
			del self.nodo3[0]
			for(x2, y2, j) in self.nodo3:
				if random() < prob:
					self.Ari.append((x1, y1, x2, y2))
					
		print(len(self.Ari))

		


	def imprimir(self, arch):
		self.archivo = arch
		#for k in range(len(self.Ari)):
			#self.dist[k] = sqrt(((self.Ari[k][0] - self.Ari[k][1]) ** 2 )+ ((self.Ari[k][2] - self.Ari[k][3]) ** 2))

		with open (self.archivo, "w") as salida:
			for nodo in range(self.n):
				print(self.P[nodo][0], self.P[nodo][1], (random() * 10),  file = salida)
		print(self.archivo)

	def grafica (self, di, pe):
		assert self.archivo is not None
		with open("nodos.plot", 'w') as salida: 
			print('set term eps', file = salida)
			print('set output "nodos.eps"', file = salida)
			print('set size square', file = salida)
			print('set key off', file = salida)
			print ('set xrange [-.1:1.1]', file = salida)
			print ('set yrange [-.1:1.1]', file = salida)
			id = 1
			for i in range(len(self.Ari)):
				if di is 1 :
					print('set arrow', id, 'from', self.Ari[i][0], ',', self.Ari[i][1], 'to', self.Ari[i][2], ',', self.Ari[i][3], 'head filled lw 1',  file = salida)
					id +=1
				else:
					print('set arrow', id, 'from', self.Ari[i][0], ',', self.Ari[i][1], 'to', self.Ari[i][2], ',', self.Ari[i][3], 'nohead filled lw 1', file = salida)
					id +=1
				#if pe is 1:

			print('plot "nodos.dat" using 1:2:3 with points pt 7 lc var ps 2 ', file = salida)
			print('quit()', file =  salida)




