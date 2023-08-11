pts = {tuple([int(x) for x in line.split(',')]):True for line in open("inpd18.txt","r").read().split('\n')}
ans = 0
for pt in pts.keys():
    n = 0
    for mod in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
        if (pt[0]+mod[0],pt[1]+mod[1],pt[2]+mod[2]) in pts.keys():
            n += 1
    ans += 6-n

print(ans)