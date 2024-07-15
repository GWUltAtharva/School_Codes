#Without Function
a = int(input("Enter your age = "))
if a<=8 and a>=0:
 print("You cannot do any rides, sorry:(")
elif a<=18 and a>8:
 print("Do your rides under surveillance of an elder")
elif a<=70 and a>18:
 print("You can do any ride you want")
else:
 print("Not recommended to do rides, but no limitations")
#With Function
def amuse(a):
 if a<=8 and a>=0:
   print("You cannot do any rides, sorry:(")
 elif a<=18 and a>8:
   print("Do your rides under surveillance of an elder")
 elif a<=70 and a>18:
   print("You can do any ride you want")
 else:
   print("Not recommended to do rides, but no limitations")
r = int(input("Enter your age = "))
amuse(r)
