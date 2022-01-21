def short(amount, price):
    print(amount)
    print(price)

def buy_dollars(price, dollars):
    shares = dollars/price
    cost = -(price * shares)
    return [shares, cost]

def buy_shares(price, shares):
    return_amount = -(price * shares)
    return [shares, return_amount]

def sell_dollars(price, dollars):
    shares = -(dollars/price)
    return_amount = price * shares
    return [shares, return_amount]

def sell_shares(price, shares):
    return_amount = price * shares
    return [-shares, return_amount]