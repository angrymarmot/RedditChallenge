from sys import argv
from collections import defaultdict
 
logs = open("log.txt")
roomMax, visitorMax, timeMax = 99, 1023, 1439
rooms = {}
vals = {}
avgs = {}
rmv = {}
for line in logs:
    line = line.strip().split(" ")
    p, r, d, t = int(line[0]), int(line[1]), line[2], int(line[3])
    key = (r, p)
    if key not in rooms.keys():
        rooms[key] = (d, t)
    else:
        vals[key] = t - rooms[key][1] + 1
    if key[0] not in avgs.keys():
        avgs[key[0]] = 1
    else:
        avgs[key[0]] += 1
 
for rm in vals.keys():
    if rm[0] not in avgs.keys():
        avgs[rm[0]] = 0
        avgs[rm[0]] += vals[rm]
 
    else:
        avgs[rm[0]] += vals[rm]
print "raw"
for k, v in rooms.items():
    print k, v
print "avgs"
for a, b in vals.items():
    print a, b

 