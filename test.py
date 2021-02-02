import numpy as np
import pandas as pd

with open(r'D:\github\CrystalStructureGAN\48375') as f:
    print(len(open(r'D:\github\CrystalStructureGAN\48375').readlines()))
    line=[]
    for j in range(len(open(r'D:\github\CrystalStructureGAN\48375').readlines())):
        cur_line=f.readline()
        cur_line = cur_line.strip()
        cur_line = cur_line.split()
        if 7<j<14:
            line.append(cur_line)
line=np.array(line)
print(len(line))
line=line.reshape(1,18)
print(line)
line=pd.DataFrame(line)
print(line)
line.to_csv("line.csv")
print("all done")