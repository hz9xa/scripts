import os,sys,math,random
from bitstring import BitArray

#d: decimal, b: binary
mode='d'
size=200000000
#max=1.0
#min=
outfile="/home/hz9xa/scratch/ihw/input/floats_"+str(size)+".txt"
with open(outfile,'w') as of:
    for i in range(size):
        if (mode=='b'):
            of.write(BitArray(float=random.uniform(0,1.0),length=32).bin)
            of.write("\n")
        elif (mode == 'd'):
            of.write("%e\n" % random.uniform(0,1.0))        
