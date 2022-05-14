#import
import os
import numpy as np
import matplotlib.pyplot as plt


files = []

inputpath = './output/coverlap/'

comfile = open('./output/coverlap.csv', 'w')

structfile = open('./output/aa_number.csv', 'r')
for line in structfile:
    if line[0] == '>':
        files.append(line.split(',')[0][1:])
        comfile.write(line.split(',')[0][1:] + ',')
structfile.close()

comfile.write('\n')

cov = np.zeros((len(files),len(files)))
i = 0
j = 0

for fname in files:
    print (fname)
    j = 0
    comfile.write(fname + ',')
    for gname in files:
        covfile = open(inputpath + fname + '_' + gname + '.txt', 'r')
        for line in covfile:
            if line[11:18] == 'overlap':
                comfile.write(str(1 - float(line[19:])) + ',')
                cov[i][j] = 1 - float(line[19:])
        j += 1        
    comfile.write('\n')
    i += 1
hm = plt.imshow(cov, cmap='Greys_r', interpolation='nearest',label="covariance complement",vmin = 0.0, vmax = 0.15)
plt.colorbar(hm)
plt.savefig('./output/cov_heatmap.png')

