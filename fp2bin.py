
import struct
def binary(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0')\
    for c in struct.pack('!f', num))
        

def fp2bin(a):
    return binary(a)


if __name__ == "__main__":
    while(True):
        fp = input("Floating number:")
        print("%s" % fp2bin(fp))
