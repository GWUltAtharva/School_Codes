#Mutable Parameters - Dictionary type
def rm(s, p):
  s['Marks'] = ((100 + p) / 100)
  s['Status'] = 'Changed'

S1 = {'R.no.': 19,
      'Name': 'Ramesh',
      'Marks': 87,
      'Status': '*'}
S2 = {'R.no.': 3,
      'Name': 'Anishka',
      'Marks': 55,
      'Status': '*'}

rm(S1, 7)
rm(S2, 15)
print(S1)
print(S2)
