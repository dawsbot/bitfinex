bitfinex
========
Open source ripped and changed from http://jndoksarchive.altervista.org/bitfinexapi.html <br>
Original Author: jndok <br>
Python scripts for the [Bitfinex](https://www.bitfinex.com/) Bitcoin exchange.


# Install
```pip install requirements.txt```<br>
```sudo python setup.py install```

#Keys
Create file ```keys.txt``` in the main directory with the following syntax:

    public key
    private key
    [insert newline here]

#Purpose
Open sourced deveopment and learning about algorithmic trading on the Bitcoin market.<br>
Feel free to use and modify anything here.<br>
```putTake.py``` is the most interest development file occuring here <br>
It takes the current market price and places a put and take on each side of the market value.

For fun, here is a little vis of my trade history on BitFinex. (The smallest dots were indeed performed by execution of the file ```/examples/putTake.py```)<br>
Create this for your account by executing ```/examples/showPastTrades.py```<br>
![screenshot](http://i.imgur.com/8PBxnvZ.png)

As always, you take responsibility for everything you do with this code. I am not liable for any losses or gains.
