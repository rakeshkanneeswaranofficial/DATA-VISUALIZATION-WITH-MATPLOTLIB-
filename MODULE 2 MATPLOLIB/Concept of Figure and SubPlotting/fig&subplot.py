import matplotlib.pyplot as plt
import numpy as np
ti=i = np.arange(0.0,5.0,0.1)
y1 = np.sin(2*np.pi*ti)
y2 = np.cos(2*np.pi*ti)

plt.figure()

plt.subplot(211)
plt.plot(ti,y1,'r')
 
plt.subplot(212)
plt.plot(ti,y2,'g')

plt.show()