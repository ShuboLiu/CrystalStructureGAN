import pymysql
import pandas as pd
import xlrd
import os
import numpy as np

present_dir = os.path.abspath(os.curdir)
xlsx_file_path = os.path.join(present_dir, 'structures.xlsx')
POSCAR_dir_path = '/home/liusb/POSCAR/'

data_raw = pd.read_excel(xlsx_file_path)
data_raw = data_raw.values
data = data_raw[data_raw.n_atom==6]

id = data.loc[:, 'id']
entry_id = data.loc[:,'entry_id']

data=[]
for i in range(len(id)):
    file_name=str(id[i])
    file_dir_path=os.path.join(POSCAR_dir_path, str(entry_id[i]))
    file_path=os.path.join(POSCAR_dir_path, str(entry_id[i]), file_name)
    with open(file_path,'r') as f:
        line=[]
        for j in range(len(open(file_path,'r').readlines())):
            cur_line=f.readline()
            cur_line = cur_line.strip()
            cur_line = cur_line.split()
            if 8<j<14:
                line.append(cur_line)
    line=np.array(line)
    data=data.append(line.reshape(1,3*len(line)))

data=pd.DataFrame(data)
data.to_csv("data.csv")