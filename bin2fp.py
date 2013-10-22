#!/usr/bin/python
from bitstring import BitArray

def bin2fp(a):
	alpha = BitArray(bin=a)
	print(alpha.float)
	print(alpha.hex)
	
if __name__ == "__main__":
	while True:
		cm = input("Enter a binary string(q to exit): ")
		if cm == 'q':
			print("Bye")
			break;
		bin2fp(cm)
