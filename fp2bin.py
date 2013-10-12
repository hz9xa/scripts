from bitstring import BitArray
import sys

def fp2bin(a,len):
	alpha = BitArray(float=a,length=len)
	print(alpha.bin)
	print(alpha.hex)
	
if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("usage: python fp2bin.py [bit width]")
		sys.exit(1)
	len = int(sys.argv[1])
	while True:
		cm = input("Enter a floating number(q to exit): ")
		if cm =='q':
			print("Bye")
			break;
		fp = float(cm)
		fp2bin(fp,len)
