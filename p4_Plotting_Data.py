"""
-> Plotting and Visualizing Data
"""


import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'names' : ['Ben', 'Gwen', 'Max', 'Kevin', 'Julie'],
    'age' : [21, 20, 60, 22, 19], 
    'height' : [175, 165, 185, 180, 160], 

})

df.sort_values(by = ['age', 'height'])
df.plot()
#df.hist() - for histogram
plt.show()