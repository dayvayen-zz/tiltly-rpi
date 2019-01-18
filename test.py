from os import uname
from socket import gethostname
import json
import sys
import time
import tilt
import datetime as dt
import plotly
plotly.offline.init_notebook_mode(connected=True)
import plotly.offline as py

while True:
    beacon = tilt.getFirstTilt()
    now = dt.datetime.now()
    print({'time': now, 'gravity': beacon['Gravity']})
    time.sleep(2)
