set term postscript color eps
set output "nodos.eps"
set size square
set key off
set xrange [-.5:1.5]
set yrange [-.1:1.1]
set label    '  0    '  at -0.3 , 0.5
set label    '  1    '  at 0.3740004642847248 , 0.6867972917643426
set label    '  2    '  at 0.5295590919751489 , 0.8936834956423404
set label    '  3    '  at 0.5978094237310939 , 0.9266519843838616
set label    '  4    '  at 1.3 , 0.5
set arrow 1 from -0.3 , 0.5 to 0.3740004642847248 , 0.6867972917643426 nohead filled lw 1
set label  '  6  '  at 0.037000232142362394 , 0.5933986458821713
set arrow 2 from -0.3 , 0.5 to 0.5978094237310939 , 0.9266519843838616 nohead filled lw 1
set label  '  9  '  at 0.14890471186554696 , 0.7133259921919308
set arrow 3 from -0.3 , 0.5 to 1.3 , 0.5 nohead filled lw 1
set label  '  16  '  at 0.5 , 0.5
set arrow 4 from 0.5295590919751489 , 0.8936834956423404 to 0.3740004642847248 , 0.6867972917643426 nohead filled lw 1
set label  '  2  '  at 0.45177977812993686 , 0.7902403937033415
set arrow 5 from 0.5295590919751489 , 0.8936834956423404 to 0.5978094237310939 , 0.9266519843838616 nohead filled lw 1
set label  '  0  '  at 0.5636842578531214 , 0.910167740013101
set arrow 6 from 0.5978094237310939 , 0.9266519843838616 to -0.3 , 0.5 nohead filled lw 1
set label  '  9  '  at 0.14890471186554696 , 0.7133259921919308
set arrow 7 from 0.5978094237310939 , 0.9266519843838616 to 0.5295590919751489 , 0.8936834956423404 nohead filled lw 1
set label  '  0  '  at 0.5636842578531214 , 0.910167740013101
set arrow 8 from 1.3 , 0.5 to -0.3 , 0.5 nohead filled lw 1
set label  '  16  '  at 0.5 , 0.5
set arrow 9 from 1.3 , 0.5 to 0.3740004642847248 , 0.6867972917643426 nohead filled lw 1
set label  '  9  '  at 0.8370002321423624 , 0.5933986458821713
set arrow 10 from 1.3 , 0.5 to 0.5295590919751489 , 0.8936834956423404 nohead filled lw 1
set label  '  8  '  at 0.9147795459875745 , 0.6968417478211701
plot "grafo.dat" using 1:2:3 with points pt 7 lc var ps 2 
quit()
