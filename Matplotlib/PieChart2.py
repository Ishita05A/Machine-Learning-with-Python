import matplotlib.pyplot as plt
import pandas as pd
fifa = pd.read_csv('./Matplotlib/fifa_data.csv')
plt.style.use('ggplot')
fifa.Weight = [int(x.strip('lbs')) if type(
    x) == str else x for x in fifa.Weight]
light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa.loc[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
medium = fifa[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
medium_heavy = fifa[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
heavy = fifa[(fifa.Weight >= 200)].count()[0]
weights = [light, light_medium, medium, medium_heavy, heavy]
labels = ['Under 125', '125 - 150', '150 - 175', '175 - 200', 'Over 200']
explode = [.4, 0.2, 0, 0, .4]
plt.title('Weight Distribution of FIFA Player (in lsb)')
plt.pie(weights, labels=labels, autopct='%2.f%%',
        pctdistance=0.8, explode=explode)
plt.show()
