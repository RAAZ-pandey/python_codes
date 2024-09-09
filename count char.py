print("^^^^^^^^^count occurance of char*********")
string1 = input("Enter a string: ")
char1 = input("Enter a character: ")


count = 0


for i in string1:
    if i == char1:
        count += 1


print(f"Number of occurrences of '{char1}' in the string: {count}")