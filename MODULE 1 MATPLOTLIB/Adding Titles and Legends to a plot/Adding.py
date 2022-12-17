import matplotlib.pyplot as plt
x_data = [1,2,3,4,5]
y_data = [1,4,9,16,25]
plt.plot(x_data,y_data,"v--b")
plt.plot(y_data,x_data,"^--r")
plt.show()