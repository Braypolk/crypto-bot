import pymongo, json, os
from pymongo import MongoClient, InsertOne
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient("mongodb+srv://"+os.getenv('MONGO_USER')+":"+os.getenv('MONGO_PASS')+"@cluster0.8ttfr.mongodb.net/"+os.getenv('MONGO_DATABASE')+"?retryWrites=true&w=majority")
db = client.crypto
collection = db.solana
requesting = []

for filename in os.listdir(os.path.join(os.getcwd(), "data")):
    with open(os.path.join(os.path.join(os.getcwd(), "data"), filename), 'r') as f:
        for jsonObj in f:
            myDict = json.loads(jsonObj)
            myDict["_id"] = os.path.splitext(filename)[0]
            requesting.append(InsertOne(myDict))

result = collection.bulk_write(requesting)
client.close()