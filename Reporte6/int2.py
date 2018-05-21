from random import random, randint, choice, sample
from math import sqrt



class Grafo:

	def __init__(self):
		self.n = None
		self.aristas = dict()
		self.nodos = []
		self.A = []
		self.pesos = []
		self.sec = []
		self.aux = []

	def puntos (self, num):
		self.n = num
		self.nodos.append((-.3, 0.5, 0))
		self.aux.append((0))
		self.sec.append((0))
		for i in range(1, self.n - 1):
			self.nodos.append((random(), random(), i))
			self.aux.append((i))
			self.sec.append((i))
		self.nodos.append((1.3, 0.5, self.n -1))
		self.aux.append((self.n -1))
		self.sec.append((self.n -1))

	def conect (self, prob):
		for (x1, y1, u) in self.nodos:
			for(x2, y2, v) in self.nodos:
				if u is not v:
					if random() < prob:
						self.aristas[(u,v)] = self.aristas[(v, u)] = int(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * 10)
						self.A.append((x1, y1, x2, y2, u, v))
						self.pesos.append(((sqrt((x2 - x1) ** 2 + (y2 - y1 )** 2)*10), (x1+x2)/2, (y1+y2)/2))
		#print (self.aristas)

	def merge(self):
		while len(self.aux) > 2:
			w = choice(self.aux) 
			z = choice(self.aux) 
			if w is not z:
				if w is not self.nodos[0][2] and w is not self.nodos[len(self.nodos) - 1][2]:
					if w in self.aux:
						if (z, w) in self.aristas:
							del self.aristas[(z, w)]
							del self.aristas[(w, z)]
							self.sec[z] = str(self.sec[z]) +"#"+ str(self.sec[w])
							self.aux.remove(w)

							#print (self.aux)
							#print (z, w)
							for i in range(0, len(self.nodos) - 1):
								if w is self.nodos[i][2]:
									self.nodos.pop(i)
									#print(self.nodos)

							for i in range(0, self.n):
								if(i, w) in self.aristas:
									if(z, i) in self.aristas:
										self.aristas[(i, z)] = (list(self.aristas.values())[list(self.aristas.keys()).index((i, z))]) + (list(self.aristas.values())[list(self.aristas.keys()).index((i, w))])
								#self.aristas[(i,z)] = self.aristas[(i, z)].value() + self.aristas[(w, i)].value()
								#self.aristas[(z, i)] =self.aristas[(z, i)].value() + self.aristas[(w, i)].value()
										self.aristas[(z, i)] = (list(self.aristas.values())[list(self.aristas.keys()).index((z, i))]) + (list(self.aristas.values())[list(self.aristas.keys()).index((w, i))])
									else:
										self.aristas[(i, z)] = (list(self.aristas.values())[list(self.aristas.keys()).index((w, i))]) 
								
								#self.aristas[(i, z)] = self.aristas[(w, i)]
										self.aristas[(z, i)] = (list(self.aristas.values())[list(self.aristas.keys()).index((w, i))]) 
						
									#print('estoy aqui')
									#print (w,i)
									#print(list(self.aristas.values())[list(self.aristas.keys()).index((i, w))])	

		#print(self.nodos)
		#print(self.sec)
		#print (self.aristas)
		self.final = (list(self.aristas.values())[list(self.aristas.keys()).index((0, self.n -1))])	
		#print(self.final)
		with open("Final.txt", 'at') as salida:
			print(self.final, file = salida)
					
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


	def ford_fulkerson(self): 

		with open ("Ford.txt", 'at') as salida:
			self.s = self.aux[0]
			self.t = self.aux[self.n - 1]

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

	def imprimir(self):
		with open("grafo.dat", 'w') as salida:
			for n in range(self.n):
				print(self.nodos[n][0], self.nodos[n][1], self.nodos[n][2], file = salida)


	def imprimir2(self, num):
		with open("grafo"+str(num)+".dat", 'w') as salida:
			for n in range(len(self.nodos)):
				print(self.nodos[n][0], self.nodos[n][1], self.nodos[n][2], file = salida)



	def grafica (self, eps = True):
		with open("nodos.plot", 'w') as salida: 
			if eps:
				print("set term postscript color eps", file = salida)
				print('set output "nodos.eps"', file = salida)
			else:
				print('set term png', file = salida)
				print('set output "nodos.png"', file = salida)
			print('set size square', file = salida)
			print('set key off', file = salida)
			print ('set xrange [-.3:1.3]', file = salida)
			print ('set yrange [-.1:1.1]', file = salida)
			print('unset border',file = salida)
			print('unset xtics', file = salida)
			print('unset ytics', file = salida)
			for n in range(len(self.nodos)):
				print('set label', "   ' " , int(self.nodos[n][2]), "   ' ", 'at', self.nodos[n][0], ",", self.nodos[n][1],  file = salida )
			
			id = 1
			for i in range(len(self.A)):
				print('set arrow', id, 'from', self.A[i][0], ',', self.A[i][1], 'to', self.A[i][2], ',', self.A[i][3], 'nohead filled lw 1', file = salida)
				print('set label', " ' ", int(self.pesos[i][0]), " ' ", 'at', self.pesos[i][1], ',', self.pesos[i][2], file = salida)
				id += 1
			print('plot "grafo.dat" using 1:2:3 with points pt 7 lc var ps 2 ', file = salida)
			print('quit()', file =  salida)

	def grafica2(self,num, eps = True):
		with open("nodos"+str(num)+".plot", 'w') as salida: 
			if eps:
				print("set term postscript color eps", file = salida)
				print('set output "nodos'+str(num)+'.eps"', file = salida)
			else:
				print('set term png', file = salida)
				print('set output "nodos.png"', file = salida)
			print('set size square', file = salida)
			print('set key off', file = salida)
			print ('set xrange [-.3:1.3]', file = salida)
			print ('set yrange [-.1:1.1]', file = salida)
			print('unset border',file = salida)
			print('unset xtics', file = salida)
			print('unset ytics', file = salida)
			print('set label', " ' " , self.sec[0], "   ' ", 'at', self.nodos[0][0], ",", self.nodos[0][1],  file = salida)
			print('set label', " ' " , self.sec[self.n - 1], "   ' ", 'at', self.nodos[1][0], ",", self.nodos[1][1],  file = salida )
			print('set arrow', 1, 'from', self.nodos[0][0], ',', self.nodos[0][1], 'to', self.nodos[len(self.nodos) - 1][0], ',', self.nodos[len(self.nodos) - 1][1], 'nohead filled lw 1', file = salida)
			print('set label', " ' ", int(self.final), " ' ", 'at', (0.5), ',', (0.44), file = salida)
			
			print('plot "grafo'+str(num)+'.dat" using 1:2:3 with points pt 7 lc var ps 2 ', file = salida)
			print('quit()', file =  salida)

p = Grafo()

p.puntos(100)
p.imprimir()
p.conect(0.4)
p.grafica()
#print(p.ford_fulkerson())
p.merge()
p.imprimir2(2)
p.grafica2(2)

