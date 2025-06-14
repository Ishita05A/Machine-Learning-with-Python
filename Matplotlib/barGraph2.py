import matplotlib.pyplot as plt
labels = ['A', 'B', 'C', 'D']
values = [2, 6, 4, 8]
pattern = ['/', 'o', '-', '+']
bars = plt.bar(labels, values)
for bar in bars:
    bar.set_hatch(pattern.pop(0))

plt.show()
