import os
import pandas as pd
import xlrd

# con = pymysql.connect(host = "192.168.3.18", 
#            user = "root", password = '123456', 
#            db = "oqmd", charset='utf8')
# sql = "select * from structures;"
# df_raw = pd.read_sql(sql, con)
# con.close()

# entry_id=df_raw.loc[:,'entry_id']
# id=df_raw.loc[:,'id']
# print(entry_id.shape)
# print(id.shape)

data = pd.read_excel(r'D:\Download\EXPORT\structures.xlsx')
data = data.values

id = data.loc[:, 'id']
entry_id = data.loc[:,'entry_id']

for i in range(1, len(id)):
    id_int = int(id[i])    
    output_file_name = id_int
    present_dir = os.path.abspath(os.curdir)
    file_name = os.path.join(present_dir, str(entry_id[i]), output_file_name)
    file_path = os.path.join(present_dir, str(entry_id[i]))
    with open(file_name,'r') as f:

#Representation矩阵应为三个晶格矢量，然后是fractional coordination
#根据第一行判断一元/二元/三元化合物
#忽略第二行
#第三行到第五行，存储3*3的矩阵作为Representation矩阵
#第六行开始，都存
