def check_anagram(str1, str2):    
    if len(str1) != len(str2):     #cheking if they have same length  
        return False

    for char in str1:
        if str1.count(char) != str2.count(char):
            return False

    return True

# Input two strings
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if check_anagram(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")