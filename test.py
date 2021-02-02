import numpy as np
import pandas as pd

with open(r'D:\github\CrystalStructureGAN\48375') as f:
    print(len(open(r'D:\github\CrystalStructureGAN\48375').readlines()))
    line=[]
    for j in range(len(open(r'D:\github\CrystalStructureGAN\48375').readlines())):
        cur_line=f.readline()
        cur_line = cur_line.strip()
        cur_line = cur_line.split()
        #print(type(cur_line))
        #print(cur_line)
        if j==6:
            a=int(cur_line[0])
            b=int(cur_line[1])
            c=a+b
            print(c)
        if 7<j<14:
            line.append(cur_line)
    line=np.array(line)
    line=line.reshape(1,18)
# line=np.array(line)
# line=line.reshape(1,18)
# print(line)
line=pd.DataFrame(line)
# print(line)
line.to_csv("line.csv")
# print("all done")