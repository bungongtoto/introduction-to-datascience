import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
#df = pd.DataFrame(data)
# we can also name the indexes
df = pd.DataFrame(data, index=["day1","day2","day3"])

print(df) 

#refer to the row index:
#print(df.loc[0])
print(df.loc["day2"])

#use a list of indexes:
#print(df.loc[[0, 1]])

# loading a csv file

lf = pd.read_csv('data.csv')

print(lf)