import pymysql
import pandas as pd
import xlrd
import os
import numpy as np

present_dir = os.path.abspath(os.curdir)
xlsx_file_path = os.path.join(present_dir, 'structures.xlsx')
POSCAR_dir_path = '/home/liusb/POSCAR/'

#data_raw = pd.read_excel(xlsx_file_path)
con = pymysql.connect(host = "localhost", 
           user = "root", password = '123456', 
           db = "qmdb", charset='utf8')
sql = "select * from structures;"
df_raw = pd.read_sql(sql, con)
con.close()

data_raw=df_raw.iloc[0:110000,:]
data = data_raw[data_raw.natoms==6]

id = data.loc[:, 'id']
entry_id = data.loc[:,'entry_id']
print(entry_id.shape)
print(id.shape)

def get_cell_num(file_path):
    with open(file_path,'r') as f:
        total = 0
        for k in range(len(open(file_path,'r').readlines())):
            cur_line_c=f.readline()
            cur_line_c = cur_line_c.strip()
            cur_line_c = cur_line_c.split()
            if k==6:
                cur_line_c = [int(x) for x in cur_line_c]
                for ele in range(0, len(cur_line_c)): 
                    total = total + cur_line_c[ele] 
    return total


output=[]
for i in range(1, len(id)):
    print(i)
    print('We are processing id=',id[i],'entry_id=',entry_id[i])
    id_i=id[i]
    file_name=str(id_i)
    file_dir_path=os.path.join(POSCAR_dir_path, str(entry_id[i]))
    file_path=os.path.join(POSCAR_dir_path, str(entry_id[i]), file_name)
    with open(file_path,'r') as f:
        line=[]
        if get_cell_num(file_path)==6:
            for j in range(len(open(file_path,'r').readlines())):
                cur_line=f.readline()
                cur_line = cur_line.strip()
                cur_line = cur_line.split()
                if 7<j<14:
                    line.append(cur_line)
            line=np.array(line)
            line=line.reshape(18)
            output.append(line)

output=pd.DataFrame(output)
output.to_csv("output.csv")
print('all done')