### This file is used for calculation the holistic power&energy savings for 
### each GPGPU benchmarks based on the synthesis power and delay data
### and the performance counters from GPGPU-SIM simulator (number of 
### accesses) for each function
### Requires performance counters as input file and fpu&sfu power percentage
### as command line arguments  
### 
### To run, first make sure the input performance counter file is present in 
### current folder. Second, get fpu&power percentage data from excel. 
### Third, modify the impre_mode.txt file to make sure the correct imprecise
### operations are used



import sys,math
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("USAGE: python holistic_power_model.py [acc_profile.txt] [per_fpu_pwr] [per_sfu_pwr]");
        sys.exit(1);
    acc_file = sys.argv[1]
    per_fpu_pwr = float(sys.argv[2])        
    per_sfu_pwr = float(sys.argv[3])

    CLK_FREQ = 700 #MHz

    fpu_acc = {'F32_add':0,'F64_add':0,'F32_mul':0,'F64_mul':0,'F32_div':0,\
                'F64_div':0,'F32_fma':0,'F64_fma':0}
    sfu_acc = {'F32_rcp':0, 'F64_rcp':0,'F32_rsqrt':0,'F64_rsqrt':0,'F32_sqrt':0,\
                'F64_sqrt':0,'F32_lg2':0,'F64_lg2':0}

    op_map = {'F32_add':['fpadd','ifpadd'],'F64_add':['fpadd64','ifpadd64'],'F32_mul':['fpmul','ifpmul'],'F64_mul':['fpmul64','ifpmul64'],'F32_div':['fpdiv','ifpdiv'],\
                'F64_div':['fpdiv64','ifpdiv64'],'F32_fma':['fma','ifma'],'F64_fma':['fma64','ifma64'], 'F32_rcp':['rcp','ircp'], 'F64_rcp':['rcp64','ircp64'],'F32_rsqrt':['rsqrt','irsqrt'],'F64_rsqrt':['rsqrt64','irsqrt64'],'F32_sqrt':['sqrt','isqrt'], 'F64_sqrt':['sqrt64','isqrt64'],'F32_lg2':['log2','ilog2'],'F64_lg2':['log2_64','ilog2_64']}
    fpu_op_map = {} # key in F32_add
    sfu_op_map = {} # key in F32_add
    perf_acc = {} # key in F32_add
    lat_raw = {} # key in fpadd,etc
    pow_raw = {} # key in fpadd,etc
    impre_mode = {} # key in F32_add etc  
    
    avg_fpu_pwr_ihw = 0.0
    avg_sfu_pwr_ihw = 0.0
    avg_fpu_pwr_dw = 0.0
    avg_sfu_pwr_dw = 0.0

    ihw_fpu_energy = 0.0
    ihw_fpu_latency = 0.0
    dw_fpu_energy = 0.0
    dw_fpu_latency = 0.0
    ihw_sfu_energy = 0.0
    ihw_sfu_latency = 0.0
    dw_sfu_energy = 0.0
    dw_sfu_latency = 0.0
    
