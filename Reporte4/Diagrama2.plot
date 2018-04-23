set terminal png truecolor
set output 'Diagrama1.png'
set key off
set title 'Diagramas de tiempos '
set xlabel 'Potencias de 2 nodos por grafo'
set ylabel 'Logaritmo de tiempo de procesamiento'
set style fill solid 0.25 border -1
set style boxplot outliers pointtype 7
set style data boxplot
plot 'Tiempoclus.csv' using (-8):(log($3)):(0.5):1
