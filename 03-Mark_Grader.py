# Without Function
g = int(input("Enter your marks = "))
if g > 90:
 print("Grade A")
elif g > 80 and g<=90:
 print("Grade B")
elif g > 70 and g<=80:
 print("Grade C")
elif g > 50 and g<=70:
 print("Grade D")
else:
 print("Grade F")

# With Function
def grade(g):
  if g > 90:
   print("Grade A")
  elif g > 80 and g<=90:
   print("Grade B")
  elif g > 70 and g<=80:
   print("Grade C")
  elif g > 50 and g<=70:
   print("Grade D")
  else:
   print("Grade F")
a = int(input("Enter your marks = "))
grade(a)
