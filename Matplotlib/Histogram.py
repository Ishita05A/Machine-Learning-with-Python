import matplotlib.pyplot as plt
import pandas as pd
fifa = pd.read_csv('./Matplotlib/fifa_data.csv')
num_rows = 5
num_cols = 5
print(fifa.iloc[:num_rows, :num_cols])
bins = [40, 50, 60, 70, 80, 90, 100]
plt.xticks(bins)
plt.title('Distribution of player skill in FIFA 2018')
plt.xlabel('Skill Level')
plt.ylabel('Number of Players')
plt.hist(fifa.Overall, bins, color="#18497a")
plt.show()
