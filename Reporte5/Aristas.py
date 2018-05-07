from grid import Grafo
import time

p = Grafo()
p.puntos(10)
p.conexiones(2)
p.aleatorio(0.002)
with open("TiemposAristas.csv", 'at') as salida:

	for i in range (0, 20):
		for j in range(1, 21):
			tiempo = time.clock()
			p.perAristas(j)
			p.ford_fulkerson(2)
			print(j, time.clock() - tiempo, file = salida)

