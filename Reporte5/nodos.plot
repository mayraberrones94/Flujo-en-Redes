set term postscript color eps
set output "nodos.eps"
set size square
set key off
set xrange [-1: 5 ]
set yrange [-1: 5 ]
plot "grafica.dat" using 1:2 with points pt 7 ps 2 
quit()
