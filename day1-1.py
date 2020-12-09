er = list(map(int,open('day1.in','r').read().strip().split('\n'))) #er meaning expense report

for i in range(len(er)): #first number loop
 for j in range(i+1,len(er)): #second number loop
  #print(er[i]+er[j]) #just for debugging
  if er[i]+er[j]==2020: #if it sums
   print(er[i]*er[j]) #print the multiplied
   exit() #then quit
