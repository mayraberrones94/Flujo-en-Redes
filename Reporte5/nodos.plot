set term postscript color eps
set output "nodos4.eps"
set size square
set key off
set xrange [-1: 4 ]
set yrange [-1: 4 ]
set arrow 1 from 0 , 0 to 0 , 1 nohead lw 2 
set arrow 2 from 0 , 1 to 0 , 0 nohead lw 2 
set arrow 3 from 0 , 1 to 0 , 2 nohead lw 2 
set arrow 4 from 0 , 2 to 0 , 1 nohead lw 2 
set arrow 5 from 0 , 1 to 1 , 1 nohead lw 2 
set arrow 6 from 1 , 1 to 0 , 1 nohead lw 2 
set arrow 7 from 0 , 2 to 1 , 2 nohead lw 2 
set arrow 8 from 1 , 2 to 0 , 2 nohead lw 2 
set arrow 9 from 1 , 1 to 1 , 2 nohead lw 2 
set arrow 10 from 1 , 2 to 1 , 1 nohead lw 2 
set arrow 11 from 1 , 1 to 2 , 1 nohead lw 2 
set arrow 12 from 2 , 1 to 1 , 1 nohead lw 2 
set arrow 13 from 1 , 2 to 1 , 3 nohead lw 2 
set arrow 14 from 1 , 3 to 1 , 2 nohead lw 2 
set arrow 15 from 1 , 3 to 2 , 3 nohead lw 2 
set arrow 16 from 2 , 3 to 1 , 3 nohead lw 2 
set arrow 17 from 2 , 0 to 2 , 1 nohead lw 2 
set arrow 18 from 2 , 1 to 2 , 0 nohead lw 2 
set arrow 19 from 2 , 1 to 3 , 1 nohead lw 2 
set arrow 20 from 3 , 1 to 2 , 1 nohead lw 2 
set arrow 21 from 2 , 3 to 3 , 3 nohead lw 2 
set arrow 22 from 3 , 3 to 2 , 3 nohead lw 2 
set arrow 23 from 3 , 1 to 3 , 2 nohead lw 2 
set arrow 24 from 3 , 2 to 3 , 1 nohead lw 2 
set arrow 25 from 3 , 2 to 3 , 3 nohead lw 2 
set arrow 26 from 3 , 3 to 3 , 2 nohead lw 2 
set arrow 27 from 2 , 1 to 0 , 1 head filled lw 1 lc 3
plot "grafica4.dat" using 1:2:3 with points pt 7 lc var ps 2  
quit()
