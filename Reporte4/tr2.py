
from intento import Grafo
import time

prom = [.1, .2, .3, .4, .5, .6, .7, .8, .9]
nodos = [10, 20,30,40,50,60,70,80,90,100]
with open("Tiempoargv.csv", 'at') as salida:
	with open("Tiempoclus.csv", 'at') as dato:
		for i in range (0, 10):
			for j in range(0, 9):
				Tiempo1 = time.clock()
				p = Grafo()
				p.puntos(nodos[i], 2)
				p.k_conect(2)
				p.conecta(prom[j])
				p.floyd_warshall()
				p.argdist()
				print(time.clock() - Tiempo1, file = salida)
				p.clustercoef()
				print(time.clock() - Tiempo1, file = dato)
