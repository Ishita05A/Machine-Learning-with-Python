import pandas as pd
coffee = pd.read_csv(
    'https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')
print(coffee[(coffee['Units Sold'] > 40)])
print()
print(coffee[(coffee['Units Sold'] > 20) & (
    coffee['Coffee Type'] == 'Espresso')])
print()
print(coffee[coffee['Day'].str.contains("Sun|Sat")])
print()
print(coffee[coffee['Day'].str.contains("Sun|Sat", case=False)])
