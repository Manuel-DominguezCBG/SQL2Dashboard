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

cnx = sqlite3.connect('./COVID_19.db') # The database


# The tables of the databases
People_vaccinated = pd.read_sql_query("SELECT * FROM People_vaccinated", cnx)
People_teste_positive = pd.read_sql_query("SELECT * FROM People_teste_positive", cnx)
Deaths_wihing_28_days = pd.read_sql_query("SELECT * FROM Deaths_wihing_28_days", cnx)
patients_adm = pd.read_sql_query("SELECT * FROM patients_adm", cnx)
Virus_tested = pd.read_sql_query("SELECT * FROM Virus_tested", cnx)
People_vaccinated_regions = pd.read_sql_query("SELECT * FROM People_vaccinated_regions", cnx)

#### CREATING THE PLOTS ####

# The graphs show in the dashboard are created in advances

# Vaccines plots

People_vaccinated_regions_new = px.line(People_vaccinated_regions, x='date', y='newPeopleVaccinatedFirstDoseByPublishDate',
              color='areaName')
People_vaccinated_regions_new.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})




external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

app = JupyterDash(external_stylesheets=external_stylesheets) # For jupyter notebook

app.layout = html.Div([
            html.Div([
               html.Div(children="Coronavirus (COVID-19) in the UK",className="Title",
                        style={
                        'backgroundColor':'white',
                        'color':'black',
                       # 'height':'40px',
                        'width':'80%',
                        'text-align':'left',
                        'display':'inline-block',
                        'font-size': "40px",
                        }),
                html.Img(src=app.get_asset_url('./logo_hospital.png'),style={
                        'backgroundColor':'white',
                        'color':'lightsteelblue',
                        'height':'50px',
                        'width':'5%',
                        'text-align':'left',
                        'display':'inline-block'}),
                        ], ),
    html.P(
            children="The official UK government website for data and insights on coronavirus (COVID-19).",
        ),
             html.Div([
               html.Div(children="People vaccinated",className="box1",
                        style={
                        'backgroundColor':'white',
                        "text-decoration": "underline",
                        "border-style": "solid",
                        "border-color": "#3B73E5",
                        "border-width": "1px",
                        'color':'black',
                        'margin-left':'10px',
                        "background-color": "#C6D7F9",
                        'height':'100px',
                        'width':'1000px',
                        'text-align':'left',
                        'display':'inline-block'},
                        
                       ),
                        ]),
    
           
               html.Div([
               html.Div(children="Block 1",className="box1",
                        style={
                        'backgroundColor':'darkslategray',
                        'color':'lightsteelblue',
                        'height':'100px',
                        'margin-left':'10px',
                        'width':'45%',
                        'text-align':'center',
                        'display':'inline-block'
                        }),
            
                html.Div(dcc.Dropdown (options=[{'label':"England",'value':"England"},{'label':"Northern Ireland",'value':"Northern Ireland"},{'label':"Scotland",'value':"Scotland"},{'label':"Wales",'value':"Wales"},],value = "England"),className="box2",
                         style={
                        'backgroundColor':'darkslategray',
                        'color':'lightsteelblue',
                        'height':'100px',
                        'margin-left':'10px',
                        'text-align':'center',
                        'width':'40%',
                        'display':'inline-block'
               })
                        ]),
            
            
      ])

#app.run_server(mode='external')
if __name__ == '__main__':
    app.run_server(debug=True)
