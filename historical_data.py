import requests, json, time
from datetime import datetime

utc_start = 1629176400000 # example 1641016800000 = 1/1/22 midnight trailing 0's required
utc_end = utc_start+86400000
coin = "solana"

for i in range(61):
    # get data
    response = requests.get("https://api.cryptorank.io/v0/coins/"+coin+"/chart/history?fromTs="+str(utc_start)+"&toTs="+str(utc_end))

    res = response.json()

    # remove unneeded data
    res = res["data"]
    res.pop("BTC", None)
    res.pop("ETH", None)
    
    date = datetime.utcfromtimestamp(utc_start/1000).strftime("%Y-%m-%d")

    # write to file
    f = open("data/"+str(date)+".json", "w")
    f.write(json.dumps(res))
    f.close()
    
    print(datetime.utcfromtimestamp(utc_start/1000), " : ", utc_start)

    utc_start += 86400000
    utc_end = utc_start+86400000


    time.sleep(.4)
print(utc_end)