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

	def floyd_warshall (self): 
		self.d = {}
		for (x, y) in self.nodos:
			self.d[((x, y), (x, y))] = 0 # distancia reflexiva es cero
			for u in self.vecinos[(x, y)]:
				if ((x, y), u) in self.aristas:
					self.d[((x, y),u)] = self.aristas[((x, y),u)]
				else:
					self.d[((x, y),u)] = self.aristas[(u, (x, y))]
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
		return self.d

	def argdist(self):
		self.sumaDist = 0
		for i in self.d:
			self.sumaDist += self.d[i]
		self.promDist2 = self.sumaDist/((self.n * (self.n - 1))/ 2)
		self.arg2 = self.promDist2 / (self.n - 1)
		with open("Prom_dis.csv", 'a') as salida:
			print(self.arg2, file = salida)


	def clustercoef (self):
		with open("Cluster_coef.csv", 'at') as salida:
			self.clus = []
			for (x, y) in self.nodos:
				self.cff = []
				idvec = len(self.vecinos[(x,y)])
				self.clustcoef2 = 0
				for t in range(0, idvec - 1):
					self.clustcoef = 0
					h = self.vecinos[(x,y)][t]
					if(x,y) is not h:
						for m in self.vecinos[h]:
							if(x,y) is not m:
								if m is not h:
									if h is not m:
										if h is not (x, y):
											if m is not (x, y):
												if m in self.vecinos[(x,y)]:
													if (h,m) not in self.cff:
														self.cff.append((h, m))
													if (m, h) not in self.cff:
														self.cff.append((m, h))
														self.clustcoef +=1
					self.clustcoef2 += self.clustcoef
				dens = (self.clustcoef2) / (((idvec) * (idvec - 1)) / 2)
				self.clus.append(dens)
			c = 0
			for d in range(0, len(self.clus) - 1):
				c += self.clus[d]
			self.DensidadProm = c / len(self.clus)
			print(self.DensidadProm, file = salida)


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

	def diagrama1 (self, plot, diagrama):
		with open(plot, 'w') as diagrama:
			print("set terminal png truecolor", file = diagrama)
			print("set output 'Diagrama1.png'", file = diagrama)
			print("set key off", file = diagrama)
			print("set title 'Diagramas de tiempos '", file = diagrama)
			print("set xlabel 'Potencias de 2 nodos por grafo'", file = diagrama)
			print("set ylabel 'Logaritmo de tiempo de procesamiento'", file = diagrama)
			print("set style fill solid 0.25 border -1", file = diagrama)
			print("set style boxplot outliers pointtype 7", file = diagrama)
			print("set style data boxplot", file = diagrama)
			diagrama1 = "plot 'Tiempoargv.csv' using (-8):(log($3)):(0.5):1"                       
			print(diagrama1, file = diagrama)

	def diagrama2 (self, eps = True):
		with open("Diagrama.plot", 'w') as diagrama:
			print("set term postscript color eps", file = diagrama)
			print("set output 'Diagrama3.eps'", file = diagrama)
			print("set key off", file = diagrama)
			print("set xlabel 'Probabilidad P'", file = diagrama)
			print("set ylabel 'Distancia Normalizada'", file = diagrama)
			print("set y2label 'Densidad Promedio'", file = diagrama)
			print("set style fill solid 0.25 border -1", file = diagrama)
			print("set style line 1 lt 1 linecolor rgb 'red' lw 2 pt 1", file = diagrama)
			print("set style line 2 lt 1 linecolor rgb 'blue' lw 2 pt 1", file = diagrama)
			print("set style line 2 lt 1 linecolor rgb 'blue' lw 2 pt 1", file = diagrama)
			diagrama3 = "plot 'Prom.txt' using 1:2 ls 1 title 'Probabilidad' with line , 'Cluster.txt' using 1:2 ls 2 title 'Distancias' with lines "                       
			print(diagrama3, file = diagrama)




