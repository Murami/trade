#!/usr/bin/python

import sys

factor_main = 1
factor_sell = 0.1
factor_buy = 0.0001
capital = 0
capital_start = 0
nb_days = 0
nb_days_total = 0
stocks_prices = []
stocks = 0

## AU DERNIER JOUR ON RENVEND TOUTES NOS ACTIONS

def avg(l):
    return sum(l) / float(len(l))
#avg#

def calc_commision(stock_price, nb_stock) :
    return ceil(nb_stock * stock_price * 0.15)
#calc_commision#

def calc_buy_outcome(stock_price, nb_stock) :
    return (nb_stock * stock_price + calc_commision(stock_price, nb_stock))
#calc_buy_outcome#

def calc_sell_income(stock_price, nb_stock) :
    return (stock_price * nb_stock - calc_commision(stock_price, nb_stock))
#calc_sell_income#

def buy_stock(stock_price, nb_stock):
    global capital
    global stocks

    capital = capital - calc_buy_outcome(stock_price, nb_stock)
    stocks = stocks + nb_stock
    print("buy " + str(nb_stock))
#buy_stock#

def sell_stock(stock_price, nb_stock):
    global capital
    global stocks

    capital = capital + calc_sell_income(stock_price, nb_stock)
    stocks = stocks - nb_stock
    print("sell " + str(nb_stock))
#sell_stock#

def wait():
    print("wait")
#wait#

def safe_sell(stock_price, nb_stock):
    global capital
    global stocks

    if (ammount == 0):
        wait()
    else:
        commision_unit = 0.15 * float(stock_price)
        sell_capacity = int(float(capital) / float(commision_unit))
        
#safe_sell#

def safe_buy(stock_price, nb_stock):
    global capital
    global stocks
#safe_buy#

def sell_actions(stock_price, avg_price):
    variation = float(abs(avg_price - stock_price)) / float(avg_price)
    factor = 1 - float(nb_days) / float(nb_days_total)
    ammount = int(factor_main * factor_sell * factor * variation * capital_start)
    safe_sell(stock_price, ammount)
#sell_actions#

def buy_actions(stock_price, avg_price):
    variation = float(abs(avg_price - stock_price)) / float(avg_price)
    factor = float(nb_days) / float(nb_days_total)
    ammount = int(factor_main * factor_buy * factor * variation * capital * capital_start)
    safe_buy(stock_price, ammount)
#buy_actions#

def initialize():
    global capital
    global nb_days
    global nb_days_total
    global capital_start

    capital = int(sys.stdin.readline())
    capital_start = capital
    nb_days = int(sys.stdin.readline())
    nb_days_total = nb_days
#initialize#

def make_action(stock_price):
    global stocks_prices;

    avg_price = avg(stocks_prices[-50:])
    if (stock_price > avg_price):
        sell_actions(stock_price, avg_price)
    elif (stock_price < avg_price):
        buy_actions(stock_price, avg_price)
    else:
        wait();
#make_action#

def trade():
    global capital
    global stocks
    global nb_days
    global stocks_prices;

    initialize()
    while nb_days > 0:
        stock_price = int(sys.stdin.readline()[:-1])
        stocks_prices.append(stock_price)
        make_action(stock_price)
        nb_days = nb_days - 1
#trade#
trade()
