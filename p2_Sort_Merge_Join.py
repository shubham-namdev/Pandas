"""
->Pandas - Sorting, Joining & Merging
"""
import pandas as pd
import numpy as np

#~ Sorting 

df = pd.DataFrame(np.random.rand(10, 2), 
                  index=[1,5,3,6,7,2,8,9,0,4], 
                  columns=['A', 'B'])

#-- Sort By Index

print(df.sort_index())
"""
          A         B
0  0.930077  0.027715
1  0.723681  0.774488
2  0.259950  0.886363
3  0.253637  0.970234
4  0.323325  0.611983
...     ...     ...
"""

#-- Sorting Inplace

df.sort_index(inplace=True)

#-- Sort By Columns

print(df.sort_values(by=['A']))
"""
 A         B
0  0.211975  0.130228
8  0.378723  0.000353
2  0.454905  0.504803
5  0.515232  0.441410
1  0.564693  0.447613
...    ...       ...
"""

#~ Joining & Merging

#-- Merging

import pandas as pd
import numpy as np
names = pd.DataFrame({
    'id' : [1, 2, 3, 4, 5],
    'name' : ['Ben', 'Gwen', 'Kevin', 'Julie', 'Ship']
})

genders = pd.DataFrame({
    'id' : [1, 2, 3, 4, 5],
    'gender' : ['M', 'F', 'M', 'F', 'Alien']
})

df = pd.merge(names, genders, on = 'id')
df.set_index('id', inplace = True)

print(df)

"""
     name gender
id
1     Ben      M
2    Gwen      F
3   Kevin      M
4   Julie      F
5    Ship  Alien
"""

#-- Joins

#>> left    =>  Uses all keys from left object and merges with right
#>> right   =>  Uses all keys from right object and merges with left
#>> outer   =>  Uses all keys from bot objects and merges them
#>> inner   =>  Uses only the keys which both objects have and merges them (default)


import pandas as pd
import numpy as np

names = pd.DataFrame({
    'id' : [1, 2, 3, 4, 5, 6],
    'name' : ['Ben', 'Gwen', 'Kevin', 'Julie', 'Ship', 'Max']
})

genders = pd.DataFrame({
    'id' : [1, 2, 3, 4, 5, 7],
    'gender' : ['M', 'F', 'M', 'F', 'Alien', 'F']
})

#-- Inner Join
df = pd.merge(names, genders, on = 'id', how = 'inner')
"""
   id   name gender
0   1    Ben      M
1   2   Gwen      F
2   3  Kevin      M
3   4  Julie      F
4   5   Ship  Alien

Only takes keys common in both frames. 
"""
#-- Left Join

df = pd.merge(names, genders, on = 'id', how = 'left')
"""
   id   name gender
0   1    Ben      M
1   2   Gwen      F
2   3  Kevin      M
3   4  Julie      F
4   5   Ship  Alien
5   6    Max    NaN
"""

#-- Right Join
df = pd.merge(names, genders, on = 'id', how = 'right')
"""
   id   name gender
0   1    Ben      M
1   2   Gwen      F
2   3  Kevin      M
3   4  Julie      F
4   5   Ship  Alien
5   7    NaN      F
"""

#-- Outer Join
df = pd.merge(names, genders, on = 'id', how = 'outer')
"""
   id   name gender
0   1    Ben      M
1   2   Gwen      F
2   3  Kevin      M
3   4  Julie      F
4   5   Ship  Alien
5   6    Max    NaN
6   7    NaN      F
"""
