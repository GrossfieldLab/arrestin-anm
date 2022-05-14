import numpy as np
import matplotlib.pyplot as plt
import sys

mode_limit = int(sys.argv[1])
mode_offset = 6
anmpath = "./output/vsa/"
output = "./output/modes/"



def loader(fname):#Loads the relavant files
    global anmpath
    U = np.loadtxt(anmpath + fname + "_U.asc", dtype='float')
    s = np.loadtxt(anmpath + fname + "_s.asc", dtype='float')
    i = 0
    N = len(s)
    for i in range(N):
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

def saver(name,cnt):
    np.savetxt(output + name + '.csv',cnt,delimiter=',')
    hm = plt.imshow(cnt, cmap='Greys', interpolation='nearest',vmin = 0.5,vmax = 1.0)
    plt.colorbar(hm)
    plt.savefig(output + name + '.png')
    plt.clf()

def number_saver(fname,data):
    with open(output + str(fname) + '_modes.csv', 'w') as f:
        np.savetxt(f,data.T, delimiter = ',')
    f.close()

def mode_compare(fname1,fname2):
    s1, U1 = loader(fname1)
    s2, U2 = loader(fname2)
    dot = np.zeros(mode_limit)
    for i in range(mode_limit):
        dot[i] = np.abs(np.dot(U1[i + mode_offset],U2[i + mode_offset]))
    return dot

def compiler():
    N = len(files)
    modes = np.zeros((mode_limit,N,N))
    for i in range(N):
        for j in range(N):
            tmp = mode_compare(files[i],files[j])
            for k in range(mode_limit):
                modes[k][i][j] = tmp[k]
        s, U = loader(files[i])
        m_list = np.zeros((mode_limit,len(U[0])))
        for k in range(mode_limit):
            m_list[k] = U[k + mode_offset]
        number_saver(files[i],m_list)
    for k in range(mode_limit):
        saver('Mode_' + str(k),modes[k])


files = fileripper()
compiler()

