#Without Function
lst = []
n = int(input("Enter number of elements = "))
for k in range(0, n):
  ele = int(input("Enter item = "))
  lst.append(ele) 
  for i in range(len(lst)):
    if lst[i] % 2:
      lst[i] -= 1
    else:
      lst[i] += 2
  print(lst)

#With Function
def ed(lst):
  for i in range(len(lst)):
    if lst[i] % 2:
      lst[i] -= 1
    else:
      lst[i] += 2
  print(lst)
lst = []
n = int(input("Enter number of elements = "))
for k in range(0, n):
 ele = int(input("Enter item = "))
 lst.append(ele)
ed(lst)
