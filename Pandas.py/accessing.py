import pandas as pd
coffee = pd.read_csv(
    'https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')

print(coffee.loc[0])
print()
print(coffee.loc[[0, 1, 5]])
print()
print(coffee.loc[0:7:2])
print()
print(coffee.loc[0:9:2, 'Day'])
print(coffee.iloc[0:5], [0, 2])  # Using only Index value
coffee.loc[0:3, 'unit sold'] = 10
print()
print(coffee.head())
print()
print(coffee.sort_values("Units Sold"))
for index, row in coffee.iterrows():
    print(index)
    print(row['Units Sold'])
    print("\n\n\n\n\n\n")
