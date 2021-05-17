
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



# LottieFiles - https://lottiefiles.com/
cases = "https://assets4.lottiefiles.com/datafiles/dNJ1QgOiCpNbFKD/data.json" 
vaccine = "https://assets8.lottiefiles.com/packages/lf20_d2iuvfbu.json"
death = "https://assets4.lottiefiles.com/packages/lf20_r44tksh6.json"
patients = "https://assets9.lottiefiles.com/packages/lf20_vPnn3K.json"
tested = "https://assets6.lottiefiles.com/packages/lf20_cepqhm3v.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))


# The database used

cnx = sqlite3.connect('./COVID_19.db') 


# Import App data from database 

People_vaccinated = pd.read_sql_query("SELECT * FROM People_vaccinated", cnx)
People_teste_positive = pd.read_sql_query("SELECT * FROM People_teste_positive", cnx)
Deaths_wihing_28_days = pd.read_sql_query("SELECT * FROM Deaths_wihing_28_days", cnx)
patients_adm = pd.read_sql_query("SELECT * FROM patients_adm", cnx)
Virus_tested = pd.read_sql_query("SELECT * FROM Virus_tested", cnx)
People_vaccinated_regions = pd.read_sql_query("SELECT * FROM People_vaccinated_regions", cnx)


# Bootstrap themes by Ann: https://hellodash.pythonanywhere.com/theme_explorer
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY])

app.layout = dbc.Container([
    dbc.Row([                                                                  ### FIRST ROW ###
        dbc.Col([
            dbc.Card([ 
                dbc.CardImg(src='/assets/wrgllogohighres.png')                   # Card 1 Image
            ],className='mb-2'),
            dbc.Card([
                dbc.CardBody([
                    dbc.CardLink("By Manuel Dominguez", target="_blank",          # Card 2 Name
                                 href="https://github.com/Manuel-DominguezCBG"
                    )
                ])
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([ 
                dbc.CardLink("COVID-19 in the UK", target="_blank", 
                    style = {'font-size': "30px"}                                  # Card 2 Name
                                 ),     
                dbc.CardLink("Vaccination, cases and death patients data in the selected period of time", 
                target="_blank", 
                    style = {'font-size': "10px"}                                  # Card 2 Name
                                 ),                                                                    # Card 3 Title
                dbc.CardBody([
               
                    dcc.DatePickerSingle(
                        id='my-date-picker-start',
                        date=date(2021, 5, 5),
                        className='ml-5',
                        style = {'width':'8',
                        'height':'5' } 
                    ),
                    dcc.DatePickerSingle(
                        id='my-date-picker-end',
                        date=date(2021, 8, 5),
                        className='mb-2 ml-2'
                    ),
                ])
            ], color="info", style={'height':'18vh'}),
        ], width=8),
    ],className='mb-2 mt-2'),
    dbc.Row([                                                                   ### SECOND ROW ###                                                       
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="40%", height="40%", url=vaccine)),
                dbc.CardBody([
                    html.H6('People vaccinated'),
                    html.H2(id='content-connections', children="000")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="40%", height="40%", url=cases)),
                dbc.CardBody([
                    html.H6('People tested positive'),
                    html.H2(id='content-companies', children="000")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="40%", height="40%", url=death)),
                dbc.CardBody([
                    html.H6('Deaths within 28 days of positive test'),
                    html.H2(id='content-msg-in', children="000")
                ], style={'textAlign':'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="40%", height="40%", url=patients)),
                dbc.CardBody([
                    html.H6('Patients admitted'),
                    html.H2(id='content-msg-out', children="000")
                ], style={'textAlign': 'center'})
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="40%", height="40%", url=tested)),
                dbc.CardBody([
                    html.H6('Virus test conducted'),
                    html.H2(id='content-reactions', children="000")
                ], style={'textAlign': 'center'})
            ]),
        ], width=2),
    ],className='mb-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='line-chart', figure={}, config={'displayModeBar': False}),
                ])
            ]),
        ], width=8),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='bar-chart', figure={}, config={'displayModeBar': False}),
                ])
            ]),
        ], width=4),
    ],className='mb-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='pie-chart', figure={}, config={'displayModeBar': False}),
                ])
            ]),
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='line-chart2', figure={}, config={'displayModeBar': False}),
                ])
            ]),
        ], width=8),
        
    ],className='mb-2'),
   
    
],



 fluid=True)


