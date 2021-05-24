"""
NAME:          Fake_db2dashboard.py
AUTHOR:        Manuel Dominguez
EMAIL:         manolo.biomero@gmail.com
DATE:          18/05/2021
INSTITUTION:   Salisbury Hospital
DESCRIPTION:   From fake database to dashboard
               
"""








import dash                              # pip install dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input

from dash_extensions import Lottie       # pip install dash-extensions
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import plotly.express as px              # pip install plotly
import pandas as pd                      # pip install pandas
from datetime import date
import calendar
from wordcloud import WordCloud          # pip install wordcloud
import sqlite3                           # pip install sqlite3
import plotly.graph_objects as go
import dash_table
from dash.dependencies import Input, Output, State

# LottieFiles - https://lottiefiles.com/
cases = "https://assets4.lottiefiles.com/datafiles/dNJ1QgOiCpNbFKD/data.json" 
vaccine = "https://assets8.lottiefiles.com/packages/lf20_d2iuvfbu.json"
death = "https://assets4.lottiefiles.com/packages/lf20_r44tksh6.json"
patients = "https://assets9.lottiefiles.com/packages/lf20_vPnn3K.json"
tested = "https://assets6.lottiefiles.com/packages/lf20_cepqhm3v.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))



# The database used

cnx = sqlite3.connect('./fake_db.db') 


# Import tables data from database 

patient_data = pd.read_sql_query("SELECT * FROM patient_data", cnx)
covid_19_admission = pd.read_sql_query("SELECT * FROM covid_19_admission", cnx)
covid_19_death = pd.read_sql_query("SELECT * FROM covid_19_death", cnx)
Hospital_features = pd.read_sql_query("SELECT * FROM Hospital_features", cnx)




# Bootstrap themes by Ann: https://hellodash.pythonanywhere.com/theme_explorer
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])

app.layout = dbc.Container([
    dbc.Row([                                                                  
        dbc.Col([
            dbc.Card([ 
                dbc.CardImg(src='/assets/wrgllogohighres.png')                   
            ],className='mb-2'),
                     dbc.Button("Author", id="Author"),
        dbc.Modal(
            [
                dbc.ModalHeader("Manuel Dominguez"),
                dbc.ModalBody("A clinical bioinformatician who is learning how to create informative and beautiful dashboards"),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close", className="ml-auto")
                ),
            ],
            id="modal",
        ),
        ], width=2),
       dbc.Col([
            dbc.Card([ 
                dbc.CardBody([
                    html.H1('Fake COVID-19 data dashboard'),
                    html.H3('A learning project to connect a database with a interactive dashboard'),
                    dcc.Checklist(
                           id= "my_checklist",
                           options=[   
                               {'label': ' Hospital 1     ', 'value': '224323'},
                               {'label': ' Hospital 2     ', 'value': '3234234'},
                               {'label': ' Hospital 3     ', 'value': '214321'}
                               ],
                               value=['224323','3234234','214321']
                               )  


                ], style={'textLeft':'center'})
                      ], 
                       style={'height':'18vh'}),
                       
                ], 
                width=8),
    ],className='mb-2 mt-2'),
    dbc.Row([                                                                                                                      
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H3('Cases'),style={'textAlign':'center'}),
                    dbc.CardBody([
                    html.H2(id='Cases', children="000"),
                ], style={'textAlign':'center'})  
            ], style={'margin-right': '40px', 'margin-left': '30px'}
            #       color="info"
             ),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H3('Deads'),style={'textAlign':'center'}),
                    dbc.CardBody([
                    html.H2(id='Deads', children="000"),
                ], style={'textAlign':'center'})
            ], style={'margin-right': '40px', 'margin-left': '0px'}
            #color="info"
            ),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H3('Average days hospitalised'),style={'textAlign':'center'}),
                    dbc.CardBody([
                    html.H2(id='Average-hospitalised', children="000"),
                ], style={'textAlign':'center'})
            ],
            #        color="info"
            ),
        ], width=3 ),

    ],className='mb-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=4),
    ],className='mb-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=4),
    ],className='mb-2'),
], fluid=True)



# The callback for the 3 cards 
@app.callback(
    Output(component_id = 'Cases',component_property = 'children'),
    #Output('Deads','children'),
    #Output('Average-hospitalised','children'),
    [Input(component_id='my_checklist', component_property='value')]
)
def update_small_cards(options_chosen):
    
    dff = covid_19_admission[covid_19_admission['Hospital_ID'].isin(options_chosen)]
    print(covid_19_admission)
    print(dff)
    print(options_chosen)
    TOTAL_PA = len(dff)

    return TOTAL_PA


if __name__=='__main__':
    app.run_server(debug=True, port=8001)