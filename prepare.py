import os
import pandas as pd
import seaborn as sns



def get_prep_store():

    df = pd.read_csv('store.csv')
    df.sale_date = pd.to_datetime(df.sale_date)
    sns.displot(df["item_price"])
    sns.displot(df["sale_amount"])    
    df = df.set_index('sale_date')
    df['month'] = df.index.month
    df['day_of_week'] = df.index.day_name()
    df['sales_total'] = df['sale_amount'] * df['item_price']

    return df



