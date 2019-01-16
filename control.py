from os import uname
from socket import gethostname
import sys
import time
import tilt

beacon = {}

def getTemp():
    return beacon['Temp'] if beacon else 60


def getGravity():
    return beacon['Gravity']/1000 if beacon else 1000
# first let's try just getting a streaming graph with the gravity data.
global beacon
beacon = tilt.getFirstTilt()

variables = {
        'Gravity': {
            'type': 'numeric',
            'bind': getGravity
        },
        'Beer Temp': {
            'type': 'numeric',
            'bind': getTemp
        }
    }
