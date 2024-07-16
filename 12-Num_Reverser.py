# Without function
n = 1234
r = 0
while n > 0:
  rem = n % 10
  r = r * 10 + rem
  n = n // 10
print(r)

# With function
def rev_number(n):
  r = 0
  while n > 0:
    rem = n % 10
    r = r * 10 + rem
    n = n // 10
    return r
print(rev_number(1234))
