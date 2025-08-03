import pandas as pd
import numpy as np
coffee = pd.read_csv(
    'https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')
coffee_new = coffee.copy()  # We can make new copy to avoid changes in original
print(coffee_new)
coffee_new['Price'] = 199.9
print(coffee_new)

# To directly change in original
coffee['price'] = 200.0
print(coffee)
# Remove permanently
coffee = coffee[['Day', 'Coffee Type', 'Units Sold']]
print(coffee)
print()
coffee = coffee.drop(columns=['Units Sold'])
print(coffee)
