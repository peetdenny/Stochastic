import numpy as np
import monty.BitcoinChartsLoader as loader
import math
from scipy.stats import norm
import random


def set_pdr(data):
    # Add Periodic Daily Returns to column 3.
    # This column is currently occupied by the trading volume which we don't need, so let's overwrite that
    rows, cols = np.shape(data)
    for i in range(1, rows):
        pdr = math.log((data[i, 1] / data[i - 1, 1]))
        data[i, 2] = pdr


def calc_mean_pdr(data):
    return np.mean(data[1:, 2])  # ignore the first row, as it won't have a PDR value set


def calc_pdr_variance(data):
    return np.var(data[1:, 2])


def calc_std_dev(data):
    return np.std(data[1:, 2])


def model():
    data = loader.get_prices()
    set_pdr(data)
    mean = calc_mean_pdr(data)
    variance = calc_pdr_variance(data)
    std_dev = calc_std_dev(data)
    return data, mean, variance, std_dev


def get_price_for_today(yesterday_price, mean, variance, std_dev):
    drift = mean - (variance/2)
    return yesterday_price * math.exp(drift + (std_dev * norm.ppf(random.random())))


def forecast():
    data, mean, variance, std_dev = model()
    price = data[np.shape(data)[0]-1,:][1]
    print("Yesterday's price was $%d/BTC" % price)
    for day in range(1,10):
        price = get_price_for_today(price, mean, variance, std_dev)
        print("Price forecast for day +%d is $%d" % (day, price))


forecast()
