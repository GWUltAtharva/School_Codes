#Immutable Parameters - tuple type
def imp(a):
  a = list(a)
  a[0] = a[0] * 2
  a[1] = a[1] + 2
  print("Calc:", a)
x = (5, 6)
print("Tuple before function: ", x)
imp(x)
print("Tuple after function: ", x)
