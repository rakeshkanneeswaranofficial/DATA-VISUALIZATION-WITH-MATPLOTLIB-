import matplotlib.pyplot as plt
import numpy as np
x = np.arange(70)
y1 = np.random.randn(70)
y2 = np.random.randn(70)
plt.scatter(x, y1, marker = 'o',c='r')
plt.scatter(x, y2,marker = 'v',c='b')
plt.show()