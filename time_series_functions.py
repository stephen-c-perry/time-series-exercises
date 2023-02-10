import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import timedelta, datetime


############################################################
########### Plotting Viz for Time Series Analysis ##########
############################################################


#basic histogram
def hist(target):
    [target].plot.hist()   



#Bar Chart by Month
def bar_month(target, title=None, xlabel= None, ylabel= None):
    ax = [target].groupby([target].index.month).mean().plot.bar(width=.9, ec='black')
    plt.xticks(rotation=0)
    ax.set(title= title, xlabel=xlabel, ylabel=ylabel)



#Bar Chart by Day
#not working
def bar_day(target, title=None, xlabel= None, ylabel= None):
    ax = [target].groupby([target].index.day_name).mean().plot.bar(width=.9, ec='black')
    plt.xticks(rotation=0)
    ax.set(title= title, xlabel=xlabel, ylabel=ylabel)


#AVG per week
# tested and works
def line_avg_week(target, title= None):
    [target].resample('W').mean().plot(title= title)


#Compare Averages by Hour, Day, Week, Month, Year

def line_avg_comparisons(target, title=None):
    [target].plot(alpha=.2, label='Hourly', title= title)
    [target].resample('D').mean().plot(alpha=.5, label='Daily')
    [target].resample('W').mean().plot(alpha=.8, label='Weekly')
    [target].resample('M').mean().plot(label='Montly')
    [target].resample('Y').mean().plot(label='Yearly')
    plt.legend()



# Variance in average per week

def line_variance_week(target, title=None):
    [target].resample('W').mean().diff().plot(title= title) #Orange line
    [target].resample('M').mean().diff().plot() #Blue line


# Seasonal Plot

def seasonal_line_plot(target, title=None, xlabel=None, ylabel= None):
    [target].groupby([[target].index.year, [target].index.month]).mean().unstack(0).plot(title= title, xlabel= xlabel, ylabel= ylabel)


