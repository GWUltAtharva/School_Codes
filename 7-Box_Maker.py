#Without Function
ch = input("Enter a character = ")
r = int(input("Enter number of rows = "))
c = int(input("Enter number of coulums = "))
for i in range(1,r+1):
 for j in range(1,c+1):
   if i == 1 or i == r or j == 1 or j == c:
     print(ch, end = "")
   else:
     print(" ", end = "")
     print()

#With Function
def box(ch,r,c):
 for i in range(1,r+1):
   for j in range(1,c+1):
     if i == 1 or i == r or j == 1 or j == c:
       print(ch, end = "")
     else:
       print(" ", end = "")
       print()
a = input("Enter a character = ")
b = int(input("Enter number of rows = "))
c = int(input("Enter number of coulums = "))
box(a,b,c)
