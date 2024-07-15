#Without Function
h = int(input("Enter the time in hrs = "))
m = int(input("Enter the time in mins = "))
if h>=0 and h<24 and m>=0 and m<60:
 if h>=0 and h<5 or h>=21 and h<24:
   print("Good Night")
 elif h>=5 and h<12:
   print("Good Morning")
 elif h==12 and m==0:
   print("Good Noon")
 elif h==12 and m!=0 or h>=13 and h<17:
   print("Good Afternoon")
 else:
   print("Good Evening")
else:
  print("Enter correct time")
 
#With Function
def greet(h,m):
 if h>=0 and h<24 and m>=0 and m<60:
   if h>=0 and h<5 or h>=21 and h<24:
     print("Good Night")
   elif h>=5 and h<12:
     print("Good Morning")
   elif h==12 and m==0:
     print("Good Noon")
   elif h==12 and m!=0 or h>=13 and h<17:
     print("Good Afternoon")
   else:
     print("Good Evening")
   else:
     print("Enter correct time")
a = int(input("Enter the time in hrs = "))
b = int(input("Enter the time in mins = "))
greet(a,b)
