# Bitfinex

Python scripts for the [Bitfinex](https://www.Bitfinex.com/) exchange.
Use this to learn about algorithmic trading on the Bitcoin market.<br>

⚠️  Searching for co-owners on this project. Bitfinex is no longer available to US residents and I cannot execute the code on my account any longer. Please open an issue to help.   


## Install

```sh
$ pip install -r requirements.txt
$ sudo python setup.py install
```

## Keys

Create file ```keys.txt``` in the main directory with the following syntax:

    public key
    private key
    [insert newline here]

## Funds

Ensure you have at least 0.01 BTC in your <b>exchange</b> wallet <br>
The scripts are configured for this wallet and not your <b>trading</b> wallet

## Contents

```/examples/putTake.py``` places a put and take on each side of the market value.<br>
```/examples/cancelAll.py``` cancels all orders in your exchange account.<br>
```/examples/showPastTrades.py``` creates a visualization of past trades. Below is a screenshot. <br>

Here is a vis of my trade history on Bitfinex. 
(The smallest dots were performed by execution of ```/examples/putTake.py```)

<br>

![screenshot](http://i.imgur.com/8PBxnvZ.png)

In using this software, you take full responsibility of the results.

Hard forked from [jndok](http://jndok.net/bitfinexapi.html)
