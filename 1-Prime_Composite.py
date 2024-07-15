# Without Function
a = int(input("Enter a number = "))
b = a//2 + 1
for i in range(2,b):
  if a%i==0:
    print("Number is composite")
    break
  else:
    print("Number is prime")
  
# With Function
def f(a):
  b = a//2 + 1
  for i in range(2,b):
    if a%i==0:
     print("Number is composite")
     break
    else:
     print("Number is prime")
a = int(input("Enter a number = "))
f(a)
