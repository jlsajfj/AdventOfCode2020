er = list(map(int,open('day1.in','r').read().strip().split('\n'))) #er meaning expense report again

# the brute force method is just doing an O(n^3) algorithm
# which is what I will be doing

# obviously this isnt the most efficient algorithm,
# it's just an extention of the previous algorithm
# so it's what i'm going with, as it takes the least thinking

l = len(er) # i'm getting tired of typing len(er)
for i in range(l):
 for j in range(i+1,l):
  for k in range(j+1,l):
   if er[i]+er[j]+er[k] == 2020:
    print(er[i]*er[j]*er[k])
    exit()
