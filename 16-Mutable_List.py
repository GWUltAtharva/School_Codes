#Mutable Parameters - List type
def mp(a):
  a[0] = a[0] * 2
  a[1] = a[1] + 2
  print("Calc:", a)
x = [3, 4]
print("List before function: ", x)
mp(x)
print("List after function: ", x)
