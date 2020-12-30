seats = open('day5.in','r').read().strip().split('\n')
#m = 0

free = [True for _ in range(1024)]
#print(free)
#tmp = []

for seat in seats:
 l,h = 0, 1023
 for p in seat:
  #print(str(l)+' '+str(h))
  #print(p+' '+str(l)+' '+str(h))
  if p == 'F' or p == 'L':
   h = int((l+h)/2)
  else:
   l = int((l+h)/2.0+0.5)
 #print(str(l)+' '+str(h))
 #print(l)
 #m = max(m,l)
 #print(l)
 #tmp.append(l)
 free[l] = False
 #print()

#print(sorted(tmp))

for _ in range(1021):
 if not free[_] and free[_+1] and not free[_+2]:
  print(_+1)

#print(free)
#print(free.count(False))
#print(m)