import pandas as pd
import numpy as np

dict1 = {'Employee Code':[11,12,13,14],
    'Client Id':[100, 90, 91, 95],
        'Gross Salary': [30000, 45000, 560000, 89000],
        'Name':['Sunder', 'Raji','Ali', 'Chitrarth']}
        
        
dict2 = {'Employee Code':[13,14,15,16,11],
    'Client Id':[ 91, 95, 98,97,89],
        'Gross Salary': [120,12000, 23000,3200,6000],
        'Name':['Ali', 'Chitrarth', 'Ram', 'Vikram','Sunder']}
        
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

right_join = pd.merge(df1, df2, left_on=['Employee Code','Client Id','Name'], right_on=['Employee Code','Client Id','Name'], how='right')
left_join = pd.merge(df1, df2, left_on=['Employee Code','Client Id','Name'], right_on=['Employee Code','Client Id','Name'], how='left')
inner_join = pd.merge(df1, df2, left_on='Employee Code', right_on='Employee Code', how='inner')
outer_join = pd.merge(df1, df2, left_on=['Employee Code','Client Id','Name'], right_on=['Employee Code','Client Id','Name'], how='outer')
#cross_join = df1.merge(df2, how='cross')


file_path = "D:/Test Pandas/Pandas_Merge.xlsx"

writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
right_join.to_excel(writer, sheet_name="right", index=False)
left_join.to_excel(writer, sheet_name="left", index=False)
outer_join.to_excel(writer, sheet_name="outer", index=False)
writer.save()

#right_join.to_excel("D:/Test Pandas/right_join.xlsx", index=False)
#left_join.to_excel("D:/Test Pandas/left_join.xlsx", index=False)
#inner_join.to_excel("D:/Test Pandas/inner_join.xlsx", index=False)
#outer_join.to_excel("D:/Test Pandas/outer_join.xlsx", index=False)


