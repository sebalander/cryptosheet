import cryptocompare
import datetime

print(cryptocompare.get_price('BTC', 'USD'))
# or
# print(cryptocompare.get_price('BTC',curr='USD',full=True))

# print(cryptocompare.get_coin_list(format=False))
# or
#print(cryptocompare.get_price(['BTC','ETH'],['EUR','GBP']))

# {'BTC': {'EUR': 3709.04, 'GBP': 3354.78},
#  'ETH': {'EUR': 258.1, 'GBP': 241.25}}


# pass either datetime or time instance
# print(cryptocompare.get_historical_price('BTC', timestamp=datetime.datetime(2018,3,11)))
# or
print(cryptocompare.get_historical_price('BTC', 'USD', datetime.datetime.now(tz=datetime.tzinfo(0))))
