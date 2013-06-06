'''
This scipt generates random numbers
with a given bitwidth and size

Created on Oct 4, 2012

Updated on June 4, 2013
  Modified: generate unique random numbers 


@author: Eric Zhang
@email: hz9xa@virginia.edu
'''
import sys,os,random,math

def create_dir(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


if __name__ == "__main__":
    if(len(sys.argv)!=3):
        print("python3 rmgenerator.py [bitwidth] [size]")
        exit(-1)
    bitwidth = int(sys.argv[1])
    LIMIT = int(sys.argv[2])
    
    outdir = "output"
    create_dir(outdir)

    ofa = open(outdir + "/f" + str(bitwidth) + "a.txt",'w')
    ofb = open(outdir + "/f" + str(bitwidth) + "b.txt",'w')
    
    seta = set()
    setb = set()

    while(len(seta) < LIMIT):
        seta.add(random.randint(-1*math.pow(2, bitwidth-1),\
                            (math.pow(2, bitwidth-1)-1)))

    for i in range(len(seta)):
        ofa.write('%d\n' % seta.pop())

    ofa.close()

    while(len(setb) < LIMIT):
        setb.add(random.randint(-1*math.pow(2, bitwidth-1),\
                           (math.pow(2, bitwidth-1)-1)))

    for i in range(len(setb)):
        ofb.write('%d\n' % setb.pop())
  
    ofb.close()
   
    
    print('Files generated!')
    print('Total number of random numbers: ',LIMIT)
                    
