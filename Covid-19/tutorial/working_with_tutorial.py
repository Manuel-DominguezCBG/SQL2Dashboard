import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px


# Initialise the app
app = dash.Dash(__name__)


df = pd.read_csv('/home/manuel/Desktop/Manuel_project/SQL project/SQL2Dashboard/Covid-19/tutorial/stockdata2.csv'
                 , index_col=0, parse_dates=True)
df.index = pd.to_datetime(df['Date'])

# Define the app
app.layout = html.Div()

app.layout = html.Div(children=[
                      html.Div(className='row',  # Define the row element
                               children=[
                                  html.Div(className='four columns div-user-controls'),  # Define the left element
                                  html.Div(className='eight columns div-for-charts bg-grey')  # Define the right element
                                  ])
                                ])


children = [
    html.H2('Dash - STOCK PRICES'),
    html.P('''Visualising time series with Plotly - Dash'''),
    html.P('''Pick one or more stocks from the dropdown below.''')
]


dcc.Graph(id='timeseries',
          config={'displayModeBar': False},
          animate=True,
          figure=px.line(df,
                         x='Date',
                         y='value',
                         color='stock',
                         template='plotly_dark').update_layout(
                                   {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                    'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
                                    )



# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
