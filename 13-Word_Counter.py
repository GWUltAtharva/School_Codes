#Without Function
s = "Come let us have some fun"
l = s.split()
t = ()
for w in l:
  t += (len(w),)
print(t)

# With function
def wl(s):
  l = s.split()
  t = ()
  for w in l:
    t += (len(w),)
    print(t)
s = "Come let us have some fun"
wl(s)
