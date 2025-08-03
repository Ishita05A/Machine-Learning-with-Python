import pandas as pd
df = pd.read_csv(
    'https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')
print(df.head())
print()
print(df)
print()
print(df.tail())
print()
print(df.head(2))
print()
print(df.sample(10))
