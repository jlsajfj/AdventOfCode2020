p = open('day4.in','r').read().split('\n\n') #get input and split by double line
req = ['byr','iyr','eyr','hgt','hcl','ecl','pid'] #all required fields

cnt = 0
for passport in p: #isolate individual passports
 if all(map(lambda x: x in passport,req)): #if all values exist
  cnt += 1
print(cnt)

# lets see if this can be one lined

# input:
# [open('day4.in','r').read().split('\n\n'), ['byr','iyr','eyr','hgt','hcl','ecl','pid']]

# processing:
# lambda x: filter(lambda y: all(map(lambda z: z in y, x[1])), x[0])

print(len(list((lambda x: filter(lambda y: all(map(lambda z: z in y, x[1])), x[0]))([open('day4.in','r').read().split('\n\n'), ['byr','iyr','eyr','hgt','hcl','ecl','pid']]))))

"""
 explanation
 
 input
 [...]
  packing them all into one array

 open('day4.in','r').read().split('\n\n')
  same as always except splitting by two lines
 
 ['byr','iyr','eyr','hgt','hcl','ecl','pid']
  all the requirements
 
 processing
 lambda x: ...
  setting input array to x

 filter(...)
  remove all undesired elemnts
 
 lambda y: ...
  function that filter uses to check
 
 all(map(lambda z: z in y, x[1]))
  check that all elements required are present
"""