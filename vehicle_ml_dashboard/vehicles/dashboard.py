import plotly.express as px
import plotly.offline as opy
import plotly.graph_objects as go

import pandas as pd


def frequency_table(df):
    """Generate a one-way frequency table for manufacturers."""
    manufacturer_counts = df['manufacturer'].value_counts().reset_index()
    manufacturer_counts.columns = ['Manufacturer', 'Count']

   
    table_html = manufacturer_counts.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='%.2f',
        justify='center'
    )
    return table_html

def profit_calculation(df):
    df["profit"]=df["selling_price"]-df["wholesale_price"]
    df.groupby(["manufacturer","transmission","fuel_type"]).agg({
        "profit":"sum",
        "selling_price":["sum","count"],
        "wholesale_price":"sum"
    })

def profit_table(df):
    """Generate a summary of profit by manufacturer."""
    profit_calculation(df)
    profit_summary = (
        df[['manufacturer', 'profit']]
        .groupby('manufacturer', as_index=False)
        .agg(Total_Profit=('profit', 'sum'),
             Average_Profit=('profit', 'mean'),
             Count=('profit', 'size'))
    )
    table_html = profit_summary.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='%.2f',
        index=False,
        justify='center'
    )
    return table_html

def crosstab(df): 
    return pd.crosstab([df['manufacturer'], df['body_type']],[df["engine_type"], df["transmission"]], margins=True)






