import numpy as np
array1 = np.array([[1,2,3,4],[5,6,7,8]])
list1 = [1,2,4,5,6,7,8,9]
list2 = list1[0:5]
print(list2)
list2[0] = 100
print(list2)
print(list1)