import pandas as pd

a =[1,7,4]

#myvar = pd.Series(a)
# creating labels
myvar = pd.Series(a, index=["x","y","z"])
# without specifying the index, it is going to labels as array indexes.

# key/value objects as series.
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar1 = pd.Series(calories, index=["day1","day2"])
# you can select only some indexes in by adding the index referce with the keys needed.



print(myvar1)