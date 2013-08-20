import sys,os,glob
import numpy as np
import matplotlib.pyplot as plt
import math

def IPlotBar(x,y,title):
    bar_width = 1
    opacity = 0.8
    plt.bar(x,y,bar_width,alpha=opacity,color='b')
    plt.xlabel("Range",fontsize=16)
    plt.ylabel(u"\u03B5",fontsize=16)    
    plt.title(title,fontsize=24)
    plt.xticks(x,x)
    plt.tight_layout()
    filename = "output/"+title+".jpg"
    plt.savefig(filename)
    


if __name__ == '__main__':
    if(len(sys.argv) != 4):
        print("python draw_err_distri.py [file pattern] [total number] [Title]")
        sys.exit(1)
    patrn = sys.argv[1]
    total = float(sys.argv[2])
    title = sys.argv[3]
    files = glob.glob(patrn)
    for f in files:
        dist={}
        num_zeros = 0
        with open(f,'r') as inf:
            for line in inf:
                nums = line.split(" ")
                for num in nums:
                    num = int(num)
                    if (num < 0):
                        num = -1 * num
                        k = -1*int(math.log(num)/math.log(2)) - 1
                        if not dist.has_key(k):
                            dist[k] = 0
                        dist[k]+=1;
                    elif num > 0:
                        k = int(math.log(num)/math.log(2))
                        if not dist.has_key(k):
                            dist[k] = 0
                        dist[k]+=1;
                    else: 
                        num_zeros+=1         
        keys = dist.keys()
        keys.sort()
        xmin = keys[0]
        xmax = keys[-1]
        absmax = max(abs(xmin),abs(xmax))
        xmin = -1 * absmax - 1
        xmax = absmax + 1
        x = np.arange(xmin,xmax+1,1)
        y = []
        for i in x:
            if i not in dist.keys():
                y.append(0)
            else:
                y.append(dist[i]/total)
        IPlotBar(x,y,title)
        
     


