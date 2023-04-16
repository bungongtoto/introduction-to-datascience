import pandas as pd

list_nums = [10,15,18,17,20]

df = pd.Series(list_nums, index=["a","b","c","d","e"])

print(df)