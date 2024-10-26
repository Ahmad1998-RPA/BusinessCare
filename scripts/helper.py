import pandas as pd

df = pd.read_excel('scripts/preprocessed_data.xlsx')

def month_year_list(df):
    year = df['EYear'].unique().tolist()
    year.sort()
    year.insert(0, 'Overall')

    month = df['EMonth'].unique().tolist()
    month.sort()
    month.insert(0, 'Overall')

    return month, year