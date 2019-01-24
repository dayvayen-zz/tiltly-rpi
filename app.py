import plotly
import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime as dt
import time
import sqlite3
import pandas as pd
from dash.dependencies import Input, Output

external_css = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_css)

db_file = "tiltdata.db"
beerName = "oaty"
n_records = "20"

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def updateData(db_file, beerName, n_records):
    conn = create_connection(db_file)
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + beerName + " ORDER BY time DESC LIMIT " + n_records)
    rows = cur.fetchall()
    labels = ['time', 'temperature', 'gravity']
    df = pd.DataFrame.from_records(rows, columns=labels)
    return(df)

def getMaxGravity(db_file, beerName):
    conn = create_connection(db_file)
    cur = conn.cursor()
    cur.execute("SELECT MAX(gravity) FROM " + beerName)
    maxGravity = cur.fetchone()[0]
    return(maxGravity)

def getMinGravity(db_file, beerName):
    conn = create_connection(db_file)
    cur = conn.cursor()
    cur.execute("SELECT MIN(gravity) FROM " + beerName)
    minGravity = cur.fetchone()[0]
    return(minGravity)

beerData = updateData(db_file, beerName, n_records)
maxGravity = getMaxGravity(db_file, beerName)
minGravity = getMinGravity(db_file, beerName)
updateTime = beerData['time'].max()

app.layout = html.Div(children = [
    html.H1(children = "Tilt hydrometer data for beer " + beerName),
    html.H2(children = "I was last updated at " + str(updateTime)),
    html.Div(id = 'og-toggle'),
    dcc.Input(id = 'og-value', value = maxGravity, type = 'float'),
    html.Div(id = 'abv-value'),
    html.Div([
        dcc.Graph(id = "temperature-graph",
                  figure = {
                    'data': [
                        {'x': beerData['time'], 'y': beerData['temperature'], 'type': 'scatter'}
                    ],
                    'layout': {
                        'title': 'Temperature'
                    }
            })
            ],
            style={'width': '48%', 'display': 'inline-block'}),
    html.Div([
        dcc.Graph(id = "gravity-graph",
              figure = {
                'data': [
                    {'x': beerData['time'], 'y': beerData['gravity'], 'type': 'scatter'}
                ],
                'layout' : {
                    'title': 'Specific gravity'
                }
              })
              ],
              style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
])

@app.callback(
    Output(component_id = 'og-toggle', component_property = 'children'),
    [Input(component_id = 'og-value', component_property = 'value')]
)

def update_og_toggle(input_value):
    return 'Please enter your original gravity if it is not {}.'.format(maxGravity)

@app.callback(
    Output(component_id = 'abv-value', component_property = 'children'),
    [Input(component_id = 'og-value', component_property = 'value')]
)
def update_abv(input_value):
    abv = round((float(input_value) - float(minGravity)) * 131.25, 2)
    return 'Your current ABV is {} %.'.format(abv)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
