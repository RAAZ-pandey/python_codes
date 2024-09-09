from numpy import *

arr1 = array([6,7,8,9,3,5])

#arr2 = arr1           # not an actual copy just assigned values both original and copied array have same memery address : check out
#arr2 = arr1.view()    # shallow copy means dependent on one another 
arr2 =arr1.copy()     # deep copy means independent baby 

arr1[2] = 1

print (arr1)    
print (arr2)

print(id(arr1))
print(id(arr2))