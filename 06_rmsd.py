#imports of all kinds go here
import sys, math, os
import numpy as np
import matplotlib.pyplot as plt

sequencefile = open('./output/aa_number.csv', 'r')
rmsdfile = open('./output/rmsd.csv', 'w')
files = []
coord = []
inputpath = './input/structure_rmsd/'


for line in sequencefile:
    if line[0] == '>':
        files.append(line.split(',')[0][1:])
        rmsdfile.write(line.split(',')[0][1:] + ',')

rmsdfile.write('\n')

for filename in files:
    structurefile = open(inputpath + filename + '.pdb', 'r')
    count = 0
    c = []
    c.append(filename)
    for line in structurefile:
        if line[0:4]== "ATOM":
            c.append([float(line[30:38]),float(line[39:47]),float(line[48:55])])
    coord.append(c)

fnum = len(files)
cnum = len(coord[0])
rmsd = np.zeros((fnum,fnum))

i = 0
j = 0
k = 0

while i < fnum:
    j = 0
    dist = []
    rmsdfile.write(coord[i][0] + ',')
    while j < fnum:
        k = 1
        d = 0
        while k < cnum:
            d += math.pow(coord[i][k][0] - coord[j][k][0],2)
            d += math.pow(coord[i][k][1] - coord[j][k][1],2)
            d += math.pow(coord[i][k][2] - coord[j][k][2],2)
            k += 1
        d = d / (cnum - 1)
        d = math.sqrt(d)
        rmsdfile.write(str(d) + ',')
        rmsd[i,j] = d
        j += 1
    rmsdfile.write('\n')
    i += 1
hm = plt.imshow(rmsd, cmap='Greys_r', interpolation='nearest',vmin = 0.0, vmax = 3.5)
plt.colorbar(hm)
plt.savefig('./output/rmsd_heatmap.png')

