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

#unixtime,volume,amount
def trades(timeSince): # gets the innermost bid and asks and information on the most recent trade.
  adjustedTime = int(time.time()) - timeSince
  response = requests.get(URL + str(adjustedTime))
  splitResponse = response.text.splitlines()
  volumes = []
  timestamps = []
  amounts = [] 

  lowp = []
  highp = []
  openp = []
  closep = []
   
  #Only keep one of each 30 lines
  #splitResponse = splitResponse[::30]  

  print "First entry to splitResponse ", splitResponse[0]
#Generate arrays for timestamp, volume, and volume
  for i,line in enumerate(splitResponse):
    splitline = splitResponse[i].split(',') 
    timestamp = splitline[0] 
    volume = round(float(splitline[1]),2)
    amount = splitline[2] 
    times = []
    vols = [] 
    #print "appending timestamp ", timestamp
    '''
    timestamps.append(float(timestamp))
    volumes.append(float(volume))
    amounts.append(float(amount))
    '''
    timestamps.insert(0, float(timestamp))
    volumes.insert(0,float(volume))
    amounts.insert(0, float(amount))

  #currentTime = calendar.timegm(time.gmtime())
  currentTime = timestamps[0]
  print "time remainder: ", (currentTime % 60)
  targetTime = currentTime - (currentTime % 60)
  print "current time: ", currentTime
  print "closest minute epoch: ", targetTime

  currentHigh = timestamps[0]
  currentLow = timestamps[0]

  for i,element in enumerate(timestamps):
    #print "inside for loop at timestamp", element
    if (i == len(timestamps) - 1): #Stop one early so we don't go over bounds
      break
    if (currentHigh < element):
      currentHigh = element
    else:
      if (currentLow > element):
        currentLow = element
    #print "timestamps[i], +1: ", timestamps[i], ", ", timestamps[i+1]
    if timestamps[i] > targetTime and timestamps[i+1] < targetTime:
      times.append(timestamps[i])
      openp.append(timestamps[i])
      closep.append(timestamps[i+1])
      highp.append(currentHigh)
      lowp.append(currentLow)
      vols.append(volumes[i])
      print "\n\nclose: ", timestamps[i], " open: ", timestamps[i+1] 
      targetTime -= 60 #Look at open/close of next minute
      currentLow = timestamps[i+1]
      currentHigh = currentLow

  candleAr = []
  for i, element in enumerate(times):
    appendLine = mdates.epoch2num(times[i]), openp[i], closep[i], highp[i], lowp[i], vols[i]
    candleAr.append(appendLine)


  fig = plt.figure()

  #Generate first volume chart (on top)
  ax1 = plt.subplot(2,1,1)
  secs = mdates.epoch2num(timestamps)
  candlestick(ax1, candleAr, width=1, colorup='g', colordown='r')
  #ax1.plot_date(secs, volumes, 'k-', linewidth=.7)

  ax1.grid(True)
  plt.xlabel('Date')
  plt.ylabel('Bitcoin Price')

  #Generate second volume chart (on bottom)
  ax2 = plt.subplot(2,1,2, sharex=ax1)
  ax2.plot(secs, amounts)
  ax2.grid(True)
  plt.ylabel('Volume')

  #Use a DateFormatter to set the data to the correct format.
  #Choose your xtick format string
  #date_fmt = '%d-%m-%y %H:%M:%S'
  date_fmt = '%d %H:%M'
  date_formatter = mdates.DateFormatter(date_fmt)
  ax1.xaxis.set_major_formatter(date_formatter)

  #Tilt x-axis text to fit
  fig.autofmt_xdate()

  plt.show()

trades(1290)
