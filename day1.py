er = open('day1.in','r').read().split('\n') #er meaning expense report

for i in range(len(er)):
 for j in range(i+1,len(er)):
  print(er[i]+er[j])
  if er[i]+er[j]==2020:
   print(er[i]*er[j])
   exit()
