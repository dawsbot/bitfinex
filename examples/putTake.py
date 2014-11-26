#!/usr/bin/env python
#Places a put and take 2btc above and 1btc last price
import FinexAPI

diff = 2 #The amount above or below you want
amount = "0.01"

marketPrice = FinexAPI.ticker()["last_price"]
buyPrice = float(marketPrice) - diff
sellPrice = float(marketPrice) + diff

print FinexAPI.place_order(amount, str(buyPrice), "buy", "exchange limit")
print FinexAPI.place_order(amount, str(sellPrice), "sell", "exchange limit")
