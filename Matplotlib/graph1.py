import matplotlib.pyplot as plt
x = (1, 2, 3, 4)
y = (2, 4, 6, 8)
plt.title('Straight Line Graph', fontdict={
          'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.plot(x, y, label='2x', color='Green',
         linewidth=8, marker='.', markersize=10)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend()
plt.xticks([1, 2, 3, 4])
plt.yticks([2, 4, 6, 8])
plt.show()
