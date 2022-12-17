import matplotlib.pyplot as plt
import numpy as np
x_data = np.linspace(0,10,100)
a_data = x_data**2
b_data = x_data**3
c_data = x_data**4
plt.plot(x_data,a_data,label = "SQUARE")
plt.plot(x_data,b_data,label = "CUBE")
plt.plot(x_data,c_data,label = "POWER OF FOUR")
plt.title("Graph of three lines ")
plt.xlabel("100 values between 0 and 10")
plt.ylabel("Different Calculations")
plt.legend(loc=9)
plt.show()

"""                              LOCATION OF LEDGENDS
LOCATION STRING            LOCATION CODE
'best'                            0
'upper right'                     1
'upper left'                      2
'lower right'                     3
'lower left'                      4
'right'                           5
'center left'                     6
'lower center'                    7
'upper center'                    8
'center'                          9 







"""