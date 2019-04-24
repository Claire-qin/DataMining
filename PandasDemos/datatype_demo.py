import pandas as pd
import numpy as np
from pprint import pprint

# df = pd.read_csv('srcdata/sales_data_types.csv')
# print(df.info())
# print(df['Customer Name'].str.get_dummies())




from datetime import datetime
a = datetime.strptime("2018-10-20 12:10:11", '%Y-%m-%d %H:%M:%S')
print(a)

df = pd.DataFrame({"k1":["two"*2 + "one"+2 + "three"*2], "k2":[1,2,3,4,5,6]})
df.duplicated()
df.drop_duplicates()

df11 = pd.DataFrame([[0,'a'], [1,'a'], [2,'b'], [3, 'b']], columns=['data1', 'key'])
df12 = pd.DataFrame([[0,'b'], [1,'b'], [2,'c'], [3, 'c']], columns=['data2', 'key'])
pd.merge(df11,df12)
