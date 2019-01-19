import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.plotly as py # plotly library
from plotly.graph_objs import *
import datetime as dt
import time
import tilt

external_css = ["https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
                "https://fonts.googleapis.com/css?family=Raleway:400,400i,700,700i",
                "https://fonts.googleapis.com/css?family=Product+Sans:400,400i,700,700i"]

app = dash.Dash(
    'beer-app',
    external_stylesheets=external_css
)

server = app.server

app.layout = html.Div([
  html.Div([
    html.H2("Beer data")
  ], className='banner'),
  html.Div([
    html.Div([
      html.H3("WIND SPEED (mph)")
      ], className='Title'),
    html.Div([
      dcc.Graph(id='wind-speed'),
  ], className='twelve columns wind-speed'),
  dcc.Interval(id='wind-speed-update', interval=1000, n_intervals=0),
], className='row wind-speed-row')
])
