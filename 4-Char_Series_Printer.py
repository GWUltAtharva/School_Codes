#Without Function
ch = input("Enter a character = ")
t = int(input("Enter number of times = "))
f = ch*t
print(ch,"character",t,"number of times is :-",f)

#With Function
def charac(ch,t):
 f = ch*t
 print(ch,"character",t,"number of times is :-",f)
a = input("Enter a character = ")
b = int(input("Enter number of times = "))
charac(a,b)
