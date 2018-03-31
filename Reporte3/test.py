
from exp1 import Grafo
p = Grafo()
p.puntos(10)
p.conecta(0.5)
print(p.vecinos[1])
print(p.V)
print(p.E)

#g2 = p.complemento()
#print(g2.E)

p.floyd_warshall()

