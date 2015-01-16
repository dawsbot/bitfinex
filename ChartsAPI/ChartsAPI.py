# Python implementation. Written by Dawson Botsford - 2014. Distributed under).v. 0.0.1-4]
# report ANY bug @ https://github.com/dawsonbotsford/bitfinex/issues

import requests
import time
import calendar
import matplotlib.pyplot as plt

__all__ = ['trades']

#CSV endpoint where transaction history exists
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

  #Only keep one of each 30 lines
  splitResponse = splitResponse[::30]  

  for i,line in enumerate(splitResponse):
    splitline = splitResponse[i].split(',') 
    timestamp = splitline[0] 
    price = round(float(splitline[1]),2)
    amount = splitline[2] 
    #print "amount: " + str(amount)
    if mymax < amount:
       mymax = amount
    timestamps.append(float(timestamp))
    prices.append(float(price))
    amounts.append(float(amount)*5 )
  #print "mymax: " + mymax
  #plt.scatter(timestamps, prices, s=amounts, alpha=.2)
  plt.plot(timestamps, prices, 'k-', linewidth=.7)
  plt.show()

#unixtime,price,amount
'''
  inputs:

    timeSince: the epoch length behind this moment you want to pull
    
'''
#unixtime,price,amount
def sma(timeSince): # gets the innermost bid and asks and information on the most recent trade.
  adjustedTime = int(time.time()) - timeSince
  response = requests.get(URL + str(adjustedTime))
  splitResponse = response.text.splitlines()
  prices = []
  timestamps = []
  amounts = [] 
  mymax = 0

  #Only keep one of each 30 lines
  splitResponse = splitResponse[::30]  

  
  for i,line in enumerate(splitResponse):
    splitline = splitResponse[i].split(',') 
    timestamp = splitline[0] 
    price = round(float(splitline[1]),2)
    amount = splitline[2] 
    #print "amount: " + str(amount)
    if mymax < amount:
       mymax = amount
    timestamps.append(float(timestamp))
    prices.append(float(price))
    amounts.append(float(amount)*5 )
  #print "mymax: " + mymax
  #plt.scatter(timestamps, prices, s=amounts, alpha=.2)
  plt.plot(timestamps, prices, 'k-', linewidth=.7)
  plt.show()

'''
  inputs:

    splitResponse: Full string of transactions 
    timeStamp: the epoch time closest you want a transaction of
    
'''
def get_transaction(splitResponse, timeStamp):
  time = calendar.timegm(time.gmtime()) - 10   
  
