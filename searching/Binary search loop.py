from array import *

arr = array('i', [])

n= int(input("enter length of array you want \t"))

for i in range(n) :
    x = int(input("Enter the  value \t"))
    arr.append(x)


print(arr)
val= int(input("enter element you wanna search \t"))

def search():
    low =0
    high= len(arr)-1

    while  low<= high:
        mid =(low+high)//2
        if arr[mid] == val:
            return mid
        elif arr[mid]<val:
            low=mid+1
        else:
            high=mid-1
    return-1

result = search()

if result!= -1:
    print(f"Element found at : {result}")
else:
    print("nahi mila yaar")


