# Q.No.2
# Daily Closing Prices of Two Stocks arranged as per returns. So calculate Covariance using R, Python and Formula.
# x: 1.8, 1.5, 2.1, 2.4, 0.2
# y: 2.5, 4.3, 4.5, 4.1, 2.2


import numpy as np
import pandas as pd

def function():
    x = np.array([1.8, 1.5, 2.1, 2.4, 0.2])
    y = np.array([2.5, 4.3, 4.5, 4.1, 2.2])

    covarience_matrix = np.cov(x,y)
    print(covarience_matrix)
    print(f"Covarience = {covarience_matrix[0][1]}")

    print()

    correlation = np.corrcoef(x,y)
    print(correlation)
    print(f"Correlation = {correlation[0][1]}")


function()