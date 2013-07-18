logs = open("log.txt")
rooms = {}
avgs = {}

for line in logs:
    line = line.strip().split(" ")
    p, r, d, t = int(line[0]), int(line[1]), line[2], int(line[3])
    key = (r, p)
    if key not in rooms.keys():
        rooms[key] = (d, t)
    else:
        if r in avgs:
            avgs[r] += [t - rooms[key][1] + 1]
        else:
            avgs[r] = [t - rooms[key][1] + 1]

for room in sorted(avgs.keys()):
    if len(avgs[room]) > 1:
        print "Room", room, "-", sum(avgs[room]) / len(avgs[room]), "minute average visit,", len(avgs[room]), "visitors total."
    else:
        print "Room", room, "-", sum(avgs[room]) / len(avgs[room]), "minute average visit,", len(avgs[room]), "visitor total."




