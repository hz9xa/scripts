'''
This scipt generates random numbers
Created on Oct 4, 2012

@author: Eric Zhang
'''
import sys,random,math



if __name__ == "__main__":
    if(len(sys.argv)!=3):
        print("python3 rmgenerator.py [bitwidth] [size]")
        exit(-1)
    bitwidth = int(sys.argv[1])
    LIMIT = int(sys.argv[2])

    ofa = open("f" + str(bitwidth) + "a.txt",'w')
    ofb = open("f" + str(bitwidth) + "b.txt",'w')

    for j in range(LIMIT):
        ofa.write('%d\n' % (random.randint(-1*math.pow(2, bitwidth-1),\
                            (math.pow(2, bitwidth-1)-1))))
        ofb.write('%d\n' % (random.randint(-1*math.pow(2, bitwidth-1),\
                            (math.pow(2, bitwidth-1)-1))))
   
    ofa.close()
    ofb.close()
    print('Files generated!\n')                    
