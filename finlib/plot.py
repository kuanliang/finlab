import pandas_datareader as pdr
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
from matplotlib import style
style.use('ggplot')

def graph_data(stock):
    
    
    stock_data = pdr.get_data_google(stock)
    
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    
    ax1.plot(stock_data.index, stock_data['Close'])
    ax1.plot([], [], label='loss', color='r', linewidth=5)
    ax1.plot([], [], label='gain', color='g', linewidth=5)
    
    ax1.fill_between(stock_data.index, stock_data['Close'], stock_data['Close'][0], 
                     where=(stock_data['Close'] > stock_data['Close'][0]), facecolor='g', alpha=0.4)
    ax1.fill_between(stock_data.index, stock_data['Close'], stock_data['Close'][0],
                     where=(stock_data['Close'] < stock_data['Close'][0]), facecolor='r', alpha=0.4)
    
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    
    ax1.grid(True)
    #ax1.xaxis.label.set_color('c')
    #ax1.yaxis.label.set_color('r')
    #ax1.set_yticks([0, 25, 50, 75])
    
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    plt.legend()
    

        
    plt.show()
    
    
def plot_ohlc(stock, mov_avg):
    '''plot ohlc graph 
    
    Args:
        stock (string): stock name in string format, e.g, 'NVDA', 'GOOGL'
        mov_avg (int): the range used to calculate moving average
        start (string):
        stop (string):
        
    Return:
        matplotlib graph
    
    Notes:
    
    '''
    
    stock_data = pdr.get_data_google(stock)
    
    
    stock_data[str(mov_avg)] = np.round(stock_data["Close"].rolling(window = mov_avg, center = False).mean(), 2)
    
    
    # stock_data['Date'] = stock_data.index
    time_stamp = mdates.date2num(stock_data.index.to_pydatetime())
    # drop the date index from the dataframe
    stock_data.reset_index(inplace=True)
    stock_data['Date'] = time_stamp
    
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))
    
    
    # x = 0
    # y = len(stock_data)
    
    # while x < y:
     #   append_me = 
    
    #ax1.xaxis.label.set_color('c')
    #ax1.yaxis.label.set_color('r')
    #ax1.set_yticks([0, 25, 50, 75])
    
    candlestick_ohlc(ax1, stock_data.values, width=0.4, colorup='#77d879', colordown='#db3f3f')
    
    
    if mov_avg != None:
        ax1.plot(stock_data['Date'], stock_data[str(mov_avg)])
    
    
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
        
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    
    
    
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(stock)
    # plt.legend()
    

    plt.show()

