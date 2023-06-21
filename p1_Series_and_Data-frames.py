"""
-> Pandas
>> provides high-performance tools for data manipulation and analysis.
>> is very effective at converting data formats and querying data out of databases
"""
import pandas as pd
import numpy as np

#~ Pandas Series

# ? One-dimentional array which is labelled
#>> Data Science Equivalent of Ordinary Python Dictionary

series = pd.Series([10, 20, 30, 40, 50], ['A', 'B', 'C', 'D', 'E'])

print(series)
"""
A    10
B    20
C    30
D    40
E    50
dtype: int64
"""

#-- Accessing Values

#>> We need to address the key or the position(index) to get the desired value

print(series[1])   # 20
print(series['A']) # 10

#-- Dictionary to Series

myDict = {'A' : 10, 'B' : 20, 'C' : 30, 'D' : 40}
series = pd.Series(myDict)

#-- Changing order

series = pd.Series(myDict, index = ['C', 'A', 'B', 'D'])

print(series)
"""
C    30
A    10
B    20
D    40
dtype: int64
"""

#~ Pandas Data Frame
#>> multi-dimensional and looks like a table. 
#>> imagine it to be like an Excel table or a data base table.

data = {'Name' : ['Bob', 'Sam', "Tim"],
        'Age'  : [48, 24, 30],
        'Height':[172, 159, 171],
        'Country': ['USA', 'AUS', "CND"]
       }

df = pd.DataFrame(data)

print(df)
"""
     Name  Age  Height Country
0     Bob   48     172     USA
1     Sam   24     159     AUS
2     Tim   30     171     CND
"""

#-- Accessing Values

print(df['Name'][1]) # Sam

#>> Printing Columns

print(df[['Name', 'Age']])
"""
  Name  Age
0  Bob   48
1  Sam   24
2  Tim   30
"""

#~ Data Frame Functions and Attributes                                                       

#>> df.T        =>  Transpose of Rows and Columns
#>> df.dtypes   =>  Return data types of data frame
#>> df.ndim     =>  Returns number of dimensions
#>> df.shape    =>  Returns shape of data frame
#>> df.size     =>  Returns number of elements in data frame
#>> df.head(n)  =>  Returns first n rows of data frame (default 5)
#>> df.tail(n)  =>  Returns last n rows of data frame (default 5)

#~ Statistical Functions

#>> count()     =>  Count number of non-null elements
#>> sum()       =>  Returns sum of values of selected column
#>> mean()      =>  Returns mean of values of selected column
#>> median()    =>  Returns median of values of selected column
#>> mode()      =>  Returns most occuring value of selected column
#>> std()       =>  Returns standard deviation of values
#>> min()       =>  Returns minimum value
#>> max()       =>  Returns maximum value
#>> abs()       =>  Returns absolute values of elements
#>> prod()      =>  Returns product of selected elements
#>> describe()  =>  Returns data frame with all statistical values summarized

print(df.describe())

"""
             Age      Height
count   3.000000    3.000000
mean   34.000000  167.333333
std    12.489996    7.234178
min    24.000000  159.000000
25%    27.000000  165.000000
50%    30.000000  171.000000
75%    39.000000  171.500000
max    48.000000  172.000000

"""

#~ Applying Functions

#-- lambda function
print(df['Age'].apply(lambda x : x * 2))
"""
0    96
1    48
2    60
Name: Age, dtype: int64
"""

#-- Applying Numpy functions
print(df['Age'].apply(np.sin))
"""
0   -0.768255
1   -0.905578
2   -0.988032
Name: Age, dtype: float64
"""

#~ Iterating over Data Frames

#>> items()   =>  Iterator for key-value pairs
#>> iterrows()    =>  Iterator for the rows (index, series)
#>> itertuples()  =>  Iterator for the rows as named tuples

for key, value in df.items():
    print(f"{key} : {value}")

"""Name : 0    Bob
          1    Sam
          2    Tim
Name: Name, dtype: object

Age : 0    48
      1    24
      2    30
Name: Age, dtype: int64

Height : 0    172
         1    159
         2    171
Name: Height, dtype: int64
Country : 0    USA
          1    AUS
          2    CND
Name: Country, dtype: object"""

for index, value in df.iterrows():
    print(f"{index} : {value}")

"""
0 : Name       Bob
    Age         48
    Height     172
    Country    USA
Name: 0, dtype: object

1 : Name       Sam
    Age         24
    Height     159
    Country    AUS
Name: 1, dtype: object

2 : Name       Tim
    Age         30
    Height     171
    Country    CND
Name: 2, dtype: object

"""