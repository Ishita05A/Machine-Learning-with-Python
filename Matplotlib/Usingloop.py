import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
gas = pd.read_csv('./Matplotlib/gas_prices.csv')
# print(gas)
for country in gas:
    if (country != 'Year'):
        plt.plot(gas.Year, gas[country], marker='.')
plt.show()
