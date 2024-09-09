x = int (input ("enter your number ? "))
for i in range (2,x):
    if  x%i==0:
        print ('its a non prime number')
        break
else:
    print ('its a prime number')