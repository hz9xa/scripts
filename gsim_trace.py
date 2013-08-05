#!/usr/bin/python
import os,sys

def init():
	ops={"abs":0,'add':0,'addp':0,'addc':0,'and':0,'andn':0, \
	     'cos':0,'div':0,'ex2':0,'fma':0,'lg2':0,'mad24':0, \
             'mad':0,'madp':0,'max':0,'min':0,'mul24':0,'mul':0,\
             'neg':0,'nandn':0,'norn':0,'not':0,'or':0,'orn':0,\
             'rcp':0,'rem':0, 'rsqrt':0,'sad':0,'popc':0,'set':0,\
             'shl':0,'shr':0,'sin':0,'slct':0,'sub':0,'subc':0,\
             'xor':0}
	typename={'298':'S8_TYPE','299':'S16_TYPE','300':'S32_TYPE',\
             '301':'S64_TYPE','302':'U8_TYPE','303':'U16_TYPE',\
             '304':'U32_TYPE','305':'U64_TYPE','306':'F16_TYPE',\
             '307':'F32_TYPE','308':'F64_TYPE'}
	types={}
	for key in typename.keys():
		types[key]=dict(ops)

	return typename,types




if __name__ == '__main__':
	typename,types = init()
 	size=0
	fname = 'arith.txt'
	with open(fname,'r') as f:
		for line in f:
			size+=1
			entry = line.split()
#			if not types[entry[-1]].has_key(entry[0]):
#				print("Missing operaiton type: %s" % entry[0])
#				sys.exit(1)
			types[entry[-1]][entry[0]] += 1;
#			if size == 10:
#				break		
	
	print("Total # of operations: %d" % size)
	with open('analysis.txt','w') as of:
		for type in types.keys():
			of.write("%s\n" % (typename[type]))
			for op in types[type].keys():
				of.write("%s\t%d\n" % (op,types[type][op]))
   
	

