import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
import numpy
import datetime as dt

# *************************************************** #
# FUNCTIONS #

def set_dates():
    syear,smonth,sday = (input('provide starting year,month,day:').split(','))
    syear, smonth, sday = int(syear),int(smonth),int(sday)
    eyear,emonth,eday = input('provide ending year,month,day:').split(',')
    eyear, emonth, eday = int(eyear),int(emonth),int(eday)
    start = dt.datetime(syear,smonth,sday)
    end = dt.datetime(eyear,emonth,eday)
    return start,end


def main(stock):
    print('welcome!')
    start,end = set_dates()
    df = web.DataReader(stock,'yahoo',start,end)
    if input('would you like to create an excel file? (yes/no):') == 'yes':
        df.to_csv(str(stock)+'.csv')
        df = pd.read_csv('')
        print('Success\n')
        if input('would you like to graph results? (yes/no') == 'yes':
                create_graph(str(stock)+'.csv')
                print('something went wrong')
        print('something went wrong')
    else:
        print('excel file was not created, stock is still available')
    return df


def create_graph(stockfile):
    df = pd.read_csv(stockfile, parse_dates=True, index_col=0)
    data_to_show = input('which data would you like to see?\n'
                         '1.Open\n'
                         '2.High\n')
    df[data_to_show].plot()
    plt.title(stockfile+'Stock')
    plt.ylabel('USD $')
    plt.xlabel('Date')
    plt.show()

#main('MSFT')
# ************************************************ #
# Trying things out
# pick stock
stock = 'AMZN'
source = 'yahoo'
# set time
start = dt.datetime(2019,1,1)
end = dt.datetime(2019,6,18)
# create stock + excel
df = web.DataReader(stock,source,start,end)
df.to_csv('amzn.csv')
df = pd.read_csv('amzn.csv',parse_dates=True,index_col=0)
#create graph
df[['Open','High']].plot()
plt.title('Amazon Stock')
plt.ylabel('USD $')
plt.xlabel('Date')
plt.show()
