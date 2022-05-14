#import
import sys, os

files = []


structfile = open('./output/aa_number.csv', 'r')
for line in structfile:
    if line[0] == '>':
        files.append(line.split(',')[0][1:])
structfile.close()



for fname in files:
	print (fname)
	os.system("/opt/LOOS/bin/vsa --nomass 1 ./input/structure_anm/"+fname+".pdb 'id >= 1 && id <=8000 && name == "+'"CA"'+"' 'id >= 9000 && name == "+'"CA"'+"' ./output/vsa/"+fname)

