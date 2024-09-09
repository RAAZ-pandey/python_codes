from numpy import *
arr = array([

          [1,2,3],
          [5,6,9],
          [7,5,9]
                  ])
#print(arr)
arr1 =arr.flatten()
print(arr1)
arr2 = arr1.reshape(3,3)
print(arr2)