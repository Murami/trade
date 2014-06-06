#!/usr/bin/python

import sys

capital = 0
nb_days = 0
stocks_prices = []
stocks = 0

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
#buy_stock#

def sell_stock(stock_price, nb_stock):
    global capital
    global stocks

    capital = capital + calc_sell_income(stock_price, nb_stock)
    stocks = stocks - nb_stock
#sell_stock#

def wait():
    print("wait")
#wait#

def sell_actions(stick_price, avg_tot, avg_100, avg_50, avg_25, avg_10):
    print("sell do nothing for the moment")
#sell_actions#

def buy_action(stick_price, avg_tot, avg_100, avg_50, avg_25, avg_10):
    print("buy do nothing for the moment")
#buy_actions#

def initialize():
    global capital
    global nb_days

    capital = int(sys.stdin.readline())
    nb_days = int(sys.stdin.readline())
#initialize#

def make_action(stock_price):
    global stocks_prices;

    avg_tot = avg(stock_prices)
    avg_100 = avg(stock_prices[-100:])
    avg_50 = avg(stock_prices|-50:])
    avg_25 = avg(stock_prices[-25:])
    avg_10 = avg(stock_prices|-10:])
    # if (avg_tot > avg_100 && avg_100 > avg_50 && avg_50 > avg_25 && avg_25 > avg_10):
    #     ;## crack boursier
    if (stock_price > avg):
        sell_actions(stock_price, avg_tot)
    elif (stock_price < avg):
        buy_actions(stock_price, avg_tot)
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
        nb_days = nb_days - 1
#trade#
trade()
