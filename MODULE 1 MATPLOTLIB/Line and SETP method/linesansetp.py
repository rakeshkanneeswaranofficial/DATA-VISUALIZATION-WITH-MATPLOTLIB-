import matplotlib.pyplot as plt
import numpy as np
x = np.arange(10)
y1 = [1,9,7,10,3,16,2,20,5,22]
y2 = [11,22,7,14,6,8,2,15,3,5]
lines = plt.plot(x,y1,x,y2)
plt.setp(lines,color = 'r',linewidth = 3)
plt.show()