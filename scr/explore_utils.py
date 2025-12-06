#Import libraries
import logging
import pandas as pd

logger = logging.getLogger(__name__)

# Funtions
def null_analysis(df):
    '''
    Generates a summary dataframe with basic info od the dataframe: count not null and null values in columns, perfect of null values and types.

    Args:
    - df: dataframe

    Returns
    - Summary dataframe
    '''
    column_info = []
    total_rows = len(df)
    
    for col in df.columns:
        non_null_count = int(df[col].notnull().sum())
        null_count = total_rows - non_null_count
        null_percent = round( null_count / total_rows * 100, 2)
        dtype = df[col].dtype

        column_info.append(
            {
                "COLUMN_NAME" : col,
                "NON_NULL_COUNT" : non_null_count,
                "NULL_COUNT" : null_count,
                "NULL_PERCENT" : null_percent,
                "DTYPE" : dtype
            }
        )
    
    info_df = pd.DataFrame(column_info)

    return info_df

def column_type_dataframe(df, col_type):
    """
    Returns a filtered dataframe that only shows the columns of a defined type (object, float, int, date...) and a list with the columns of that data type.

    Args:
        df (datafrane): Original dataframe
        col_type (string): The desired data type of the columns

    Returns:
        _type_: A filtered dataframe and the columns of that type (for making changes in original df)
    """
    df_info = info_dataframe(df)
    df_filtered = df_info[df_info["DTYPE"] == col_type]
    type_cols = [x for x in df_filtered["COLUMN_NAME"]]
    df_type = df[type_cols]
    return df_type, type_cols