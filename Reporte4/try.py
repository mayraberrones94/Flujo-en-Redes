from intento import Grafo
from math import sqrt, pi, sin, cos, ceil, floor
nodos = 20
k = 5

p = Grafo()
p.puntos(nodos, k)
p.k_conect(k)
p.conecta(0.1)
p.graficar()