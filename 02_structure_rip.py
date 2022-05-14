#imports of all kinds go here
import sys, math, os

inputpath = './input/structure/'
outputpath = './input/structure_anm/'
rmsdpath = './input/structure_rmsd/'

sequencefile = open('./output/aa_number.csv', 'r')
files = []

for line in sequencefile:
    if line[0] == '>':
        name = line.split(',')
        name[0] = name[0][1:]
        count = len(name)
        i = 1
        while i < count:
            name[i] = int(name[i])
            i += 1
        files.append(name)

for filename in files:
    structurefile = open(inputpath + filename[0] + '.pdb', 'r')
    outfile = open(outputpath + filename[0] + '.pdb', 'w')
    rmsdfile = open(rmsdpath + filename[0] + '.pdb', 'w')
    outfile.write('REMARK ' + filename[0] + '\n')
    rmsdfile.write('REMARK ' + filename[0] + '\n')
    for line in structurefile:
        if line[0:4]== "ATOM" and line[13:15]=="CA" and line[21]=="A" and int(line[23:26]) in filename:
             outfile.write(line)
             rmsdfile.write(line)
        elif line[0:4]== "ATOM" and line[13:15]=="CA":
            outfile.write(line[0:5] + ' 10000 ' + line[12:])
    outfile.close()
    rmsdfile.close()
structurefile.close()
