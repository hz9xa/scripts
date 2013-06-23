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
    if(len(sys.argv)!=3 and len(sys.argv)!=4):
        print("python3 rmgenerator.py [bitwidth] [size] <mode hex|dec>")
        exit(-1)
    bitwidth = int(sys.argv[1])
    LIMIT = int(sys.argv[2])
    mode = 'dec'
    if(len(sys.argv)==4):
        mode = sys.argv[3]
        if(mode != 'dec' and mode!='hex'):
            print("Specify correct mode");
            sys.exit(1)

    outdir = "output"
    create_dir(outdir)

    ofa = open(outdir + "/f" + str(bitwidth) + "_" + mode + "_a.txt",'w')
    ofb = open(outdir + "/f" + str(bitwidth) + "_" + mode + "_b.txt",'w')
    
    seta = set()
    setb = set()

    while(len(seta) < LIMIT):
#       seta.add(random.randint(-1*math.pow(2, bitwidth-1),\
#                            (math.pow(2, bitwidth-1)-1)))
        seta.add(random.randint(0,(math.pow(2, bitwidth-2)-1)))

    for i in range(len(seta)):
        a = seta.pop()
        if(mode=='dec'):
            ofa.write('%d\n' % a)
        else:
            ofa.write('%s\n' % '{0:04x}'.format(a))
    ofa.close()

    while(len(setb) < LIMIT):
#        setb.add(random.randint(-1*math.pow(2, bitwidth-1),\
#                           (math.pow(2, bitwidth-1)-1)))
        setb.add(random.randint(0,(math.pow(2, bitwidth-2)-1)))

    for i in range(len(setb)):
        b = setb.pop()
        if(mode=='dec'):
            ofb.write('%d\n' % b)
        else:
            ofb.write('%s\n' % '{0:04x}'.format(b))
    ofb.close()
   
    
    print('Files generated!')
    print('Total number of random numbers: ',LIMIT)
                    
