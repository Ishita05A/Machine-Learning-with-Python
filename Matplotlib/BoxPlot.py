import matplotlib.pyplot as plt
import pandas as pd
fifa = pd.read_csv('./Matplotlib/fifa_data.csv')
plt.figure(figsize=(5, 8))
barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
revs = fifa.loc[fifa.Club == 'New England Revolution']['Overall']
labels = ['FC Barcelona', 'Real Madrid', 'NE Revolution']
plt.title('Professional Soccer Team Comparision')
plt.ylabel('FIFA Overall Rating')
boxes = plt.boxplot([barcelona, madrid, revs],
                    labels=labels, patch_artist=True, medianprops={'linewidth': 2})
for box in boxes['boxes']:
    box.set(color="#193d60", linewidth=2)
    box.set(facecolor='#abcdef')
plt.show()
