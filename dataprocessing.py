'''
Created on Oct 4, 2012

@author: Eric
'''
import os
import math
from numpy import *

LIMIT= 100000

k32 = [2,4,8]
#xb32 = [[1],[1,2],[1,2,3,4],[1,2,3,4,5,6,7,8]]

k24 = [2,3,4,6,8]
#xb24 = [[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]]

k16 = [2,4]
#xb16 = [[1],[1,2,3],[1,2,3]]
k8 = [2,4]

mode = [k32,k24,k16,k8]

of = open('finalresult.txt','w')

for i in range(len(mode)): # for each # of bits
    n = (4-i)*8 
    for j in range(len(mode[i])): # for each k
        k = mode[i][j]
        for xb in range(1,k+1): # for each xb 1<= xb <= k
            fa = open('n%s_k%d_xb%derr.txt' % (n,k,xb),'r')
            fb = open('n%s_k%d_xb%d.txt' % (n,k,xb),'r')
            li = []
            lb = []
            for m in range(LIMIT):
                x = int(fa.readline())
                li.append(x)
                if(x<0): print('negative')
                lb.append(float(fb.readline()))
                
            fa.close()
            fb.close()
            #of.write('n%sk%dxb%d:' % (n,k,xb))
            su = 0;
            ls = []
            for x in li:
                su +=x
                ls.append(math.pow(x,2))
            of.write('%s:' % (su/len(li)))
            su=0
            for x in ls:
                su+=x
            of.write('%.10f:' % math.sqrt(su/len(li)))
            su = 0
            for x in lb:
                su+=x
            of.write('%.20f\n'%(su/len(lb)))
            print('Done with n%sk%dxb%d' % (n,k,xb))
            
            
of.close()
            
print('DATA PROCESSING DONE!!!')   