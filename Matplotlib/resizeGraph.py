import matplotlib.pyplot as plt
import numpy as np
x = [0, 1, 2, 3, 4, 5]
y = [0, 2, 4, 6, 8, 10]
plt.figure(figsize=(5, 3), dpi=200)
plt.title('GRAPH', fontdict={
          'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.plot(x, y, label='2X', color='blue', marker='.', linewidth=2)
x1 = np.arange(0, 4.5, 0.5)
plt.plot(x1, x1**2, 'r--', label='X**2',
         color='red', linewidth='2', marker='^')
plt.plot(x1[:5], x1[:5]**2, linewidth=2, color='green')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.savefig('mygraph.png', dpi=300)
plt.show()
