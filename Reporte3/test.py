import time
from exp2 import Grafo
puntos = 10
di = 3
proba = 0.5

if di > 2:
	for n in range(1, 21):
		for j in range(0, 10):
			if di is 3:
				with open("TiempoNoDir.csv", "at") as salida:
					tim = time.clock()
					i = 5 * n
					p = Grafo()
					p.puntos(i)
					p.conecta(proba, di)
					p.ford_fulkerson()
					p.floyd_warshall()
					p.imprimir("nodos.dat")
					p.grafica(di)
					print(time.clock() - tim, file = salida)

			elif di is 4:
				with open("TiempoDir.csv", "at") as salida:
					tim = time.clock()
					i = 5 * n
					p = Grafo()
					p.puntos(i)
					p.conecta(proba, di)
					p.ford_fulkerson()
					p.floyd_warshall()
					p.imprimir("nodos.dat")
					p.grafica(di)
					print(time.clock() - tim, file = salida)

else: 
	p = Grafo()
	p.puntos(puntos)
	p.conecta(proba, di)
	p.ford_fulkerson()
	p.floyd_warshall()
	p.imprimir("nodos.dat")
	p.grafica(di)



#print(g2.V)

#p.floyd_warshall()

