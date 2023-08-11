p = [[(0,0),(1,0),(2,0),(3,0)],[(1,0),(0,1),(1,1),(2,1),(1,2)],[(0,0),(1,0),(2,0),(2,1),(2,2)],[(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,0),(0,1),(1,1)]]
max_y = 0
s = open("inpd17.txt","r").read()
ind = 0
rind = 0
vis = {}
f = False
extra = 0
d = {}
cnt = 0
for temp in range(int(1e12)):
    b_y = max_y+4
    b_x = 2
    
    if not f:
        if (rind,ind) not in d:
            d[(rind,ind)] = [cnt,max_y,1]
        elif d[(rind,ind)][2] == 1:
            d[(rind,ind)] = [cnt,max_y,2]
        else:
            f = True
            extra = ((int(1e12)-cnt)//(cnt-d[(rind,ind)][0]))*(max_y-d[(rind,ind)][1])
            cnt += ((int(1e12)-cnt)//(cnt-d[(rind,ind)][0]))*(cnt-d[(rind,ind)][0])
            rind = cnt%5
    
    while True:
        mn_x = min([x[0] for x in p[rind]])+b_x
        mx_x = max([x[0] for x in p[rind]])+b_x
        mn_y = min([x[1] for x in p[rind]])+b_y
        mx_y = max([x[1] for x in p[rind]])+b_y
        l_pts,r_pts = [],[]
        for y in range(mn_y,mx_y+1):
            l_pts.append((min([x[0]+b_x for x in p[rind] if x[1]+b_y == y]),y))
            r_pts.append((max([x[0]+b_x for x in p[rind] if x[1]+b_y == y]),y))
        d_pts = []
        for x in range(mn_x,mx_x+1):
            d_pts.append((x,min([y[1]+b_y for y in p[rind] if y[0]+b_x == x])))
        if s[ind] == '<' and mn_x > 0 and sum([1 for x in l_pts if (x[0]-1,x[1]) in vis.keys()]) == 0:
            b_x -= 1
            d_pts = [(x[0]-1,x[1]) for x in d_pts]
        elif s[ind] == '>' and mx_x < 6 and sum([1 for x in r_pts if (x[0]+1,x[1]) in vis.keys()]) == 0:
            b_x += 1
            d_pts = [(x[0]+1,x[1]) for x in d_pts]
        ind += 1
        ind %= len(s)
        if mn_y > 0 and sum([1 for x in d_pts if (x[0],x[1]-1) in vis.keys()]) == 0:
            b_y -= 1
        else:
            break
    for (x,y) in p[rind]:
        vis[(x+b_x,y+b_y)] = True
        max_y = max(max_y,y+b_y)
    rind += 1
    rind %= 5
    cnt += 1
    if cnt == int(1e12):
        break
print(max_y+extra)