#!/usr/bin/env python
import FinexAPI

myvar = FinexAPI.past_trades(0)

for obj in myvar:
	print "price: " + str(obj["price"]) + " type: " + str(obj["type"])
