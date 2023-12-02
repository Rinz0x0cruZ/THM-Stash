import pandas as pd
import matplotlib .pyplot as plt

df=pd.read_csv("somefile.csv", usecols=columns)
df.head(5) #just the top 5 rows of the dataset
df.count() #counts the number of values for each column
df.groupby(['Source']) #groups the values of a certain column and counts the non-unique
df.value.count(['Protocol']) #counts the number of times a value appears in a column

