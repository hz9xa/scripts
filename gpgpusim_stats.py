#!/usr/bin/python
import os,sys


def process_file(f):
    stats = {"gpu_avg_power":[],"gpu_max_power":[], "gpu_min_power":[], "gpu_avg_SFUP":[],\
             "gpu_avg_FPUP":[],"gpu_avg_SP_ACC":[],"gpu_avg_SFU_ACC":[],"gpu_avg_FPU_ACC":[]}
    with open(f,'r') as inf:
        for line in inf.readlines():
            if 'gpu' in line:
                line = line.replace(',','');
                record = line.split()
                if record[0] in stats.keys():
                    stats[record[0]].append(float(record[-1]))

    avg_power = sum(stats["gpu_avg_power"])/float(len(stats["gpu_avg_power"]))
    avg_SFUP = sum(stats["gpu_avg_SFUP"])/float(len(stats["gpu_avg_SFUP"]))
    avg_FPUP = sum(stats["gpu_avg_FPUP"])/float(len(stats["gpu_avg_FPUP"]))
    max_power = max(stats["gpu_max_power"])
    tot_SP_ACC = sum(stats["gpu_avg_SP_ACC"])
    tot_SFU_ACC = sum(stats["gpu_avg_SFU_ACC"])
    tot_FPU_ACC = sum(stats["gpu_avg_FPU_ACC"])

    print("avg_power:\t%f" % avg_power)
    print("max_power:\t%f" % max_power)
    print("avg_SFUP:\t%f" % avg_SFUP)
    print("avg_FPUP:\t%f" % avg_FPUP)
    print("tot_SP_ACC:\t%d"% tot_SP_ACC)
    print("tot_SFU_ACC:\t%d"% tot_SFU_ACC)
    print("tot_FPU_ACC:\t%d"% tot_FPU_ACC)

    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please specify stats file: ");
        sys.exit(1);

    process_file(sys.argv[1])
    print("Done")
