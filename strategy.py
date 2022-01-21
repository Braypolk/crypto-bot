
# 300000 = 5 min in unix time

# strategy 1: buy at midnight, sell at 3:30ish

# Based on certain factors a decicion to buy/sell/nothing will be made

from datetime import datetime, timedelta
from actions import *

def strat1(account, data, i, time):

    date = datetime.strptime(datetime.utcfromtimestamp(time/1000).strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S") - timedelta(hours=6)

    # at around midnight short position with half of amount 
    if i == 0:
        transaction = sell_dollars(data, account["balance"]/2)
        account["shares"] += transaction[0]
        account["balance"] += transaction[1]

        return account
        
    # buy back all shares when time is around 3:30
    elif  date.time() > datetime.strptime("03:30:00", "%H:%M:%S").time() and date.time() < datetime.strptime("6:30:00", "%H:%M:%S").time() :
        transaction = buy_shares(data, account["shares"])
        account["shares"] += transaction[0]
        account["balance"] += transaction[1]

        return account