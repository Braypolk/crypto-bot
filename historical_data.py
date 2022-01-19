import requests, json, time, pymongo, os
from datetime import datetime
from pymongo import MongoClient, InsertOne
from dotenv import load_dotenv

load_dotenv()

utc_start = 1629003600000 # example 1641016800000 = 1/1/22 midnight trailing 0's required
utc_end = utc_start+86400000
coin = "solana"

client = pymongo.MongoClient("mongodb+srv://"+os.getenv('MONGO_USER')+":"+os.getenv('MONGO_PASS')+"@cluster0.8ttfr.mongodb.net/"+os.getenv('MONGO_DATABASE')+"?retryWrites=true&w=majority")
db = client.crypto
collection = db.solana
requesting = []

for i in range(2):
    # get data
    response = requests.get("https://api.cryptorank.io/v0/coins/"+coin+"/chart/history?fromTs="+str(utc_start)+"&toTs="+str(utc_end))

    res = response.json()

    # remove unneeded data
    res = res["data"]
    res.pop("BTC", None)
    res.pop("ETH", None)
    
    date = datetime.utcfromtimestamp(utc_start/1000).strftime("%Y-%m-%d")

    # if you want to write to file uncomment this
    # f = open("data/"+str(date)+".json", "w")
    # f.write(json.dumps(res))
    # f.close()

    # add entry to send to mongo
    res["_id"] = str(date)
    requesting.append(InsertOne(res))
    
    print(datetime.utcfromtimestamp(utc_start/1000), " : ", utc_start)

    utc_start += 86400000
    utc_end = utc_start+86400000


    time.sleep(.4)
print(utc_end)

# send all entries to mongo
result = collection.bulk_write(requesting)
client.close()