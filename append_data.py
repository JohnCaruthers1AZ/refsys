import pandas as pd

#import data
point_data = pd.read_csv(r"/home/engineering/Documents/PdM/data/temp_data/point_names.csv", low_memory=False)
df = pd.DataFrame(point_data)