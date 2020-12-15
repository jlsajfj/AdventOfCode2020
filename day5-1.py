seats = open('day5.in','r').read().strip().split('\n')
max = 0

for seat in seats:
 l,h = 0, 1023
 for p in seat:
  if p == 'F':
   h = int((l+h)/2)
  else:
   l = int((l+h)/2.0+0.5)
  print(l)