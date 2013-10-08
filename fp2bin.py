# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Eric\.spyder2\.temp.py
"""
import sys,struct
def binary(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0')\
    for c in struct.pack('!f', num))
        

def fp2bin(a):
    return binary(a)


if "__name__" == "__main__":
    while(True):
        print("%s" % fp2bin(input("Floating number:")))
