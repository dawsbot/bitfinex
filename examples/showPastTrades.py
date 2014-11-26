#!/usr/bin/env python
import FinexAPI
import matplotlib.pyplot as plt

timestamps = []
prices = []
colors = []

myvar = FinexAPI.past_trades()

for obj in myvar:
	prices.append(obj["price"])
	timestamps.append(obj["timestamp"])
	if (obj["type"] == "Sell"):
		colors.append("red")
	else:
		colors.append("green")
		

	print "price: " + str(obj["price"]) + " type: " + str(obj["type"])

plt.scatter(timestamps, prices, s=300, c=colors, alpha=.7)
plt.show()
