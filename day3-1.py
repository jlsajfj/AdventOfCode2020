trees = open('day3.in','r').read().strip().split('\n') #same input style as always

cnt = 0
for i, line in enumerate(trees):
 loc = 3*i%len(line)
 if line[loc] == '#':
  cnt+=1
 #nl = line[:loc]+'X'+line[loc+1:]
 #print(nl)
print(cnt)

# i think i'm going to try to one line every problem
# just cause

# input:
# enumerate(open('day3.in','r').read().strip().split('\n'))

# processing:
# lambda x: x[1][3*x[0]%len(x[1])]=='#'

print(len(list(filter(lambda x: x[1][3*x[0]%len(x[1])]=='#',enumerate(open('day3.in','r').read().strip().split('\n'))))))

"""
 explanation:
 wow this one is short
 
 input
 open('day3.in','r').read().strip().split('\n')
  same as always
 
 enumerate(...)
  convert it to an array of (index, value)
 
 processing
 lambda x: ...
  set the (idx, value) to x
 
 x[1][3*x[0]%len(x[1])]=='#'
  condition to check
"""