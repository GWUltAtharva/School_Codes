#Without Function
s1 = int(input("Enter start = "))
s2 = int(input("Enter stop = "))
s3 = int(input("Enter step = "))
for i in range(s1,s2,s3):
 if i == s1:
   print("The initial value for start number = ",i)
 else:
   print("The value for start number after the step of",s3,"=",i)
   print("Since the stop value is",s2,", this value is not included in the final iteration")
   
#With Function
def dema(s1,s2,s3):
 for i in range(s1,s2,s3):
   if i == s1:
     print("The initial value for start number = ",i)
   else:
     print("The value for start number after the step of",s3,"=",i)
   print("Since the stop value is",s2,", this value is not included in the final iteration")
s1 = int(input("Enter start = "))
s2 = int(input("Enter stop = "))
s3 = int(input("Enter step = "))
dema(s1,s2,s3)
