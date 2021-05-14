import pandas as pd
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State




# Data source https://finance.yahoo.com  -Data owner: Stefano Leone on Kaggle
df = pd.read_csv('./vaccinated by regions.csv')  

colors = ["black", "blue", "red", "yellow", "pink", "orange"]

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        dcc.Dropdown(id='my-dropdown', multi=True,
                     options=[{'label': x, 'value': x} for x in sorted(df.areaName.unique())],
                     value=["Fidelity 500 Index Fund", "Fidelity Advisor Freedom 2035 Fund Class A",
                            "Fidelity Freedom 2035 Fund"]),
        html.Button(id='my-button', n_clicks=0, children="Show breakdown"),
        dcc.Graph(id='graph-output', figure={}),

        html.Div(id="sentence-output", children=["This is the color I love"], style={}),
        dcc.RadioItems(id='my-radioitem', value="black", options=[{'label': c, 'value': c} for c in colors]),
    ]
)






if __name__ == '__main__':
    app.run_server(debug=True)

    
# https://youtu.be/mTsZL-VmRVE
