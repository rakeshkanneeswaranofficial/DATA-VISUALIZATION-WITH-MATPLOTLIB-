import matplotlib.pyplot as plt
import numpy as np

subjects = ["math","chemistry","english","physics"]
marks = [25,25,20,30]
plt.pie(marks,labels=subjects,explode = (0,0.1,0,0),shadow= True,autopct='%1.0f%%')
plt.show()
