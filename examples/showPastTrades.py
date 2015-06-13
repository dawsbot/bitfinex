#!/usr/bin/env python
import FinexAPI
import matplotlib.pyplot as plt

timestamps = []
prices = []
colors = []
amounts = []

myvar = FinexAPI.past_trades()
#print myvar

for obj in myvar:
  price = obj["price"]
  prices.append(price)
  timestamps.append(obj["timestamp"])
  amounts.append(float(obj["amount"]) * 170 + 10)
  if (obj["type"] == "Sell"):
    colors.append("red")

  else:
    colors.append("green")


  print str(obj["type"] + " " + str(obj["amount"]) + "BTC at " + str(obj["price"]))

plt.scatter(timestamps, prices, s=amounts, c=colors, alpha=.6)
plt.show()
