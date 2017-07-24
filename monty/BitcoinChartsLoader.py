import requests
import gzip
import shutil
import os
import time
import numpy as np


url = 'http://api.bitcoincharts.com/v1/trades.csv?symbol=krakenUSD'
filename = 'resource/krakenUSD.csv'
numpy_store_filename = 'resource/data.npy'


def get_price_data():
    if os.path.isfile(numpy_store_filename) and os.stat(numpy_store_filename).st_mtime > (time.time() - (24 * 3600)):
        print('Reusing file loaded within the last 24 hours')
        return np.load(numpy_store_filename)
    return None


def get_prices_from_remove_gzip_file():
    data = get_price_data()
    if data is not None:
        return data

    print('Downloading new file from %s' % url)
    zipped_filename = filename + '.gz'
    with open(zipped_filename, "wb") as f:
        r = requests.get(url)
        f.write(r.content)
    with gzip.open(zipped_filename, 'rb') as f_in:  # TODO refactor to do this in one step
        with open(filename, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    arr = np.genfromtxt(filename, delimiter=',')
    print('Saving data in numpy store')
    np.save(numpy_store_filename, arr)
    return arr


def get_prices_from_remote_csv():
    data = get_price_data()
    if data is not None:
        return data

    print('Downloading new file from %s' % url)
    with open(filename, "wb") as f:
        r = requests.get(url)
        f.write(r.content)
    arr = np.genfromtxt(filename, delimiter=',')
    print('Saving data in numpy store')
    np.save(numpy_store_filename, arr)
    return arr


def get_prices():
    return get_prices_from_remote_csv()
