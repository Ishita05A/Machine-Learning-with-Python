import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
gas = pd.read_csv('./Matplotlib/gas_prices.csv')
print(gas)
for country in gas:
    if (country != 'Year'):
        plt.plot(gas.Year, gas[country], marker='.', label=country)
plt.title('USD of Countries over years')
plt.xlabel('Year')
plt.ylabel('USD')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()
plt.savefig('gas_price_data.png', dpi=300)
# Another way to plot many values
country_to_look_at = ['Australia', 'France', 'Germany', 'Mexico']
plt.title('Graph')
for i in gas:
    if (i in country_to_look_at):
        plt.plot(gas.Year, gas[i], marker='*', label=i)
plt.legend()
plt.show()
