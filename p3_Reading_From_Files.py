"""
-> Quering Data From Data Frames
"""
#>> We use loc() function for this.

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'id' : [1, 2, 3, 4, 5],
    'names' : ['Ben', 'Gwen', 'Max', 'Kevin', 'Julie'],
    'age' : [21, 20, 60, 22, 19]
})

#print(df.loc[df['age'] < 30] ['names'])
"""
0      Ben
1     Gwen
3    Kevin
4    Julie
"""

#~ Reading & Writing Data

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'id' : [1, 2, 3, 4, 5],
    'names' : ['Ben', 'Gwen', 'Max', 'Kevin', 'Julie'],
    'age' : [21, 20, 60, 22, 19]
})

#-- Saving Data to a CSV file

df.to_csv('myTen.csv')

#-- Reading from CSV File

df = pd.read_csv('myTen.csv')
df.set_index('id', inplace = True)
print(df)

"""
    Unnamed: 0  names  age
id
1            0    Ben   21
2            1   Gwen   20
3            2    Max   60
4            3  Kevin   22
5            4  Julie   19
"""