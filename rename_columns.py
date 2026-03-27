import pandas as pd

#import data
temp_point_data = pd.read_csv(r"/home/engineering/Documents/PdM/data/temp_data/point_names.csv", low_memory=False)
temp_point_df = pd.DataFrame(temp_point_data)