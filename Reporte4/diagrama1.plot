set term postscript color eps
set output 'Diagrama3.eps'
set key off
set xlabel 'Probabilidad P'
set ylabel 'Distancia Normalizada'
set y2label 'Densidad Promedio'
set style fill solid 0.25 border -1
set style line 1 lt 1 linecolor rgb 'red' lw 2 pt 1
set style line 2 lt 1 linecolor rgb 'blue' lw 2 pt 1
set style data boxplot
plot 'Prom_dis.csv' using 1:2 ls 1 title 'Probabilidad' with lines, 'Cluster_coef.csv' using 1:2 ls 2 title 'Distancias' with lines
