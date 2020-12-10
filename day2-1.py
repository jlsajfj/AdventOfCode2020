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
# list(map((lambda x: [x[0].split(' '),x[1].strip()]),list(map(lambda x: x.split(':'),open('day2.in','r').read().strip().split('\n')))))

print(len(list(filter(lambda ps: ((lambda x: ((lambda m: m[0] <= x and x <= m[1])(list(map(int,ps[0][0].split('-'))))))(ps[1].count(ps[0][1]))), list(map((lambda x: [x[0].split(' '),x[1].strip()]),list(map(lambda x: x.split(':'),open('day2.in','r').read().strip().split('\n')))))))))