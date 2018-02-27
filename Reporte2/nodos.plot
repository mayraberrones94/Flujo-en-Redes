set term poscript eps
set output "nodos.eps"
set size square
set key off
set xrange [-.1:1.1]
set yrange [-.1:1.1]
set arrow 1 from 0.049398174901299274 , 0.23805462511158026 to 0.2838338702070258 , 0.12840767903857309 nohead
set arrow 2 from 0.8691241760493784 , 0.7413023689518122 to 0.2838338702070258 , 0.12840767903857309 nohead
plot nodos.txt using 1:2 with points pt 7
quit()
