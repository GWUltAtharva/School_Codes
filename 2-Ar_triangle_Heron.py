# Without Function
a = int(input("Enter first number = "))
b = int(input("Enter second number = "))
c = int(input("Enter third number = "))
s = (a+b+c)/2
x = s-a
y = s-b
z = s-c
h = (s*x*y*z)**0.5
# With Function
def f(a,b,c):
  s = (a+b+c)/2
  x = s-a
  y = s-b
  z = s-c
  h = (s*x*y*z)**0.5
  print("Area of the triangle = ",h)
a = int(input("Enter first number = "))
b = int(input("Enter second number = "))
c = int(input("Enter third number = "))
f(a,b,c)
