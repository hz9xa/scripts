#!/bin/python
import sys,os,math

if __name__ == "__main__":
    filename = sys.argv[1]    
    buckets={}
    weights={}
    crt_bkt=0
    invalid_entry = 0
    num_entries=0
    with open(filename,'r') as inf:
        lines = inf.readlines()
        num_entries = len(lines)
        for line in lines:
            if line == 'nan':
                invalid_entry+=1
            elif float(line) == 0.0:
                crt_bkt+=1
            else:
                flt = float(line)
                brac = math.floor(math.log(flt,2))
                if not buckets.has_key(brac):
                    buckets[brac]=0
                buckets[brac]+=1
    num_valid_entries = num_entries - invalid_entry
    for key in buckets.keys():
        weights[key] = buckets[key]/num_entries
    print(buckets)
    print(weights)
    



                
