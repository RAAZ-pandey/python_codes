from functools import reduce  #library to import reduce

nums = [3,2,6,8,4,6,2,9]   #taimg a list

evens = list(filter(lambda n : n%2==0 , nums))  # use filter function in lambda to filter even numbers out of a list
print(evens)

doubles = list(map(lambda n : n*2 , evens))  #here we are using map function in lambda to double all elements of evens  
print(doubles)

sum = reduce(lambda a,b :a+b,doubles)    # using reduce  in lamda to  add just two numbers at a time instead of list 
print(sum)