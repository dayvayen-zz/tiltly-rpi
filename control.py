from os import uname
from socket import gethostname
import json
import sys
import time
import tilt
import plotly.plotly as py # plotly library
from plotly.graph_objs import *
import datetime as dt

with open('./config.json') as config_file:
    plotly_user_config = json.load(config_file)

    py.sign_in(plotly_user_config["plotly_username"], plotly_user_config["plotly_api_key"])

url = py.plot([
    {
        'x': [], 'y': [], 'type': 'scatter',
        'stream': {
            'token': plotly_user_config['plotly_streaming_tokens'][0],
            'maxpoints': 200
        }
    }], filename='Raspberry Pi Streaming Example Values')

print "View your streaming graph here: ", url

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
    stream.write({'x': dt.datetime.now(), 'y': beacon['Temp']})
    time.sleep(0.25)
