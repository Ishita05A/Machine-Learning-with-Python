import pandas as pd
bios = pd.read_csv(
    'https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv')
print(bios)
# print(bios.query('[Coffee Type] == "Latte" and Day == "Sunday"'))
