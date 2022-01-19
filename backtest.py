import time, pymongo
import dotenv, os
from datetime import datetime, timedelta
from pymongo import MongoClient, InsertOne
from dotenv import load_dotenv
from strategy import strat1
from actions import *

dotenv.load_dotenv()

client = pymongo.MongoClient("mongodb+srv://"+os.getenv('MONGO_USER')+":"+os.getenv('MONGO_PASS')+"@cluster0.8ttfr.mongodb.net/"+os.getenv('MONGO_DATABASE')+"?retryWrites=true&w=majority")
db = client.crypto
collection = db.solana

# convert to unix time
start_date = datetime.strptime("2021-08-17", "%Y-%m-%d")
end_date = datetime.strptime("2021-08-20", "%Y-%m-%d")
delta = timedelta(days=1)

start_date_unix = int(start_date.timestamp())
end_date_unix = int(end_date.timestamp())

amount = 10000

# loop through dates (this could be multithreaded in the future)
    # send current data to strategy
    # based on return complete action of either buy/sell/nothing
    # buy operation will buy half of current amount
    # update amount

# while start_date <= end_date:
data = collection.find_one({"_id": str(start_date.date())})
for i, time in enumerate(data["dates"]):
    price = data["USD"][i]
    date = datetime.strptime(datetime.utcfromtimestamp(time/1000).strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S") - timedelta(hours=6)

    # short position with half of amount 
    if i == 0:
        # short(amount, price)
        print("first")
    # buy back all shares when time is around 3:30
    elif  date.time() > datetime.strptime("03:30:00", "%H:%M:%S").time() and date.time() < datetime.strptime("6:30:00", "%H:%M:%S").time() :
        print(i)
        break
    # else
        # maybe at one point check if we have reach certain profit percentage and take profits
    # start_date += delta