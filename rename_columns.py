"""
I want to create a file that inputs a dataframe and outputs a new 
dataframe with columns renamed
"""

import pandas as pd

#import data
temp_point_data = pd.read_csv(r"/home/engineering/Documents/PdM/data/temp_data/point_names.csv", low_memory=False)
temp_point_df = pd.DataFrame(temp_point_data)

temp_data = pd.read_csv(r"/home/engineering/Documents/PdM/data/temp_data/temp_data_2026_01_19.csv", low_memory=False)
temp_df = pd.DataFrame(temp_data)

test_df = temp_df.copy()

point_num = []
point_name = []
for i in temp_point_df.loc[:,"Point_Name"]:
    point_num.append(i)
for j in temp_point_df.loc[:,"TechID"]:
    point_name.append(j)

rename_dict = {}
for k in range(0,38):
    rename_dict[point_num[k]] = point_name[k]

test_df.rename(columns=rename_dict)