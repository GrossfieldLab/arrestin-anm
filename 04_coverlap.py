#import
import os

files = []

structfile = open('./output/aa_number.csv', 'r')
for line in structfile:
    if line[0] == '>':
        files.append(line.split(',')[0][1:])
structfile.close()

for fname in files:
    print (fname)
    for gname in files:
    	os.system("/opt/LOOS/bin/coverlap  -e1 -E1 ./output/vsa/" + fname + "_s.asc ./output/vsa/" + fname + "_U.asc ./output/vsa/" + gname + "_s.asc ./output/vsa/" + gname + "_U.asc > ./output/coverlap/" + fname + "_" + gname + ".txt")

