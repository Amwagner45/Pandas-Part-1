import pandas as pd

'''
DEFINE PANDAS SERIES
'''
#Defining list of cryptocurrencies I am interested in analyzing
crypto_list = ['BTC', 'XRP',  'LTC', 'ADA', 'ETH']

#Checking the data type of the created list
type(crypto_list)

#Converting the list into a Pandas data Series
#Pandas Series contain only 1 column of data
#Conversely, a Pandas DataFrame is a multidimensional Pandas framework with multiple columns
crypto_series = pd.Series(data = crypto_list)

#Checking the data type of the created Pandas Series
type(crypto_series)

#Creating an additional Series to contain the prices of cryptocurrencies
crypto_prices_series = pd.Series(data = [2000, 500, 2000, 20, 50])

#Creating a list of Stocks to compare against cryptocurrencies
stock_series = pd.Series(data = ['TSLA', 'AAPL', 'AMD'])


'''
DEFINE PANDAS SERIES USING CUSTOM INDEX
'''
#Defining list of labels to replace default index number
crypto_labels = ['crypto#1', 'crypto#2', 'crypto#3', 'crypto#4', 'crypto#5']

#Re-Defining the crypto_series using custom index labels we defined previously.
crypto_series = pd.Series(data = crypto_list, index = crypto_labels)


'''
DEFINE PANDAS SERIES FROM DICTIONARY
'''
#Creating Python Dictionary using Stock information
stocks = {
    'TSLA': 895,
    'AAPL': 158,
    'AMD': 86
}

#Re-Defining stock_series using a predefined dictionary
#Do not need to use "data=" argument when creating a Series using Dictionary
stock_series = pd.Series(stocks)

'''
PANDAS ATTRIBUTES
'''
#Each Pandas Series has attributes one can access. 
#The code below obtains the values in the given Pandas Series
crypto_series.values

#Returns index/axis labels of the Series
crypto_series.index

#Returns the datatype of the Series
#For Example, the output of this code results in 'O' for Object
crypto_series.dtype

#Returns True if all elements within Series are unique, vice versa.
crypto_series.is_unique

#Used to check the shape/dimensions of the Series
#In this case, a Pandas Series is one-dimentsional
crypto_series.shape


'''
PANDAS METHODS
'''
#Pandas also has built in methods which are denoted by parentheses
#The code below will add up all the values within the Series
crypto_prices_series.sum()

#Returns result of all values within a Series multiplied together
crypto_prices_series.product()

#Returns average of all values within a Series
crypto_prices_series.mean()

#head function returns the top rows of a Series
#The code below will only return the first 2 rows
#The result does not modify the original Series in memory
crypto_prices_series.head(2)

#Assign the result of the head function to a new variable "new_crypto_prices"
new_crypto_prices = crypto_prices_series.head(3)

#Returns the last 2 rows of a Series
crypto_prices_series.tail(2)

#Check how many bytes of memory is allocated to the variable "crypto_prices_series"
crypto_prices_series.memory_usage


'''
IMPORT CSV DATA USING PANDAS
'''
#read_csv function can be used to import csv data using Pandas
#First argument within quotations is case sensitive and must be located in the same folder as the script file
#squeeze argument asks whether the data should be squeezed into a Series
BTC_price_series = pd.read_csv('crypto.csv', squeeze = True)

#Check the datatype of the Series
type(BTC_price_series)

#We can try to set the squeeze to false and the resule will be a Pandas DataFrame
BTC_price_dataframe = pd.read_csv('crypto.csv', squeeze = False)

#Check the datatype of the DataFrame
type(BTC_price_dataframe)

#If squeeze argument is not included, Pandas will default the import as a DataFrame
BTC_price_default = pd.read_csv('crypto.csv')

#Check the datatype of Default
type(BTC_price_default)

'''
PYTHON BUILT-IN FUNCTIONS
'''
#One can leverage the usefulness of Pandas with the built-in functions of Python
#The code below checks the length (number of rows) within the Pandas Series
len(BTC_price_series)

#Returns the maximum value within a Pandas Series
max(BTC_price_series)

#Returns the minimum value within a Pandas Series
min(BTC_price_series)

#Assigned a list of random numbers to a Pandas Series
my_series = pd.Series(data = [-10, 100, -30, 50, 100])
my_series

#Used a for loop to return a new list of prices that have their signs flipped
my_series_flipped = []
for num in my_series:
    new_num = num * -1
    my_series_flipped.append(new_num)
    
my_series_flipped

#Changed all the values of the Pandas Series to be negative using the absolute Python method
my_series_negative = abs(my_series) * -1
my_series_negative

#Used the set Python method to remove duplicates from the series
set(my_series)


'''
SORTING PANDAS SERIES
'''
#One can sort a Pandas Series using the sort_values() method
#Pandas will default the sorting to be ascending
#This will temporarily return the result but will not commit any change to the variable in memory
BTC_price_series.sort_values()

#To commit this change to memory, use the inplace=True argument
BTC_price_series.sort_values(inplace = True)

#Code below sorts the Series by index/axis label and commits the change to memory
BTC_price_series.sort_index(inplace = True)

#Sorts values in descending order
BTC_price_series.sort_values(ascending = False, inplace = True)


'''
PANDAS SERIES MATH OPERATIONS
'''
#Counts all the rows/elements in a Pandas Series
BTC_price_series.count()

#Results in the maximum value in a Pandas Series
BTC_price_series.max()

#Results in the minimum value in a Pandas Series
BTC_price_series.min()

#Results in the average value in a Pandas Series
BTC_price_series.mean()

#Returns basic statistical information about a Pandas Series
BTC_price_series.describe()


'''
CHECK IF GIVEN ELEMENT EXISTS IN PANDAS SERIES
'''
#Value in Pandas Series; returns True or False
#Code below checks if 1295.500000 is one of the values in the Pandas Series
1295.500000 in BTC_price_series.values

#Checks if there is an index number containing value of 1295
1295 in BTC_price_series.index

#If no attribute is designated, Pandas will default to search via index
1295 in BTC_price_series
