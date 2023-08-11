from queue import Queue

pts = {tuple([int(x) for x in line.split(',')]):True for line in open("inpd18.txt","r").read().split('\n')}
ans = 0
for pt in pts.keys():
    n = 0
    for mod in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
        if (pt[0]+mod[0],pt[1]+mod[1],pt[2]+mod[2]) in pts.keys():
            n += 1
    ans += 6-n

poss = [(x,y,z) for x in range(-1,23) for y in range(-1,23) for z in range(-1,23) if (x,y,z) not in pts.keys()]

q = Queue(maxsize=0)
q.put((-1,-1,-1))
poss.remove((-1,-1,-1))
while q.qsize() > 0:
    pt = q.get()
    for mod in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
        if (pt[0]+mod[0],pt[1]+mod[1],pt[2]+mod[2]) in poss:
            q.put((pt[0]+mod[0],pt[1]+mod[1],pt[2]+mod[2]))
            poss.remove((pt[0]+mod[0],pt[1]+mod[1],pt[2]+mod[2]))

pts = {x:True for x in poss}
for pt in pts.keys():
    n = 0
    for mod in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
        if (pt[0]+mod[0],pt[1]+mod[1],pt[2]+mod[2]) in pts.keys():
            n += 1
    ans -= 6-n

print(ans)