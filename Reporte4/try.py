from intento import Grafo
import time
nodos = [10, 20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200] 
p = Grafo()

p.puntos(10, 2)
p.k_conect(2)
p.conecta(.1)
p.graficar()
p.diagrama2()

for i in range(0, 20):
	for j in range(0, 20):
		TiempoInicio1 = time.clock()
		k = int(nodos[i] / 10) 
		proba = nodos[j] / 220
		with open("file.csv", 'at') as salida:
			print (proba,  file =salida)


		


