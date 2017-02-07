import datetime
import random
import matplotlib.pyplot as plt
# make up some data


def plotDate(trades):
    x_g = []
    y_g = []

    x_f = []
    y_f = []
    for trade in trades:
        if(trade.getFraud()):
            date = datetime.datetime.strptime(trade.getTradeDate(),"%Y-%m-%d %H:%M:%S")
            x_f.append(date)
            y_f.append(0.5)
        else:
            date = datetime.datetime.strptime(trade.getTradeDate(),"%Y-%m-%d %H:%M:%S")
            x_g.append(date)
            y_g.append(0.5)
    # plot
    plt.plot(x_f,y_f,'ro')
    plt.plot(x_g,y_g,'bx')
    # beautify the x-labels
    plt.gcf().autofmt_xdate()
    plt.show()
    return x_g,x_f
