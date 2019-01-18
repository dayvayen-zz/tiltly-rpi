from os import uname
from socket import gethostname
import json
import sys
import time
import tilt
import plotly as py # plotly library
from plotly.graph_objs import *
import datetime as dt

while True:
    beacon = tilt.getFirstTilt()
    now = dt.datetime.now()
    print({'time': now, 'gravity': beacon['Gravity']})
    time.sleep(2)
