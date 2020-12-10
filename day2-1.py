pwin = open('day2.in','r').read().strip().split('\n') #get the input, split by line. pwin meaning password in
pwsplit = list(map(lambda x: x.split(':'),pwin)) #split line by colon. pwsplit meaning password split
pw = list(map((lambda x: [x[0].split(' '),x[1].strip()]),pwsplit)) #further split the requirements and strip the passwords. pw just meaning password

num = 0 #number of valid password
for ps in pw: #ps meaning password (requirement) set
 req = ps[0][1] #required character
 min, max = list(map(int,ps[0][0].split('-'))) #range of numbers
 cnt = ps[1].count(req) #count of required character
 if min <= cnt and cnt <= max: #update
  num += 1
print(num)

# technically this can be done on one line

# input:
# map((lambda x: [x[0].split(' '),x[1].strip()]),map(lambda x: x.split(':'),open('day2.in','r').read().strip().split('\n')))

# processing:
# lambda ps: (lambda x: (lambda m: m[0] <= x and x <= m[1])(list(map(int,ps[0][0].split('-')))))(ps[1].count(ps[0][1]))

print(len(list(filter(lambda ps: (lambda x: (lambda m: m[0] <= x and x <= m[1])(list(map(int,ps[0][0].split('-')))))(ps[1].count(ps[0][1])), map((lambda x: [x[0].split(' '),x[1].strip()]),map(lambda x: x.split(':'),open('day2.in','r').read().strip().split('\n')))))))

"""
 explanation:
 
 print(len(list(filter(...))))
  this just uses a filter to remove stuff that
  doesnt fall under constraints, sets it to a
  list, and outputs the size of the list.
 
 lambda ps: ...
  this just sets the current working element to ps
 
 (lambda x: ...)(ps[1].count(ps[0][1]))
  set the count variable to x
 
 (lambda m: ...)(list(map(int,ps[0][0].split('-'))))
  sets the array of min,max to the variable map
  the list is necessary for the lambda to function
 
 m[0] <= x and x <= m[1]
  condition for filter to keep element
 
 open('day2.in','r').read().strip().split('\n')
  open and read file, removing excess new lines,
  then splitting by new line
 
 map(lambda x: x.split(':'),...)
  split each element by the colon. originally this
  had list(...) wrapping it, but that turned out
  to be unnecessary.
 
 map((lambda x: [x[0].split(' '),x[1].strip()]),...)
  this takes each value, then further splits the
  first section (the "1-3" section) and strips
  the second section of unnecessary spaces. this
  is unnecessary, i could have just used x[1][1:]
  instead. it also puts it into a neat array
"""