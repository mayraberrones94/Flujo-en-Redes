from intento import Grafo
from math import sqrt, pi, sin, cos, ceil, floor
nodos = 10
k = 3

p = Grafo()
p.puntos(nodos, k)
p.k_conect(k)
p.conecta(0.9)
p.floyd_warshall()
p.argdist()
p.clustercoef()
p.graficar()