import pandas as pd
import numpy as np

data = pd.read_excel("G:/AdventsProduct/Others/A-Testing/Medical Insurance/Testing/data_check.xlsx")

# data_proper = data.replace(np.nan, '')
# data_male = data_proper[data_proper['Gender'] == 'M']
# data_female = data_proper[data_proper['Gender'] == 'F']
#
# frames = [data_male, data_female]
# result = pd.concat(frames).sort_index()
#
# # print(data_proper)
# print(data_male)
# print(data_female)
# print(result)

print(data)

data_dict_list = []
data_name_list = []

for index, rows in data.iterrows():
    data_dict = {"Name": rows['Name'], "Gender": rows['Gender']}
    data_dict_list.append(data_dict)
    data_name_list.append(rows['Name'])

print(data_dict_list)
print(data_name_list)
print(data_dict_list[data_name_list.index('John')])