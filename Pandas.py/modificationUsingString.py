import pandas as pd

coffee = pd.read_csv(
    'https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')
coffee_new = coffee.copy()
print(coffee_new)
coffee_new['Code'] = coffee_new['Coffee Type'].str.split('e').str[0]
print()
print(coffee_new)
coffee_new = coffee_new.rename(columns={'Coffee Type': 'Coffee_Type'})
print(coffee_new)
print(coffee_new.query('Coffee_Type == "Latte" '))
print()
print(coffee_new.info())
