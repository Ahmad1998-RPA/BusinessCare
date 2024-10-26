# Importing libraries
import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# reading input data

df = pd.read_excel("inputdata/inputdata.xlsx")
df.drop_duplicates(inplace=True) # droping duplicates

# Adding columns name into list of string
colums_list = df.columns

# Convert 'EDate' to datetime, invalid parsing will be set as NaT
df['EDate_parsed'] = pd.to_datetime(df['EDate'], errors='coerce')

# Find rows where 'EDate' contains integer values (non-dates)
invalid_rows = df[df['EDate'].apply(lambda x: isinstance(x, int))]

# Count how many rows have integer values in 'EDate'
num_invalid_rows = len(invalid_rows)
# print(f"Number of rows with integer values in 'EDate': {num_invalid_rows}")

# Remove rows with integer values in 'EDate'
df_cleaned = df[~df['EDate'].apply(lambda x: isinstance(x, int))]

# Drop the helper 'EDate_parsed' column (optional)
df_cleaned.drop(columns=['EDate_parsed'], inplace=True)

# funtion to replace NaN values with the previous record value (forward fill) or backward fill
def fill_null(df, colums_list):
    for col_name in colums_list:
        df_cleaned[col_name].fillna(method='ffill', inplace=True)
        df_cleaned[col_name].fillna(method='bfill', inplace=True)
    return df_cleaned

fill_null(df_cleaned, colums_list)

# Ensure 'EDate' is in datetime format
df_cleaned.loc[:, 'EDate'] = pd.to_datetime(df_cleaned['EDate'], errors='coerce').dt.date

# Extract month as abbreviated names (Jan, Feb, etc.)
df_cleaned.loc[:, 'EMonth'] = pd.to_datetime(df_cleaned['EDate'], errors='coerce').dt.strftime('%b')

# Extract the year
df_cleaned.loc[:, 'EYear'] = pd.to_datetime(df_cleaned['EDate'], errors='coerce').dt.year
# Drop rows where 'EDate' is null or NaN
df_cleaned = df_cleaned.dropna(subset=['EDate'])

# Optional: Reset the index after dropping the rows
df_cleaned.reset_index(drop=True, inplace=True)
drop_columns = ['EVALUATION_ID', 'RECORD_ID', 'Contact_Number', 'Comments','Remarks','Cust_Ac Number', 'Referance_No']
df_cleaned = df_cleaned.drop(columns=drop_columns)

df_cleaned.to_excel('scripts/preprocessed_data.xlsx', index=False)