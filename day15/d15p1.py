Y = 2000000
rngs = []
for line in open("inpd15.txt","r").read().split('\n'):
    sx = int(line.split("=")[1].split(",")[0])
    sy = int(line.split("=")[2].split(":")[0])
    bx = int(line.split("=")[3].split(",")[0])
    by = int(line.split("=")[4])
    print(sx,sy,bx,by)
    dis = abs(sx-bx)+abs(sy-by)
    if abs(sy-Y) > dis:
        continue
    if by == Y:
        if bx == sx-abs(dis-abs(sy-Y)):
            rngs.append([bx+1,sx+abs(dis-abs(sy-Y))])
        elif bx == sx+abs(dis-abs(sy-Y)):
            rngs.append([sx-abs(dis-abs(sy-Y)),bx-1])
        else:
            rngs.append([sx-abs(dis-abs(sy-Y)),bx-1])
            rngs.append([bx+1,sx+abs(dis-abs(sy-Y))])
    else:
        rngs.append([sx-abs(dis-abs(sy-Y)),sx+abs(dis-abs(sy-Y))])

rngs.sort()
r = rngs[0][0]-1
l = -1e18
n_rngs = []
for i in range(0,len(rngs)):
    cl,cr = rngs[i][0],rngs[i][1]
    if cl > r:
        n_rngs.append([l,r])
        l = cl
        r = cr
    else:
        r = max(r,cr)
n_rngs.append([l,r])
n_rngs = n_rngs[1:]

ans = 0
for (l,r) in n_rngs:
    ans += r-l+1
print(ans)