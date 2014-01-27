import sys
import math
import numpy as np
from hellinger import *

def MSE(p,q):
    if len(p) != len(q) :
        print("ERROR: unequal length in mse");
        sys.exit(1)
    s = 0
    N = len(p)
    for (x,y) in zip(p,q):
        s += (x-y)*(x-y)
    return s/N
def test(p,name):
    for x in p:
        try:
            r = math.sqrt(x)
        except:
            print("%s %f" % (name,x))

if __name__=='__main__':
    refile = open('ref.txt','r')
    imprefile = open('output.txt','r')
    reflines = refile.readlines()[2:]
    imprelines = imprefile.readlines()[2:]
    
    errsum = 0
    abserrsum = 0
    maxerr = 0
    minerr = 0
    stddev = 0    
    h1 = 0; h2 = 0; h3 = 0;

    refnums = []
    imprenums = []
    errs = []

    for refline in reflines:
        strings = refline.rstrip().split(' ')
 #       print(len(strings))
        for stringnum in strings:
            refnums.append(float(stringnum))

    for impreline in imprelines:
        strings = impreline.rstrip().split(' ')
        for stringnum in strings:
            imprenums.append(float(stringnum))

    for (ref,impre) in zip(refnums,imprenums):
        #errsum += ref - impre
        #abserrsum += abs(ref - impre)
        errs.append(ref-impre)
    
    errarry = np.array(errs)
    meanerr = np.mean(errarry)
    mae = np.mean(np.absolute(errarry))
    mse = MSE(refnums,imprenums)
    std = np.std(errarry)
    
    h1=hellinger1(np.absolute(np.array(refnums)),np.absolute(np.array(imprenums)));
    h2=hellinger2(np.absolute(np.array(refnums)),np.absolute(np.array(imprenums)));
    h3=hellinger3(np.absolute(np.array(refnums)),np.absolute(np.array(imprenums)));
#    test(refnums,'ref');
#    test(imprenums,'impre');

    print("="*40)
    print("mean error: %f" % meanerr)
    print("MAE: %f" % mae)
    print("mse: %f" % mse)
    print("std: %f" % std)
    print("h1: %f" % h1)
    print("h2: %f" % h1)
    print("h3: %f" % h1)
    print("="*40)
