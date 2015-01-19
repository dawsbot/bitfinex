#!/usr/bin/env python
# Python implementation. Written by Dawson Botsford - 2014. Distributed under).v. 0.0.1-4]
# report ANY bug @ https://github.com/dawsonbotsford/bitfinex/issues

import requests
import time

import datetime
import numpy as np


import calendar
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates

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

  fig = plt.figure()
  ax1 = plt.subplot(1,1,1)

  secs = mdates.epoch2num(timestamps)
  ax1.plot_date(secs, prices, 'k-', linewidth=.7)
  ax1.grid(True)
  plt.xlabel('Date')
  plt.ylabel('Bitcoin Price')

  #Choose your xtick format string
  #date_fmt = '%d-%m-%y %H:%M:%S'
  date_fmt = '%d-%m-%y %H:%M'

  #Use a DateFormatter to set the data to the correct format.
  date_formatter = mdates.DateFormatter(date_fmt)
  ax1.xaxis.set_major_formatter(date_formatter)

  #Tilt x-axis text to fit
  fig.autofmt_xdate()

  plt.show()

trades(100000)
