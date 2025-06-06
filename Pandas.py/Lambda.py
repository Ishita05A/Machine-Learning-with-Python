import pandas as pd
import numpy as np
coffee = pd.read_csv(
    'https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')
print(coffee)
coffee['Price'] = np.where(coffee['Coffee Type'] == "Espresso", 500.0, 400.0)
print(coffee)

coffee['Category'] = coffee['Price'].apply(
    lambda x: 'Expensive' if x > 450 else 'Average')
print(coffee)
