from random import random #importar libreria para generar tus numeros aleatorios.
nodos = [] #matriz donde vas a ir creando num
n = 30 #cantidad de numeros que voy a generar de manera aleatoria
p = 0.09 #Variable de probabilidad para que una coordenada se una con otra.
id = 1 #Esto lo necesito para nombrar a las aristas mas adelante.

with open ("nodos.dat", 'w') as salida: #generamos un archivo de salida para mis datos.
	for nod in range (n): #Este for me genera dos numeros aleatorios n veces.
		x = random()
		y = random()
		nodos.append((x,y))
		print(x, y, file = salida)
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

#Para el siguiente FOR, llame a los datos ya agrupados, en donde toma el primero, y lo compara con todos los demas.
	for(x1, y1) in nodos:
		for (x2, y2) in nodos:
		#El siguente IF es donde entra en juego la probabilidad p, en la cual un numero aleatorio decidira si la va a unirse
		#con otra coordenada o no.
			if random () < p:
				#El sig. print es el comando de gnuplot para unir un punto con otro.
				print ('set arrow', id, 'from', x1, ',',y1,'to', x2, ',', y2, 'nohead', file = salida)
				id += 1
	
	print ('plot "nodos.dat" using 1:2 with points pt 7', file = salida)
	print ('quit()', file = salida)
