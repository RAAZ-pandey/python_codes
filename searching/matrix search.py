from numpy import *
arr = [[1, 2, 3],
        [4, 5, 6], 
        [17, 8, 9]]
n = len(arr)
sum1 = 0
sum2 =0
total_sum=0

for i in range(n):
  #  print(i)
    sum1 += arr[i][i]
    sum2 += arr[i][n-i-1] 

total_sum = sum1+sum2     

print("sum of diagonal1 of matrix is :", sum1)
print("sum of diagonal2 of matrix is :", sum2)
print("sum of elements of both diagonals of matrix is :" ,total_sum)
