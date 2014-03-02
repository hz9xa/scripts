'''
This file is used to generate test vectors for HSIM
arguments: None
outputs: ./output/hsim.vec, text based stimulus file to be used by vectorgen.pl
'''

import sys,math,random
from bitstring import BitArray
######################
period=1.7 
numVecs=1000 #number of input vectors for each input
inputs=["X","Y"]
inputWidth=32 #LSb is bit 0
c=0
outfile="./output/hsim.vec"
######################
vecs=[]
numInputs=len(inputs)
with open(outfile,"w") as of:
    of.write("TUNIT=ns\n")
    of.write("TSU=0.001\n")
    of.write("VHI=VDD\n")
    of.write("VLO=0\nSLEW=0.001\n")
    of.write("TCYCLE="+str(period)+"\n\n")

    # generating input vectors btw 0,1.0
    for i in range(numInputs * numVecs):
        vecs.append(BitArray(float=random.uniform(0,1.0),length=inputWidth).bin)
#    print(vecs)
    for input in inputs:
        index = inputs.index(input)
        for i in range(inputWidth):
            of.write(input+"<"+str(i)+"> ")                
            for j in range(index*numVecs,(index+1)*numVecs):
                if i < c:
                    of.write("0")
                else:
                    of.write(vecs[j][inputWidth-i-1])
            of.write("\n")
