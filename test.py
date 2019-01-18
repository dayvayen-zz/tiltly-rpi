from os import uname
from socket import gethostname
import json
import sys
import time
import tilt
import datetime as dt
import plotly as py # plotly library
from plotly.graph_objs import Scatter, Layout, Figure # plotly graph objects
import time

py.sign_in(username, api_key)

username = 'dayvayen'
api_key = 'cxKRDUgmdRm70fXKPNW3'
stream_token = '231cxdk5rc'

trace1 = Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token,
        maxpoints=200
    )
)

layout = Layout(
    title='Raspberry Pi Streaming Sensor Data'
)

fig = Figure(data=[trace1], layout=layout)

print py.plot(fig, filename='Raspberry Pi Streaming Example Values')

stream = py.Stream(stream_token)
stream.open()

while True:
    beacon = tilt.getFirstTilt()
    now = dt.datetime.now()
    stream.write({'x': now, 'y': beacon['Gravity']})
    time.sleep(0.25)