# Updating the 5 number cards 
@app.callback(
    Output('content-connections','children'),
    Output('content-companies','children'),
    Output('content-msg-in','children'),
    Output('content-msg-out','children'),
    Output('content-reactions','children'),
    Input('my-date-picker-start','date'),
    Input('my-date-picker-end','date'),
)


   
def update_small_cards(start_date, end_date):
    
    # Total people vaccinated 
    People_vaccinated2 = People_vaccinated[(People_vaccinated['date']>=start_date) & (People_vaccinated['date']<=end_date)]
    TOTAL_PV = People_vaccinated2['newPeopleVaccinatedFirstDoseByPublishDate'].sum()

    # People tested positive 
    People_teste_positive2 = People_teste_positive[(People_teste_positive['date']>=start_date) & (People_teste_positive['date']<=end_date)]
    TOTAL_TP = People_teste_positive2['newCasesBySpecimenDate'].sum()

    # Death within 28 days of positive test
    Deaths_wihing_28_days2 = Deaths_wihing_28_days[(Deaths_wihing_28_days['date']>=start_date) & (Deaths_wihing_28_days['date']<=end_date)]
    TOTAL_deaths = Deaths_wihing_28_days2['newDeaths28DaysByDeathDate'].sum()

    # Patients admitted hospital
    patients_adm2 = patients_adm[(patients_adm['date']>=start_date) & (patients_adm['date']<=end_date)]
    TOTAL_PA = patients_adm2['newAdmissions'].sum()

    # Patients admitted hospital
    Virus_tested2 = Virus_tested[(Virus_tested['date']>=start_date) & (Virus_tested['date']<=end_date)]
    TOTAL_VT = Virus_tested2['newVirusTests'].sum()


    return TOTAL_PV, TOTAL_TP, TOTAL_deaths, TOTAL_PA, TOTAL_VT

     

# Line Chart 
@app.callback(
    Output('line-chart','figure'),
    Input('my-date-picker-start','date'),
    Input('my-date-picker-end','date'),
)
def update_line(start_date, end_date):

    People_vaccinated_regions2 = People_vaccinated_regions[(People_vaccinated_regions['date']>=start_date) & (People_vaccinated_regions['date']<=end_date)]
    People_vaccinated_regions2=People_vaccinated_regions2.rename(columns = {'areaName':'UK Regions'}) 
    fig_linee = px.line(People_vaccinated_regions2, x="date", y="newPeopleVaccinatedFirstDoseByPublishDate", color='UK Regions')

    fig_linee.update_layout(
    height=400,
    title=dict(
        text='<b>Number of people vaccineted by UK regions</b>', 
        x=0.5,
        y=0.95,
        font=dict(
            family="Arial",
            size=20,
            color='#000000'
        )
    ),
    xaxis_title="<b>Selected dates</b>",
    yaxis_title='<b>People vaccinated (First dose)</b>',
    font=dict(
        family="Courier New, Monospace",
        size=12,
        color='#000000'
    )
)
    return fig_linee


