import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.plotly as py # plotly library
from plotly.graph_objs import *
import datetime as dt
import time
import tilt
from updateSQL import create_connection
import sqlite3
import pandas as pd
from dash.dependencies import Input, Output


external_css = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(
    __name__,
    external_stylesheets=external_css
)

db_file = "tiltdata.db"
beerName = "oaty"
n_records = 10

server = app.server # deploy in a Heroku app, i think.

def updateData(db_file, beerName, n_records):
    conn = create_connection(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + beerName + " ORDER BY time DESC LIMIT " + n_records)
    rows = cur.fetchall()
    labels = ['time', 'temperature', 'gravity']
    df = pd.DataFrame.from_records(rows, columns=labels)
    return(df)


beerData = updateData(db_file, beerName, n_records)


app.layout = html.Div(children = [
    html.H1(children = "some data from a tilt hydrometer"),
    dcc.Graph(id = "temperature-graph",
              figure = {
                'data': [
                    {'x': beerData['time'], 'y': beerData['temperature'], 'type': 'scatter'}
                ],
                'layout': {
                    'title': 'Temperature'
                }
        }),
    dcc.Graph(id = "gravity-graph",
              figure = {
                'data': [
                    {'x': beerData['time'], 'y': beerData['gravity'], 'type': 'scatter'}
                ],
                'layout' : {
                    'title': 'Specific gravity'
                }
              })
])


if __name__ == '__main__':
    app.run_server(debug=True)
