import pandas as pd
import numpy as np
coffee = pd.read_csv(
    'https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')
coffee['New_Price'] = np.where(
    coffee['Coffee Type'] == "Espresso", 500.0, 449.0)
print(coffee)
coffee['Revenue'] = coffee['Units Sold']*coffee['New_Price']
print(coffee)
coffee = coffee.rename(columns={'New_Price': 'Price'})
print(coffee)
