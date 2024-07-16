n1 = float(input("Enter First Number = "))
n2 = float(input("Enter Second Number = "))
o = input("Enter Operator = ")
if o == '+':
  r = n1+n2
  print(n1,o,n2,"=",r)
elif o == '-':
  r = n1-n2
  print(n1,o,n2,"=",r)
elif o == '*':
  r = n1*n2
  print(n1,o,n2,"=",r)
elif o == '/':
  r = n1/n2
  print(n1,o,n2,"=",r)
else:
  print("Invalid Operator")
