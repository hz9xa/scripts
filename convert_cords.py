import sys,os


if __name__ == '__main__':
    if(len(sys.argv)!=2):
        print("specify file name");
        sys.exit(1)

    ofname =sys.argv[1] + ".txt"
    of = open(ofname,'w')
    row = 0
    col = 0
    with open(sys.argv[1],'r') as f:
        for line in f:
            data = line.split() 
            ind = int(data[0])
            temp = data[1]
            row = ind / 1024
            col = ind % 1024
            of.write("%d\t%d\t%s\n" % (row,col,temp));
    of.close()


