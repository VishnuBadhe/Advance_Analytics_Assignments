# Q.NO.1]
# 1] Read the data from a jamesbond.csv file from Dataset folder
#
# 2] plot scatter plot where xlable - Year.Ylable - Box Office title - Box Office vs Year
#
# 3] plot scatter plot where xlable - Year.Ylable - Budget title - Budget Vs Year



import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def function():
    df = pd.read_csv("C:\\Sunbeam_DBDA_Class\\advanced_analytics_using_statistics\\Assignment\\jamesbond.csv")
    print(df)



    x_values = np.arange(df['Year'].size)

    plt.subplot(1,2,1)
    plt.plot(x_values, df['Box Office'], label='Box Office')
    plt.scatter(x_values, df['Box Office'])

    plt.legend()

    plt.xlabel("Year")
    plt.ylabel("Box Office")
    plt.title("Box Office vs Year")

    plt.tight_layout()



    plt.subplot(1,2,2)
    plt.plot(x_values, df['Budget'], label='Budget')
    plt.scatter(x_values, df['Budget'])

    plt.legend()

    plt.xlabel("Year")
    plt.ylabel("Budget")
    plt.title("Budget vs Year")

    plt.tight_layout()

    plt.show()



function()



