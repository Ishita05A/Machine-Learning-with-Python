import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
gas = pd.read_csv('./Matplotlib/gas_prices.csv')
print(gas)
plt.title('Gas Price Overtime (in USD)')
plt.plot(gas.Year, gas.USA, 'g.-', label='USA')
plt.plot(gas.Year, gas.Canada, 'r.-', label='Canada')
plt.plot(gas.Year, gas['South Korea'], 'b.-', label='South Korea')
plt.xticks(gas.Year[::3])
plt.xlabel('Years')
plt.ylabel('US Dollers')
plt.legend()
plt.show()
