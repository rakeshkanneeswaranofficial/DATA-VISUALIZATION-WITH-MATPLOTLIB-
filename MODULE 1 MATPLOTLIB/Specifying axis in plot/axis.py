import matplotlib.pyplot as plt
x_data = [1,2,3,4,5]
y_data = [1,4,9,16,25]
plt.plot(x_data, y_data)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.axis([0,6,0,30])
plt.show()