import numpy as np
import matplotlib.pyplot as plt
import operator
import os,sys

def IPlot(x,ys,xlabel,ylabels):
    for i in range(len(ys)):
        title=ylabels[i] + "vs. xlabel"
        fname='output/'+ylabels[i]+'.pdf'
        plt.figure(i)
        plt.plot(x,ys[i])
        plt.xlabel(xlabel)
        plt.ylabel(ylabels[i])
        plt.title(title)
        savefig(fname)
        print("Plotted %s" % title)

        

if __name__ == '__main__':
    if(len(sys.argv)!= 2):
        print("Specify a file pattern");
        sys.exit(1)
    ylabes=["power","area","Energy","EDP"]
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
                    
       IPlot(delay,[power,area,energy,EDP],'delay',ylabels)


               
