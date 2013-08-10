import numpy as np
from pylab import *
import operator
import os,sys
    

if __name__ == '__main__':
    if(len(sys.argv)!= 2):
        print("Specify a file pattern");
        sys.exit(1)
    patn = sys.argv[1]
    files = glob.glob(patn);
    for file in files:
        delay=[]
        power=[]
        area=[]
        energy=[]
        EDP=[]
        with open(file,'r') as f:
            for line in f:
                res = line.split()
                delay.append(int(res[0]))
                power.append(float(res[1]))
                area.append(float(res[2]))
                energy.append(power[-1] * delay[-1])
                EDP.append(energy[-1] * delay[-1])

        
                
