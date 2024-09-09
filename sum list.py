list1 = []
n = int(input("Enter no of elements : "))
 
for i in range(0, n):
    items = int(input())
    list1.append(items)  
 
print("your list is : ",list1)
 
sum=0
for items in range(0,n):
    sum = sum + list1[items]
 

print("Sum of all elements in a list: ", sum)