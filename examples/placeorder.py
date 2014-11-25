#!/usr/bin/env python
import FinexAPI

print FinexAPI.place_order("0.01", "500.0", "sell", "exchange limit")
