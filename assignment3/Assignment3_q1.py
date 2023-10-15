# Ques1:
#
# Calculate the coefficient of covariance for the following data:
#
# X	2	8	18	20	28	30
# Y	5	12	18	23	45	50
#
# So calculate Covariance using Python ,R and Formula.

import numpy as np
import pandas as pd

def function():
    x = np.array([2, 8,	18,	20,	28,	30])
    y = np.array([5, 12, 18, 23, 45, 50])

    covarience_matrix = np.cov(x,y)
    print(covarience_matrix)
    print(f"Covarience = {covarience_matrix[0][1]}")

    print()

    correlation = np.corrcoef(x,y)
    print(correlation)
    print(f"Correlation = {correlation[0][1]}")

function()