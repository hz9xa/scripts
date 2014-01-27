import os,sys
from pylab import *
import numpy as np

file = open("output.txt",'r')
lines = file.readlines()[2:]
data = np.array([])
for line in lines:
    data = np.append(data,np.fromstring(line,dtype=float,sep=' '))

reffile=open('ref.txt','r')
lines = reffile.readlines()[2:]
refdata = np.array([])
for line in lines:
    refdata = np.append(refdata,np.fromstring(line,dtype=float,sep=' '))

(ymax,ymin)=(max(data.max(),refdata.max()),min(data.min(),refdata.min()))

x = np.arange(0,256*256,1)
p2,=plot(x,refdata,'r')
p1,=plot(x,data,'y')
ylim(ymin,ymax)
legend([p1,p2],["bit_trunc_18","ref"],loc="upper left")
show()
