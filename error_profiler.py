"""
FILE NAME: error_profiler.py
This file profiles the error in terms of positive and negative numbers

To be added:
    1. Make in to distributions log2 based 
    2. Maximum, Minimum
    3. WED,MED
"""

import sys

if __name__ == "__main__":
    if(len(sys.argv)!=2):
        print("Usage: python3 error_profiler.py [filename] ")
        exit(-1)

    posnums = []
    negnums = []
    infile = open(sys.argv[1],'r')
    lines = infile.readlines()
    for x in lines:
        num = int(x)
        if num > 0 :
            posnums.append(num)
        else:
            negnums.append(num)    
    
    posnums.sort()
    negnums.sort()
    outfile = open('error_profile.txt','w')
    outfile.write("Total # of errors: %d\n" % len(lines))
    outfile.write("# of positive errors: %d\n" % len(posnums))
    outfile.write("# of negative errors: %d\n" % len(negnums))
    outfile.write("Positive Error Rates: %.2f\n" % (len(posnums)/float(len(lines))))
    outfile.write("Negative Error Rates: %.2f\n" % (len(negnums)/float(len(lines))))
    outfile.write("Max error: %d\n" % posnums[-1])
    outfile.write("Min error: %d\n" % negnums[0])
    outfile.write("Mean error: %.4f\n" % ((sum(posnums)+sum(negnums))/float(len(posnums)+len(negnums))))
    
    outfile.close()
    infile.close()
    
