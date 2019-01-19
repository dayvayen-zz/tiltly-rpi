from os import uname
from socket import gethostname
import json
import sys
import time
import tilt
import plotly
import plotly.plotly as py # plotly library
import plotly.graph_objs as go
import datetime as dt

with open('./config.json') as config_file:
    plotly_user_config = json.load(config_file)

    py.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])


trace1 = go.Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token[0],
        maxpoints=200
    ),
    name='Temperature'
)

trace2 = go.Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token[1],
        maxpoints=200
    ),
    name='Gravity',
    yaxis='y2'
)

data = [trace1, trace2]

layout = go.Layout(
    title='Double Y Axis Example',
    yaxis=dict(
        title='Temperature'
    ),
    yaxis2=dict(
        title='Gravity',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)
fig = go.Figure(data=data, layout=layout)

plot_url = py.plot(fig, filename='beer')


print "View your streaming graph here: ", plot_url

stream = py.Stream(plotly_user_config['plotly_streaming_tokens'][0])
stream.open()


# first let's try just getting a streaming graph with the gravity data.
# steps to do that:
# 1. read in the data using tilt.getFirstTilt()
# 2. get the gravity with getGravity
# 3. stream to dash?
# maybe i could collect the data and update the plot every so often?

while True:
    beacon = tilt.getFirstTilt()
    stream.write({'x': dt.datetime.now(), 'y': beacon['Temp'], 'y2': beacon['Gravity']})
    time.sleep(0.25)
