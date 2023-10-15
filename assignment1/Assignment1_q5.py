# Q.5 Convert a 1D array to a 2D array with 2 rows
# 	Input:
# 	arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

import numpy as np

def function():
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    a1 = arr.reshape([2, 5])
    print(f"Conversion of 1D array to a 2D array with 2 rows: \n {a1}")

function()

