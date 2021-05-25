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
import plotly as py
from plotly.tools import FigureFactory as FF
import pandas as pd                      # pip install pandas
from datetime import date
import calendar
import datetime
from datetime import timedelta
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



# Age distribution Cases vs. deads plot

# First let's create two new tables that combine cases with patient_data and another table combinning dead with patient_data

date2admission = pd.read_sql_query("SELECT iD, Date, Birthdate,Hospital_ID,Discharge_date FROM patient_data INNER JOIN covid_19_admission ON covid_19_admission.Patient_admitted_id = patient_data.ID ;", cnx)
date2dead = pd.read_sql_query("SELECT iD, Birthdate,Hospital_ID FROM patient_data INNER JOIN covid_19_death ON covid_19_death.Patient_admitted_id = patient_data.ID ;", cnx)


def from_dob_to_age(born):
    '''
    To convert DOB to age
    '''
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))



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
                width=10),
    ],className='mb-2 mt-2'),
    dbc.Row([                                                                                                                      
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(html.H3('Total Cases'),style={'textAlign':'center'}),
                    dbc.CardBody([
                    html.H2(id='total_cases', children="000"),
                ], style={'textAlign':'center'})  
            ], style={'margin-right': '60px', 'margin-left': '60px'}),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H3('Total deads'),style={'textAlign':'center'}),
                    dbc.CardBody([
                    html.H2(id='total_deads', children="000"),
                ], style={'textAlign':'center'})
            ], style={'margin-right': '60px', 'margin-left': '60px'}),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H3('Average days hospitalised'),style={'textAlign':'center'}),
                    dbc.CardBody([
                    html.H2(id='average_days_hosp', children="000"),
                ], style={'textAlign':'center'})
            ],),
        ], width=3),
          dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H3('Current cases'),style={'textAlign':'center'}),
                    dbc.CardBody([
                    html.H2(id='Current_cases', children="000"),
                ], style={'textAlign':'center'})
            ], style={'margin-right': '60px', 'margin-left': '60px'}),
        ], width=3)
    ],className='mb-2',),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([dcc.Graph(id='the_graph1',
                config={'displayModeBar': False},animate=True)
                ]),
            ]),
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([dcc.Graph(id='the_graph_age_vs_days_hospitalised', 
                config={'displayModeBar': False},animate=True)
                ]),
            ]),
        ], width=6),
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
    Output(component_id = 'total_cases',component_property = 'children'),
    Output('total_deads','children'),
    Output('average_days_hosp','children'),
    Output('Current_cases','children'),
    [Input(component_id='my_checklist', component_property='value')]
)
def update_small_cards(options_chosen):
    # For total cases
    covid_19_admission_df = covid_19_admission[covid_19_admission['Hospital_ID'].isin(options_chosen)]
    total_cases = len(covid_19_admission_df)

    # For total number of deads
    total_deads_df = covid_19_death[covid_19_death['Hospital_ID'].isin(options_chosen)]
    total_deads = len(total_deads_df)

    # For getting average days hospitalised
     
    covid_19_admission['days_Hospitalised'] = (pd.to_datetime(covid_19_admission['Discharge_date']) - (pd.to_datetime(covid_19_admission['Date']))).dt.days
    test = covid_19_admission[covid_19_admission['Hospital_ID'].isin(options_chosen)]
    average_days_hosp = round(test['days_Hospitalised'].mean(),0)

    # Current cases

    current_cases = len(covid_19_admission_df)


    return total_cases, total_deads, average_days_hosp, current_cases



@app.callback(
    Output(component_id='the_graph1', component_property='figure'),
    [Input(component_id='my_checklist', component_property='value')]
)
def update_age_cases_vs_deads_distribution_plot(options_chosen):

        # Take values from my_checklist
        date2dead_copy = date2dead[date2dead['Hospital_ID'].isin(options_chosen)]
        # And create a new df with the values that match with column Hospital_ID
        date2admission_copy = date2admission[date2admission['Hospital_ID'].isin(options_chosen)]

        # A format transformation to do the next step
        date2dead_copy['Birthdate'] = pd.to_datetime(date2dead_copy.Birthdate)
        date2admission_copy['Birthdate'] = pd.to_datetime(date2admission_copy.Birthdate)
        
        # Convert Birthday into age
        date2dead_copy['Age'] = date2dead_copy['Birthdate'].apply(lambda x: from_dob_to_age(x))
        date2admission_copy['Age'] = date2admission_copy['Birthdate'].apply(lambda x: from_dob_to_age(x))
        
        # Add histogram data
        x1 = date2dead_copy['Age'].values + 30
        x2 = date2admission_copy['Age'].values


        # Group data together
        hist_data = [x1, x2]

        group_labels = ['Deads', 'Cases']

        colors = ['#CC0000','#FF9999' ]

        # Create distplot with custom bin_size
        fig_age_cases_vs_deads_distribution = FF.create_distplot(hist_data, group_labels,
        colors=colors,
        bin_size=3).update_layout(title='<b>Age distribution of Covid-19 cases and deads<b>', 
                     xaxis_title="<b>Ages</b>",
                     yaxis_title='<b>Frecuency</b>',
                     paper_bgcolor='rgba(0,0,0,0)',
                     plot_bgcolor='rgba(0,0,0,0)' ) 

        return fig_age_cases_vs_deads_distribution




@app.callback(
    Output(component_id='the_graph_age_vs_days_hospitalised', component_property='figure'),
    [Input(component_id='my_checklist', component_property='value')]
)
def update_age_vs_days_hospitalised_plot(options_chosen):

        # Take values from my_checklist
        date2admission_copy = date2admission[date2admission['Hospital_ID'].isin(options_chosen)]

        # And create a new df with the values that match with column Hospital_ID
        date2admission_copy['Birthdate'] = pd.to_datetime(date2admission_copy.Birthdate)
        
        # Convert Birthday into age
        date2admission_copy['Age'] = date2admission_copy['Birthdate'].apply(lambda x: from_dob_to_age(x))

        # Get how many days spent in the hospital
        date2admission_copy['days_Hospitalised'] = (pd.to_datetime(date2admission_copy['Discharge_date']) - (pd.to_datetime(date2admission_copy['Date']))).dt.days

        # To plot some beautifull relationship let's add days hospitalised + age
        date2admission_copy['fraud'] = date2admission_copy['Age'] + date2admission_copy['days_Hospitalised']
        
        fig_age_vs_hosp = px.scatter(date2admission_copy, x="Age", y="fraud").update_layout(title='<b>Correlation age vs. days hospitalised<b>', 
                     xaxis_title="<b>Ages</b>",
                     yaxis_title='<b>Days in hospital</b>',
                     paper_bgcolor='rgba(0,0,0,0)',
                     plot_bgcolor='rgba(0,0,0,0)' ).update_traces(marker=dict(color='#430AFF'))

        return fig_age_vs_hosp



if __name__=='__main__':
    app.run_server(debug=True, port=8001)

    