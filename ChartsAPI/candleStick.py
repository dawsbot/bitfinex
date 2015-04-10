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
from matplotlib.finance import candlestick

__all__ = ['trades']

#CSV endpoint where transaction history exists
URL = "http://api.bitcoincharts.com/v1/trades.csv?symbol=bitfinexUSD&start="

#unixtime,price,amount
def trades(timeSince): # gets the innermost bid and asks and information on the most recent trade.
  adjustedTime = int(time.time()) - timeSince
  response = requests.get(URL + str(adjustedTime))
  print "\nLooking back until ",adjustedTime
  splitResponse = response.text.splitlines()
  prices = []
  timestamps = []
  amounts = [] 

  lowp = []
  highp = []
  openp = []
  closep = []
   
  #Only keep one of each 30 lines
  #splitResponse = splitResponse[::30]  

#Generate arrays for timestamp, price, and price
  for i,line in enumerate(splitResponse):
    splitline = splitResponse[i].split(',') 
    timestamp = splitline[0] 
    price = round(float(splitline[1]),2)
    amount = splitline[2] 
    times = []
    vols = [] 
    timestamps.insert(0, float(timestamp))
    prices.insert(0,float(price))
    amounts.insert(0, float(amount))

  currentTime = timestamps[0]
  targetTime = currentTime - (currentTime % 60)
  currentHigh = prices[0]
  currentLow = prices[0]

  for i,element in enumerate(timestamps):
    if (i == len(timestamps) - 1): #Stop one early so we don't go over bounds
      break
    if (currentHigh < prices[i]):
      currentHigh = prices[i]
    else:
      if (currentLow > prices[i]):
        currentLow = prices[i]
    if timestamps[i+1] < targetTime:
      times.append(targetTime)
      openp.append(prices[i])
      closep.append(prices[i+1])
      highp.append(currentHigh)
      lowp.append(currentLow)
      vols.append(amounts[i])
      targetTime -= 60 #Look at open/close of next minute
      currentLow = prices[i+1]
      currentHigh = prices[i+1]

  candleAr = []
  for i, element in enumerate(times):
    appendLine = mdates.epoch2num(times[i]), openp[i], closep[i], highp[i], lowp[i]
    candleAr.append(appendLine)


  fig = plt.figure()

  #Generate first price chart (on top)
  #ax1 = plt.subplot(2,1,1)
  ax1 = plt.subplot(1,1,1)
  candlestick(ax1, candleAr, width = .0005, colorup='g', colordown='r')

  ax1.grid(True)
  plt.xlabel('Date')
  plt.ylabel('Bitcoin Price')
  '''
  #Generate second price chart (on bottom)
  ax2 = plt.subplot(2,1,2, sharex=ax1)
  ax2.plot(secs, amounts)
  ax2.grid(True)
  plt.ylabel('Volume')
  '''

  #Use a DateFormatter to set the data to the correct format.
  #Choose your xtick format string
  #date_fmt = '%d-%m-%y %H:%M:%S'
  date_fmt = '%H:%M'
  date_formatter = mdates.DateFormatter(date_fmt)
  ax1.xaxis.set_major_formatter(date_formatter)

  #Tilt x-axis text to fit
  fig.autofmt_xdate()
  ax1.autoscale_view()

  plt.show()

trades(4500)
