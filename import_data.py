import pandas as pd

#import data
data = pd.read_csv(r"/home/engineering/Documents/PdM/data/temp_data/temp_data_2026_01_19.csv", low_memory=False)
df = pd.DataFrame(data)
print(df.tail)