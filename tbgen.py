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
	if(len(sys.argv)!=4 and len(sys.argv)!=5):
		print("python3 tbgen.py [bitwidth] [size] [operator] <mode bin|dec|hex>")
		sys.exit(-1)	
	bitwidth = int(sys.argv[1])
	SIZE = int(sys.argv[2])
	operator = sys.argv[3]
	mode = 'dec'
	binmode = False;
	if(len(sys.argv)==5):
		mode = sys.argv[4]
		if(mode != 'bin'and mode != 'dec' and mode != 'hex'):
			print("Specify correct mode: bin|dec|hex");
			sys.exit(1)
	
	outdir = "output"
	create_dir(outdir)
	outfilename = outdir + "/tb_"+str(bitwidth)+'_'+GetOperatorName(operator)\
		+".txt"
	tbof = open(outfilename,'w')
	seta = set()
	setb = set()
	while(len(seta)<SIZE):
		seta.add(random.randint(0,(math.pow(2, bitwidth-2)-1)))
	while(len(setb)<SIZE):
		setb.add(random.randint(0,(math.pow(2, bitwidth-2)-1)))
		

	for i in range(SIZE):
		a = seta.pop();
		b = setb.pop();
		if(mode=='dec'):
			tbof.write('%d %d %d\n' % ( a, b, Operation(a, b, operator) ) )	;
		elif(mode=='hex'):
			if(operator == '*'):
				tbof.write('%s %s %s\n' % (\
					'{0:04x}'.format(a),\
					'{0:04x}'.format(b),\
					'{0:08x}'.format(Operation(a,b,operator))));
			else:
				tbof.write('%s %s %s\n' % (\
					'{0:04x}'.format(a),\
					'{0:04x}'.format(b),\
					'{0:08x}'.format(Operation(a,b,operator))))

		else:
			if(operator == '*'):
				tbof.write('%s %s %s\n' % (\
					'{0:032b}'.format(a),\
					'{0:032b}'.format(b),\
					'{0:064b}'.format(Operation(a,b,operator))));
			else:
				tbof.write('%s %s %s\n' % (\
					'{0:032b}'.format(a),\
					'{0:032b}'.format(b),\
					'{0:033b}'.format(Operation(a,b,operator))))
	tbof.close()

	print('File generated!' + outfilename)
	print('Total number of random numbers: ',SIZE)



