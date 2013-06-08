import sys,os,random,math


def create_dir(directory):
	if not os.path.exists(directory):
		os.mkdir(directory)

def Operation(a,b,operator):
	if operator == "+":
		return a+b;
	elif operator == "*" :
		return a*b;
	else:
		print("Unsupported operator: "+ operator)
		sys.exit(1)
		
def GetOperatorName(operator):
	if operator == "+":
		return "add";
	elif operator == "*" :
		return "mult";
	else:
		print("Unsupported operator: "+operator)
		sys.exit(1)

if __name__ == "__main__":
	if(len(sys.argv)!=4):
		print("python3 rmgenerator.py [bitwidth] [size] [operator]")
		sys.exit(-1)	
	bitwidth = int(sys.argv[1])
	SIZE = int(sys.argv[2])
	operator = sys.argv[3]
	
	outdir = "output"
	create_dir(outdir)
	outfilename = outdir + "/tb_"+str(bitwidth)+'_'+GetOperatorName(operator)\
		+".txt"
	tbof = open(outfilename,'w')
	seta = set()
	setb = set()
	while(len(seta)<SIZE):
		seta.add(random.randint(-1*math.pow(2, bitwidth-1),\
                            (math.pow(2, bitwidth-1)-1)))
	while(len(setb)<SIZE):
		setb.add(random.randint(-1*math.pow(2, bitwidth-1),\
                            (math.pow(2, bitwidth-1)-1)))
		

	for i in range(SIZE):
		a = seta.pop();
		b = setb.pop();
		tbof.write('%d %d %d\n' % ( a, b, Operation(a, b, operator) ) )	
	tbof.close()

	print('File generated!' + outfilename)
	print('Total number of random numbers: ',SIZE)



