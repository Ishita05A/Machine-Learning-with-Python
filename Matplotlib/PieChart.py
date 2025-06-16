import matplotlib.pyplot as plt
import pandas as pd
fifa = pd.read_csv('./Matplotlib/fifa_data.csv')
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
labels = ['left ', 'right']
colors = ["#0e6446", "#1c9f68"]
plt.title('Foot Preferrence of fifa players')
plt.pie([left, right], labels=labels, colors=colors, autopct='%2.f%%')
plt.show()
