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


def get_prep_OPS():
    
    df = pd.read_csv('opsd_germany_daily.csv')
    variables = ['Consumption','Wind', 'Solar', 'Wind+Solar']
    df[variables].plot()
    df.set_index('Date').sort_index()
    df.index = pd.to_datetime(df.index)
    df['month'] = df.index.month_name()
    df['year'] = df.index.year


    return df



