
from floyd import Grafo
G = Grafo()
G.conecta('a', 'b', 5)
G.conecta('a', 'c', 7)
G.conecta('b', 'c', 2)
G.conecta('c', 'd', 4)
#print(G.vecinos['a'])

#print(G.V)

#print(G.E)
G2 = G.complemento()
#print(G2.E)
print(G.floyd_warshall())