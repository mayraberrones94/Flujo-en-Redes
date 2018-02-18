from random import random #importar libreria para generar tus numeros aleatorios.
nodos = [] #matriz donde vas a ir creando num
n = 50 #cantidad de numeros que voy a generar de manera aleatoria

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
	#Por ultimo, se manda a llamar el archivo en el cual colocamos los numeros aleatorios.
	print ('plot "nodos.dat" using 1:2 with points pt 7', file = salida) 
	#En el 1:2 nos referimos a las columnas que tiene mi archivo, x y y.
	print ('quit()', file = salida)
