import sqlite3
from sqlite3 import Error
import tilt
import datetime as dt



def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def addData(conn, beerName, data):
    """ take beer data and add it
        to the table
    """
    sql = "insert into " + beerName + """ (time,
                                            temperature,
                                            gravity)
            VALUES(?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, data)
    return cur.lastrowid

def updateBeerTable(db_file, beerName):
    conn = create_connection(db_file)
    beacon = tilt.getFirstTilt()
    with conn:
        data = (dt.datetime.now(), beacon['Temp'], beacon['Gravity']/1000)
        addData(conn, beerName, data)
        print("Added data at " + dt.datetime.now())
        return None
