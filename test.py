
import tilt
import datetime as dt
import plotly
import plotly.plotly as py # plotly library
import plotly.graph_objs as go
import time



username = 'dayvayen'
api_key = 'cxKRDUgmdRm70fXKPNW3'
stream_token = '231cxdk5rc'

py.sign_in(username, api_key)

trace1 = go.Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token,
        maxpoints=200
    )
)

layout = go.Layout(
    title='Raspberry Pi Streaming Sensor Data'
)

fig = go.Figure(data=[trace1], layout=layout)

print py.plot(fig, filename='Raspberry Pi Streaming Example Values')

stream = py.Stream(stream_token)
stream.open()

while True:
    beacon = tilt.getFirstTilt()
    now = dt.datetime.now()
    stream.write({'x': now, 'y': beacon['Gravity']})
    time.sleep(0.25)
