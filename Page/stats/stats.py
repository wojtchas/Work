import csv
import time
from sqlalchemy import create_engine

#Globals
IPlist = []
#CounterList = []
counter = 0
db = None

###############

def connect_db():
    global db
    engine = create_engine('postgresql://postgres:postgres99@localhost/tatools')
    db = engine.connect()

def read_IPlist():
    global IPlist
    with open("IPlist.csv", "r") as f:
        read = csv.reader(f)
        IPlist = list(read)
        f.close()

def add_Count():
    global counter
    counter += 1

def send_CountINT(ip):
    CounterList.append([int(time.time()), 1, ip])
    db.close()

def send_Count(ip):
    global db
    db.execute("insert into duties_stats values (%i, 1, '%s');" % (int(time.time()),str(ip)))
    db.close()

def send_Count0():
    global db
    db.execute("insert into duties_stats values (%i, 0);" % (int(time.time())))
    db.close()

def counts_Sender():
    connect_db()
    while(True):
        global counter
        global db
        #global CounterList
        #CounterList.append([int(time.time()), counter])
        db.execute("insert into duties_stats values (%i, %i);" % (int(time.time()), counter))
        counter = 0
        time.sleep(600)

def get_CounterList():
    #return CounterList
    db_list = db.execute("select * from duties_stats;")
    db.close()
    return map(list, list(db_list))
    

if __name__ == '__main__':
    read_IPlist()
    print IPlist
