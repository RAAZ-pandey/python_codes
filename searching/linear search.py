from array import *

arr = array('i', [])

n= int(input("enter length of array you want \t"))

for i in range(n) :
    x = int(input("Enter the  value \t"))
    arr.append(x)


print(arr)
key = int(input("enter number you want to search \t"))

for x in arr:
    if x== key:
        print(" number found in array" )
        break

else:
    print("not found bruh ")   
   