# mapping to piplined architecture 
    pip_ihw_fpu_eng = 0.0
    pip_ihw_fpu_lat = 0.0
    pip_ihw_sfu_eng = 0.0
    pip_ihw_sfu_lat = 0.0
    pip_dw_fpu_eng = 0.0
    pip_dw_fpu_lat = 0.0
    pip_dw_sfu_eng = 0.0
    pip_dw_sfu_lat = 0.0    
    pip_avg_fpu_pwr_ihw = 0.0
    pip_avg_sfu_pwr_ihw = 0.0
    pip_avg_fpu_pwr_dw = 0.0
    pip_avg_sfu_pwr_dw = 0.0

   

    with open("syn_raw_data_45nm.txt",'r') as srdf:
        lines = srdf.readlines()
        for line in lines[2:]: # skip first two rows
            entry = line.split() 
            lat_raw[entry[0]] = float(entry[1])
            pow_raw[entry[0]] = float(entry[2])
   # print(lat_raw)
   # print()
   # print(pow_raw)        
    with open(acc_file,'r') as accf:
        lines = accf.readlines()
        for line in lines:                
            entry = line.split()
            if len(entry) != 3:
                continue
            if not 'add' in entry[0] and not 'sub' in entry[0]:
                perf_acc[entry[0]] = int(entry[1])
            else:
                if 'sub' in entry[0]:
                    entry[0] = entry[0].replace('sub','add')
                if not perf_acc.has_key(entry[0]):
                    perf_acc[entry[0]] = 0
                perf_acc[entry[0]] = perf_acc[entry[0]] + int(entry[1])
               
               
    #print(perf_acc)
    with open("impre_mode.txt",'r') as imf:
        lines = imf.readlines()
        for line in lines:
            entry = line.split()
            impre_mode[entry[0]] = int(entry[1])
    #print(impre_mode)
    #print(perf_acc.keys())
    for op in perf_acc.keys():
        if op in fpu_acc.keys():
            fpu_acc[op] = perf_acc[op]
            fpu_op_map[op] = op_map[op][impre_mode[op]]
            ihw_fpu_energy = ihw_fpu_energy + fpu_acc[op] * pow_raw[fpu_op_map[op]] * lat_raw[fpu_op_map[op]]
            ihw_fpu_latency = ihw_fpu_latency + fpu_acc[op] * lat_raw[fpu_op_map[op]]
            pip_lat = (fpu_acc[op]-1 + math.ceil(lat_raw[fpu_op_map[op]]/CLK_FREQ*1000))/(CLK_FREQ*1000) # Lat in ms, pwr in mW, eng in uJ
            pip_ihw_fpu_eng = pip_ihw_fpu_eng + pip_lat * pow_raw[fpu_op_map[op]]
            pip_ihw_fpu_lat = pip_ihw_fpu_lat + pip_lat 
            dw_fpu_energy = dw_fpu_energy + fpu_acc[op] * pow_raw[op_map[op][0]] * lat_raw[op_map[op][0]]
            dw_fpu_latency = dw_fpu_latency + fpu_acc[op] * lat_raw[op_map[op][0]]
            pip_lat = (fpu_acc[op]-1 + math.ceil(lat_raw[op_map[op][0]]/CLK_FREQ*1000)) / (CLK_FREQ*1000) 
            pip_dw_fpu_eng = pip_dw_fpu_eng + pip_lat * pow_raw[op_map[op][0]]
            pip_dw_fpu_lat = pip_dw_fpu_lat + pip_lat 
            print("%s %s" % (fpu_acc[op], fpu_op_map[op]))

        elif op in sfu_acc.keys():
            sfu_acc[op] = perf_acc[op]
            sfu_op_map[op] = op_map[op][impre_mode[op]]
            ihw_sfu_energy = ihw_sfu_energy + sfu_acc[op] * pow_raw[sfu_op_map[op]] * lat_raw[sfu_op_map[op]]
            ihw_sfu_latency = ihw_sfu_latency + sfu_acc[op] * lat_raw[sfu_op_map[op]]
            pip_lat = (sfu_acc[op]-1 + math.ceil(lat_raw[sfu_op_map[op]]/CLK_FREQ*1000)) / (CLK_FREQ*1000)
            pip_ihw_sfu_eng = pip_ihw_sfu_eng + pip_lat * pow_raw[sfu_op_map[op]]
            pip_ihw_sfu_lat = pip_ihw_sfu_lat + pip_lat 
            dw_sfu_energy = dw_sfu_energy + sfu_acc[op] * pow_raw[op_map[op][0]] * lat_raw[op_map[op][0]]
            dw_sfu_latency = dw_sfu_latency + sfu_acc[op] * lat_raw[op_map[op][0]]
            pip_lat = (sfu_acc[op]-1 + math.ceil(lat_raw[op_map[op][0]]/CLK_FREQ*1000)) / (CLK_FREQ*1000) 
            pip_dw_sfu_eng = pip_dw_fpu_eng + pip_lat * pow_raw[op_map[op][0]]
            pip_dw_sfu_lat = pip_dw_sfu_lat + pip_lat 
            print("%s %s" % (sfu_acc[op], sfu_op_map[op]))
   
    avg_fpu_pwr_ihw = ihw_fpu_energy / ihw_fpu_latency
    avg_sfu_pwr_ihw = ihw_sfu_energy /ihw_sfu_latency
    avg_fpu_pwr_dw = dw_fpu_energy / dw_fpu_latency
    avg_sfu_pwr_dw = dw_sfu_energy / dw_sfu_latency
    pip_avg_fpu_pwr_ihw = pip_ihw_fpu_eng / pip_ihw_fpu_lat
    pip_avg_sfu_pwr_ihw = pip_ihw_sfu_eng /pip_ihw_sfu_lat
    pip_avg_fpu_pwr_dw = pip_dw_fpu_eng / pip_dw_fpu_lat
    pip_avg_sfu_pwr_dw = pip_dw_sfu_eng / pip_dw_sfu_lat
  
    avg_fpu_pwr_impr = (avg_fpu_pwr_dw - avg_fpu_pwr_ihw) / avg_fpu_pwr_dw * 100
    avg_sfu_pwr_impr = (avg_sfu_pwr_dw - avg_sfu_pwr_ihw) / avg_sfu_pwr_dw * 100
    pip_avg_fpu_pwr_impr = (pip_avg_fpu_pwr_dw - pip_avg_fpu_pwr_ihw) / pip_avg_fpu_pwr_dw * 100
    pip_avg_sfu_pwr_impr = (pip_avg_sfu_pwr_dw - pip_avg_sfu_pwr_ihw) / pip_avg_sfu_pwr_dw * 100
       
    tot_pwr_impr = (per_fpu_pwr * avg_fpu_pwr_impr + per_sfu_pwr * avg_sfu_pwr_impr)/100
    pip_tot_pwr_impr = (per_fpu_pwr * pip_avg_fpu_pwr_impr + per_sfu_pwr * pip_avg_sfu_pwr_impr)/100
   
    engy_fpu_impr = (dw_fpu_energy - ihw_fpu_energy) / dw_fpu_energy * 100 
    engy_sfu_impr = (dw_sfu_energy - ihw_sfu_energy) / dw_sfu_energy * 100
    tot_eng_impr = (per_fpu_pwr * engy_fpu_impr + per_sfu_pwr * engy_sfu_impr)/100
    pip_eng_fpu_impr = (pip_dw_fpu_eng - pip_ihw_fpu_eng) / pip_dw_fpu_eng * 100 
    pip_eng_sfu_impr = (pip_dw_sfu_eng - pip_ihw_sfu_eng) / pip_dw_sfu_eng * 100
    pip_tot_eng_impr = (per_fpu_pwr * pip_eng_fpu_impr + per_sfu_pwr * pip_eng_sfu_impr)/100

    print("="*40)
    print("CBL model:")
    print("="*40)
    print("avg_fpu_pwr_ihw = %f" % avg_fpu_pwr_ihw)
    print("avg_sfu_pwr_ihw = %f" % avg_sfu_pwr_ihw)
    print("avg_fpu_pwr_dw = %f" % avg_fpu_pwr_dw)
    print("avg_sfu_pwr_dw = %f" % avg_sfu_pwr_dw)
    print("avg_fpu_pwr_impr = %f%%" % avg_fpu_pwr_impr)
    print("avg_sfu_pwr_impr = %f%%" % avg_sfu_pwr_impr)
    print("Holistic power savings = %f%%" % tot_pwr_impr)
    print("="*40)
    print("ihw_fpu_energy = %f" % ihw_fpu_energy);
    print("ihw_sfu_energy = %f" % ihw_sfu_energy);
    print("dw_fpu_energy = %f" % dw_fpu_energy);
    print("dw_sfu_energy = %f" % dw_sfu_energy);
    print("engy_fpu_impr = %f%%" % engy_fpu_impr);
    print("engy_sfu_impr = %f%%" % engy_sfu_impr);
    print("Holistic Energy savings = %f%%" % tot_eng_impr)
    print("="*40)
    print("PIPLINED model:")
    print("="*40)
    print("pip_avg_fpu_pwr_ihw = %f" % pip_avg_fpu_pwr_ihw)
    print("pip_avg_sfu_pwr_ihw = %f" % pip_avg_sfu_pwr_ihw)
    print("pip_avg_fpu_pwr_dw = %f" % pip_avg_fpu_pwr_dw)
    print("pip_avg_sfu_pwr_dw = %f" % pip_avg_sfu_pwr_dw)
    print("pip_avg_fpu_pwr_impr = %f%%" % pip_avg_fpu_pwr_impr)
    print("pip_avg_sfu_pwr_impr = %f%%" % pip_avg_sfu_pwr_impr)
    print("Holistic power savings = %f%%" % pip_tot_pwr_impr)
    print("="*40)
    print("pip_ihw_fpu_eng = %f" % pip_ihw_fpu_eng);
    print("pip_ihw_sfu_eng = %f" % pip_ihw_sfu_eng);
    print("pip_dw_fpu_eng = %f" % pip_dw_fpu_eng);
    print("pip_dw_sfu_eng = %f" % pip_dw_sfu_eng);
    print("pip_eng_fpu_impr = %f%%" % pip_eng_fpu_impr);
    print("pip_eng_sfu_impr = %f%%" % pip_eng_sfu_impr);
    print("Holistic Energy savings = %f%%" % pip_tot_eng_impr)
    print("="*40)


    
            
#    print(fpu_op_map)
#    print()
#    print(sfu_op_map)

   





        
