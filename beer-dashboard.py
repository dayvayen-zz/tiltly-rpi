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
    __name__,
    external_stylesheets=external_css
)

# server = app.server # deploy in a Heroku app, i think.

app.layout = html.Div([
  html.Div([
    html.H2("Beer data")
    ], className='banner'),
    html.Div([
      dcc.Graph(id='tilt-data'),
  ]),
  dcc.Interval(id='tilt-interval', interval=1000, n_intervals=0),
])

@app.callback(Output('tilt-data', 'figure'),
              [Input('tilt-interval', 'n-intervals')])
def update_tilt_data(n):
