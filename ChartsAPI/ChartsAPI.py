# Python implementation. Written by Dawson Botsford - 2014. Distributed under).v. 0.0.1-4]
# report ANY bug @ https://github.com/dawsonbotsford/bitfinex/issues

import requests
import json
import time

__all__ = ['trades']

URL = "http://api.bitcoincharts.com/v1/trades.csv?symbol="

#unixtime,price,amount
def trades(): # gets the innermost bid and asks and information on the most recent trade.
  response = requests.get(URL + "bitfinexUSD&start=1417337798")
  stringResponse = str(response.text.splitlines())
  
  splitline = stringResponse[0].split(',') 
  timestamp1 = splitline[0] 
  print "timestamp1: " + str(timestamp1)
  price1 = splitline[1]
    
  '''
	try:
		rep['last_price']
	except KeyError:
		return rep['message']

	return rep
  '''
