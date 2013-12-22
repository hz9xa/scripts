#!/usr/bin/python
"""
This script is used for profiling arithmetic operations from a GPGPU benchmark.
Input provided by arithmetic profiling from GPGPU-SIM 
Outputs the total count of each operation
"""
import os,sys

def init():
	ops={"abs":0,'add':0,'addp':0,'addc':0,'and':0,'andn':0, \
	     'cos':0,'div':0,'ex2':0,'fma':0,'lg2':0,'mad24':0, \
             'mad':0,'madp':0,'max':0,'min':0,'mul24':0,'mul':0,\
             'neg':0,'nandn':0,'norn':0,'not':0,'or':0,'orn':0,\
             'rcp':0,'rem':0, 'rsqrt':0,'sad':0,'popc':0,'set':0,\
             'shl':0,'shr':0,'sin':0,'slct':0,'sub':0,'subc':0,\
             'xor':0,'cmp':0,'sqrt':0}
	typename={'298':'S8','299':'S16','300':'S32',\
             '301':'S64','302':'U8','303':'U16',\
             '304':'U32','305':'U64','306':'F16',\
             '307':'F32','308':'F64','309':'F64','310':'B8',\
             '311':'B16','312':'B32','313':'B64','314':'B64',\
             '315':'B128'}
	types={}
	for key in typename.keys():
		types[key]=dict(ops)

	return typename,types




if __name__ == '__main__':
	if len(sys.argv) != 2 :
		print("Please specify filename");
		sys.exit(1)
	fname = sys.argv[1]
	typename,types = init()
 	size=0
	with open(fname,'r') as f:
		for line in f:
			size+=1
			entry = line.split()
			if not types[entry[-1]].has_key(entry[0]):
				print("Missing operaiton type: %s" % entry[0])
				sys.exit(1)
			types[entry[-1]][entry[0]] += 1;
#			if size == 10:
#				break		
	
	print("Total # of operations: %d" % size)
	with open(fname.split('.')[0]+'res.txt','w') as of:
		of.write("Total\t%d\n" % size)
		for type in types.keys():
			for op in types[type].keys():
				if types[type][op] != 0:
					of.write("%s\t%d\t%.2f\n" %\
                                        (typename[type]+"_"+op,types[type][op],types[type][op]/float(size)))
   				
	

