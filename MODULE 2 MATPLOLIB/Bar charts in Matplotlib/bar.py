import matplotlib.pyplot as plt
import numpy as np

sub = ["English","maths","chemistry","physics"]
marks = [35,40,50,55]
visual = ['r','k','g','b']
plt.bar(sub, marks,color = visual)
plt.show()