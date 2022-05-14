import os, sys
import numpy as np
import matplotlib.pyplot as plt


anmpath = "./output/vsa/" #Path to elastic network model files
output = "./output/bfactor/dot_product_" + sys.argv[1] + ".csv"

inputpath = './input/structure/'
outputpath = './output/bfactor/' + sys.argv[1] + '/'

if not os.path.isdir(outputpath):
     os.mkdir(outputpath)

max_mode = 6

#Copy and paste the desired array into clusters 1 and cluster 2
#apo = ['1g4r','2wtr','3p2d','3p2d_b','6kl7','2wtr_b','1g4m','1g4m_b','1jsy']
#active = ['7df9','7dfa','7dfb','7dfc','4jqi','6ni2','6up7','6u1n','6tko','6pwc']
#clathrin = ['3gd1']
cluster_1 = ['7df9','7dfa','7dfb','7dfc','4jqi','6ni2','6up7','6u1n','6tko','6pwc']
cluster_2 = ['3gd1']


def loader(fname):#Loads the relavant files
    global anmpath
    U = np.loadtxt(anmpath + fname + "_U.asc", dtype='float')
    s = np.loadtxt(anmpath + fname + "_s.asc", dtype='float')
    i = 0
    for i in range(len(s)):
        if i < 6:
            s[i] = 0
        else:
            s[i] = 1 / s[i]
    return s, U.T

def fileripper():#Rips the file names from the meta data and creates a file list
    sequencefile = open('./output/aa_number.csv', 'r')
    files = []

    for line in sequencefile:
        if line[0] == '>':
            files.append(line.split(',')[0][1:])
    return files

def mode_dot(mode):
    s, U = loader(files[0])
    l = int(len(U[0]) / 3)
    seq = np.zeros((2,l))
    n = [0,0]
    for f in files:
        s1, U1 = loader(f)
        for g in files:
            s2, U2 = loader(g)
            tmp = U1[mode] * U2[mode]
            if f in cluster_1 and g in cluster_1:
                for i in range(l):
                    seq[0][i] += np.abs(tmp[3*i] + tmp[3*i + 1] + tmp[3*i + 2])
                n[0] += 1
            elif f in cluster_2 and g in cluster_1:
                for i in range(l):
                    seq[1][i] += np.abs(tmp[3*i] + tmp[3*i + 1] + tmp[3*i + 2])
                n[1] += 1
    seq[0] = seq[0] / n[0]
    seq[1] = seq[1] / n[1]
    per_resi = np.abs(seq[0] - seq[1])
    return per_resi

files = fileripper()
vector = mode_dot(max_mode)
np.savetxt(output,vector, delimiter = ',')

vector = 100 * vector / np.amax(vector)
vector = np.around(vector, decimals=2)

files = []
sequencefile = open('./output/aa_number.csv', 'r')
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
sequencefile.close()

for filename in files:
    structurefile = open(inputpath + filename[0] + '.pdb', 'r')
    outfile = open(outputpath + filename[0] + '.pdb', 'w')
    outfile.write('REMARK ' + filename[0] + '\n')
    i = 0
    for line in structurefile:
        if line[0:4]== "ATOM" and line[13:15]=="CA" and line[21]=="A" and int(line[23:26]) in filename:
            if float(vector[i]) > 99.99:
                 outfile.write(line[0:60] + ' ' + str(vector[i]) + ' ' + line[67:])
            else:
                 outfile.write(line[0:60] + '  ' + str(vector[i]) + ' ' + line[67:])
            i += 1
        elif line[0:4]== "ATOM":
            outfile.write(line[0:60] + '  0.00' + ' ' + line[67:])
    outfile.close()
    structurefile.close()
