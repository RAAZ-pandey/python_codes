def divide(a,b):
  print(a/b)
#this is called wrapper function , where a function is wraspped around another function without changing its original implemnetation
def smart_div(func):
  def swap(a,b):
    if a<b:
      a,b == b,a
    return func(a,b)
  return swap

div  = smart_div(divide)
div(2,10)