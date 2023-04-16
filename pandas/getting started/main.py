import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myVar = pd.DataFrame(mydataset)

print(myVar)

# checking pandas version 

print(f'the version of pandas is :{pd.__version__}')


