import sqlite3
from sqlite3 import Error
import tilt
import datetime as dt



def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def addData(conn, data):
    """ take beer data from tilt and add it
        to the table
    """
    sql = "insert into " + beerName + """ (time,
                                            temperature,
                                            gravity)
            VALUES(?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, data)
    return cur.lastrowid

def updateBeerTable():
    db_file = raw_input("Enter database name: ")
    beerName = raw_input("Enter beer table name: ")
    conn = create_connection(db_file)
    beacon = tilt.getFirstTilt()
    with conn:
        data = (dt.datetime.now(), beacon['Temp'], beacon['Gravity']/1000)
        addData(conn, data)
        print("Added data at " + dt.datetime.now())
        return None
