import matplotlib.pyplot as plt
import pandas as pd
fifa = pd.read_csv('./Matplotlib/fifa_data.csv')
num_rows = 5
num_cols = 5
print(fifa.iloc[:num_rows, :num_cols])
plt.hist(fifa.Overall)
plt.show()
