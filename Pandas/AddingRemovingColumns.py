import pandas as pd
import numpy as np
coffee = pd.read_csv(
    'https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')
print(coffee)
print()
coffee['price'] = 4.99
print(coffee)
print()
coffee['new_price'] = np.where(coffee['Coffee Type'] == 'Espresso', 5.99,4.99)
print(coffee)
print()
print(coffee.drop(columns=['price']))  # It will not drop from original file
print(coffee)
print()
coffee.drop(columns=['price'], inplace=True)  # It will remove from file
print(coffee)
print()
