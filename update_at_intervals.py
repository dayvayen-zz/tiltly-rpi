import updateSQL
import time


db_file = raw_input("Enter database name: ")
beerName = raw_input("Enter beer table name: ")
interval = float(raw_input("How many minutes between updates? ")) * 60

try:
    while True:
        updateBeerTable()
        time.sleep(interval)
except KeyboardInterrupt:
    print('Manual break by user')
