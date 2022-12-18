import matplotlib.pyplot as plt
import numpy as np
subject = ['chemstry','maths','physics','english','sanskrit']
given_marks = [55,66,55,62,58]
grace_marks = [12,13,14,15,12]
visual = ['r','k','c','b','y']
plt.bar(subject,given_marks,color = visual)
plt.bar(subject,grace_marks,bottom=given_marks)
plt.show()