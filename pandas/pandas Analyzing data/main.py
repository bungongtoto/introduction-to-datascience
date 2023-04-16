import pandas as pd

df = pd.read_csv('data.csv')

#prints the first 10 rows
print(df.head(10))

# prints the first 5 rows by default
print(df.head())

#prints the last five rows by defualt
(df.tail())
# the info() method gives more information on the data set.
print(df.info()) 

