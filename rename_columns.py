"""
I want to create a file that inputs a dataframe and outputs a new 
dataframe with columns renamed
"""

# Import packages #
import pandas as pd

# Functions #
def rename_columns_with_df(column_name_df: pd.DataFrame, data_df: pd.DataFrame, common: str, label: str):
    """
    A function that renames multiple columns of a dataframe using 
    another dataframe as input. This is helpful when there are too 
    many columns to relabel manually and the column labels and the
    desired name are already in a dataframe. It returns a copy of
    the original dataframe with the newly renamed columns.

    Parameters
    ----------
    'column_name_df': Pandas DataFrame
        Contains the common label and desired label for columns
        needing renamed.

    'data_df': Pandas DataFrame
        The dataframe which contains columns needing renamed.      

    'column_name_df_common' : string
        The common label between 


    """
    column_name_df
    
    
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

def import_files(path):
    data = pd.read_csv(path, low_memory=False)
    return pd.DataFrame(data)

if __name__ == "__main__":
    rename_columns_with_df()
    import_files()