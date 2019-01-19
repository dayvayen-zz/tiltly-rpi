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

stream_token_temperature = plotly_user_config['plotly_streaming_tokens'][0]
stream_token_gravity = plotly_user_config['plotly_streaming_tokens'][1]

trace_temperature = go.Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token_temperature,
        maxpoints=80
    ),
    name='Temperature'
)

trace_gravity = go.Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token_gravity,
        maxpoints=80
    ),
    name='Gravity',
    yaxis='y2'
)



layout = go.Layout(
    title='Oaty McOatface data',
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

data = go.Data([trace_temperature, trace_gravity])
fig = go.Figure(data=data, layout=layout)

plot_url = py.plot(fig, filename='beer')


print "View your streaming graph here: ", plot_url

stream_temperature = py.Stream(stream_token_temperature)
stream_temperature.open()

stream_gravity = py.Stream(stream_token_gravity)
stream_gravity.open()


while True:
    beacon = tilt.getFirstTilt()
    stream_temperature.write({'x': dt.datetime.now(), 'y': beacon['Temp']})
    stream_gravity.write({'x': dt.datetime.now(), 'y': beacon['Gravity']/1000})
    time.sleep(5)

stream_temperature.close()
stream_gravity.close()
