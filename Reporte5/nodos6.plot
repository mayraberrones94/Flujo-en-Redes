set term postscript color eps
set output "nodos6.eps"
set size square
set key off
set xrange [-1: 5 ]
set yrange [-1: 5 ]
unset xtics
unset ytics
set arrow 1 from 0 , 0 to 0 , 1 nohead lw 2 
set arrow 2 from 0 , 1 to 0 , 0 nohead lw 2 
set arrow 3 from 0 , 1 to 1 , 1 nohead lw 2 
set arrow 4 from 1 , 1 to 0 , 1 nohead lw 2 
set arrow 5 from 0 , 3 to 0 , 4 nohead lw 2 
set arrow 6 from 0 , 4 to 0 , 3 nohead lw 2 
set arrow 7 from 0 , 3 to 1 , 3 nohead lw 2 
set arrow 8 from 1 , 3 to 0 , 3 nohead lw 2 
set arrow 9 from 0 , 4 to 1 , 4 nohead lw 2 
set arrow 10 from 1 , 4 to 0 , 4 nohead lw 2 
set arrow 11 from 1 , 1 to 1 , 2 nohead lw 2 
set arrow 12 from 1 , 2 to 1 , 1 nohead lw 2 
set arrow 13 from 1 , 2 to 1 , 3 nohead lw 2 
set arrow 14 from 1 , 3 to 1 , 2 nohead lw 2 
set arrow 15 from 1 , 2 to 2 , 2 nohead lw 2 
set arrow 16 from 2 , 2 to 1 , 2 nohead lw 2 
set arrow 17 from 1 , 3 to 1 , 4 nohead lw 2 
set arrow 18 from 1 , 4 to 1 , 3 nohead lw 2 
set arrow 19 from 1 , 3 to 2 , 3 nohead lw 2 
set arrow 20 from 2 , 3 to 1 , 3 nohead lw 2 
set arrow 21 from 1 , 4 to 2 , 4 nohead lw 2 
set arrow 22 from 2 , 4 to 1 , 4 nohead lw 2 
set arrow 23 from 2 , 0 to 3 , 0 nohead lw 2 
set arrow 24 from 3 , 0 to 2 , 0 nohead lw 2 
set arrow 25 from 2 , 2 to 2 , 3 nohead lw 2 
set arrow 26 from 2 , 3 to 2 , 2 nohead lw 2 
set arrow 27 from 2 , 2 to 3 , 2 nohead lw 2 
set arrow 28 from 3 , 2 to 2 , 2 nohead lw 2 
set arrow 29 from 2 , 3 to 2 , 4 nohead lw 2 
set arrow 30 from 2 , 4 to 2 , 3 nohead lw 2 
set arrow 31 from 2 , 3 to 3 , 3 nohead lw 2 
set arrow 32 from 3 , 3 to 2 , 3 nohead lw 2 
set arrow 33 from 2 , 4 to 3 , 4 nohead lw 2 
set arrow 34 from 3 , 4 to 2 , 4 nohead lw 2 
set arrow 35 from 3 , 2 to 3 , 3 nohead lw 2 
set arrow 36 from 3 , 3 to 3 , 2 nohead lw 2 
set arrow 37 from 3 , 3 to 3 , 4 nohead lw 2 
set arrow 38 from 3 , 4 to 3 , 3 nohead lw 2 
set arrow 39 from 3 , 3 to 4 , 3 nohead lw 2 
set arrow 40 from 4 , 3 to 3 , 3 nohead lw 2 
set arrow 41 from 3 , 4 to 4 , 4 nohead lw 2 
set arrow 42 from 4 , 4 to 3 , 4 nohead lw 2 
set arrow 43 from 4 , 3 to 4 , 4 nohead lw 2 
set arrow 44 from 4 , 4 to 4 , 3 nohead lw 2 
plot "grafica6.dat" using 1:2:3 with points pt 7 lc var ps 2  
quit()
