import matplotlib.pyplot as plt
import numpy as np
t1 = np.arange(0.0,5.0,0.1)
y1 = np.sin(2*np.pi*t1)
y2 = np.cos(2*np.pi*t1)

plt.figure(1)
plt.subplot(1,2,1)
plt.plot(t1,y1,'r')
plt.subplot(1,2,2)
plt.plot(t1,y2,'c')

plt.figure(2)
plt.subplot(1,2,1)
plt.plot(t1,y1,'b')

plt.subplot(1,2,2)
plt.plot(t1,y2,'k')

plt.show()
