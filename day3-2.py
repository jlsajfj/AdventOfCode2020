trees = open('day3.in','r').read().strip().split('\n') #same input style as always

cnt = 1
for s in [1,3,5,7]:
 tcnt = 0
 for i, line in enumerate(trees):
  loc = s*i%len(line)
  if line[loc] == '#':
   tcnt += 1
  #nl = line[:loc]+'X'+line[loc+1:]
  #print(nl)
 cnt *= tcnt
tcnt = 0
for i, line in enumerate(trees):
 if i%2 == 0:
  loc = i//2%len(line)
  if line[loc] == '#':
   tcnt += 1
cnt *= tcnt
  
print(cnt)

# this one liner might actually be tricky

# input:
# enumerate(open('day3.in','r').read().strip().split('\n'))

# processing:
# lambda t: [len(list(filter(lambda x: x[1][x[0]%len(x[1])]=='#',t))),len(list(filter(lambda x: x[1][3*x[0]%len(x[1])]=='#',t))),len(list(filter(lambda x: x[1][5*x[0]%len(x[1])]=='#',t))),len(list(filter(lambda x: x[1][7*x[0]%len(x[1])]=='#',t))),len(list(filter(lambda x: x[1][x[0]//2%len(x[1])]=='#',filter(lambda x: x[0]%2==0,t))))]

print((lambda t: [len(list(filter(lambda x: x[1][x[0]%len(x[1])]=='#',t))),len(list(filter(lambda x: x[1][3*x[0]%len(x[1])]=='#',t))),len(list(filter(lambda x: x[1][5*x[0]%len(x[1])]=='#',t))),len(list(filter(lambda x: x[1][7*x[0]%len(x[1])]=='#',t))),len(list(filter(lambda x: x[1][x[0]//2%len(x[1])]=='#',filter(lambda x: x[0]%2==0,t))))])(enumerate(open('day3.in','r').read().strip().split('\n'))))

"""
 this doesnt actually work. I'm leaving it for now, but I'll figure something out another time
"""