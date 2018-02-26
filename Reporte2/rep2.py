from random import random

class Grafo:
 
	def _init_(self):
		self.n = None
		self.nodos = []
		self.archivo = None

	def puntos(self, num, arch):
		self.n = num
		self.archivo = arch
		with open (self.archivo, 'w') as salida:
			for nod in range (self.n):
				x = random() 
				y = random() 
				self.nodos[num] = (x, y)
				print(x, y, file = salida)

	#def aristas(self, arch):
		
		
			#for nod in range (self.n):
				
		#print (self.archivo)

	def imprimir(self, p, plot):
		with open(plot, 'w') as salida: 
			print('set term poscript eps', file = salida)
			print('set output "nodos.eps"', file = salida)
			print('set size square', file = salida)
			print('set key off', file = salida)
			print ('set xrange [-.1:1.1]', file = salida)
			print ('set yrange [-.1:1.1]', file = salida)
			for(x1, y1) in self.nodos:
				for(x2, y2) in self.nodos:
					if random() < p:
						print('set arrow', id, 'from', x1, ',', y1, 'to', x2, ',', y2, 'nohead', file = salida)
			print('plot', self.archivo, 'using 1:2 with points pt 7', file = salida)
			print('quit()', file =  salida)


