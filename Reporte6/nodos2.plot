set term postscript color eps
set output "nodos2.eps"
set size square
set key off
set xrange [-.3:1.3]
set yrange [-.1:1.1]
unset border
unset xtics
unset ytics
set label  '  0#87#33#66#24#29#41#46#74#2#56#12#55#59#63#8#77#35#58#32#31#16#91#30#18#54#78#4#38#48    '  at -0.3 , 0.5
set label  '  99#68#65#69#9#96#17#26#22#62#67#40#88#19#84#93#85#10#1#94#50#61#95#97#34#75#71#39#47#76#89#64#7#73#28#49#45#43#57#6#36#79#42#20#15#11#3#70#51#25#82#90#44#81#5#60#21#52#80#37#86#92#13#72#23#14#27#53#98#83    '  at 1.3 , 0.5
set arrow 1 from -0.3 , 0.5 to 1.3 , 0.5 nohead filled lw 1
set label  '  6609  '  at 0.5 , 0.44
plot "grafo2.dat" using 1:2:3 with points pt 7 lc var ps 2 
quit()
