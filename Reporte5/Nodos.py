from grid import Grafo
import time

p = Grafo()
p.puntos(20)
p.conexiones(3)
p.aleatorio(0.003)
with open("TiemposNodos.csv", 'at') as salida:
	for i in range (0, 20 ):
		tiempo = time.clock()
		p.perNodos(i)
		p.ford_fulkerson(1)
		print(i, time.clock() - tiempo, file = salida)

