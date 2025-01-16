def translate(phrase):
  translation = ""
  for letter in phrase:
    if letter in  "123456789":             #for changing numbers into R
    #if letter in  "AEIOUaeiou":
      translation = translation + "R"
    else:
      translation + translation + letter
  return translation

print(translate(input("Enter your keyword: ")))
