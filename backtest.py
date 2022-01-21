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

account = {"balance": 10000, "shares": 0}

# loop through dates (this could be multithreaded in the future)
    # send current data to strategy
    # based on return complete action of either buy/sell/nothing
    # buy operation will buy half of current amount
    # update amount

# while start_date <= end_date:
data = collection.find_one({"_id": str(start_date.date())})
for i, time in enumerate(data["dates"]):
    account = strat1(account, data["USD"][i], i, time)
    
    # else
        # maybe at one point check if we have reach certain profit percentage and take profits
    # start_date += delta
print()