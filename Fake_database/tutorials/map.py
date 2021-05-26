import dash  # use Dash version 1.16.0 or higher for this app to work
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd
import json
from urllib.request import urlopen
import numpy as np

df = px.data.gapminder()


# data



#Load GeoJson 
with urlopen('https://opendata.arcgis.com/datasets/48b6b85bb7ea43699ee85f4ecd12fd36_4.geojson') as response:
    counties = json.load(response)
 
#Load data to be charted    
dummy_data=pd.read_csv('https://opendata.arcgis.com/datasets/48b6b85bb7ea43699ee85f4ecd12fd36_0.csv?outSR=%7B%22latestWkid%22%3A27700%2C%22wkid%22%3A27700%7D')
#add dummy data
dummy_data['value']=np.random.randint(10, 100, size=len(dummy_data))

#With Plotly
import plotly.express as px
from geojson_rewind import rewind

#Make the rings clockwwise (to make it compatible with plotly)    
counties_corrected=rewind(counties,rfc7946=False)




fig = px.choropleth(dummy_data, geojson=counties_corrected, locations='nuts218cd', featureidkey="properties.nuts218cd", color='value',
                            color_continuous_scale="PurPor", labels={'label name':'label name'}, title='MAP TITLE',
                            scope="europe").update_geos(fitbounds="locations", visible=False)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
        dcc.Graph(figure = fig, style={'width': '90vh', 'height': '90vh'})

])





# Dash version 1.16.0 or higher



if __name__ == '__main__':
    app.run_server(debug=True)
    
    
# https://youtu.be/G8r2BB3GFVY
