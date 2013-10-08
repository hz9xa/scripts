# -*- coding: utf-8 -*-
"""
Created on Tue Oct 08 09:59:44 2013

@author: Eric
"""
import sys
import fp2bin

if "__name__" == "__main__":
    if len(sys.argv) != 2:
        print("Specify filename")
        sys.exit(1)
    fname = sys.argv[1]
    ofile = open("filetered_"+sys.argv[1],'w')
    with open(fname,'r') as inf:
        for line in inf:
            items = line.split()
            if (items[0] == "mul"):
                a = fp2bin(float(items[1]))
                b = fp2bin(float(items[2]))
                r = fp2bin(float(items[3]))
                ofile.write("%s\t%s\t%s"%(a,b,r));
                 