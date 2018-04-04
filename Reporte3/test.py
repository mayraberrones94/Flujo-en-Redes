
from exp2 import Grafo
p = Grafo()
p.puntos(10)
p.conecta(0.5)
print(p.vecinos[1])
print(p.V)
print(p.E)

p.imprimir("nodos.dat")
p.grafica(2)
#g2 = p.complemento()
#print(g2.E)

#p.floyd_warshall()

