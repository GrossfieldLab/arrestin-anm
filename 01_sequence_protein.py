#imports of all kinds go here
import sys, math, os


inputpath = './input/structure/'
outpath = './output/'

files = []

for filename in os.listdir(inputpath):
	files.append(filename.split(".")[0])

print (files)

sequencefile = open(outpath + 'sequence.csv', 'w')
numberfile = open(outpath + 'sequence_number.csv', 'w')

for filename in files:
    sequencefile.write('>' + filename + '\n')
    numberfile.write('>' + filename + '\n')
    structurefile = open(inputpath + filename + '.pdb', 'r')
    for line in structurefile:
        if line[0:4]== "ATOM" and line[13:15]=="CA" and line[21]=="A":
            numberfile.write(str(int(line[23:26])) + ',')
            if line[17:20] == "ARG":
                sequencefile.write('R,')
            elif line[17:20] == "HIS":
                sequencefile.write('H,')
            elif line[17:20] == "LYS":
                sequencefile.write('K,')
            elif line[17:20] == "ASP":
                sequencefile.write('D,')
            elif line[17:20] == "GLU":
                sequencefile.write('E,')
            elif line[17:20] == "SER":
                sequencefile.write('S,')
            elif line[17:20] == "THR":
                sequencefile.write('T,')
            elif line[17:20] == "ASN":
                sequencefile.write('N,')
            elif line[17:20] == "GLN":
                sequencefile.write('Q,')
            elif line[17:20] == "CYS":
                sequencefile.write('C,')
            elif line[17:20] == "GLY":
                sequencefile.write('G,')
            elif line[17:20] == "PRO":
                sequencefile.write('P,')
            elif line[17:20] == "ALA":
                sequencefile.write('A,')
            elif line[17:20] == "ILE":
                sequencefile.write('I,')
            elif line[17:20] == "LEU":
                sequencefile.write('L,')
            elif line[17:20] == "MET":
                sequencefile.write('M,')
            elif line[17:20] == "PHE":
                sequencefile.write('F,')
            elif line[17:20] == "TRP":
                sequencefile.write('W,')
            elif line[17:20] == "TYR":
                sequencefile.write('Y,')
            elif line[17:20] == "VAL":
                sequencefile.write('V,')
    sequencefile.write('\n')
    numberfile.write('\n')


