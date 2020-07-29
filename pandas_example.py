#pandas

import os
from pathlib import path
import csv
import pandas as pd


save_path = r "c:\Users\varun\Desktop\STV_NG\"

text_file = os.path.join(save_path,'first_raw_file'+'.txt')
csv_file  = os.path.join(save_path,'first_raw'+'.csv')

txtfile = open(text_file)
conv = csv.reader(txtfile,delimiter = ' ')

csvfile = open(csv_file,'w')
out_csv = csv.writerows(conv)


txtfile.close()
csvfile.close()







'''
#df = pd.read_csv('c:\\Users\\varun\\Desktop\\sample.csv',header=None,
 #                names=['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen'])

#print(df)

data = pd.read_csv('c:\\Users\\varun\\Desktop\\sample.csv', delimiter=',')
print(data.columns)

f=data.to_csv("c:\\Users\\varun\\Desktop\\new.csv",columns=['pass/fail','EDIt','fam/L','count','pass/fail_bld-cd','buildcode','bld-cd_fam/L','bld_cd_count'])
print(f)



#data.to_csv('c:\\Users\\varun\\Desktop\\valid_data.csv',columns=['pass/fail','EDIt','modl','fam/L','count' '''
