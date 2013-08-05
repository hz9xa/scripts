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
	types={'298':[0,'S8_TYPE'],'299':[0,'S16_TYPE'],'300':[0,'S32_TYPE'],\
             '301':[0,'S64_TYPE'],'302':[0,'U8_TYPE'],'303':[0,'U16_TYPE'],\
             '304':[0,'U32_TYPE'],'305':[0,'U64_TYPE'],'306':[0,'F16_TYPE'],\
             '307':[0,'F32_TYPE'],'308':[0,'F64_TYPE']}
	return ops,types




if __name__ == '__main__':
	ops,types = init()
 	size=0
	fname = 'arith.txt'
	with open(fname,'r') as f:
		for line in f:
			size+=1
			entry = line.split()
			if not ops.has_key(entry[0]):
				print("Missing operaiton type: %s" % entry[0])
				sys.exit(1)
			ops[entry[0]] += 1
			types[entry[-1]][0] += 1;
			if size == 10:
				break		
	
	print("Total # of operations: %d" % size)
	for op in ops.keys():
		print("%s\t%d" % (op,ops[op]))
	for type in types.keys():
		print("%s\t%d" % (types[type][1],types[type][0]))
   
	

