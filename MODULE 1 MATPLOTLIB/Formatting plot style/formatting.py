import matplotlib.pyplot as plt
x_data = [1,2,3,4,5]
y_data = [1,4,9,16,25]
plt.plot(x_data, y_data,"v--g")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()


'''
LINE                                   COLOR

character   description                character         color
'-'          solid line                black              k
'--'         dashed line style         blue               b
'-.'         dash-dot line style       green              g
':'          dotted line style         yellow             y
                                       white              w
'''