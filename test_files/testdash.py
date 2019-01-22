import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.plotly as py # plotly library
from plotly.graph_objs import *
import datetime as dt
import pandas as pd
import time

beerData = pd.read_csv('beerdatatest.csv')

app = dash.Dash(__name__)

app.layout = html.Div(children = [
    html.H1(children = "some data from a tilt hydrometer"),
    dcc.Graph(id = "temperature-graph",
              figure = {
                'data': [
                    {'x': beerData['time'], 'y': beerData['temperature'], 'type': 'scatter'}
                ],
                'layout': {
                'title': 'Dash Data Visualization'
                }
        })
])

if __name__ == '__main__':
    app.run_server(debug=True)
