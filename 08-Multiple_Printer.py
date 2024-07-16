#Wihtout Funtion
m = int(input("Enter a number = "))
n = int(input("Enter nth term = "))
for i in range(1,n+1):
 print(m,"x",i,"=",m*i)

#With Function
def tab(m,n):
 for i in range(1,n+1):
   print(m,"x",i,"=",m*i)
a = int(input("Enter a number = "))
b = int(input("Enter nth term = "))
tab(a,b)
