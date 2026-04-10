"""
I want to create a file that inputs a dataframe and outputs a new 
dataframe with columns renamed
"""

# Import packages #
import pandas as pd
import csv

# Functions #
def rename_columns_with_df(
        column_name_df: pd.DataFrame, 
        data_df: pd.DataFrame, 
        common: str, 
        label: str
        )->pd.DataFrame:
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

    'common': string
        The common label between column_name_df and data_df. This
        is the label of the columns that need to be renamed in 
        data_df. In column_name_df, this should be in row format.
    
    'label': string
        The desired label for the columns needing renamed which is
        in column_name_df in row format. The columns with label
        common_1, common_2, ... common_n in column_name_df
        and data_df will be renamed to label_1, label_2, ...label_n
        with 1, 2, .., n being the associated common.

    Returns
    -------
    'return_df': Pandas DataFrame
        A deep copy of data_df with the desired columns renamed.
    """
    return_df = data_df.copy()
    
    point_num = []
    point_name = []
    for i in column_name_df.loc[:,common]:
        point_num.append(i)
    for j in column_name_df.loc[:,label]:
        point_name.append(j)

    rename_dict = {}
    for k in range(0,column_name_df.shape[0]):
        rename_dict[point_num[k]] = point_name[k]

    return_df.rename(columns=rename_dict)

    return return_df

def import_csvfile(path:str) -> pd.DataFrame:
    """
    A function that imports a csv file, verifies is correct format, 
    and returns that file as a Pandas DataFrame. Will return
    csv.Error if file is not a csv file.

    Parameters
    ----------
    'path': string
        A path to desired CSV file in the format of:
        '/d_1/d_2/ ... /d_n/filename.csv'.
    
    Returns
    -------
    'df_data': Pandas DataFrame
        The information from the inputted CSV file in DataFrame format.
    """
    try:
        with open(path, 'r', newline='') as f:
            sample = f.read(512)
            dialect = csv.Sniffer().sniff(sample)

        data = pd.read_csv(path, low_memory=False)
        df_data = pd.DataFrame(data)
        return df_data
    
    except csv.Error:
        return csv.Error

if __name__ == "__main__":
    rename_columns_with_df()
    import_csvfile()