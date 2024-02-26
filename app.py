# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_leaflet as dl

#i have pip-installed dash and dash-leaflet

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
#DATA WILL BE IMPORTED HERE

# Initialize the app - incorporate css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = html.Div([
    html.Div(className='row', children='Channel Island Dashboard',
             style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),

    html.Div(className='row', children=[
        dcc.Dropdown(options=['DO', 'pH', 'SST'],
#                       value='lifeExp',
                      # inline=True,
                       id='my-dropdown-final')
    ]),

    html.Div([
    dl.Map(center=[38.9072, -77.0369], zoom=10, children=[
        dl.TileLayer(),
        dl.Marker(position=[38.9072, -77.0369], children=[
            dl.Popup("Washington, D.C.")
        ])
    ])
])
])





# Add controls to build the interaction
@callback(
#    Output(component_id='histo-chart-final', component_property='figure'),
    Input(component_id='my-dropdown-final', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
