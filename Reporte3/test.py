
from exp2 import Grafo
p = Grafo()
p.puntos(10)
p.conecta(0.5)

print(p.vecinos[1])
print(p.V)
print(p.E)
p.ford_fulkerson(2, 8)
p.floyd_warshall()
p.imprimir("nodos.dat")
p.grafica(4)


#print(g2.V)

#p.floyd_warshall()

