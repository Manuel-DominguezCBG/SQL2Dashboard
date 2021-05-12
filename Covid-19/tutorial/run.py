
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

# Get data from database

cnx = sqlite3.connect('/Users/monkiky/Desktop/SQL2Dashboard/Covid-19/COVID_19.db')

People_vaccinated = pd.read_sql_query("SELECT * FROM People_vaccinated", cnx)
People_vaccinated_fig = px.line(People_vaccinated, x="date", y="newPeopleVaccinatedFirstDoseByPublishDate", title='Life expectancy in Canada')
theme = {
    "accent":"#fa4f56",
    "accent_negative":"#ff2c6d",
    "accent_positive":"#33ffe6",
    "background_content":"#F9F9F9",
    "background_page":"#F2F2F2",
    "body_text":"#606060",
    "border":"#e2e2e2",
    "breakpoint_font":"1200px",
    "breakpoint_stack_blocks":"700px",
    "card_border":{
        "width":"0px 0px 0px 0px",
        "style":"solid",
        "color":"#e2e2e2",
        "radius":"0px"
    },
    "card_background_color":"#F9F9F9",
    "card_box_shadow":"0px 1px 3px rgba(0,0,0,0.12), 0px 1px 2px rgba(0,0,0,0.24)",
    "card_margin":"15px",
    "card_padding":"5px",
    "card_outline":{
        "width":"0px",
        "style":"solid",
        "color":"#e2e2e2"
    },
    "card_header_border":{
        "width":"0px 0px 1px 0px",
        "style":"solid",
        "color":"#e2e2e2",
        "radius":"0px"
    },
    "card_header_background_color":"#F9F9F9",
    "card_header_box_shadow":"0px 0px 0px rgba(0,0,0,0)",
    "card_header_margin":"0px",
    "card_header_padding":"10px",
    "colorway":[
        "#fa4f56",
        "#4c78a8",
        "#f58518",
        "#72b7b2",
        "#54a24b",
        "#eeca3b",
        "#b279a2",
        "#ff9da6",
        "#9d755d",
        "#bab0ac"
    ],
    "colorscale":[
        "#fa4f56",
        "#fe6767",
        "#ff7c79",
        "#ff908b",
        "#ffa39d",
        "#ffb6b0",
        "#ffc8c3",
        "#ffdbd7",
        "#ffedeb",
        "#ffffff"
    ],
    "font_family":"Raleway",
    "font_size":"17px",
    "font_size_smaller_screen":"15px",
    "font_family_header":"Roboto",
    "font_size_header":"24px",
    "font_family_headings":"Roboto",
    "font_headings_size":None,
    "header_border":{
        "width":"0px 0px 0px 0px",
        "style":"solid",
        "color":"#e2e2e2",
        "radius":"0px"
    },
    "header_background_color":"#F9F9F9",
    "header_box_shadow":"0px 1px 3px rgba(0,0,0,0.12), 0px 1px 2px rgba(0,0,0,0.24)",
    "title_capitalization":"uppercase",
    "header_content_alignment":"spread",
    "header_margin":"0px 0px 15px 0px",
    "header_padding":"0px",
    "header_text":"#606060",
    "heading_text":"#606060",
    "text":"#606060",
    "report_font_family":"Computer Modern",
    "report_font_size":"12px",
    "report_background_page":"white",
    "report_background_content":"#FAFBFC",
    "report_text":"black"
}

app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Vaccinated',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='People_vaccinated_fig',
        figure=People_vaccinated_fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)