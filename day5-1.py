seats = open('day5.in','r').read().strip().split('\n')
m = 0

for seat in seats:
 l,h = 0, 1023
 for p in seat:
  #print(str(l)+' '+str(h))
  if p == 'F' or p == 'L':
   h = int((l+h)/2)
  else:
   l = int((l+h)/2.0+0.5)
 #print(str(l)+' '+str(h))
 #print(l)
 m = max(m,l)
print(m)
