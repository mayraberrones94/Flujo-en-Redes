set term postscript color eps
set output "nodos2.eps"
set size square
set key off
set xrange [-.5:1.5]
set yrange [-.1:1.1]
set label  '  0#3#1    '  at -0.3 , 0.5
set label  '  4#2    '  at 1.3 , 0.5
set arrow 1 from -0.3 , 0.5 to 1.3 , 0.5 nohead filled lw 1
set label  '  27  '  at 0.5 , 0.44
plot "grafo2.dat" using 1:2:3 with points pt 7 lc var ps 2 
quit()
