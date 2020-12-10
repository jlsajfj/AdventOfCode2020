pwin = open('day2.in','r').read().strip().split('\n') #get the input, split by line. pwin meaning password in
pwsplit = list(map(lambda x: x.split(':'),pwin)) #split line by colon. pwsplit meaning password split
pw = list(map((lambda x: [x[0].split(' '),x[1].strip()]),pwsplit)) #further split the requirements and strip the passwords. pw just meaning password

num = 0 #number of valid password
for ps in pw: #ps meaning password (requirement) set
 req = ps[0][1] #required character
 f,s = list(map(int,ps[0][0].split('-'))) #first and second index
 ff = ps[1][f-1] == req
 ss = ps[1][s-1] == req
 if (ff and not ss) or (ss and not ff): #update
  num += 1
print(num)

# this too can be one lined!

# input (same as before):
# list(map((lambda x: [x[0].split(' '),x[1].strip()]),list(map(lambda x: x.split(':'),open('day2.in','r').read().strip().split('\n')))))

# processing:
# lambda ps: (lambda p: (lambda x: ((x[0] and not x[1]) or (x[1] and not x[0])))([ps[1][p[0]-1]==ps[0][1],ps[1][p[1]-1]==ps[0][1]]))(list(map(int,ps[0][0].split('-'))))
# debug:
# lambda ps: (lambda p: (lambda x: (print("{} {} {} {} {}".format(x[0],x[1],ps[0][1],ps[1][p[0]-1],ps[1][p[1]-1]))))([ps[1][p[0]-1]==ps[0][1],ps[1][p[1]-1]==ps[0][1]]))(list(map(int,ps[0][0].split('-'))))

print(len(list(filter(lambda ps: (lambda p: (lambda x: ((x[0] and not x[1]) or (x[1] and not x[0])))([ps[1][p[0]-1]==ps[0][1],ps[1][p[1]-1]==ps[0][1]]))(list(map(int,ps[0][0].split('-')))),list(map((lambda x: [x[0].split(' '),x[1].strip()]),list(map(lambda x: x.split(':'),open('day2.in','r').read().strip().split('\n')))))))))

"""
explanation:
 i'll do this tomorrow
"""