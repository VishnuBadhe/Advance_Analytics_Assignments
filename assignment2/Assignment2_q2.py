 # Q.NO.2] Read Adler.csv.
	# check the number of values missing in rating column
	# get the mean value of rating
	# replace the missing values with mean of rating column
	# check the number of values missing in rating column
	# check the mean of rating column after filling the NA records with mean
	# add Extrarating column based on rating* 20
	# add Newrating column = rating + Exrtarating

import numpy as np
import pandas as pd

def function():
    df = pd.read_csv('Adler.csv')
    print(df)


    print(f"Missing Values = {df['rating'].isna().sum()}")


    mean = df['rating'].mean()
    print(f"Mean of 'rating' column = {mean}")


    df['rating'] = df['rating'].fillna(mean)
    print(df)
    print(f"no if NA values in 'rating' = {df.rating.isna().sum()}")


    df['Extrarating'] = df.rating * 20
    print(df)


    df['Newrating'] = df.rating + df.Extrarating
    print(df)


function()