import os,sys
import numpy as np

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
    std = np.std(errarry)
    print("="*40)
    print("mean error: %f" % meanerr)
    print("MAE: %f" % mae)
    print("std: %f" % std)
    print("="*40)
