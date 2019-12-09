import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy
import datetime as dt


def set_dates():
    syear, smonth, sday = (
        input('provide starting year,month,day:').split(','))
    syear, smonth, sday = int(syear), int(smonth), int(sday)
    eyear, emonth, eday = input('provide ending year,month,day:').split(',')
    eyear, emonth, eday = int(eyear), int(emonth), int(eday)
    start = dt.datetime(syear, smonth, sday)
    end = dt.datetime(eyear, emonth, eday)
    return start, end


def read_data(format,stock,source,start,end):
    all_data = web.DataReader(stock, source, start, end)
    all_data.to_csv(format)
    all_data = pd.read_csv(format, parse_dates=True, index_col=0)
    return all_data


def plot_graph(df,stock):
    df[['Open', 'High']].plot()
    plt.title(stock + ' Stock')
    plt.ylabel('USD $')
    plt.xlabel('Date')
    plt.show()


def show_result(stock, source='yahoo'):
    format = stock + '.csv'
    start, end = set_dates()
    all_data = read_data(format,stock,source,start,end)
    plot_graph(all_data,stock)


show_result('AMZN')
