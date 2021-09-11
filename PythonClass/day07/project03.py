import pybithumb
import datetime

# tickers = pybithumb.get_tickers()
# print(len(tickers))

# print(pybithumb.get_current_price("BTC"))

# detail = pybithumb.get_market_detail("BTC")
# print(detail)

# orderbook = pybithumb.get_orderbook("BTC")
# print(orderbook)

# print(orderbook['payment_currency'])
# print(orderbook['order_currency'])

# ms = int(orderbook['timestamp'])

# dt = datetime.datetime.fromtimestamp(ms/1000)
# print(dt)

# bids = orderbook['bids']
# asks = orderbook['asks']
# print(bids)
# print(asks)

orderbook = pybithumb.get_orderbook("BTC")
bids = orderbook['bids']

for bid in bids:
    print(bid)