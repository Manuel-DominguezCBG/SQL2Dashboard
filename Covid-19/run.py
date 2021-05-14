# The script that take the data from the database and create the dashboard is called run.py
# For explanation I have created an adapted scrict for jupyter that shows same output here



# In order to start using Dash, we have to install several packages.
'''
pip install dash==0.21.1  
pip install dash-renderer==0.13.0  
pip install dash-html-components==0.11.0
pip install dash-core-components==0.23.0  
pip install plotly --upgrade
'''


import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import sqlite3


#### GETTING DATA FROM DATABASE ####

# I import here all tables in pandas objects I am going to use 

cnx = sqlite3.connect('./Data/COVID_19.db') # The database


# The tables of the databases
People_vaccinated = pd.read_sql_query("SELECT * FROM People_vaccinated", cnx)
People_teste_positive = pd.read_sql_query("SELECT * FROM People_teste_positive", cnx)
Deaths_wihing_28_days = pd.read_sql_query("SELECT * FROM Deaths_wihing_28_days", cnx)
patients_adm = pd.read_sql_query("SELECT * FROM patients_adm", cnx)
Virus_tested = pd.read_sql_query("SELECT * FROM Virus_tested", cnx)
People_vaccinated_regions = pd.read_sql_query("SELECT * FROM People_vaccinated_regions", cnx)

#### CREATING THE PLOTS ####

# The graphs show in the dashboard are created in advances
People_vaccinated_regions_fig = px.line(People_vaccinated_regions, x='date', y='newPeopleVaccinatedFirstDoseByPublishDate',
              color='areaName')
People_vaccinated_regions_fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})



# Vaccines plots

PVRnew_fig = px.line(People_vaccinated_regions, x='date', y='newPeopleVaccinatedFirstDoseByPublishDate',
              color='areaName')
PVRnew_fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})
PVRnew_fig_available_indicators = People_vaccinated_regions['areaName'].unique()



external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__)

app.layout = html.Div([
                # Title and logo box
                html.Div([
                        # Title        
                        html.Div(children="Coronavirus (COVID-19) in the UK",className="Title",
                        style={
                        'backgroundColor':'white',
                        'color':'black',
                        'width':'80%',
                        'text-align':'left',
                        'display':'inline-block',
                        'font-size': "40px",}),
                        # Logo
                         html.Img(src=app.get_asset_url('./logo_hospital.png'),style={
                        'backgroundColor':'white',
                        'color':'lightsteelblue',
                        'height':'50%',
                        'width':'5%',
                        'text-align':'left',
                        'display':'inline-block'}),],),
                # Explanation dashboard box
                html.P(children="The official UK government website for data and insights on coronavirus (COVID-19)."),
                # People vaccinated box
                html.Div([ 
                        #Title of the box
                         html.Div(children="Vaccinations",className="Title",
                        style={
                                'color':'#cce0ff',
                                'width':'80%',
                                'text-align':'left',
                                'display':'inline-block',
                                'font-size': "20px",}),
                        # Indicators 
                        dcc.Dropdown(
                        id='regions',
                        options=[{'label': i, 'value': i} for i in PVRnew_fig_available_indicators],
                        value='England'),
                        # Plot
                        dcc.Graph(id='indicator-graphic',
                        style= {
                                'width':'70%',
                                'height':'100%'
                               })


                          ])



])





#@app.callback(
#    Output('indicator-graphic', 'figure'),
#    Input('xaxis-column', 'value'))



app.run_server(debug=True)