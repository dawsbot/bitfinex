#!/usr/bin/env python
#Places a put and take 2btc above and 1btc last price
import FinexAPI

diff = 2 #The amount above or below you want
ticker = FinexAPI.ticker()
available = float(FinexAPI.balances()[2]["available"])
ask = float(ticker["ask"]) 
amount = available/ask 

marketPrice = ticker["last_price"]
buyPrice = float(marketPrice) - diff
sellPrice = float(marketPrice) + diff

print FinexAPI.place_order(str(amount), str(buyPrice), "buy", "exchange limit")
print FinexAPI.place_order(str(amount), str(sellPrice), "sell", "exchange limit")