# Bar Chart ************************************************************
@app.callback(
    Output('bar-chart','figure'),
    Input('my-date-picker-start','date'),
    Input('my-date-picker-end','date'),
)
def update_bar(start_date, end_date):

    People_vaccinated_regions2 = People_vaccinated_regions[(People_vaccinated_regions['date']>=start_date) & (People_vaccinated_regions['date']<=end_date)]
    People_vaccinated_regions2=People_vaccinated_regions2.rename(columns = {'areaName':'UK Regions'}) 
    fig_bare = px.bar(People_vaccinated_regions2, x="date", y="cumPeopleVaccinatedFirstDoseByPublishDate", color='UK Regions')
    fig_bare.update_layout(title='<b>Total people vaccineted by UK regions<b>',
                   xaxis_title='Selected dates',
                   yaxis_title='People vaccinated (cumulative)',
                   paper_bgcolor='rgba(0,0,0,0)',
                   plot_bgcolor='rgba(0,0,0,0)') # Transparent background here looks better
    fig_bare.update_layout(
        height=400,
        title=dict(
        text='<b>Total people vaccineted by UK regions</b>', 
        x=0.5,
        y=0.95,
        font=dict(
            family="Arial",
            size=20,
            color='#000000'
                 )
                  ),
    xaxis_title="<b>Selected dates</b>",
    yaxis_title='<b>People vaccinated (cumulative)</b>',
    font=dict(
        family="Courier New, Monospace",
        size=12,
        color='#000000'
             ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)' # Transparent background here looks better
                          )

    return fig_bare


# Pie Chart 
@app.callback(
    Output('pie-chart','figure'),
    Input('my-date-picker-start','date'),
    Input('my-date-picker-end','date'),
)
def update_pie(start_date, end_date):

    UK_population = 66650000 # Approx
    colors = ['gold', 'lightgreen']
    total_people_vaccinated = People_vaccinated.loc[People_vaccinated['date'] == "2021-05-08", 'cumPeopleVaccinatedFirstDoseByPublishDate'].iloc[0]
    total_UK_population = UK_population - total_people_vaccinated
    fig_piee = px.pie(names=['Vacinatted','No vacinatted'], values=[total_people_vaccinated, total_UK_population],
                       )
    fig_piee.update_traces(  textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    fig_piee.update_layout(
    height=400,
    title=dict(
        text='<b>% of vacinatted and no vacinatted UK population</b>',
        x=0.5,
        y=0.95,
        font=dict(
            family="Arial",
            size=15,
            color='#000000'
        )
    )
)

    return fig_piee


# Line chart 2


@app.callback(
    Output('line-chart2','figure'),
    Input('my-date-picker-start','date'),
    Input('my-date-picker-end','date'),
)

def update_line2(start_date, end_date):


    Deaths_wihing_28_days2 = Deaths_wihing_28_days[(Deaths_wihing_28_days['date']>=start_date) & (Deaths_wihing_28_days['date']<=end_date)]
    patients_adm2 = patients_adm[(patients_adm['date']>=start_date) & (patients_adm['date']<=end_date)]

    # add line / trace 1 to fig_linee2
    fig_linee2 = go.Figure()
    fig_linee2.add_trace(go.Scatter(
    x=Deaths_wihing_28_days2["date"],
    y=Deaths_wihing_28_days2['newDeaths28DaysByDeathDate'],

    marker=dict(
        color="blue"
    ),
    showlegend=True
))

# add line / trace 2 to fig_linee2

    fig_linee2.add_trace(go.Scatter(
    x=patients_adm2["date"],
    y=patients_adm2["newAdmissions"],

    marker=dict(
        color="green"
    ),
    showlegend=True))

    fig_linee2.update_layout(
    height=400,
    title=dict(
        text='<b>Death people and admitted by COVID</b>', 
        x=0.5,
        y=0.95,
        font=dict(
            family="Arial",
            size=20,
            color='#000000'
        )
    ),
    xaxis_title="<b>Selected date</b>",
    yaxis_title='<b>Number of people</b>',
    font=dict(
        family="Courier New, Monospace",
        size=12,
        color='#000000'
    )
)
    return fig_linee2


if __name__=='__main__':
    app.run_server(debug=True, port=8001)
