import dash
from dash import dcc, html
import dask.dataframe as dd
import pandas as pd
import plotly.express as px

# Create a Dash web application
app = dash.Dash(__name__)

# Read the TSV file into a Dask DataFrame
df = dd.read_csv('C:/Nida/DADS5001/DADS5001_AfterMidterm_Class5_2024-04-20/pcb_dataset_final.tsv', sep='\t')

# Resample data to plot line chart
df_resampled = df.groupby('campaign').sum().compute()

# Define the layout of the web application
app.layout = html.Div(children=[
    html.H1("Cost vs. Campaign"),
    dcc.Graph(
        id='line-chart',
        figure=px.line(df_resampled, x=df_resampled.index, y='cost', title='Cost vs. Campaign')
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
