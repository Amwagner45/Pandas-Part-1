import pandas as pd
import numpy as np


'''
Part A:
    In this project, we would like to create a portfolio of 3 cryptocurrencies (BTC, ETH, and ADA) 
    and 3 stock (AMZN, TSLA, and APPL). Using Pandas, perform the following:
'''

'''
1. Using Yahoo Finance, search foro the current closing price of the aforementioned list of cryptos and stocks
2. Create a Python dictionary that lists the ticker symbol (Keys) and prices (values)
'''
portfolio = {'BTC':  43500,
             'ETH':  3200,
             'ADA':  1,
             'AAPL': 171,
             'TSLA': 1000, 
             'AMZN': 3175}
print(portfolio)

'''
3. Create a Pandas Series from a dictionary to showo the cryptos/stocks ticker symbols and their corresponding prices
'''
my_portfolio_series = pd.Series(portfolio)

'''
4. Assume that you have the following number of assets in your portfolio: BTC = 3, ETH = 10, ADA = 1000, AMZN = 20,
TSLA = 20, AAPL = 5. Create a new Pandas series that contains these number of securities. Use the ticker symbols as the
Pandas series labels
'''
number_securities = pd.Series(data = [10, 5, 2, 4, 5, 6],  index = ['BTC', 'ETH', 'ADA', 'AAPL', 'TSLA', 'AMZN'])

'''
5. Multiply the number of securities by the price of each security. Calculate the total value of the portfolio including
all securities
'''
Total_dollar_value = my_portfolio_series.mul(number_securities)
print(Total_dollar_value)

print('Total portfolio Value = ${}'.format(Total_dollar_value.sum()))


'''
PART B:
    Using the attaced "S&P500_Prices.csv", perform the following:
'''

'''
1. Using Pandas, read the csv file into Pandas DataFrame. Check the datatype.
'''
sp500 = pd.read_csv('S&P500_Prices.csv')
type(sp500)

'''
2. Using Pandas, read the csv file into a Pandas Series. Check the datatype.
'''
sp500 = pd.read_csv('S&P500_Prices.csv', squeeze = True)

type(sp500)

'''
3. Obtain the maximum, minimum and average values of the S&P500.
'''
len(sp500)

max(sp500)

min(sp500)

sp500.mean()

'''
4. Sort the Pandas Series in an ascending and descending order. Enforce the change in memory.
'''
sp500.sort_values(inplace = True) 

sp500.sort_index(inplace = True)

sp500.sort_values(ascending = False, inplace = True) 


'''
5. Use describe() method to obtain a statistical summary of S&P500. What is the standard deviation?
'''
descriptive_stats = sp500.describe()
standard_deviation = descriptive_stats[2]
print(f"The standard deviation is {standard_deviation}")

'''
6. With and without rounding the series to the nearest integer, search for the price 3349.
'''
3349 in sp500.values

sp500 = round(sp500)
