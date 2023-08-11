btns = []
occ = {}
for line in open("inpd15.txt","r").read().split('\n'):
    sx = int(line.split("=")[1].split(",")[0])
    sy = int(line.split("=")[2].split(":")[0])
    bx = int(line.split("=")[3].split(",")[0])
    by = int(line.split("=")[4])
    btns.append([sx,sy,bx,by])
    occ[(sx,sy)] = True
    occ[(bx,by)] = True

for Y in range(0,4000001):
    rngs = []
    for btn in btns:
        sx,sy,bx,by = btn[0],btn[1],btn[2],btn[3]
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

    lv = -1
    for i in range(len(n_rngs)):
        if n_rngs[i][0] > lv+1:
            if (lv+1,Y) in occ.keys():
                lv = n_rngs[i][1]
                continue
            print((lv+1)*4000000+Y)
            exit(0)
        else:
            lv = n_rngs[i][1]
    if lv < 4000000:
        if (lv+1,Y) not in occ.keys():
            print((lv+1)*4000000+Y)
            exit(0)