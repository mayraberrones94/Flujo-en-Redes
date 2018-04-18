set term postscript color eps
set output "nodos.eps"
set size square
set key off
set xrange [-1.1:1.1]
set yrange [-1.1:1.1]
set arrow 1 from 0.0 , 1.0 to 0.9510565162951535 , 0.30901699437494745 nohead filled lw 1 lc 2
set arrow 2 from 0.5877852522924731 , 0.8090169943749475 to 0.9510565162951535 , 0.30901699437494745 nohead filled lw 1 lc 2
set arrow 3 from 0.9510565162951535 , 0.30901699437494745 to -0.9510565162951535 , -0.30901699437494756 nohead filled lw 1 lc 2
set arrow 4 from 0.9510565162951536 , -0.30901699437494734 to 1.2246467991473532e-16 , -1.0 nohead filled lw 1 lc 2
set arrow 5 from 0.9510565162951536 , -0.30901699437494734 to -0.587785252292473 , -0.8090169943749475 nohead filled lw 1 lc 2
set arrow 6 from 0.5877852522924732 , -0.8090169943749473 to -0.9510565162951536 , 0.30901699437494723 nohead filled lw 1 lc 2
set arrow 7 from 1.2246467991473532e-16 , -1.0 to -0.5877852522924732 , 0.8090169943749473 nohead filled lw 1 lc 2
set arrow 8 from -0.587785252292473 , -0.8090169943749475 to -0.9510565162951535 , -0.30901699437494756 nohead filled lw 1 lc 2
set arrow 9 from -0.587785252292473 , -0.8090169943749475 to -0.9510565162951536 , 0.30901699437494723 nohead filled lw 1 lc 2
set arrow 10 from -0.9510565162951535 , -0.30901699437494756 to -0.5877852522924732 , 0.8090169943749473 nohead filled lw 1 lc 2
set arrow 11 from -0.9510565162951536 , 0.30901699437494723 to -0.5877852522924732 , 0.8090169943749473 nohead filled lw 1 lc 2
plot "grafica.dat" using 1:2:3 with points pt 7 ps 2 lc var 
quit()
