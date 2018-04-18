from math import pi, sin, cos

n = 10
th = 2*(pi)/n

j = 0

with open ("grafica.dat", 'w') as salida:
	for i in range(n):
		print (sin(th*j), cos(th*j), j, file = salida)
		j += 1

with open("nodos.plot", 'w') as salida:
	eps = True
	if eps:
		print("set term postscript color eps", file = salida)
		print('set output "nodos.eps"', file = salida)
	else:
		print('set term png', file = salida)
		print('set output "nodos.png"', file = salida)
	print('set size square', file = salida)
	print('set key off', file = salida)
	print('set xrange [-1.1:1.1]', file = salida)
	print('set yrange [-1.1:1.1]', file = salida)
	print('plot "grafica.dat" using 1:2:3 with points pt 7 ps 2 lc var ', file = salida)
	print('quit()', file = salida)

