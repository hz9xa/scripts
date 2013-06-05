###This script is used for input vector statistics 
### in JPEG decompression study

import sys,os

if(len(sys.argv) != 2):
    print("specify file name only")
    exit(-1);

ifile = open(sys.argv[1],'r')

both_are_zero = 0;
both_are_not_zero = 0;
at_least_one_zero = 0;
only_a_is_zero = 0;
only_b_is_zero = 0;

lines = ifile.readlines();
numbers = []
for line in lines:
    line = line.strip();
    addends = line.split(" ")
    
    for x in addends:
        numbers.append(int(x))

    if(addends[0] == '0' or addends[1] == '0'):
        at_least_one_zero+=1;
    else:
        both_are_not_zero += 1;

    if (addends[0] == '0' and addends[1] == '0'):
        both_are_zero += 1;
        continue;
    elif(addends[0] == '0' and addends[1] != '0'):
        only_a_is_zero+=1;
        continue;
    elif(addends[0] != '0' and addends[1] == '0'):
        only_b_is_zero += 1;
        continue;
numbers.sort()
print(numbers[0]," ",numbers[-1])
of = open("stat_"+sys.argv[1].strip(".txt") + ".txt","w")

of.write('Both a and b are zero: %d (%f%%) \n'% (both_are_zero,(both_are_zero/len(lines)) * 100 ))
of.write('Neither a or b is zero: %d (%f%%) \n' % (both_are_not_zero,(both_are_not_zero/len(lines)) * 100))
of.write("At least one zero: %d (%f%%)\n" % (at_least_one_zero,(at_least_one_zero/len(lines)) * 100))
of.write("A = 0, B != 0: %d (%f%%)\n" % (only_a_is_zero,(only_a_is_zero/len(lines)) * 100))
of.write("A != 0, B = 0: %d (%f%%)\n" % (only_b_is_zero,(only_b_is_zero/len(lines))* 100 ))
of.write("Total # of operations %d\n" % len(lines))

ifile.close();
of.close()

