import updateSQL
import time
from timeloop import Timeloop

db_file = raw_input("Enter database name: ")
beerName = raw_input("Enter beer table name: ")
interval = float(raw_input("How many minutes between updates? ")) * 60

loop = Timeloop()

@loop.job(interval = timedelta(seconds = interval))
def intervalUpdate():
    updateBeerTable(db_file, beerName)
