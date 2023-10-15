# Q.6] Write a Pandas program to convert a dictionary to a Pandas series.
#
# SSample dictionary: d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}

import numpy as np
import pandas as pd

def function():
     d1 = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
     s1 = pd.Series(d1)
     print(f"Conversion of dictionary to a Pandas series: \n{s1}")

function()
