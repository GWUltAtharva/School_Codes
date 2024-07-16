#Immutable Parameters - Int type
def imp(a, b):
  a = a * 5
  b = b + 7
  print("Calc:", a, b)
x, y = 10, 50
print("Values before function: ", x, y)
imp(x, y)
print("Values after function: ", x, y)
