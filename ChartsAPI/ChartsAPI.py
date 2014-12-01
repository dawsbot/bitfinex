# Python implementation. Written by Dawson Botsford - 2014. Distributed under).v. 0.0.1-4]
# report ANY bug @ https://github.com/dawsonbotsford/bitfinex/issues

import requests
import time
import matplotlib.pyplot as plt

__all__ = ['trades']

URL = "http://api.bitcoincharts.com/v1/trades.csv?symbol=bitfinexUSD&start="

#unixtime,price,amount
def trades(timeSince): # gets the innermost bid and asks and information on the most recent trade.
  adjustedTime = int(time.time()) - timeSince
  response = requests.get(URL + str(adjustedTime))
  splitResponse = response.text.splitlines()
  prices = []
  timestamps = []
  amounts = [] 
  mymax = 0
   
  for i,line in enumerate(splitResponse):
    splitline = splitResponse[i].split(',') 
    timestamp = splitline[0] 
    #print "timestamp" + str(i) + ": " + str(timestamp)
    price = round(float(splitline[1]),2)
    #print "price" + str(i) + ": " + str(price)
    amount = splitline[2] 
    print "amount: " + str(amount)
    if mymax < amount:
       mymax = amount
    #print "comparing btc sizes of " + str(mymax) + " and " + str(amount)
    timestamps.append(float(timestamp))
    prices.append(float(price))
    amounts.append(float(amount)*5 )
    #amounts.append(float(amount) * 170 + 10)
  print "mymax: " + mymax
  plt.scatter(timestamps, prices, s=amounts, alpha=.2)
  plt.show()


#unixtime,price,amount
'''
  inputs:

    timeSince: the epoch length behind this moment you want to pull

'''
def sma(timeSince): # gets the innermost bid and asks and information on the most recent trade.
  adjustedTime = int(time.time()) - timeSince
  response = requests.get(URL + str(adjustedTime))
  splitResponse = response.text.splitlines()
  prices = []
  timestamps = []
  amounts = [] 
  mymax = 0
   
  for i,line in enumerate(splitResponse):
    splitline = splitResponse[i].split(',') 
    timestamp = splitline[0] 
    #print "timestamp" + str(i) + ": " + str(timestamp)
    price = round(float(splitline[1]),2)
    #print "price" + str(i) + ": " + str(price)
    amount = splitline[2] 
    print "amount: " + str(amount)
    if mymax < amount:
       mymax = amount
    #print "comparing btc sizes of " + str(mymax) + " and " + str(amount)
    timestamps.append(float(timestamp))
    prices.append(float(price))
    amounts.append(float(amount)*5 )
    #amounts.append(float(amount) * 170 + 10)
  print "mymax: " + mymax
  plt.scatter(timestamps, prices, s=amounts, alpha=.2)
  plt.show()
 
