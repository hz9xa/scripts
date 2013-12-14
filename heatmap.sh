#!/bin/sh
out_file=./temp.gpi
font=/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf
echo "set term png font \"$font\" size 800,600" >> ${out_file}
echo "set style rectangle back fc lt -3 fillstyle  solid 1.00 border -1" >> ${out_file}
echo "unset key" >> ${out_file}
echo "set view map" >> ${out_file}
echo "set xtics border in scale 0,0 mirror norotate  offset character 0, 0, 0" >> ${out_file}
echo "set tics font \"$font,20\"" >> ${out_file}
echo "set ytics border in scale 0,0 mirror norotate  offset character 0, 0, 0" >> ${out_file}
echo "set xrange [0 : 512 ];" >> ${out_file}
echo "set yrange [0 : 512 ];" >> ${out_file}
echo "set ylabel  offset character 0, 0, 0 font \"\" textcolor lt -1 rotate by 90" >> ${out_file}
echo "set cblabel \"Temperature (Kelvin)\" " >> ${out_file}
echo "set cblabel  offset character 1.8, 0, 0 font \"$font,20\" textcolor lt -1 rotate by 90" >> ${out_file}
echo "set cbrange [ * : * ] noreverse nowriteback" >> ${out_file}
echo "set palette rgbformulae 21, 22, 23 " >> ${out_file}
echo "set term gif" >> ${out_file}
echo "set output \"$1.gif\"" >> ${out_file}
echo "plot \"$1\" using 1:2:3 with image" >> ${out_file}

gnuplot ${out_file}
rm ${out_file}
