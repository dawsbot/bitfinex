Bitfinex
========
Open source ripped and changed from [Original Author: jndok](http://jndok.net/bitfinexapi.html)<br>
Python scripts for the [Bitfinex](https://www.Bitfinex.com/) Bitcoin exchange.
Open sourced development and learning about algorithmic trading on the Bitcoin market.<br>


# Install
```pip install -r requirements.txt```<br>
```sudo python setup.py install```

#Keys
Create file ```keys.txt``` in the main directory with the following syntax:

    public key
    private key
    [insert newline here]

#Funds
Ensure you have at least 0.01 BTC in your <b>exchange</b> wallet <br>
The scripts are configured for this wallet and not your <b>trading</b> wallet

#Contents
```/examples/putTake.py``` places a put and take on each side of the market value.<br>
```/examples/cancelAll.py``` cancels all orders in your exchange account.<br>
```/examples/showPastTrades.py``` creates a visualization of past trades. Below is a screenshot. <br>

Here is a vis of my trade history on Bitfinex. (The smallest dots were performed by execution of ```/examples/putTake.py```)<br>
![screenshot](http://i.imgur.com/8PBxnvZ.png)

<b>If donating is your kind of thing: 14Gp132H9r2jUEre2TYZuVLTk5VEneBoKX</b>

If you like what you see let me know and I will continue contributing to this.<br>
In using this software, you take full responsibility of the results.
