#!/usr/bin/env python
import FinexAPI
import matplotlib.pyplot as plt

timestamps = []
prices = []
colors = []
amounts = []
profit = 0

myvar = FinexAPI.past_trades()
#print myvar

for obj in myvar:
  price = obj["price"]
  prices.append(price)
  timestamps.append(obj["timestamp"])
  amounts.append(float(obj["amount"]) * 170 + 10)
  if (obj["type"] == "Sell"):
    colors.append("red")
    profit = profit + float(obj["amount"]) * float(price)

  else:
    colors.append("green")
    profit = profit - float(obj["amount"]) * float(price)
    

  print str(obj["type"] + " " + str(obj["amount"]) + "BTC at " + str(obj["price"]))

print "\nYour unrealized potential profit: " + str(profit) + " USD"
plt.scatter(timestamps, prices, s=amounts, c=colors, alpha=.6)
plt.show()
