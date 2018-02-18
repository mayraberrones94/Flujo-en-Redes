from random import random #importar libreria para generar tus numeros aleatorios.
nodos = [] #matriz donde vas a ir creando num
n = 50 #antidacd de numeros que voy a generar de manera aleatoria
p = 0.1 #Variable de probabilidad para que una coordenada se una con otra.
id = 1 #Esto lo necesito para nombrar a las aristas mas adelante.
k=[0 for i in range(n)]

for nod in range (n): #Este for me genera dos numeros aleatorios n veces.
	x = random()
	y = random()
	nodos.append((x,y,nod))

#Las siguientes tres variables son las que me van a ayudar a formar la lista en la que 
#voy a hacer el conteo de aristas por nodo.
q=0 
nodos2=[]
nodos3=[]
#Para este primer FOR, lo que estoy buscando es que se posisione en el primer nodo a evaluar, 
#y llegue hasta el penultimo, ya que si solo pongo n, me marca error.
for i in range(n-1):
	nodos2.append(nodos[i])
#En el sig. FOR voy desde el segundo elemento hasta el ultimo.
for i in range(1,n):
	nodos3.append(nodos[i])
aristas=[] #Al igual que en la matriz de aristas, aqui voy a guardar las uniones mas adelante.

for(x1, y1,i) in nodos2:
	del nodos3[0]
	for (x2, y2,j) in nodos3:
		if random () < p:
#Al igual que en la version anterior de este programa, el IF es el que controla cuantas aristas van a formarse.
			aristas.append((x1,y1,x2,y2))
			k[i]=k[i]+1
			k[j]=k[j]+1
			q+=1
#En estos ultimos K, es donde estoy asignandole la cantidad de aristas que lleva cada nodo.

with open ("nodos.dat", 'w') as salida: #generamos un archivo de salida para mis datos.
	for nod in range (n):
		#Esta C es la que me va a ayudar a cambiar el color de los nodos para diferenciarlos tanto
		#por color como por tamanio.
		c = (nodos[nod][0] + nodos[nod][1]) /2
		print(nodos[nod][0], nodos[nod][1], c, k[nod], file = salida)

with open ("nodos.plot", 'w') as salida: #Archivo para poder generar mi grafica de salida.
	#NOTA: Recuerda que siempre tienes que llamar al dato de salida para cada uno de los comandos de gnplot
	print ('set term png', file = salida) 
	#png para formato de salida de mi grafica
	print ('set output "nodos.png"', file = salida) 
	print ('set size square', file = salida)
	#Keyoff es para que la marca de agua que sale en la parte superior der. no se vea.
	print ('set key off', file = salida)
	#El rango x y y son para el tamanio en que va a salir mi grafica.
	print ('set xrange [-.1:1.1]', file = salida)
	print ('set yrange [-.1:1.1]', file = salida)
	for i in range(q):
		#El sig. print es el comando de gnuplot para unir un punto con otro.
		print ('set arrow', id, 'from', aristas[i][0], ',',aristas[i][1],'to', aristas[i][2], ',', aristas[i][3], 'nohead', file = salida)
		id += 1
	#Por ultimo, la cuarta columna del using, es 3*256 por la paleta de colores que tiene gnuplot.
	print ('plot "nodos.dat" using 1:2:4:($3*256) with points pt 7 ps var lc var', file = salida)
	print ('quit()', file = salida)

