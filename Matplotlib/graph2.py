import numpy as np
import matplotlib.pyplot as plt
x1 = np.arange(0, 4.5, 0.5)
print(x1)
plt.title('Square graph', fontdict={
          'fontname': 'Comic Sans MS', 'fontsize': 20, })
plt.plot(x1, x1**2, 'r--', label='X^2', linewidth=2,
         color='blue', marker='^', markeredgecolor='black')
plt.plot(x1[:5], x1[:5]**2, 'r', color='green', linewidth='2')
plt.xlabel('X - axis')
plt.ylabel('Y - axis')

plt.legend()
plt.show()
